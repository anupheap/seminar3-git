<script setup lang="ts">
import { computed, onBeforeUnmount, shallowRef, ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'
import snapshots from '../python_examples/visual_states.json'

type Primitive = {
  id: string; kind: string; points: number[]; opacity: number
  stroke?: string; fill?: string; width?: number; dashed?: boolean; arrow?: boolean
  text?: string; size?: number; anchor?: string; weight?: number
}
type Snapshot = { nodes: Primitive[]; caption: string; status: string; values: Record<string, unknown> }
type Lesson = { title: string; slide: number; states: Snapshot[] }

const props = defineProps<{ lesson: string }>()
const data = snapshots as unknown as Record<string, Lesson>
const { $clicks, $page } = useSlideContext()
const lesson = computed(() => data[props.lesson])
const step = computed(() => Math.min(lesson.value.states.length - 1, Math.max(0, Number($clicks.value) || 0)))
const snapshot = computed(() => lesson.value.states[step.value])
const markerId = `code-arrow-${$page.value}-${props.lesson}`
const frame = shallowRef<Primitive[]>([])
const animating = ref(false)
let request = 0

function targetNodes() {
  const current = new Map(snapshot.value.nodes.map(node => [node.id, node]))
  const all = new Map(lesson.value.states.flatMap(state => state.nodes).map(node => [node.id, node]))
  return [...all.values()].map(node => ({ ...node, ...(current.get(node.id) || { opacity: 0 }) }))
}

function move() {
  if (request) cancelAnimationFrame(request)
  const target = targetNodes()
  if (!frame.value.length || typeof window === 'undefined' || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    frame.value = target
    animating.value = false
    return
  }
  const previous = new Map(frame.value.map(node => [node.id, node]))
  const from = target.map(node => previous.get(node.id) || { ...node, opacity: 0 })
  const started = performance.now()
  animating.value = true
  const tick = (now: number) => {
    const progress = Math.min(1, (now - started) / 700)
    const eased = progress < .5 ? 4 * progress ** 3 : 1 - (-2 * progress + 2) ** 3 / 2
    frame.value = target.map((node, i) => {
      const old = from[i]
      return {
        ...(progress < .5 ? old : node),
        id: node.id,
        points: node.points.map((value, j) => old.points.length === node.points.length
          ? old.points[j] + (value - old.points[j]) * eased : value),
        opacity: old.opacity + (node.opacity - old.opacity) * eased,
      }
    })
    if (progress < 1) request = requestAnimationFrame(tick)
    else { frame.value = target; animating.value = false; request = 0 }
  }
  request = requestAnimationFrame(tick)
}

watch([step, () => props.lesson], move, { immediate: true })
onBeforeUnmount(() => { if (request) cancelAnimationFrame(request) })
const points = (node: Primitive) => node.points.reduce((s, value, i) => s + (i % 2 ? `${value} ` : `${value},`), '')
</script>

<template>
  <figure class="code-visual" :data-lesson="props.lesson" :data-step="step"
    :data-animating="String(animating)" :aria-label="`${lesson.title}, step ${step + 1}`">
    <svg viewBox="0 0 420 295" role="img" :aria-label="snapshot.caption">
      <defs>
        <marker :id="markerId" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
          <path d="M 0 0 L 10 5 L 0 10 z" fill="context-stroke" />
        </marker>
      </defs>
      <g v-for="node in frame" :key="node.id" :data-node="node.id" :opacity="node.opacity">
        <line v-if="node.kind === 'line'" :x1="node.points[0]" :y1="node.points[1]" :x2="node.points[2]" :y2="node.points[3]"
          :stroke="node.stroke" :stroke-width="node.width" :stroke-dasharray="node.dashed ? '4 4' : undefined"
          :marker-end="node.arrow ? `url(#${markerId})` : undefined" />
        <polyline v-else-if="node.kind === 'polyline'" :points="points(node)" :stroke="node.stroke" :stroke-width="node.width" :fill="node.fill || 'none'" />
        <polygon v-else-if="node.kind === 'polygon'" :points="points(node)" :stroke="node.stroke" :stroke-width="node.width" :fill="node.fill || 'none'" />
        <circle v-else-if="node.kind === 'circle'" :cx="node.points[0]" :cy="node.points[1]" :r="node.points[2]" :fill="node.fill" :stroke="node.stroke" :stroke-width="node.width" />
        <rect v-else-if="node.kind === 'rect'" :x="node.points[0]" :y="node.points[1]" :width="node.points[2]" :height="node.points[3]" :rx="node.points[4]" :fill="node.fill" :stroke="node.stroke" :stroke-width="node.width" />
        <text v-else-if="node.kind === 'text'" :x="node.points[0]" :y="node.points[1]" :fill="node.fill" :text-anchor="node.anchor"
          :style="{ fontSize: `${node.size || 15}px`, fontFamily: 'Segoe UI, Arial, sans-serif', fontWeight: node.weight || 400 }">{{ node.text }}</text>
      </g>
    </svg>
    <Transition name="visual-caption" mode="out-in">
      <figcaption :key="step" aria-live="polite">{{ snapshot.caption }}</figcaption>
    </Transition>
  </figure>
</template>
