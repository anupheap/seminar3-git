<script setup lang="ts">
import { onBeforeUnmount, ref, watch } from 'vue'
type Media = { src: string; start: number; end: number; left: number; top: number; width: number; height: number; crop: Record<string, number> }
const props = defineProps<{ media: Media; active: boolean; playing: boolean }>()
const video = ref<HTMLVideoElement>()
const src = `${import.meta.env.BASE_URL}${props.media.src.replace(/^\//, '')}`
function sync(restart = false) {
  const element = video.value
  if (!element) return
  if (!props.active || !props.playing) { element.pause(); return }
  if (restart || element.currentTime < props.media.start) element.currentTime = props.media.start
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) void element.play().catch(() => {})
}
function endTrim() {
  const element = video.value
  if (element && props.media.end > props.media.start && element.currentTime >= props.media.end) element.pause()
}
watch([() => props.active, () => props.playing, video], (_, old) => sync(!old || !old[0]), { flush: 'post' })
onBeforeUnmount(() => video.value?.pause())
</script>

<template>
  <div class="original-video" :style="{ left: `${media.left}%`, top: `${media.top}%`, width: `${media.width}%`, height: `${media.height}%` }"
    @click.stop @pointerdown.stop @keydown.stop>
    <video ref="video" :src="src" controls muted playsinline preload="metadata" aria-label="Original embedded PowerPoint video"
      @loadedmetadata="sync(true)" @timeupdate="endTrim" />
  </div>
</template>

<style scoped>
.original-video { position: absolute; overflow: hidden; }
video { width: 100%; height: 100%; object-fit: fill; }
</style>
