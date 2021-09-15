<template>
  <form class="form-template" @submit.prevent="submit">
    <!-- Form Template -->
    <template v-for="(field, key) in formFields">
      <field-group :field-id="key" :key="`${_uid}-${field.name}`">
        <div class="field-area" v-bind:class="field.class">
          <field-label :for="`${_uid}-${field.name}`"> {{ field.label }} </field-label>
          <Component
            v-model="questionData[field.name]"
            :is="field.component"
            v-bind="{ ...field.options.attrs }"
            :id="`${_uid}-${field.name}`"
            :name="`${field.name}`"
            :description="field.description"
            :type="field.type"
            @input="updateField({ key: field.name, value: questionData[field.name] })"
            v-validate="field.validation"
            :data-vv-as="field.label"
            :answer_bounds="!!field.answer_bounds ? field.answer_bounds : false"
            :value_range="!!field.value_range ? field.value_range : false"
            :options="!!field.options.choices ? field.options.choices : false"
          />
        </div>
        <field-error>{{ errors.first(field.name) }}</field-error>
      </field-group>
    </template>

    <!-- Next and Back Nav -->
    <form-nav @back="back" @next="next" v-colorswatch:bg="formState.activeField" />

    <!-- Form Results -->
    <form-result />
  </form>
</template>

<script>
import FieldGroup from "./FormElements/FieldGroup.vue"
import FieldError from "./FormElements/FieldError.vue"
import FieldLabel from "./FormElements/FieldLabel.vue"

import FormNav from "./FormElements/FormNav.vue"
import FormResult from "./FormElements/FormResult.vue"

import formMixin from "../mixins/formMixin"
import { mapMutations } from "vuex"

export default {
  name: "form-template",
  mixins: [formMixin],
  props: ["formFields"],
  components: {
    FieldGroup,
    FieldError,
    FieldLabel,
    FormNav,
    FormResult
  },
  provide() {
    return {
      formState: this.formState
    }
  },
  methods: {
    ...mapMutations({
      updateField: "lead/updateField"
    })
  }
}
</script>
