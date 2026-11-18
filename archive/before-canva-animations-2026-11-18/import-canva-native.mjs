// Read the supplied shared design. Never edits or embeds the Canva application.
import fs from 'node:fs/promises'
import path from 'node:path'
import crypto from 'node:crypto'
let playwright
try {playwright=await import('playwright')}catch{playwright=await import('../.cache/qa/node_modules/playwright/index.mjs')}
const bi=process.argv.indexOf('--browser')
const browser=await playwright.chromium.launch({headless:true,...(bi>=0?{executablePath:process.argv[bi+1]}:{})})
const target='public/sources/canva-native'
await fs.mkdir(`${target}/assets`,{recursive:true})
const metadata=JSON.parse(await fs.readFile('sources/canva.json','utf8'))
const styles=new Map(),fontRules=new Set(),assetUrls=new Set(),pages=[]
const properties=`display position top right bottom left width height min-width min-height max-width max-height box-sizing margin-top margin-right margin-bottom margin-left padding-top padding-right padding-bottom padding-left border-top-width border-right-width border-bottom-width border-left-width border-top-style border-right-style border-bottom-style border-left-style border-top-color border-right-color border-bottom-color border-left-color border-top-left-radius border-top-right-radius border-bottom-left-radius border-bottom-right-radius background-color background-image background-size background-position background-repeat background-origin background-clip opacity visibility overflow overflow-x overflow-y clip clip-path transform transform-origin transform-style perspective perspective-origin backface-visibility z-index isolation mix-blend-mode filter backdrop-filter box-shadow flex flex-direction flex-wrap flex-grow flex-shrink flex-basis align-items align-self align-content justify-content justify-items justify-self gap row-gap column-gap grid-template-columns grid-template-rows grid-column grid-row object-fit object-position aspect-ratio vertical-align float clear color font-family font-size font-weight font-style font-stretch font-variant font-kerning font-feature-settings font-variation-settings line-height letter-spacing word-spacing text-align text-align-last text-indent text-transform text-decoration-line text-decoration-color text-decoration-style text-decoration-thickness text-underline-offset text-shadow white-space word-break overflow-wrap tab-size writing-mode direction unicode-bidi list-style-type list-style-position fill fill-opacity fill-rule stroke stroke-width stroke-opacity stroke-dasharray stroke-dashoffset stroke-linecap stroke-linejoin stroke-miterlimit vector-effect paint-order dominant-baseline alignment-baseline text-anchor mask-image mask-size mask-repeat mask-position`.split(' ')
try{
 const page=await browser.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:1})
 await page.addInitScript(()=>{
  window.__nativeAnimations=[]
  const original=Element.prototype.animate
  Element.prototype.animate=function(frames,options){
   const animation=original.call(this,frames,options)
   window.__nativeAnimations.push({target:this,animation})
   return animation
  }
 })
 await page.goto(metadata.url.replace('/edit','/view')+'?embed#1',{waitUntil:'domcontentloaded'})
 await page.getByText('LECTURE 9:',{exact:true}).first().waitFor()
 for(let number=1;number<=29;number++){
  await page.waitForTimeout(1200)
  await page.evaluate(()=>document.fonts.ready)
  await page.waitForFunction(()=>{
   const root=[...document.querySelectorAll('._mXnjA')].find(e=>!e.closest('[aria-hidden="true"]')&&e.getBoundingClientRect().width>1900)
   return root&&[...root.querySelectorAll('img')].every(image=>image.complete&&image.naturalWidth>0)
  })
  await page.waitForTimeout(350)
  const snapshot=await page.evaluate(({properties,number})=>{
   const root=[...document.querySelectorAll('._mXnjA')].find(e=>{
    const r=e.getBoundingClientRect();return r.width>1900&&r.height>1000&&r.x>-5&&r.x<5&&!e.closest('[aria-hidden="true"]')
   })
   if(!root)throw new Error('Original native Canva page not found')
   const styleMap={},fonts=new Set(),urls=new Set(),prefix=`canva-${number}-`,map=new Map()
   let counter=0
   const cssFor=(el,pseudo)=>{
    const c=getComputedStyle(el,pseudo),values={}
    for(const p of properties){const value=c.getPropertyValue(p);if(value)values[p]=value}
    if(pseudo)values.content=c.content
    fonts.add(c.fontFamily.split(',')[0].replaceAll('"','').trim())
    return values
   }
   const copy=(el)=>{
    if(['SCRIPT','STYLE','NOSCRIPT','IFRAME','BUTTON'].includes(el.tagName))return null
    const clone=el instanceof HTMLCanvasElement ? document.createElement('img') : el.cloneNode(false),id=prefix+(counter++)
    if(el instanceof HTMLCanvasElement){
     // Canva paints some individual picture effects into a canvas. Preserve
     // that original picture with its alpha/effect, never the slide canvas.
     clone.setAttribute('src',el.toDataURL('image/png'))
     clone.setAttribute('data-original-picture-effect','true')
    }
    map.set(el,id);clone.setAttribute('data-canva-node',id)
    styleMap[id]=cssFor(el)
    clone.removeAttribute('class');clone.removeAttribute('style');clone.removeAttribute('tabindex')
    if(clone.hasAttribute('srcset'))clone.removeAttribute('srcset')
    if(el instanceof HTMLImageElement){clone.setAttribute('src',el.currentSrc||el.src);clone.removeAttribute('loading')}
    for(const child of el.childNodes){
     if(child.nodeType===Node.ELEMENT_NODE){const c=copy(child);if(c)clone.append(c)}
     else if(child.nodeType===Node.TEXT_NODE)clone.append(document.createTextNode(child.textContent))
    }
    for(const which of ['::before','::after']){
     const c=getComputedStyle(el,which)
     if(c.content!=='none'&&c.content!=='normal'&&c.display!=='none'){
      const pseudo=document.createElement('span'),pid=prefix+(counter++)
      pseudo.setAttribute('data-canva-node',pid);pseudo.textContent=c.content.replace(/^"|"$/g,'')
      styleMap[pid]=cssFor(el,which)
      if(which==='::before')clone.prepend(pseudo);else clone.append(pseudo)
     }
    }
    return clone
   }
   const clone=copy(root)
   // Prefix SVG identifiers to keep references local when adjacent slides mount.
   const ids=new Map([...clone.querySelectorAll('[id]')].map(e=>[e.id,prefix+e.id]))
   for(const e of [clone,...clone.querySelectorAll('*')]){
    for(const a of [...e.attributes]){
     let value=a.value
     if(a.name==='id')value=ids.get(value)||value
     for(const [old,next] of ids){value=value.replaceAll(`url(#${old})`,`url(#${next})`);if(value===`#${old}`)value=`#${next}`}
     if(value.startsWith('http')&&(a.name==='src'||a.localName==='href')&&!value.includes('/design/'))urls.add(value)
     e.setAttribute(a.name,value)
    }
   }
   for(const values of Object.values(styleMap))for(const [key,value] of Object.entries(values)){
    let updated=value
    for(const [old,next] of ids)updated=updated.replaceAll(`#${old}`,`#${next}`)
    updated=updated.replace(/url\("?https:\/\/www\.canva\.com\/[^#"]+#([^"\)]+)"?\)/g,'url(#$1)')
    values[key]=updated
    for(const m of updated.matchAll(/url\(["']?(https?:[^"'\)]+)["']?\)/g))urls.add(m[1])
   }
   const rules=[]
   for(const sheet of document.styleSheets)try{for(const rule of sheet.cssRules)if(rule.cssText?.startsWith('@font-face')&&[...fonts].some(f=>rule.cssText.includes(`font-family: ${f};`)||rule.cssText.includes(`font-family: "${f}";`)))rules.push(rule.cssText)}catch{}
   const animations=[]
   for(const {target,animation} of window.__nativeAnimations||[]){
    if(map.has(target)&&target.isConnected){
     const timing=animation.effect.getTiming()
     if(Number.isFinite(timing.duration)&&timing.duration>0)animations.push({node:map.get(target),frames:animation.effect.getKeyframes(),timing:{...timing,fill:'both'}})
    }
   }
   return {html:clone.outerHTML,styles:styleMap,fonts:rules,urls:[...urls],animations,text:root.textContent,
           textNodes:root.querySelectorAll('p,svg text').length,images:root.querySelectorAll('img,image').length,nodes:counter,
           background:getComputedStyle(root).backgroundColor}
  },{properties,number})
  for(const rule of snapshot.fonts)fontRules.add(rule)
  for(const url of snapshot.urls)assetUrls.add(url)
  for(const [id,values] of Object.entries(snapshot.styles)){
   const css=Object.entries(values).filter(([p])=>p!=='content').map(([p,v])=>`${p}:${v}`).join(';')
   styles.set(id,css)
  }
  pages.push({number,...snapshot,styles:undefined,fonts:undefined,urls:undefined})
  console.log(`Read native Canva page ${number}/29 (${snapshot.textNodes} text blocks, ${snapshot.images} original images).`)
  if(number<29)await page.getByRole('button',{name:'Next page',exact:true,includeHidden:true}).evaluate(b=>b.click())
 }
 let css=[...styles].map(([id,rules])=>`[data-canva-node="${id}"][data-canva-node]{${rules}}`).join('\n')
 let fontCss=[...fontRules].join('\n')
 for(const m of fontCss.matchAll(/url\("?(https?:[^"\)]+)"?\)/g))assetUrls.add(m[1])
 const replacements=new Map()
 const pending=[...assetUrls]
 for(let i=0;i<pending.length;i+=6)await Promise.all(pending.slice(i,i+6).map(async url=>{
  const response=await page.request.get(url)
  if(!response.ok())throw new Error(`Original Canva asset unavailable: ${response.status()} ${new URL(url).hostname}`)
  const data=await response.body(),type=response.headers()['content-type']||''
  const ext=type.includes('woff2')||url.includes('.woff2')?'woff2':type.includes('svg')?'svg':type.includes('png')?'png':type.includes('webp')?'webp':type.includes('avif')?'avif':type.includes('jpeg')?'jpg':'bin'
  const name=crypto.createHash('sha256').update(data).digest('hex').slice(0,20)+'.'+ext
  await fs.writeFile(`${target}/assets/${name}`,data)
  replacements.set(url,`/sources/canva-native/assets/${name}`)
 }))
 const localize=value=>{
  for(const [url,local]of replacements)value=value.replaceAll(url,local).replaceAll(url.replaceAll('&','&amp;'),local)
  return value
 }
 css=localize(css);fontCss=localize(fontCss)
 await fs.writeFile(`${target}/styles.css`,fontCss+'\n'+css)
 await fs.writeFile('styles/canva-native.css',fontCss+'\n'+css)
 const manifest={width:1920,height:1080,source:metadata.url,pages:[]}
 for(const page of pages){
  for(const m of page.html.matchAll(/(?:src|href)="(data:image\/[^;]+;base64,([^"]+))"/g)){
   const data=Buffer.from(m[2],'base64'),name=crypto.createHash('sha256').update(data).digest('hex').slice(0,20)+'.png'
   await fs.writeFile(`${target}/assets/${name}`,data)
   page.html=page.html.replaceAll(m[1],`/sources/canva-native/assets/${name}`)
  }
  await fs.writeFile(`${target}/${String(page.number).padStart(2,'0')}.html`,localize(page.html))
  await fs.mkdir('sources/canva-native',{recursive:true})
  await fs.writeFile(`sources/canva-native/${String(page.number).padStart(2,'0')}.html`,localize(page.html))
  manifest.pages.push({...page,html:undefined,file:`/sources/canva-native/${String(page.number).padStart(2,'0')}.html`})
 }
 await fs.writeFile('sources/canva-native.json',JSON.stringify(manifest,null,2)+'\n')
 console.log(`Imported 29 native Canva pages; ${replacements.size} local original assets; ${fontRules.size} source font rules.`)
}finally{await browser.close()}
