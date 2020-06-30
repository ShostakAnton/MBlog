<template>
    <div id="app">
        <Menu @showLogin="setLogin(true)"></Menu>
        <Login v-if="login" @hideLogin="setLogin(false)"></Login>
        <router-view/>
    </div>
</template>

<script>
    import Menu from '@/components/Menu.vue'
    import Login from "./components/Login";

    export default {
        name: 'app',
        components: {
            Menu,
            Login,
        },
        data() {
            return{
                login: false
            }
        },
        created() {
             if (sessionStorage.getItem("token")) {         // проверка на существование токена
                 this.$store.commit("set_auth", true)
             }
             else {
                 this.$store.commit("set_auth", false)
             }
        },
        methods: {
            setLogin(value) {
                this.login = value
            }
        }
    }
</script>

<style>
    body {
        background: #e6ecf0;
    }
</style>
