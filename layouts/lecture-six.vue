<script setup lang="ts">
defineProps<{frontmatter:{class?:string}}>()
</script>
<template>
 <main class="slidev-layout lecture-six" :class="frontmatter.class"><slot /></main>
</template>
