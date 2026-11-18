<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
import lessons from '../sources/code-lessons.json'
const props = defineProps<{ lesson: string }>()
const { $clicks } = useSlideContext()
const data = computed(() => lessons.find(item => item.key === props.lesson)!)
const index = computed(() => Math.min(data.value.stages.length - 1, Math.max(0, Number($clicks.value) || 0)))
const stage = computed(() => data.value.stages[index.value])
</script>

<template>
  <aside class="code-output" :data-lesson="lesson" :data-step="index" aria-live="polite">
    <div class="output-label">Output added · Step {{ index + 1 }} / {{ data.stages.length }}</div>
    <pre>{{ stage.output || 'No output in this step.' }}</pre>
    <Transition name="output-caption" mode="out-in">
      <p :key="index">{{ stage.caption }}</p>
    </Transition>
  </aside>
</template>
