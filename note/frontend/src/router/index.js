import Vue from 'vue'
import Router from 'vue-router'
import FormComponent from '@/components/FormComponent'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'FormComponent',
      component: FormComponent
    }
  ]
})
