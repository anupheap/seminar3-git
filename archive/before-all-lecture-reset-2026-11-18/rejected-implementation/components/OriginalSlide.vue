<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'
import sources from '../sources/powerpoint.json'
import canva from '../sources/canva.json'
import OriginalVideo from './OriginalVideo.vue'
import LearningObjectives from './LearningObjectives.vue'

const props = defineProps<{ deck: string; slide: number }>()
const objectives = computed(() => props.deck === 'Seminar' && props.slide === 3)
const { $slidev, $page, $clicks, $renderContext } = useSlideContext()
const deck = computed(() => sources.find(item => item.id === props.deck))
const page = computed(() => props.deck === 'CanvaLecture9'
  ? canva.pages.find(item => item.number === props.slide)!
  : deck.value!.slides.find(item => item.number === props.slide)!)
const ppt = computed(() => props.deck === 'CanvaLecture9' ? undefined : deck.value!.slides.find(item => item.number === props.slide))
const active = computed(() => $slidev.nav.currentPage === $page.value)
const stage = computed(() => Number($clicks.value) || 0)
const print = computed(() => $renderContext.value === 'print')
const reduced = ref(false)
const settled = ref(false)
const animate = ref(true)
const run = ref(0)
let timer: ReturnType<typeof setTimeout> | undefined
let media: MediaQueryList | undefined
const url = (path: string) => `${import.meta.env.BASE_URL}${path.replace(/^\//, '')}`
const effectFor = (shape: number) => ppt.value?.effects.find(effect => effect.shape === shape && effect.type < 80)
const isVisible = (shape: number) => !effectFor(shape) || stage.value >= effectFor(shape)!.step

function effectStyle(shape: number) {
  const effect = effectFor(shape)
  const layer = ppt.value?.layers.find(item => item.shape === shape)
  if (!effect || !animate.value || reduced.value || stage.value !== effect.step)
    return { animationName: 'none' }
  const names: Record<number, string> = { 1: 'ppt-appear', 2: 'ppt-fly', 10: 'ppt-fade', 22: 'ppt-wipe', 23: 'ppt-zoom' }
  const directions: Record<number, string[]> = { 1: ['0', '100%'], 2: ['-100%', '0'], 3: ['100%', '0'], 4: ['0', '-100%'] }
  const [x, y] = directions[effect.direction] || ['0', '12%']
  return { animationName: names[effect.type] || 'ppt-fade', animationDuration: `${effect.duration}s`,
    animationDelay: `${effect.delay}s`, '--fly-x': x, '--fly-y': y,
    transformOrigin: layer?.origin ? `${layer.origin[0]}% ${layer.origin[1]}%` : 'center',
    '--wipe-hidden': `${100 - (layer?.bounds?.[0] || 0)}%`,
    '--wipe-visible': `${100 - (layer?.bounds?.[0] || 0) - (layer?.bounds?.[2] || 100)}%` }
}

function updateMotion() { reduced.value = media?.matches || false }
onMounted(() => {
  media = window.matchMedia('(prefers-reduced-motion: reduce)')
  updateMotion()
  media.addEventListener('change', updateMotion)
})
watch([active, stage, reduced], ([isActive, current], previous) => {
  clearTimeout(timer)
  settled.value = false
  if (!isActive) return
  run.value++
  animate.value = !previous || !previous[0] || current === previous[1] + 1
  if (current < (ppt.value?.clicks || 0)) return
  const finish = Math.max(0, ...(ppt.value?.effects || []).filter(effect => effect.step === current).map(effect => effect.delay + effect.duration))
  timer = setTimeout(() => { settled.value = true }, !animate.value || reduced.value ? 0 : finish * 1000 + 80)
}, { immediate: true })
onBeforeUnmount(() => { clearTimeout(timer); media?.removeEventListener('change', updateMotion) })
</script>

<template>
  <div class="original-slide" :data-deck="props.deck" :data-original-slide="props.slide" :data-step="stage">
    <LearningObjectives v-if="objectives" :active="active" :print="print" />
    <img v-else-if="!ppt?.layers.length || print" class="original-frame" :src="url(page.image)" :alt="ppt?.text || `Canva Lecture 9, original page ${slide}`" />
    <template v-else>
      <img class="original-frame" :src="url(ppt.background)" alt="" />
      <img v-for="layer in ppt.layers" :key="`${run}-${layer.shape}`" class="original-frame original-layer"
        :src="url(layer.src)" alt="" :style="{ ...effectStyle(layer.shape), visibility: isVisible(layer.shape) ? 'visible' : 'hidden' }"
        :data-shape="layer.shape" :data-visible="isVisible(layer.shape)" />
      <img v-if="settled && !ppt.media?.length" class="original-frame original-final" :src="url(page.image)" :alt="ppt.text" />
    </template>
    <OriginalVideo v-for="item in ppt?.media || []" :key="item.shape" :media="item" :active="active"
      :playing="stage < (ppt?.effects.find(effect => effect.type === 84)?.step ?? Infinity)" />
    <nav v-if="ppt?.links.length" class="source-toolbar" aria-label="Linked demonstrations" @click.stop @pointerdown.stop @keydown.stop>
      <a v-for="(link, i) in ppt?.links || []" :key="link" :href="link" target="_blank" rel="noopener">Linked demo {{ i + 1 }}</a>
    </nav>
  </div>
</template>
