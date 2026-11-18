<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'
import source from '../sources/canva-native.json'
import motion from '../sources/canva-motion.json'
import {createCanvaPaintMask} from '../utils/canva-paint-mask'
import type {AnimationItem} from 'lottie-web'
const pages=import.meta.glob('../sources/canva-native/*.html',{query:'?raw',import:'default',eager:true})
const props=defineProps<{slide:number; hideImages?:boolean}>()
const { $slidev,$page,$renderContext }=useSlideContext()
const active=computed(()=>$slidev.nav.currentPage===$page.value)
const original=computed(()=>source.pages[props.slide-1])
const root=ref<HTMLElement>()
const ready=ref(false)
const motionReady=ref(false)
const motionPage=computed(()=>motion.pages[props.slide-1])
const markup=computed(()=>{
 let html=String(pages[`../sources/canva-native/${String(props.slide).padStart(2,'0')}.html`])
 .replaceAll('="/sources/',`="${import.meta.env.BASE_URL}sources/`)
 .replace(/<img\b[^>]*>/g,tag=>props.hideImages?'':tag)
 for(const effect of motionPage.value.effects){
  const id=`canva-${props.slide}-${effect.id}`
  html=html.replace(`id="${id}"`,`id="${id}" data-canva-motion="${effect.id}"`)
 }
 return html
})
let animations:Animation[]=[]
const liquidPlayers:AnimationItem[]=[]
const paints:ReturnType<typeof createCanvaPaintMask>[]=[]
let disposed=false
let preference:MediaQueryList|undefined
const staticView=()=>['print','overview','preview','presenter'].includes($renderContext.value)||Boolean(preference?.matches)
function effectElement(effect:typeof motion.pages[number]['effects'][number]){
 if('replacement' in effect&&props.hideImages){
  return root.value?.closest('[data-slidev-no]')?.querySelector<HTMLElement>(effect.replacement==='code'?'.stepped-source-code.walk-sympy':'.stepped-source-result.walk-sympy')
 }
 return root.value?.querySelector<HTMLElement>(`[id="canva-${props.slide}-${effect.id}"]`)
}
async function preparePaints(){
 for(const effect of motionPage.value.effects){
  if(!('paint' in effect))continue
  const image=effectElement(effect)?.querySelector<HTMLImageElement>('img')
  if(!image)throw new Error(`Missing original Canva paint picture on page ${props.slide}`)
  const painter=createCanvaPaintMask(image,`${import.meta.env.BASE_URL}sources/canva-native/animations/${effect.paint.file}`,effect.paint.duration)
  paints.push(painter)
  if(staticView())painter.showStatic()
 }
 await Promise.all(paints.map(p=>p.ready))
}
function syncLiquid(){
 for(const player of liquidPlayers){
  if(staticView())player.goToAndStop(0,true)
  else if(active.value)player.play()
  else player.pause()
 }
}
async function loadLiquid(){
 if(props.slide!==2||!root.value)return
 const {default:lottie}=await import('lottie-web')
 const shapes=[
  {node:41,file:'shape-35.json',color:[37,193,113]},
  {node:85,file:'shape-34.json',color:[255,190,79]},
  {node:130,file:'shape-36.json',color:[195,143,248]},
 ]
 for(const shape of shapes){
  const container=root.value?.querySelector<HTMLElement>(`[data-canva-node="canva-2-${shape.node}"]`)
  if(!container)continue
  const response=await fetch(`${import.meta.env.BASE_URL}sources/canva-native/animations/${shape.file}`)
  const data=await response.json()
  if(disposed)return
  // Canva recolors the stock animation. Keep the deck's original three fills.
  const recolor=(value:any)=>{
   if(!value||typeof value!=='object')return
   if(value.ty==='fl'&&value.c?.a===0)value.c.k=[...shape.color.map(c=>c/255),1]
   for(const child of Object.values(value))recolor(child)
  }
  recolor(data)
  const layer=document.createElement('div')
  layer.className='canva-liquid-layer';layer.setAttribute('data-original-liquid',shape.file)
  container.append(layer)
  const player=lottie.loadAnimation({container:layer,renderer:'svg',loop:true,autoplay:false,animationData:data,rendererSettings:{preserveAspectRatio:'xMidYMid meet'}})
  liquidPlayers.push(player)
  player.addEventListener('DOMLoaded',()=>{
   if(disposed)return
   container.querySelector(':scope > svg')?.remove()
   syncLiquid()
  })
 }
}
function play(){
 motionReady.value=false
 animations.forEach(a=>a.cancel());animations=[]
 paints.forEach(p=>p.pause())
 syncLiquid()
 if(!ready.value)return
 if(staticView()){paints.forEach(p=>p.showStatic());motionReady.value=true;return}
 if(!active.value)return
 for(const effect of motionPage.value.effects){
  const element=effectElement(effect)
  if(!element)continue
  element.dataset.canvaMotion=effect.id
  animations.push(element.animate([
   {translate:`0 ${effect.distance}px`,opacity:0},
   {translate:'0 0',opacity:1},
  ],{duration:effect.duration,delay:effect.delay,easing:'cubic-bezier(.16,1,.3,1)',fill:'both'}))
  if('wipe' in effect)animations.push(element.animate([
   {clipPath:'inset(0 100% 0 0)'},{clipPath:'inset(0 0% 0 0)'},
  ],{duration:effect.wipe.duration,delay:effect.delay,easing:'cubic-bezier(.2,.6,.3,1)',fill:'both'}))
 }
 for(const effect of original.value.animations){
  const element=root.value?.querySelector<HTMLElement>(`[data-canva-node="${effect.node}"]`)
  if(element)animations.push(element.animate(effect.frames as Keyframe[],effect.timing as KeyframeAnimationOptions))
 }
 paints.forEach(p=>void p.play())
 motionReady.value=true
}
watch([active,$renderContext],()=>void nextTick(play))
onMounted(async()=>{
 preference=window.matchMedia('(prefers-reduced-motion: reduce)')
 preference.addEventListener('change',play)
 await nextTick()
 const paintReady=preparePaints()
 root.value?.getBoundingClientRect();await document.fonts.ready
 await Promise.all([...root.value?.querySelectorAll('img')??[]].map(image=>image.decode().catch(()=>{})))
 await Promise.all([paintReady,loadLiquid()])
 if(disposed)return
 ready.value=true;play()
})
onBeforeUnmount(()=>{disposed=true;preference?.removeEventListener('change',play);animations.forEach(a=>a.cancel());liquidPlayers.forEach(player=>player.destroy());paints.forEach(p=>p.dispose())})
</script>

<template>
 <main class="canva-source-slide" :data-source-slide="slide" :data-motion-ready="motionReady">
  <svg class="canva-source-canvas" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
   <foreignObject width="1920" height="1080">
    <div ref="root" class="canva-native-content" v-html="markup" />
   </foreignObject>
  </svg>
 </main>
</template>

<style>
.canva-source-slide{position:absolute;inset:0;overflow:hidden;background:#a182b7}
.canva-source-canvas{display:block;width:100%;height:100%;overflow:hidden}
.canva-native-content{position:relative;width:1920px;height:1080px;overflow:hidden}
.canva-liquid-layer{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.canva-source-slide[data-motion-ready="false"] [data-canva-motion],
.canva-source-slide[data-motion-ready="false"] ~ .stepped-source-code.walk-sympy,
.canva-source-slide[data-motion-ready="false"] ~ .stepped-source-result.walk-sympy{opacity:0!important}
@media print{.canva-source-slide [data-canva-motion]{opacity:1!important;translate:none!important;clip-path:none!important}}
</style>
