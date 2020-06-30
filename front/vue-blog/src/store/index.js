import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        url_server: "http://127.0.0.1:8000/",
        auth_user: false,
    },
    getters: {      // для получения обьектов из state
        get_url_server(state) {
            return state.url_server
        },
        get_auth(state) {
            return state.auth_user
        }
    },
    mutations: {
        set_auth(state, value) {
            state.auth_user = value
        },
    },
    actions: {},
    modules: {}
})
