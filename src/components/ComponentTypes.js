import FormTemplate from "./FormTemplate.vue"
import InputBox from "./FormElements/Fields/InputBox.vue"
import TextArea from "./FormElements/Fields/TextArea.vue"
import RadioButton from "./FormElements/Fields/RadioButton.vue"
import CheckBox from "./FormElements/Fields/CheckBox.vue"
import RadioButtonVertical from "./FormElements/Fields/RadioButtonVertical.vue"
import RangeSelector from "./FormElements/Fields/RangeSelector.vue"
import RichText from "./FormElements/Fields/RichText.vue"

const COMPONENT_MAP = {
  formTemplate: FormTemplate,
  textField: InputBox, //type of question
  textarea: TextArea, //type of question
  radio: RadioButton, //type of question
  vradio: RadioButtonVertical, //type of question
  range: RangeSelector, //type of question
  check: CheckBox, //type of question
  richText: RichText
}

export function getComponent(type) {
  return COMPONENT_MAP[type]
}
