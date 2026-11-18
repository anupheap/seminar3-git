import { chromium } from '../.cache/qa/node_modules/playwright/index.mjs'
import fs from 'node:fs/promises'
const source=JSON.parse(await fs.readFile('sources/lecture1-native.json','utf8'))
const browserIndex=process.argv.indexOf('--browser')
const executablePath=browserIndex>=0 ? process.argv[browserIndex+1] : undefined
const browser=await chromium.launch({...(executablePath ? {executablePath} : {}),headless:true})
try {
 const page=await browser.newPage()
 await page.goto('http://localhost:3031/1',{waitUntil:'networkidle'})
 const metrics=await page.evaluate(async source=>{
  await document.fonts.load('40px "Cambria Math"')
  const ns='http://www.w3.org/2000/svg',canvas=document.createElement('canvas'),ctx=canvas.getContext('2d')
  const result=[]
  for(const slide of source.slides)for(const object of slide.objects){
   if(!object.omml.length)continue
   const svg=document.createElementNS(ns,'svg');svg.setAttribute('viewBox','0 0 1280 720');svg.innerHTML=object.svg
   svg.style.cssText='position:fixed;left:-10000px;top:0;width:1280px;height:720px;visibility:hidden'
   document.body.append(svg)
   const xml=new DOMParser().parseFromString('<root>'+object.omml.join('')+'</root>','application/xml')
   const candidates=[...xml.getElementsByTagNameNS('http://schemas.openxmlformats.org/officeDocument/2006/math','r')].map(r=>{
    const text=[...r.getElementsByTagNameNS('http://schemas.openxmlformats.org/officeDocument/2006/math','t')].map(t=>t.textContent).join('')
    const pr=r.getElementsByTagNameNS('http://schemas.openxmlformats.org/drawingml/2006/main','rPr')[0]
    return {text,size:pr?.getAttribute('sz')/100 || 30,bold:pr?.getAttribute('b')==='1'}
   })
   const tokens=[]
   for(const [index,text] of [...svg.querySelectorAll('text[fill-opacity="0"]')].entries()){
    const path=text.previousElementSibling,token=text.textContent
    if(path?.tagName!=='path' || !token || token==='Ԧ')continue
    const original=candidates.find(r=>r.text===token)||candidates.find(r=>r.text.includes(token))||candidates[0]
    const fontSize=original.size*4/3
    const weight=original.bold && ![...token].some(c=>c.codePointAt(0)>=0x1d400 && c.codePointAt(0)<=0x1d7ff) ? 700 : 400
    ctx.font=`${weight} ${fontSize}px "Cambria Math"`
    const m=ctx.measureText(token),b=path.getBBox()
    const w=m.actualBoundingBoxLeft+m.actualBoundingBoxRight,h=m.actualBoundingBoxAscent+m.actualBoundingBoxDescent
    if(w<=0||h<=0)throw new Error(`Missing math font: ${token}`)
    const sx=b.width/w,sy=b.height/h
    tokens.push({index,text:token,size:fontSize,weight,fill:path.getAttribute('fill')||'#FFFFFF',matrix:[sx,0,0,sy,b.x+m.actualBoundingBoxLeft*sx,b.y+m.actualBoundingBoxAscent*sy],bounds:{x:b.x,y:b.y,width:b.width,height:b.height}})
   }
   svg.remove()
   result.push({slide:slide.number,shape:object.id,tokens})
  }
  return result
 },source)
 await fs.writeFile('sources/lecture1-math-metrics.json',JSON.stringify(metrics,null,2)+'\n')
 console.log(`Measured ${metrics.reduce((n,o)=>n+o.tokens.length,0)} equation text tokens against their original glyph positions.`)
}finally{await browser.close()}
