// Read only the supplied design's element settings and its public mask asset.
import fs from 'node:fs/promises'
let playwright
try{playwright=await import('playwright')}catch{playwright=await import('../.cache/qa/node_modules/playwright/index.mjs')}
const metadata=JSON.parse(await fs.readFile('sources/canva.json','utf8'))
const bi=process.argv.indexOf('--browser')
const browser=await playwright.chromium.launch({headless:true,...(bi>=0?{executablePath:process.argv[bi+1]}:{})})
try{
 const page=await browser.newPage({viewport:{width:1920,height:1080}})
 await page.goto(metadata.url.replace('/edit','/view')+'#1',{waitUntil:'domcontentloaded'})
 await page.getByRole('button',{name:'Present full screen',exact:true}).waitFor()
 const settings=await page.evaluate(()=>{
  const script=[...document.scripts].find(s=>s.textContent.includes('PBnhjG1ZplhmYDrL'))?.textContent
  if(!script)throw new Error('Original Canva design metadata not found')
  let i=script.indexOf('JSON.parse(')+'JSON.parse('.length
  const quote=script[i++];let decoded=''
  for(;i<script.length;i++){
   const c=script[i]
   if(c===quote)break
   if(c!=='\\'){decoded+=c;continue}
   const next=script[++i]
   if(next==='u'){decoded+=String.fromCharCode(parseInt(script.slice(i+1,i+5),16));i+=4}
   else if(next==='x'){decoded+=String.fromCharCode(parseInt(script.slice(i+1,i+3),16));i+=2}
   else decoded+=({n:'\n',r:'\r',t:'\t',b:'\b',f:'\f',v:'\v','0':'\0'})[next]??next
  }
  const data=JSON.parse(decoded)
  const pages=data.page.Pm.E.draft.content.A.map((page,index)=>{
   const elements=[]
   const walk=(items,parent=null)=>{
    if(!Array.isArray(items))return
    for(const item of items){
     if(!item||typeof item!=='object')continue
     const id=item._
     if(id)elements.push({id,parent,type:item['A?'],bounds:[item.B??0,item.A??0,item.D??0,item.C??0],animation:item.X??null})
     walk(item.c,id??parent)
    }
   }
   walk(page.E)
   return{number:index+1,id:page.a,elements}
  })
  const asset=data.page.Pm.N.o.find(asset=>asset.id==='VAF8jiLDuRo')
  const file=asset.files.find(file=>file.width===1920)
  // Deliberately omit account/session data, asset access tokens and signed manifests.
  return{pages,maskAsset:{id:asset.id,title:asset.title,duration:1600,file:'paint-01.mp4',url:file.url}}
 })
 if(settings.pages.length!==metadata.pages.length||settings.pages.some((page,i)=>page.id!==metadata.pages[i].page_id))throw new Error('Canva page IDs changed; review the source mapping before importing motion')
 await fs.writeFile('sources/canva-animation-settings.json',JSON.stringify({source:metadata.url,...settings},null,2)+'\n')
 const response=await page.request.get(settings.maskAsset.url)
 if(!response.ok())throw new Error(`Original paint mask unavailable: ${response.status()}`)
 await fs.mkdir('public/sources/canva-native/animations',{recursive:true})
 await fs.writeFile(`public/sources/canva-native/animations/${settings.maskAsset.file}`,await response.body())
 console.log(`Read original animation settings for ${settings.pages.length} pages; saved the original paint mask. No Canva changes made.`)
}finally{await browser.close()}
