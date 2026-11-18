<script setup lang="ts">
defineProps<{ lines: string[] }>()
</script>

<template><pre class="native-output">{{ lines.join('\n') }}</pre></template>
