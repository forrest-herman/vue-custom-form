// import formConfig from "../../config/formConfig.json"
import backend from "@/backend"

const state = {
  // formData: {},
  questionsData: [],
  questionData: {},
  questionsComponent: [],
  isLoading: false,
  results: {}
}

const actions = {
  async getQuestions({ commit }) {
    const response = await backend.fetchResource()
    const questionDataBuilder = []

    if (response.status == 200) {
      response.data.content.forEach(field => {
        // Rich Text Title
        if (field.type == "richText") {
          const obj = {
            type: "richText",
            class: field.value.title_type,
            label: field.value.title,
            name: field.value.title, // to be ajusted
            description: field.value.description,
            options: {
              attrs: {
                placeholder: ""
              }
            },
            validation: ""
          }
          questionDataBuilder.push(obj)
        }
        // Question - Range Selection
        if (field.type == "question_range") {
          const obj = {
            type: "range",
            label: field.value.question,
            name: field.value.question,
            answer_bounds: {
              low_text: field.value.range_min_text,
              high_text: field.value.range_max_text
            },
            value_range: {
              min_range: field.value.range_min_value,
              max_range: field.value.range_max_value
            },
            options: {},
            validation: field.value.question_mandatory ? "required" : ""
          }
          questionDataBuilder.push(obj)
        }
        // Question - Text Field
        if (field.type == "question_text") {
          const obj = {
            type: "textField",
            label: field.value.question,
            name: field.value.question,
            options: {},
            validation: field.value.question_mandatory
              ? "required|" + field.value.validation_type
              : field.value.validation_type
          }
          questionDataBuilder.push(obj)
        }
        // Question - Multiple Choice Questions
        if (field.type == "question_mc") {
          // how many choices were provided?
          const choices = [
            field.value.choice_1,
            field.value.choice_2,
            field.value.choice_3,
            field.value.choice_4,
            field.value.choice_5
          ]
          var narrowed_choices = []
          for (const choice of choices) {
            if (choice == "") break
            else narrowed_choices.push(choice)
          }

          if (field.value.mc_type == "mc_radio") {
            const obj = {
              type: "radio",
              label: field.value.question,
              name: field.value.question,
              result: {
                low: field.value.q_min,
                high: field.value.q_max
              },
              options: {
                choices: narrowed_choices
              },
              validation: field.value.question_mandatory ? "required" : ""
            }
            questionDataBuilder.push(obj)
          }
          if (field.value.mc_type == "mc_checkbox") {
            const obj = {
              type: "check",
              label: field.value.question,
              name: field.value.question,
              options: {
                choices: narrowed_choices
              },
              validation: field.value.question_mandatory ? "required" : ""
            }
            questionDataBuilder.push(obj)
          }
        }
      })
    }
    localStorage.setItem("questions", JSON.stringify(questionDataBuilder))
    commit("setQuestions", questionDataBuilder)
  },
  setQuestionsComponent({ commit }, payload) {
    commit("updateQuestionsComponent", payload)
  },
  async postQuestions({ commit }, payload) {
    const response = await backend.postAnswers(payload)
    if (response.status == 200) {
      commit("setLoading", "success")
      commit("setResult", response.data)
      console.log("SUCCESSFULY POSTED TO BACKEND") //eslint-disable-line
    } else {
      commit("setLoading", true)
      console.log("ERRORS POSTED TO BACKEND") //eslint-disable-line
    }
  }
}

const mutations = {
  updateField(state, payload) {
    state.questionData[payload.key] = payload.value
  },
  setResult(state, result) {
    state.results = result.data
  },
  setQuestions(state, questions) {
    state.questionsData = questions
  },
  updateQuestionsComponent(state, payload) {
    state.questionsComponent = payload
  },
  setLoading(state, loading) {
    state.isLoading = loading
  }
}

const getters = {
  allResults: state => state.results,
  allQuestions: state => state.questionsData,
  allComponents: state => state.questionsComponent
}

state.questionsData.forEach(field => {
  state.questionData[field.name] = ""
})

// formConfig.forEach(field => {
//   state.formData[field.name] = ""
// })

export default {
  namespaced: true,
  mutations,
  actions,
  getters,
  state
}
