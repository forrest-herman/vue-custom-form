import axios from "axios"

const $axios = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v2/pages/",
  timeout: 5000,
  headers: { "Content-Type": "application/json" }
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(
  function(response) {
    return response
  },
  function(error) {
    // Handle Error
    return Promise.reject(error)
  }
)

export default {
  $axios,
  fetchResource() {
    return $axios.get(`20/`)
  },
  postAnswers(answer) {
    return $axios.post(`process-data`, answer)
  }
}
