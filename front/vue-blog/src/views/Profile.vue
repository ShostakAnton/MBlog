<template>
    <div class="container">
        <div class="row">
            <div class="col-md-6">
                <p>Welcome to your profile,
                    <span v-if="$store.getters.get_user_info.nike">
                        {{ $store.getters.get_user_info.nike }}
                    </span>
                    <span v-else>
                        {{ $store.getters.get_user_info.user.username }}
                    </span>
                    <!--                {% if profile.nike %}-->
                    <!--                {{profile.nike}}-->
                    <!--                {% else %}-->
                    <!--                {{user}}-->
                    <!--                {% endif %}</p>-->
                <hr>
                <p>Your avatar:</p>
                <img class="rounded-circle avatar"
                     :src="$store.getters.get_url_media + $store.getters.get_user_info.avatar">
                <p>Followers:
                {{ $store.getters.get_user_info.follow.length }}
                </p>
                <span v-for="follow in $store.getters.get_user_info.follow">
                    {{follow.username}}<br>
                </span>
            </div>
            <div class="col-md-4">
                <a href="">
                    <button type="submit" class="btn btn-success btn-md" name="button">Update profile</button>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Profile"
    }
</script>

<style scoped>
    .avatar {
        width: 150px;
        height: 150px;
        border-radius: 50% 50%;
    }

</style>