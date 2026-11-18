<script setup lang="ts">
import { useNav } from '@slidev/client'
import chapters from '../sources/lecture-index.json'
const nav = useNav()
</script>

<template>
  <nav class="lecture-index" aria-label="Lectures">
    <button v-for="chapter in chapters" :key="chapter.lecture" @click.stop="nav.go(chapter.start)">
      <span class="lecture-number">{{ String(chapter.lecture).padStart(2, '0') }}</span>
      <span>{{ chapter.title }}</span>
    </button>
  </nav>
</template>
