<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'
import lecture2 from '../sources/lecture2-native.json'
import lecture3 from '../sources/lecture3-native.json'
import lecture5 from '../sources/lecture5-native.json'
import lecture3Layout from '../sources/lecture3-layout.json'

const props = defineProps<{ lecture: number; slide: number; hideShapes?: number[] }>()
const source = computed(() => ({2:lecture2,3:lecture3,5:lecture5})[props.lecture as 2 | 3 | 5])
const { $slidev, $page, $clicks, $renderContext } = useSlideContext()
const page = computed(() => source.value.slides.find(item => item.number === props.slide)!)
const objects = computed(() => page.value.objects.filter(item => !props.hideShapes?.includes(item.id)))
const layout = computed(() => props.lecture===3 ? lecture3Layout[String(props.slide) as keyof typeof lecture3Layout] as Record<string,{box:number[];stretch?:boolean;maxScale?:number;svg?:string;role?:string}> : undefined)
const active = computed(() => $slidev.nav.currentPage === $page.value)
const step = computed(() => Number($clicks.value) || 0)
const print = computed(() => $renderContext.value === 'print')
const root = ref<SVGSVGElement>()
const ready = ref(false)
const reduce = ref(false)
const animate = ref(true)
const run = ref(0)
const origins = ref<Record<number, string>>({})
const boxes = ref<Record<number, { x: number; y: number; width: number; height: number }>>({})
const frameCallbacks = new Map<number, number>()
let preference: MediaQueryList | undefined
const url = (path: string) => `${import.meta.env.BASE_URL}${path.replace(/^\//, '')}`

function effectFor(id: number) {
  return page.value.effects.find(effect => effect.shape === id && effect.type < 80)
}
function visible(id: number) {
  if (print.value) return true
  const effect = effectFor(id)
  return !effect || (effect.exit ? step.value < effect.step : step.value >= effect.step)
}
function motion(id: number) {
  const effect = effectFor(id)
  if (!ready.value || !effect || print.value || reduce.value || !animate.value || !active.value || step.value !== effect.step)
    return { animationName: 'none' }
  const names: Record<number, string> = { 1: 'l1-source-appear', 2: 'l1-source-fly', 10: 'l1-source-fade', 22: 'none', 23: 'l1-source-zoom' }
  const directions: Record<number, string[]> = {
    1: ['0px', '760px'], 2: ['-1320px', '0px'], 3: ['1320px', '0px'], 4: ['0px', '-760px'],
  }
  const [x, y] = directions[effect.direction] || ['0px', '35px']
  const item = page.value.objects.find(object => object.id === id)!
  return {
    animationName: names[effect.type] || 'l1-source-fade',
    animationDuration: `${effect.type === 1 ? .001 : effect.duration}s`, animationDelay: `${effect.delay}s`,
    ...(effect.type === 1 ? { animationTimingFunction: 'steps(1,end)' } : {}),
    transformOrigin: origins.value[id] || `${item.bounds[0] + item.bounds[2] / 2}px ${item.bounds[1] + item.bounds[3] / 2}px`,
    '--l1-fly-x': x, '--l1-fly-y': y,
  }
}
const wipes = computed(() => page.value.effects.filter(effect => effect.type === 22))
const wipeId = (id: number) => `l1-wipe-${$page.value}-${id}`
function wiping(id: number) {
  const effect = effectFor(id)
  return ready.value && effect?.type === 22 && active.value && animate.value && !reduce.value && !print.value && step.value === effect.step
}
function objectTransform(id:number){
  const target=layout.value?.[id],measured=boxes.value[id]
  if(!target||!measured||measured.width<=4||measured.height<=4)return undefined
  const x=measured.x+2,y=measured.y+2,w=measured.width-4,h=measured.height-4
  const [left,top,width,height]=target.box
  // A nearly horizontal line must keep its stroke thickness when moved.
  if(w<1||h<1)return `translate(${left-x} ${top-y})`
  const scale=Math.min(width/w,height/h,target.maxScale??Infinity)
  const sx=target.stretch?width/w:scale,sy=target.stretch?height/h:scale
  return `translate(${left-x*sx} ${top-y*sy}) scale(${sx} ${sy})`
}
function markup(svg: string,id:number) {
  // Original source images are the only image elements in these SVG objects.
  return (layout.value?.[id]?.svg??svg).replaceAll('="/sources/', `="${url('/sources/')}`)
}
async function measure() {
  await nextTick()
  const next: Record<number, string> = {}
  const nextBoxes: typeof boxes.value = {}
  root.value?.querySelectorAll<SVGGElement>('.l1-source-geometry').forEach(element => {
    const b = element.getBBox()
    next[Number(element.dataset.shape)] = `${b.x + b.width / 2}px ${b.y + b.height / 2}px`
    nextBoxes[Number(element.dataset.shape)] = { x: b.x - 2, y: b.y - 2, width: b.width + 4, height: b.height + 4 }
  })
  origins.value = next
  boxes.value = nextBoxes
}
function mediaElement(id: number) {
  return root.value?.querySelector<HTMLVideoElement>(`[data-video-shape="${id}"]`)
}
function syncMedia(restart = false) {
  for (const item of page.value.objects) {
    if (!('media' in item)) continue
    const video = mediaElement(item.id)
    if (!video) continue
    const media = item.media!
    if (!active.value || print.value || reduce.value) { video.pause(); continue }
    if (restart || video.currentTime < media.start) video.currentTime = media.start
    if (!restart && video.currentTime >= media.end) { video.pause(); continue }
    if (!reduce.value) void video.play().catch(() => {})
  }
}
function mediaStyle(crop: Record<string, number>) {
  const width = 1 - (crop.l || 0) - (crop.r || 0)
  const height = 1 - (crop.t || 0) - (crop.b || 0)
  return { left: `${-(crop.l || 0) / width * 100}%`, top: `${-(crop.t || 0) / height * 100}%`, width: `${100 / width}%`, height: `${100 / height}%` }
}
function trim(id: number) {
  const item = page.value.objects.find(object => object.id === id)
  if (!item || !('media' in item)) return
  const video = mediaElement(id)
  if (video && video.currentTime >= item.media!.end) video.pause()
}
function watchFrames(id: number) {
  const video = mediaElement(id)
  if (!video?.requestVideoFrameCallback) return
  const previous = frameCallbacks.get(id)
  if (previous !== undefined) video.cancelVideoFrameCallback(previous)
  frameCallbacks.set(id, video.requestVideoFrameCallback(() => {
    trim(id)
    if (!video.paused) watchFrames(id)
  }))
}
function updatePreference() { reduce.value = preference?.matches || false; syncMedia() }

