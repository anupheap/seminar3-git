<script setup lang="ts">
defineProps<{ frontmatter: { lecture?: number; class?: string } }>()
</script>

<template>
  <main class="slidev-layout native-slide" :class="[`native-lecture-${frontmatter.lecture}`, frontmatter.class]">
    <slot />
  </main>
</template>
