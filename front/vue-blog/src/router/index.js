import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
// import Login from "../components/Login.vue"
import myTweets from "../components/myTweets";

import index from '../store/index.js'


Vue.use(VueRouter)

export default new VueRouter({
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/my',
            name: 'my_tweets',
            component: myTweets,

            beforeEach: (to, from, next) => {
                if (index.getters.get_auth) {         // если пользователь аторизован
                    next()
                } else {
                    next({name: 'home'})
                }
            }
        }
    ]
})