watch([active, step], ([isActive, current], previous) => {
  animate.value = isActive && (!previous || !previous[0] || current === previous[1] + 1)
  if (isActive && (!previous || !previous[0])) run.value++
  // Slidev can mount upcoming slides while hidden, when SVG getBBox is empty.
  if (isActive && props.lecture===3) void nextTick(measure)
  void nextTick(() => syncMedia(!previous || !previous[0]))
}, { immediate: true })
onMounted(async () => {
  preference = window.matchMedia('(prefers-reduced-motion: reduce)')
  updatePreference()
  preference.addEventListener('change', updatePreference)
  await document.fonts.ready
  await measure()
  ready.value = true
  syncMedia(true)
})
onBeforeUnmount(() => {
  preference?.removeEventListener('change', updatePreference)
  root.value?.querySelectorAll('video').forEach(video => {
    video.pause()
    const frame = frameCallbacks.get(Number(video.dataset.videoShape))
    if (frame !== undefined) video.cancelVideoFrameCallback?.(frame)
  })
})
</script>

<template>
  <main class="l1-source-slide ppt-source-slide" :class="{'lecture-three-theme':lecture===3}" :data-lecture="lecture" :data-source-slide="slide" :style="{ backgroundColor: lecture===3?'#faf9f5':page.backgroundColor }" :data-step="step" :data-run="run" :aria-label="`Lecture ${lecture}, original PowerPoint content`">
    <svg ref="root" class="l1-source-canvas" :viewBox="`0 0 ${source.width} ${source.height}`" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <defs>
        <clipPath v-for="effect in wipes" :id="wipeId(effect.shape)" :key="effect.shape" clipPathUnits="userSpaceOnUse">
          <rect v-if="boxes[effect.shape]" v-bind="boxes[effect.shape]" class="l1-source-wipe-window"
            :style="{ animationName: wiping(effect.shape) ? 'l1-source-wipe-rect' : 'none', animationDuration: `${effect.duration}s`, animationDelay: `${effect.delay}s`, transformOrigin: `${boxes[effect.shape].x}px ${boxes[effect.shape].y}px` }" />
        </clipPath>
      </defs>
      <image v-if="page.background" class="l1-source-background" :href="url(page.background)" :width="source.width" :height="source.height" preserveAspectRatio="none" aria-hidden="true" />
      <line v-if="lecture===3&&slide!==1" class="lecture-three-title-rule" x1="56" y1="126" x2="1224" y2="126" aria-hidden="true" />
      <g v-for="item in objects" :key="item.id" class="l1-source-object" :data-shape="item.id" :data-visible="visible(item.id)"
        :data-design-role="layout?.[item.id]?.role"
        :transform="objectTransform(item.id)"
        :style="{ visibility: ready && visible(item.id) ? 'visible' : 'hidden', ...motion(item.id) }">
        <g class="l1-source-geometry" :data-shape="item.id" :clip-path="wiping(item.id) ? `url(#${wipeId(item.id)})` : undefined" v-html="markup(item.svg,item.id)" />
        <foreignObject v-if="'media' in item && !print" :x="item.bounds[0]" :y="item.bounds[1]" :width="item.bounds[2]" :height="item.bounds[3]">
          <div class="l1-source-media-frame">
            <video :data-video-shape="item.id" :src="url(item.media!.src)" :style="mediaStyle(item.media!.crop)" muted playsinline preload="metadata"
              aria-label="Original embedded geometry video" @loadedmetadata="syncMedia(true)" @timeupdate="trim(item.id)" @play="watchFrames(item.id)" />
          </div>
        </foreignObject>
      </g>
    </svg>
  </main>
</template>
