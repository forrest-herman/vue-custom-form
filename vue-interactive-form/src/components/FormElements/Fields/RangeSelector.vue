<template>
  <div>
    <div class="col-4 text-center pe-3">
      <p>{{ answer_bounds.low_text }}</p>
    </div>
    <div class="col-4 range d-flex flex-column">
      <b-form-input
        id="range-1"
        class="range-slider-div"
        v-model="rating_value"
        @change="emitValue"
        v-validate
        type="range"
        :min="value_range.min_range"
        :max="value_range.max_range"
      ></b-form-input>
      <div class="d-flex justify-content-between range-slider-div align-items-center">
        <p class="text-center range-text-sm">{{ value_range.min_range }}</p>
        <p class="text-center range-text">{{ rating_value }}</p>
        <p class="text-center range-text-sm">{{ value_range.max_range }}</p>
      </div>
    </div>
    <div class="col-4 text-center ps-3">
      <p>{{ answer_bounds.high_text }}</p>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    answer_bounds: {},
    options: {},
    value_range: {},
    value: {
      default: "",
      type: String
    }
  },
  data() {
    return {
      rating_value: this.value //"3"
    }
  },
  methods: {
    emitValue(value) {
      this.$emit("input", value)
    }
  }
}
</script>
