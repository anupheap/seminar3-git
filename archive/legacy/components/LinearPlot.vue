<script setup lang="ts">
const props = withDefaults(defineProps<{ mode?: 'rows' | 'space' }>(), { mode: 'rows' })
const originX = props.mode === 'rows' ? 93 : 72
const originY = props.mode === 'rows' ? 255 : 271
const sx = props.mode === 'rows' ? 62 : 55
const sy = props.mode === 'rows' ? 43 : 26
const px = (x: number) => originX + x * sx
const py = (y: number) => originY - y * sy
const row1 = `${px(-.7)},${py(-1.4)} ${px(2.7)},${py(5.4)}`
const row2 = `${px(-.7)},${py(1.15)} ${px(3.8)},${py(3.4)}`
const space = `${px(-.8)},${py(-1.6)} ${px(4.7)},${py(9.4)}`
</script>

<template>
  <figure class="plot-wrap">
    <svg viewBox="0 0 385 330" role="img" :aria-label="mode === 'rows' ? 'The lines 2x minus y equals zero and minus x plus 2y equals three intersect at one, two.' : 'The column space is the line b2 equals twice b1. The point four, eight is on the line and four, seven is off it.'">
      <defs><clipPath id="chart-area"><rect x="24" y="9" width="337" height="299" /></clipPath></defs>
      <g stroke="#d8ddd9" stroke-width="1" clip-path="url(#chart-area)">
        <line v-for="x in [0,1,2,3,4]" :key="`x${x}`" :x1="px(x)" y1="12" :x2="px(x)" y2="300" />
        <line v-for="y in [0,1,2,3,4,5,6,7,8,9]" :key="`y${y}`" x1="26" :y1="py(y)" x2="358" :y2="py(y)" />
      </g>
      <g stroke="#657681" stroke-width="1.4">
        <line x1="25" :y1="py(0)" x2="360" :y2="py(0)" />
        <line :x1="px(0)" y1="12" :x2="px(0)" y2="300" />
      </g>
      <g fill="#657681" font-size="13">
        <text v-for="x in [1,2,3,4]" :key="x" :x="px(x)-4" :y="py(0)+18">{{ x }}</text>
        <text :x="px(0)-18" :y="py(0)+17">0</text>
        <text x="362" :y="py(0)+5">{{ mode === 'rows' ? 'x' : 'b₁' }}</text>
        <text :x="px(0)-19" y="16">{{ mode === 'rows' ? 'y' : 'b₂' }}</text>
      </g>
      <template v-if="mode === 'rows'">
        <g clip-path="url(#chart-area)">
          <polyline :points="row1" stroke="#246a9c" fill="none" stroke-width="3" />
          <polyline :points="row2" stroke="#c15b35" fill="none" stroke-width="3" />
        </g>
        <circle :cx="px(1)" :cy="py(2)" r="6" fill="#192b3a" stroke="#f7f5ee" stroke-width="2" />
        <text :x="px(1)+11" :y="py(2)+23" fill="#192b3a" font-size="17" font-weight="600">(1, 2)</text>
        <text x="177" y="26" fill="#246a9c" font-size="16">2x − y = 0</text>
        <text x="202" y="119" fill="#c15b35" font-size="16">−x + 2y = 3</text>
      </template>
      <template v-else>
        <polyline :points="space" stroke="#246a9c" fill="none" stroke-width="3" clip-path="url(#chart-area)" />
        <circle :cx="px(4)" :cy="py(8)" r="6" fill="#246a9c" stroke="#f7f5ee" stroke-width="2" />
        <circle :cx="px(4)" :cy="py(7)" r="6" fill="#c15b35" stroke="#f7f5ee" stroke-width="2" />
        <text x="169" y="24" fill="#246a9c" font-size="16">b₂ = 2b₁</text>
        <text :x="px(4)-89" :y="py(8)-7" fill="#246a9c" font-size="16">(4, 8)</text>
        <text :x="px(4)+12" :y="py(7)+16" fill="#c15b35" font-size="16">(4, 7)</text>
      </template>
    </svg>
    <figcaption class="plot-key">{{ mode === 'rows' ? 'Each row describes a line. The solution lies on both.' : 'Only right-hand sides on the blue line are achievable.' }}</figcaption>
  </figure>
</template>
