<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'

const props = withDefaults(defineProps<{
  src: string
  poster?: string
  label?: string
  active?: boolean
  autoplay?: boolean
  loop?: boolean
}>(), { label: 'Animation', active: true, autoplay: true, loop: true })

const video = ref<HTMLVideoElement>()
const hovered = ref(false)
const keyboardFocus = ref(false)
const touchControls = ref(false)
const reducedMotion = ref(typeof window !== 'undefined' && window.matchMedia('(prefers-reduced-motion: reduce)').matches)
const showControls = computed(() => hovered.value || keyboardFocus.value || touchControls.value)
let media: MediaQueryList | undefined
const updateMotion = (event: MediaQueryListEvent) => { reducedMotion.value = event.matches }

onMounted(() => {
  media = window.matchMedia('(prefers-reduced-motion: reduce)')
  reducedMotion.value = media.matches
  media.addEventListener('change', updateMotion)
})
onBeforeUnmount(() => {
  media?.removeEventListener('change', updateMotion)
  video.value?.pause()
})

watch([video, () => props.active, () => props.autoplay, () => props.src, reducedMotion] as const,
  ([element, active, autoplay, src, reduce], previous) => {
    if (!element) return
    if (previous && previous[3] !== src) element.load()
    if (!active) {
      element.pause()
      hovered.value = keyboardFocus.value = touchControls.value = false
      return
    }
    if (autoplay && !reduce) {
      element.currentTime = 0
      void element.play().catch(() => {})
    } else element.pause()
  }, { immediate: true, flush: 'post' })

function enter(event: PointerEvent) {
  if (event.pointerType !== 'touch') hovered.value = true
}
function pointerDown(event: PointerEvent) {
  keyboardFocus.value = false
  if (event.pointerType === 'touch') touchControls.value = true
}
function focus() {
  keyboardFocus.value = !!video.value?.matches(':focus-visible')
}
</script>

<template>
  <div class="hover-video" :data-controls="String(showControls)"
    @pointerenter="enter" @pointerleave="hovered = false" @pointerdown="pointerDown">
    <video ref="video" :controls="showControls" :loop="props.loop" muted playsinline
      preload="metadata" :poster="props.poster" :aria-label="props.label" tabindex="0"
      @focus="focus" @blur="keyboardFocus = false">
      <source :src="props.src" type="video/mp4">
      Your browser does not support video playback.
    </video>
  </div>
</template>

<style scoped>
.hover-video { width: 100%; overflow: hidden; border-radius: 3px; background: #13222f; }
.hover-video video { display: block; width: 100%; }
</style>
