<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
const props = withDefaults(defineProps<{ lesson: string; offset?: number; maxStep?: number; augmented?: number }>(), { offset: 0, maxStep: 99, augmented: -1 })
const { $clicks } = useSlideContext()
const copy = (a: number[][]) => a.map(row => [...row])
const elimination = [[1,2,1,2],[3,8,1,12],[0,4,1,2]]
const failure = [[1,2,1,2],[3,8,1,12],[0,4,-4,2]]
function eliminate(a: number[][]) {
  const states = [copy(a)]
  a[1] = a[1].map((v,j) => v - 3*a[0][j]); states.push(copy(a))
  a[2] = a[2].map((v,j) => v - 2*a[1][j]); states.push(copy(a))
  return states
}
function inverse() {
  const a=[[1,3,1,0],[2,5,0,1]], states=[copy(a)]
  a[1]=a[1].map((v,j)=>v-2*a[0][j]); states.push(copy(a))
  a[1]=a[1].map(v=>-v); states.push(copy(a))
  a[0]=a[0].map((v,j)=>v-3*a[1][j]); states.push(copy(a))
  return states
}
function dependence() {
  const a=[[3,4,7],[2,7,9],[5,2,7]], states=[copy(a)]
  a[0]=a[0].map((v,j)=>v-a[1][j]);states.push(copy(a))
  a[1]=a[1].map((v,j)=>v-2*a[0][j]);states.push(copy(a))
  a[2]=a[2].map((v,j)=>v-5*a[0][j]);states.push(copy(a))
  a[1]=a[1].map(v=>v/13);states.push(copy(a))
  a[2]=a[2].map((v,j)=>v-17*a[1][j]);states.push(copy(a))
  return states
}
const catalogs: Record<string, { matrices: number[][][]; captions: string[]; rows: number[] }> = {
  elimination: { matrices: eliminate(copy(elimination)), captions:['Start with [A | b]','R₂ ← R₂ − 3R₁','R₃ ← R₃ − 2R₂'], rows:[-1,1,2] },
  failure: { matrices: eliminate(copy(failure)), captions:['Change the final equation to 4y − 4z = 2','R₂ ← R₂ − 3R₁','R₃ ← R₃ − 2R₂: the last row is 0 = −10'], rows:[-1,1,2] },
  inverse: { matrices: inverse(), captions:['Start with [A | I]','R₂ ← R₂ − 2R₁','R₂ ← −R₂','R₁ ← R₁ − 3R₂: the right half is A⁻¹'], rows:[-1,1,1,0] },
  dependence: { matrices: dependence(), captions:['Place the three vectors in columns','R₁ ← R₁ − R₂','R₂ ← R₂ − 2R₁','R₃ ← R₃ − 5R₁','R₂ ← R₂ / 13','R₃ ← R₃ − 17R₂'], rows:[-1,0,1,2,1,2] },
}
const data=computed(()=>catalogs[props.lesson])
const step=computed(()=>Math.min(data.value.matrices.length-1,props.offset+Math.min(props.maxStep,Math.max(0,Number($clicks.value)||0))))
const matrix=computed(()=>data.value.matrices[step.value])
const format=(value:number)=>Object.is(value,-0)?'0':String(value)
</script>

<template>
  <figure class="native-matrix-steps" :data-lesson="lesson" :data-step="step">
    <div class="native-matrix" :style="{ '--matrix-columns': matrix[0].length }" role="table" aria-label="Current matrix">
      <div v-for="(row,i) in matrix" :key="i" class="native-matrix-row" :class="{ 'native-row-active': data.rows[step]===i }" role="row">
        <span v-for="(value,j) in row" :key="j" class="native-matrix-cell" :class="{ 'native-augmented': j===augmented }" role="cell" :data-value="value">{{ format(value) }}</span>
      </div>
    </div>
    <figcaption>{{ data.captions[step] }}</figcaption>
  </figure>
</template>
