<script setup lang="ts">
import { ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'
defineProps<{ items: string[] }>()
const { $slidev, $page, $renderContext } = useSlideContext()
const run = ref(0)
watch(() => $slidev.nav.currentPage === $page.value, active => { if (active) run.value++ }, { immediate: true })
</script>

<template>
  <section :key="run" class="native-objectives" :class="{ 'native-objectives-print': $renderContext === 'print' }" aria-label="Learning Objectives">
    <h1>Learning Objectives</h1>
    <ol>
      <li v-for="(item, index) in items" :key="item" :style="{ '--entrance-delay': `${.3 + index * .24}s` }">
        <span class="native-objective-number">{{ String(index + 1).padStart(2, '0') }}.</span>
        <span class="native-objective-text">{{ item }}</span>
      </li>
    </ol>
  </section>
</template>
