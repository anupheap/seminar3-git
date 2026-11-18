<script setup lang="ts">
import {computed,onBeforeUnmount,ref,watch} from 'vue'
import {useSlideContext} from '@slidev/client'
const {$slidev,$page,$clicks,$renderContext}=useSlideContext()
const video=ref<HTMLVideoElement>()
const src=`${import.meta.env.BASE_URL}animations/lecture6/SubspaceClosure.mp4`
const active=computed(()=>$slidev.nav.currentPage===$page.value)
const stage=computed(()=>Math.min(2,Math.max(0,Number($clicks.value)||0)))
const cues=[0,2.2,4.4,7]
let frame:number|undefined
function tick(){const v=video.value;if(!v)return;if(v.currentTime>=cues[stage.value+1]-.025){v.pause();return}frame=v.requestVideoFrameCallback(tick)}
function sync(){const v=video.value;if(!v||v.readyState<1)return;if(!active.value){v.pause();return}if(frame!==undefined)v.cancelVideoFrameCallback(frame);const reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;v.currentTime=$renderContext.value==='print'?6.9:reduced?cues[stage.value+1]-.06:cues[stage.value];if(!reduced&&$renderContext.value!=='print')void v.play().then(()=>{frame=v.requestVideoFrameCallback(tick)}).catch(()=>{})}
watch([active,stage,video],sync,{flush:'post'})
onBeforeUnmount(()=>{video.value?.pause();if(frame!==undefined)video.value?.cancelVideoFrameCallback(frame)})
</script>
<template><video ref="video" class="l6-film" :src="src" muted playsinline preload="auto" aria-label="Manim animation: vector addition and scaling stay in a plane through zero" @loadedmetadata="sync" /></template>
