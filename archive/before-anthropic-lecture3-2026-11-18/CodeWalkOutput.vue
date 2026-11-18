<script setup lang="ts">
import {computed,nextTick,ref,watch} from 'vue'
import {useSlideContext} from '@slidev/client'
import examples from '../sources/code-walkthroughs.json'
const props=defineProps<{lesson:string}>()
const {$clicks,$renderContext,$slidev,$page}=useSlideContext()
const lesson=computed(()=>examples[props.lesson as keyof typeof examples])
const step=computed(()=>$renderContext.value==='print'?lesson.value.outputs.length-1:Math.min(lesson.value.outputs.length-1,Math.max(0,Number($clicks.value)||0)))
const active=computed(()=>$slidev.nav.currentPage===$page.value)
const root=ref<HTMLElement>()
const visibleStep=ref<number>()
const frame=()=>new Promise<void>(resolve=>requestAnimationFrame(()=>resolve()))

watch([step,active,$renderContext,root],async([target],_,onCleanup)=>{
 let cancelled=false
 onCleanup(()=>{cancelled=true})
 // Clear stale output immediately, including when stepping backwards.
 visibleStep.value=undefined
 if($renderContext.value==='print'){visibleStep.value=target;return}
 if(!active.value||!root.value)return
 await nextTick()
 // Magic Move updates its tokens in a nested Vue tick. Let those transitions start.
 await frame();await frame()
 if(cancelled)return
 const code=root.value.closest('[data-slidev-no]')?.querySelector('.slidev-code-magic-move')
 let animations=code?.getAnimations({subtree:true})??[]
 while(!cancelled&&animations.length){
  await Promise.allSettled(animations.map(animation=>animation.finished))
  animations=code?.getAnimations({subtree:true}).filter(animation=>animation.playState==='running'||animation.pending)??[]
 }
 if(!cancelled)visibleStep.value=target
},{immediate:true,flush:'post'})
</script>
<template><pre ref="root" class="code-walk-output" :data-lesson="props.lesson" :data-code-step="visibleStep" :data-pending-step="step">{{ visibleStep===undefined?'':lesson.outputs[visibleStep] }}</pre></template>
