<template>
    <div class="navbar navbar-expand-lg navbar-dark menu">
        <!-- Collapse button -->
        <button class="navbar-toggler" type="button" data-toggle="collapse"
                data-target="#basicExampleNav"
                aria-controls="basicExampleNav" aria-expanded="false"
                aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="basicExampleNav">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <a v-if='auth' class="nav-link" href="#" @click="goPage('home')">Главная</a>
                </li>
            </ul>
            <ul class="navbar-nav mr-0">
                <li class="nav-item">
                    <a v-if='auth' class="nav-link" href="#" @click="goPage('my_follow_tweets')">
                        My Posts + Whom I follow
                    </a>
                </li>
                <li class="nav-item my-0">
                    <a v-if='auth' class="nav-link" href="#" @click="goPage('my_tweets')">Мои записи</a>
                </li>
                <li class="nav-item my-0">
                    <a v-if='auth' class="nav-link"
                       href="#" @click="goPage('profile')">
                        <span>{{ $store.getters.get_user_info.user.username }}</span>
                    </a>
                </li>
                <li v-if="auth" class="nav-item my-0">
                    <img class="avatar"
                         :src="$store.getters.get_url_media + $store.getters.get_user_info.avatar">
                </li>
                <li class="nav-item my-0">
                    <a v-if='auth' @click="logout" class="nav-link" href="#">Выход</a>
                </li>
                <li class="nav-item my-0">
                    <a v-if='!auth'
                       @click="goLogin"
                       class="nav-link"
                       href="#"
                       data-toggle="modal"
                       data-target="#loginModal">
                        Вход
                    </a>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    import auth from '../mixins/computedAuth.js'

    export default {

        name: "Menu",
        mixins: [
            auth,
        ],
        methods: {
            goPage(item) {
                this.$router.push({name: item})
            },
            goLogin() {
                this.$emit("showLogin")
            },
            logout() {
                this.$store.commit("set_auth", false)   // отображение кнопки входа
                sessionStorage.removeItem("token")      // удаление токена
                $.ajaxSetup({       // чистка хидера
                    headers: {'Authorization': ""},
                });
                window.location = '/'
            }
        },

    }
</script>

<style scoped>
    .menu {
        margin: 0 auto;
        background: #2a2a2a;
        display: flex;
        flex: 0 0 auto;
        width: 100%;
    }

    .avatar {
        width: 50px;
        height: 50px;
        border-radius: 50% 50%;
    }
</style>