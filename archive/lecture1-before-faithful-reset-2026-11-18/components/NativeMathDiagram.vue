<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
const props=withDefaults(defineProps<{ kind: string; stage?: number }>(),{stage:-1})
const { $clicks, $page }=useSlideContext()
const step=computed(()=>props.stage>=0?props.stage:Math.max(0,Number($clicks.value)||0))
const marker=`native-arrow-${$page.value}-${props.kind}`
const x=(v:number)=>180+75*v
const y=(v:number)=>285-45*v
const project=(v:number[])=>[230+18*(v[0]-.65*v[1]),270+18*(.3*v[0]+.25*v[1]-.95*v[2])]
const line3=(a:number[],b:number[])=>{const p=project(a),q=project(b);return {x1:p[0],y1:p[1],x2:q[0],y2:q[1]}}
const points=(values:number[][])=>values.map(project).map(v=>v.join(',')).join(' ')
const origin=[0,0,0]
const a=[3,2,5],b=[4,7,2],c=[7,9,7]
</script>

<template>
  <svg class="native-math-diagram" viewBox="0 0 520 360" role="img" :aria-label="kind">
    <defs><marker :id="marker" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="context-stroke" /></marker></defs>
    <template v-if="['rows','columns','independent','dependent','plane2','zero'].includes(kind)">
      <g class="diagram-grid"><line v-for="n in [-1,0,1,2,3,4]" :key="`x${n}`" :x1="x(n)" y1="32" :x2="x(n)" y2="330" /><line v-for="n in [-1,0,1,2,3,4,5]" :key="`y${n}`" x1="70" :y1="y(n)" x2="490" :y2="y(n)" /></g>
      <g class="diagram-axes"><line x1="65" :y1="y(0)" x2="495" :y2="y(0)" :marker-end="`url(#${marker})`"/><line :x1="x(0)" y1="333" :x2="x(0)" y2="23" :marker-end="`url(#${marker})`"/><text x="497" :y="y(0)+22">x</text><text :x="x(0)-21" y="27">y</text><text :x="x(0)-18" :y="y(0)+20">0</text><text :x="x(1)-4" :y="y(0)+20">1</text><text :x="x(0)-20" :y="y(2)+5">2</text></g>
      <template v-if="kind==='rows'">
        <g class="diagram-reveal" :class="{shown:step>=1}"><path :d="`M ${x(-.5)} ${y(-1)} L ${x(2.7)} ${y(5.4)}`" class="diagram-line first"/><text :x="x(2)+8" :y="y(4)-12" class="first">2x − y = 0</text></g>
        <g class="diagram-reveal" :class="{shown:step>=2}"><path :d="`M ${x(-1.4)} ${y(.8)} L ${x(4)} ${y(3.5)}`" class="diagram-line second"/><text :x="x(2.3)" :y="y(2.65)+30" class="second">−x + 2y = 3</text></g>
        <g class="diagram-reveal" :class="{shown:step>=3}"><line :x1="x(1)" :y1="y(0)" :x2="x(1)" :y2="y(2)" class="diagram-guide"/><line :x1="x(0)" :y1="y(2)" :x2="x(1)" :y2="y(2)" class="diagram-guide"/><circle :cx="x(1)" :cy="y(2)" r="6" class="target-fill"/><text :x="x(1)+12" :y="y(2)-12" class="target">(1, 2)</text></g>
      </template>
      <template v-else-if="kind==='columns'">
        <line :x1="x(0)" :y1="y(0)" :x2="x(2)" :y2="y(-1)" class="diagram-vector first" :marker-end="`url(#${marker})`"/><text :x="x(2)+7" :y="y(-1)-5" class="first">a₁</text>
        <g class="diagram-reveal" :class="{shown:step>=1}"><line :x1="x(0)" :y1="y(0)" :x2="x(-1)" :y2="y(2)" class="diagram-vector second" :marker-end="`url(#${marker})`"/><text :x="x(-1)-23" :y="y(2)-8" class="second">a₂</text></g>
        <g class="diagram-reveal" :class="{shown:step>=2}"><line :x1="x(0)" :y1="y(0)" :x2="x(-2)" :y2="y(4)" class="diagram-vector second" :marker-end="`url(#${marker})`"/><text :x="x(-2)+8" :y="y(4)-8" class="second">2a₂</text></g>
        <g class="diagram-reveal" :class="{shown:step>=3}"><line :x1="x(2)" :y1="y(-1)" :x2="x(0)" :y2="y(3)" class="diagram-vector second" :marker-end="`url(#${marker})`"/><line :x1="x(0)" :y1="y(0)" :x2="x(0)" :y2="y(3)" class="diagram-vector target" :marker-end="`url(#${marker})`"/><text :x="x(0)+12" :y="y(3)-8" class="target">b = (0, 3)</text></g>
      </template>
      <template v-else-if="kind==='zero'"><circle :cx="x(0)" :cy="y(0)" r="6" class="target-fill"/></template>
      <template v-else-if="kind==='plane2'"><rect x="75" y="35" width="410" height="290" class="diagram-plane first-plane"/><text x="360" y="80">ℝ²</text></template>
      <template v-else>
        <line :x1="x(0)" :y1="y(0)" :x2="x(2)" :y2="y(kind==='dependent'?1:3)" class="diagram-vector first" :marker-end="`url(#${marker})`"/>
        <line :x1="x(0)" :y1="y(0)" :x2="x(kind==='dependent'?4:1)" :y2="y(kind==='dependent'?2:4)" class="diagram-vector second" :marker-end="`url(#${marker})`"/>
        <text :x="x(2)+10" :y="y(kind==='dependent'?1:3)+3" class="first">u</text><text :x="x(kind==='dependent'?4:1)+5" :y="y(kind==='dependent'?2:4)-10" class="second">{{kind==='dependent'?'2u':'v'}}</text>
      </template>
    </template>
    <template v-else>
      <g class="diagram-axes"><line v-bind="line3(origin,[9,0,0])" :marker-end="`url(#${marker})`"/><line v-bind="line3(origin,[0,9,0])" :marker-end="`url(#${marker})`"/><line v-bind="line3(origin,[0,0,12])" :marker-end="`url(#${marker})`"/><text v-for="(v,i) in [[9.5,0,0],[0,9.7,0],[0,0,12.8]]" :key="i" :x="project(v)[0]" :y="project(v)[1]">{{['x','y','z'][i]}}</text><text :x="project(origin)[0]-18" :y="project(origin)[1]+18">0</text></g>
      <template v-if="kind==='planes'">
        <polygon :points="points([[-3,-6,-1],[3,6,-1],[3,6,7],[-3,-6,7]])" class="diagram-plane first-plane diagram-reveal" :class="{shown:step>=1}"/>
        <polygon :points="points([[-4,-3,-1],[4,1,-1],[4,5,7],[-4,1,7]])" class="diagram-plane second-plane diagram-reveal" :class="{shown:step>=2}"/>
        <polygon :points="points([[-4,-4,-2],[4,-4,-2],[4,4,4],[-4,4,4]])" class="diagram-plane third-plane diagram-reveal" :class="{shown:step>=3}"/>
        <g class="diagram-reveal" :class="{shown:step>=3}"><circle :cx="project([0,0,1])[0]" :cy="project([0,0,1])[1]" r="6" class="target-fill"/><text :x="project([0,0,1])[0]+15" :y="project([0,0,1])[1]-10" class="target">(0, 0, 1)</text></g>
      </template>
      <template v-else-if="kind==='three-columns'">
        <line v-for="(v,i) in [[2,-1,0],[-1,2,-3],[0,-1,4]]" :key="i" v-bind="line3(origin,v)" class="diagram-vector" :class="['first','second','target'][i]" :marker-end="`url(#${marker})`"/>
        <text :x="project([2,-1,0])[0]+6" :y="project([2,-1,0])[1]+12" class="first">a₁</text><text :x="project([-1,2,-3])[0]-25" :y="project([-1,2,-3])[1]" class="second">a₂</text><text :x="project([0,-1,4])[0]+12" :y="project([0,-1,4])[1]-8" class="target">a₃ = b</text>
      </template>
      <template v-else-if="kind==='basis3'">
        <line v-for="(v,i) in [[6,0,0],[0,6,0],[0,0,8]]" :key="i" v-bind="line3(origin,v)" class="diagram-vector" :class="['first','second','target'][i]" :marker-end="`url(#${marker})`"/>
        <text :x="project([6,0,0])[0]+8" :y="project([6,0,0])[1]" class="first">e₁</text><text :x="project([0,6,0])[0]-22" :y="project([0,6,0])[1]" class="second">e₂</text><text :x="project([0,0,8])[0]+8" :y="project([0,0,8])[1]" class="target">e₃</text>
      </template>
      <template v-else>
        <polygon v-if="['span3','column-space'].includes(kind)" :points="points([[0,0,0],a,c,b])" class="diagram-plane first-plane"/>
        <line v-bind="line3(origin,a)" class="diagram-vector first" :marker-end="`url(#${marker})`"/><line v-bind="line3(origin,b)" class="diagram-vector second" :marker-end="`url(#${marker})`"/>
        <line v-if="kind!=='span3'" v-bind="line3(origin,c)" class="diagram-vector target" :marker-end="`url(#${marker})`"/>
        <line v-if="step>=1 && kind!=='span3'" v-bind="line3(a,c)" class="diagram-vector second diagram-tip-tail" :marker-end="`url(#${marker})`"/>
        <text :x="project(a)[0]-24" :y="project(a)[1]-8" class="first">v₁</text><text :x="project(b)[0]-24" :y="project(b)[1]+20" class="second">v₂</text><text v-if="kind!=='span3'" :x="project(c)[0]+12" :y="project(c)[1]-5" class="target">v₃</text>
      </template>
    </template>
  </svg>
</template>
