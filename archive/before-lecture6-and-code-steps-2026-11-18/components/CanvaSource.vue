<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'
import source from '../sources/canva-native.json'
const pages=import.meta.glob('../sources/canva-native/*.html',{query:'?raw',import:'default',eager:true})
const props=defineProps<{slide:number}>()
const { $slidev,$page,$renderContext }=useSlideContext()
const active=computed(()=>$slidev.nav.currentPage===$page.value)
const original=computed(()=>source.pages[props.slide-1])
const root=ref<HTMLElement>()
const ready=ref(false)
const markup=computed(()=>String(pages[`../sources/canva-native/${String(props.slide).padStart(2,'0')}.html`])
 .replaceAll('="/sources/',`="${import.meta.env.BASE_URL}sources/`))
let animations:Animation[]=[]
function play(){
 animations.forEach(a=>a.cancel());animations=[]
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
})
onBeforeUnmount(()=>animations.forEach(a=>a.cancel()))
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
</style>
