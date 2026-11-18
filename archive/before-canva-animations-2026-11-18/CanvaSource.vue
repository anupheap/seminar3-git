<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'
import source from '../sources/canva-native.json'
import type {AnimationItem} from 'lottie-web'
const pages=import.meta.glob('../sources/canva-native/*.html',{query:'?raw',import:'default',eager:true})
const props=defineProps<{slide:number; hideImages?:boolean}>()
const { $slidev,$page,$renderContext }=useSlideContext()
const active=computed(()=>$slidev.nav.currentPage===$page.value)
const original=computed(()=>source.pages[props.slide-1])
const root=ref<HTMLElement>()
const ready=ref(false)
const markup=computed(()=>String(pages[`../sources/canva-native/${String(props.slide).padStart(2,'0')}.html`])
 .replaceAll('="/sources/',`="${import.meta.env.BASE_URL}sources/`)
 .replace(/<img\b[^>]*>/g,tag=>props.hideImages?'':tag))
let animations:Animation[]=[]
const liquidPlayers:AnimationItem[]=[]
let disposed=false
function syncLiquid(){
 for(const player of liquidPlayers){
  if($renderContext.value==='print'||window.matchMedia('(prefers-reduced-motion: reduce)').matches)player.goToAndStop(0,true)
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
 animations.forEach(a=>a.cancel());animations=[]
 syncLiquid()
 if(!active.value||!ready.value||$renderContext.value==='print'||window.matchMedia('(prefers-reduced-motion: reduce)').matches)return
 for(const effect of original.value.animations){
  const element=root.value?.querySelector<HTMLElement>(`[data-canva-node="${effect.node}"]`)
  if(element)animations.push(element.animate(effect.frames as Keyframe[],effect.timing as KeyframeAnimationOptions))
 }
}
watch(active,()=>void nextTick(play))
onMounted(async()=>{
 await nextTick();root.value?.getBoundingClientRect();await document.fonts.ready
 ready.value=true;play()
 void loadLiquid()
})
onBeforeUnmount(()=>{disposed=true;animations.forEach(a=>a.cancel());liquidPlayers.forEach(player=>player.destroy())})
</script>

<template>
 <main class="canva-source-slide" :data-source-slide="slide">
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
</style>
