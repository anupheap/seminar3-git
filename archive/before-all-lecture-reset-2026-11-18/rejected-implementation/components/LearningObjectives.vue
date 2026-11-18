<script setup lang="ts">
import { ref, watch } from 'vue'
import artwork from '../sources/learning-objectives.json'
import edits from '../sources/deck-edits.json'

const props = defineProps<{ active: boolean; print: boolean }>()
const run = ref(0)
const layers = artwork.layers.filter(layer => !edits.hiddenObjectiveShapes.includes(layer.shape))
watch(() => props.active, active => { if (active) run.value++ }, { immediate: true })
const url = (path: string) => `${import.meta.env.BASE_URL}${path.replace(/^\//, '')}`
</script>

<template>
  <div class="learning-objectives" :class="{ 'learning-objectives-print': print }" :data-active="active" aria-label="Learning Objectives">
      <img class="original-frame objectives-background" :src="url(artwork.background)" alt="" />
      <div :key="run" class="objectives-elements">
        <img v-for="layer in layers" :key="layer.shape" class="objective-element"
          :src="url(layer.src)" :alt="layer.label" :data-element="layer.shape" :data-motion="layer.motion"
          :style="{ left: `${layer.box[0]}%`, top: `${layer.box[1]}%`, width: `${layer.box[2]}%`, height: `${layer.box[3]}%`,
            animationName: `objective-${layer.motion}`, animationDelay: `${layer.delay}s`, animationDuration: `${layer.duration}s`,
            transformOrigin: layer.motion === 'grow-x' ? 'left center' : layer.motion === 'grow-y' ? 'center top' : `${layer.origin[0]}% ${layer.origin[1]}%` }" />
      </div>
  </div>
</template>

<style>
.learning-objectives, .objectives-elements { position: absolute; inset: 0; }
.learning-objectives { overflow: hidden; }
.objective-element { position: absolute; max-width: none; animation-fill-mode: both; animation-timing-function: cubic-bezier(.18,.72,.25,1); }
[data-active="false"] .objective-element { visibility: hidden; animation: none !important; }
.learning-objectives-print .objective-element { visibility: visible !important; animation: none !important; opacity: 1; transform: none; clip-path: none; }
@keyframes objective-top { from { opacity: 0; transform: translateY(-100%); } to { opacity: 1; transform: translateY(0); } }
@keyframes objective-bottom { from { opacity: 0; transform: translateY(100%); } to { opacity: 1; transform: translateY(0); } }
@keyframes objective-left { from { opacity: 0; transform: translateX(-100%); } to { opacity: 1; transform: translateX(0); } }
@keyframes objective-right { from { opacity: 0; transform: translateX(100%); } to { opacity: 1; transform: translateX(0); } }
@keyframes objective-grow-x { from { opacity: 0; clip-path: inset(0 100% 0 0); } to { opacity: 1; clip-path: inset(0); } }
@keyframes objective-grow-y { from { opacity: 0; clip-path: inset(0 0 100% 0); } to { opacity: 1; clip-path: inset(0); } }
@keyframes objective-fade { from { opacity: 0; } to { opacity: 1; } }
@media (prefers-reduced-motion: reduce) { .objective-element { animation-duration: 0ms !important; animation-delay: 0ms !important; } }
</style>
