<template>
    <div class="modal fade" id="loginModal">
        <div class="modal-dialog modal-dialog-centered auth-modal">
            <div class="modal-content">
                <!-- Modal Header -->
                <div class="modal-header">
                    <h4 class="modal-title">Вход</h4>
                    <button  type="button" class="close" data-dismiss="modal">x</button>
                </div>

                <!-- Modal body -->
                <div class="modal-body">
                    <input type="text" placeholder="Логин" value="" v-model="user.username">
                    <input type="password" placeholder="Пароль" value="" v-model="user.password">
                    <button type="button" @click="setLogin">Войти</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                user: {
                    username: "",
                    password: "",
                }
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: this.$store.getters.get_url_server + 'auth/token/login/',
                    type: "POST",
                    data: {
                        username: this.user.username,
                        password: this.user.password
                    },
                    success: (response) => {
                        // sessionStorage.setItem("token", response.auth_token)
                        // this.$store.commit("set_auth", true)
                        // $.ajaxSetup({
                        //     headers: {'Authorization': "Token " + sessionStorage.getItem('token')},
                        // });
                        // this.close()
                        sessionStorage.setItem("token", response.auth_token)        // запоминаем наш токен
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        // if (response.status === 400) {
                        //     this.mess = response.responseJSON.non_field_errors[0]
                        // }
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>