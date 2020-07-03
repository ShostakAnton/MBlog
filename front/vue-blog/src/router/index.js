import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
// import Login from "../components/Login.vue"
import Profile from "../views/Profile";
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
            component: Home,

            beforeEach: (to, from, next) => {
                if (index.getters.get_auth) {         // если пользователь аторизован
                    next()
                } else {
                    next({name: 'home'})
                }
            }
        },
        {
            path: '/my-follow',
            name: 'my_follow_tweets',
            component: Home,
            beforeEach: (to, from, next) => {
                if (index.getters.get_auth) {         // если пользователь аторизован
                    next()
                } else {
                    next({name: 'home'})
                }
            }
        },
        {
            path: '/profile',
            name: 'profile',
            component: Profile,
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