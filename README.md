# A Custom and Interactive Form with Vue

## Live Demo

__Form:__ https://vue-custom-form.herokuapp.com/

__Backend to customize form items:__ https://wagtail-form-generator.herokuapp.com/admin to log in, and https://wagtail-form-generator.herokuapp.com/admin/pages/4/edit/ to edit the form contents.

### Default login credentials for Wagtail: 

__Username:__ admin \
__Password:__ password


## About

This is a project making use of the article **[Building an Interactive and Distraction-free Form with Vue](https://medium.com/vue-mastery/building-an-interactive-and-distraction-free-form-with-vue-bfe23907e981)**.

This implementation uses a JSON file to generate the custom form. In our use case, the JSON file is fetched via a wagtail site (REST Framework), where the form can be easily created using the wagtail CMS login and included UI.


## Project setup

```bash
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Run your tests

```
npm run test
```

### Lints and fixes files

```
npm run lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).
