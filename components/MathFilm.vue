<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
import HoverVideo from './HoverVideo.vue'

const props = withDefaults(defineProps<{
  src: string; poster: string; caption: string; autoplay?: boolean; loop?: boolean
}>(), { autoplay: true, loop: true })
const { $slidev, $page } = useSlideContext()
const active = computed(() => $slidev.nav.currentPage === $page.value)
</script>

<template>
  <figure class="math-film" @click.stop @pointerdown.stop @keydown.stop>
    <HoverVideo :src="props.src" :poster="props.poster" :label="props.caption"
      :active="active" :autoplay="props.autoplay" :loop="props.loop" />
    <figcaption>{{ caption }}</figcaption>
  </figure>
</template>
