<template>
  <div class="info-text" v-html="description">
    {{ description }}
  </div>
</template>
<script>
export default {
  props: ["type", "description"]
}
</script>
