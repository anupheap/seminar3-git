<script setup lang="ts">
const origin = { x: 192, y: 250 }
const scale = 55
const point = (x: number, y: number) => `${origin.x + x * scale},${origin.y - y * scale}`
</script>

<template>
  <figure class="source-vector-figure">
    <svg viewBox="0 0 430 330" role="img" aria-label="The vector (2, minus 1) plus twice the vector (minus 1, 2) reaches the target (0, 3).">
      <defs>
        <marker id="vector-arrow-blue" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#246a9c" /></marker>
        <marker id="vector-arrow-orange" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#c15b35" /></marker>
        <marker id="vector-arrow-ink" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#192b3a" /></marker>
      </defs>
      <g stroke="#d8ddd9" stroke-width="1">
        <line v-for="i in [-2,-1,0,1,2,3]" :key="`x-${i}`" :x1="origin.x+i*scale" y1="20" :x2="origin.x+i*scale" y2="300" />
        <line v-for="i in [-1,0,1,2,3,4]" :key="`y-${i}`" x1="38" :y1="origin.y-i*scale" x2="390" :y2="origin.y-i*scale" />
      </g>
      <g stroke="#657681" stroke-width="1.5"><line x1="38" :y1="origin.y" x2="390" :y2="origin.y" /><line :x1="origin.x" y1="20" :x2="origin.x" y2="300" /></g>
      <line :x1="origin.x" :y1="origin.y" :x2="origin.x+2*scale" :y2="origin.y+scale" stroke="#246a9c" stroke-width="4" marker-end="url(#vector-arrow-blue)" />
      <line :x1="origin.x+2*scale" :y1="origin.y+scale" :x2="origin.x" :y2="origin.y-3*scale" stroke="#c15b35" stroke-width="4" marker-end="url(#vector-arrow-orange)" />
      <line :x1="origin.x" :y1="origin.y" :x2="origin.x" :y2="origin.y-3*scale" stroke="#192b3a" stroke-width="3" stroke-dasharray="7 5" marker-end="url(#vector-arrow-ink)" />
      <circle :cx="origin.x" :cy="origin.y-3*scale" r="5" fill="#192b3a" />
      <text x="295" y="293" fill="#246a9c">a₁ = (2, −1)</text>
      <text x="40" y="80" fill="#c15b35">2a₂ = (−2, 4)</text>
      <text x="205" y="80" fill="#192b3a">b = (0, 3)</text>
    </svg>
    <figcaption>Follow the blue vector, then twice the orange column, to reach the target.</figcaption>
  </figure>
</template>
