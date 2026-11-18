<script setup lang="ts">
import { onMounted } from 'vue'
onMounted(() => {
  // Warm the source font faces before later lectures enter the viewport.
  for (const face of document.fonts) {
    if (/YAF|Nunito|Montserrat|Inter|Playfair|Space Grotesk|Source Serif 4/.test(face.family)) void face.load().catch(() => {})
  }
})
</script>
<template><span hidden aria-hidden="true" /></template>
