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
const additionRoot=ref<HTMLElement>()
const previousOutput=ref('')
const addedOutput=ref('')
const frame=()=>new Promise<void>(resolve=>requestAnimationFrame(()=>resolve()))

watch([step,active,$renderContext,root],async([target],old,onCleanup)=>{
 let cancelled=false
 let animationFrame:number|undefined
 onCleanup(()=>{cancelled=true;if(animationFrame!==undefined)cancelAnimationFrame(animationFrame)})
 const output=lesson.value.outputs[target]
 previousOutput.value='';addedOutput.value=''
 if($renderContext.value==='print'){previousOutput.value=output;return}
 if(!active.value||!root.value)return
 const advancing=old?.[1]&&target>old[0]
 const prefix=advancing?lesson.value.outputs[Math.max(0,target-1)]:''
 previousOutput.value=output.startsWith(prefix)?prefix:''
 addedOutput.value=output.slice(previousOutput.value.length)
 if(!addedOutput.value)return
 await nextTick()
 // Match the new result to the actual statement entrance, including its stagger.
 await frame();await frame()
 if(cancelled)return
 const code=root.value.closest('[data-slidev-no]')?.querySelector('.shiki-magic-move-container')
 const lines:Element[][]=[[]]
 for(const token of Array.from(code?.children??[])){
  if(token.classList.contains('shiki-magic-move-leave-active'))continue
  if(token.tagName==='BR')lines.push([])
  else if(token.classList.contains('shiki-magic-move-item'))lines[lines.length-1].push(token)
 }
 const line=lesson.value.outputLines[target]
 const tokens=line?lines[line-1]??[]:[]
 const entrance=tokens.find(token=>token.textContent?.trim()&&token.classList.contains('shiki-magic-move-enter-active'))
  ??tokens.find(token=>token.getAnimations().some(animation=>animation.effect?.getKeyframes().some(key=>'opacity' in key)))
 const element=additionRoot.value
 if(!element)return
 if(!entrance){element.style.opacity='1';return}
 // Mirror the live token rather than a timer: Magic Move can retime transitions
 // while updating highlighting, and fast clicks can cancel an entrance.
 const sync=()=>{
  if(cancelled)return
  element.style.opacity=getComputedStyle(entrance).opacity
  if(entrance.getAnimations().some(animation=>animation.playState==='running'||animation.pending))animationFrame=requestAnimationFrame(sync)
 }
 sync()
},{immediate:true,flush:'post'})
</script>
<template><pre ref="root" class="code-walk-output" :data-lesson="props.lesson" :data-code-step="step">{{ previousOutput }}<span v-if="addedOutput" :key="step" ref="additionRoot" class="code-output-addition" style="opacity:0">{{ addedOutput }}</span></pre></template>
