<script setup lang="ts">
import { computed, useId } from 'vue'
import { useSlideContext } from '@slidev/client'
const props=defineProps<{kind:'map'|'columns'|'union'|'null'|'family'|'code-columns'|'code-null';stage?:number}>()
const {$clicks,$renderContext}=useSlideContext()
const stage=computed(()=>props.stage??($renderContext.value==='print'?3:Number($clicks.value)||0))
const id=useId().replaceAll(':','')
const blue='#58c4dd',green='#83c167',gold='#f0ac5f',yellow='#ffea94',red='#fc6255'
const project=([x,y,z]:number[])=>[220+40*x-28*y,170+14*x+14*y-42*z]
const p=(x:number,y:number,z=0)=>project([x,y,z])
const pts=(points:number[][])=>points.map(point=>point.join(',')).join(' ')
const plane=pts([p(-2,-2),p(2,-2),p(2,2),p(-2,2)])
const column=computed(()=>['columns','code-columns'].includes(props.kind))
const family=computed(()=>props.kind==='family'||(props.kind==='code-null'&&stage.value>=3))
const direction=computed(()=>[1,1,-1])
const t=computed(()=>props.kind==='code-null'?(stage.value>=4?2:stage.value===3?0:1):[0,1,-1,2][Math.min(stage.value,3)])
const point=computed(()=>project(direction.value.map((v,i)=>v*t.value+(family.value&&i===0?1:0))))
const end=(sign:number)=>project(direction.value.map((v,i)=>sign*2.1*v+(family.value&&i===0?1:0)))
</script>

<template>
 <figure class="l6-diagram" :data-diagram="kind" :data-step="stage">
  <svg viewBox="0 0 440 340" role="img" :aria-label="kind==='map'?'A maps inputs in R three to outputs in R four, with a nullspace line and a column-space plane':column?'Column combinations in coefficient coordinates':kind==='union'?'A plane and line through zero, with a sum outside their union':'A line of input vectors in three-dimensional space'">
   <defs><marker :id="id+'-arrow'" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="context-stroke" /></marker></defs>
   <template v-if="kind==='map'">
    <text x="35" y="52" :fill="yellow">input space ℝ³</text>
    <text x="273" y="52" :fill="blue">output space ℝ⁴</text>
    <g stroke="#6d7882" stroke-width="1.5" fill="none">
     <path d="M98 240V92M48 201L154 132M51 145L158 222" />
     <path d="M333 248V94M273 208L400 141M276 142L395 217" />
    </g>
    <line x1="56" y1="224" x2="143" y2="118" :stroke="yellow" stroke-width="3" />
    <circle cx="98" cy="173" r="4" fill="white" />
    <text x="23" y="258" :fill="yellow">N(A): Ax = 0</text>
    <polygon points="282,195 326,112 399,147 354,230" :fill="blue" fill-opacity=".18" :stroke="blue" stroke-width="2" />
    <text x="273" y="271" :fill="blue">C(A): b = Ax</text>
    <path d="M169 170H259" :stroke="gold" stroke-width="3" :marker-end="`url(#${id}-arrow)`" />
    <text x="206" y="151" :fill="gold">A</text>
   </template>
   <template v-else-if="column">
    <g stroke="#252a30" stroke-width="1"><line v-for="i in 7" :key="'h'+i" x1="55" :y1="35+i*35" x2="405" :y2="35+i*35" /><line v-for="i in 10" :key="'v'+i" :x1="55+i*35" y1="35" :x2="55+i*35" y2="300" /></g>
    <path d="M55 230H405M160 300V35" stroke="#737d86" stroke-width="1.5" fill="none" :marker-end="`url(#${id}-arrow)`" />
    <path d="M160 230H230" :stroke="blue" stroke-width="3" :marker-end="`url(#${id}-arrow)`" />
    <path d="M160 230V160" :stroke="green" stroke-width="3" :marker-end="`url(#${id}-arrow)`" />
    <path d="M160 230L230 160" :stroke="gold" stroke-width="2.5" :stroke-dasharray="kind==='code-columns'&&stage>=1?'5 5':undefined" :marker-end="`url(#${id}-arrow)`" />
    <text x="234" y="251" :fill="blue">a₁</text><text x="130" y="151" :fill="green">a₂</text><text x="237" y="151" :fill="gold">a₃ = a₁ + a₂</text>
    <g v-if="kind==='code-columns'&&stage>=2" class="l6-reveal"><path d="M160 230L300 300" stroke="#d147bd" stroke-width="3" :marker-end="`url(#${id}-arrow)`" /><text x="307" y="304" fill="#dc75cd">b</text></g>
    <circle cx="160" cy="230" r="3.5" fill="white" /><text x="143" y="253" fill="#aaa">0</text>
   </template>
   <template v-else>
    <g stroke="#626b74" stroke-width="1.25"><line v-for="axis in [[2.7,0,0],[0,2.7,0],[0,0,2.7]]" :key="axis.join()" :x1="p(0,0)[0]" :y1="p(0,0)[1]" :x2="project(axis)[0]" :y2="project(axis)[1]" :marker-end="`url(#${id}-arrow)`" /></g>
    <text :x="p(2.9,0)[0]" :y="p(2.9,0)[1]+5" fill="#8d969e">x₁</text><text :x="p(0,2.9)[0]-22" :y="p(0,2.9)[1]+5" fill="#8d969e">x₂</text><text :x="p(0,0,2.9)[0]-8" :y="p(0,0,2.9)[1]-6" fill="#8d969e">x₃</text>
    <template v-if="kind==='union'">
     <polygon :points="plane" :fill="blue" fill-opacity=".10" :stroke="blue" stroke-opacity=".5" />
     <line :x1="p(0,0,-2.5)[0]" :y1="p(0,0,-2.5)[1]" :x2="p(0,0,2.5)[0]" :y2="p(0,0,2.5)[1]" :stroke="yellow" stroke-width="2.5" />
     <path :d="`M220 170L${p(1.3,1)[0]} ${p(1.3,1)[1]}`" :stroke="blue" stroke-width="3" :marker-end="`url(#${id}-arrow)`" />
     <path :d="`M220 170L${p(0,0,1.7)[0]} ${p(0,0,1.7)[1]}`" :stroke="yellow" stroke-width="3" :marker-end="`url(#${id}-arrow)`" />
     <text x="92" y="230" :fill="blue">P</text><text x="235" y="60" :fill="yellow">L</text>
     <g :opacity="stage>=1?1:0" class="l6-fade"><line :x1="p(1.3,1)[0]" :y1="p(1.3,1)[1]" :x2="p(1.3,1,1.7)[0]" :y2="p(1.3,1,1.7)[1]" stroke="#555" stroke-dasharray="4 4" /><path :d="`M220 170L${p(1.3,1,1.7)[0]} ${p(1.3,1,1.7)[1]}`" :stroke="red" stroke-width="3" :marker-end="`url(#${id}-arrow)`" /><text x="265" y="120" :fill="red">u + v</text></g>
     <circle v-if="stage>=2" cx="220" cy="170" r="8" fill="none" stroke="white" stroke-width="2" />
    </template>
    <g v-else :opacity="kind==='code-null'&&stage===0?0:1" class="l6-fade">
     <line :x1="end(-1)[0]" :y1="end(-1)[1]" :x2="end(1)[0]" :y2="end(1)[1]" :stroke="yellow" stroke-width="2.5" />
     <g class="l6-moving-point" :style="{transform:`translate(${point[0]}px,${point[1]}px)`}"><circle r="6" :fill="yellow" /><text x="14" y="5" :fill="yellow">{{ family?'x₀ + t n':`${t} n` }}</text></g>
     <text x="58" y="303" :fill="yellow">{{ family?'A(x₀ + t n) = Ax₀':'A(t n) = 0' }}</text>
    </g>
    <circle cx="220" cy="170" r="3.5" fill="white" /><text x="201" y="187" fill="#aaa">0</text>
   </template>
  </svg>
 </figure>
</template>
