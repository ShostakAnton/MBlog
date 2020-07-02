<template>
    <div class="MyTweets">
        <Tweets :tweet="tweets" @reload="loadTweets"></Tweets>
    </div>
</template>

<script>
    import Tweets from "../components/Tweets";

    export default {
        name: "MyTweets",
        components: {
            Tweets
        },
        data() {
            return {
                tweets: "",
                url: 'api/v1/app/my/',
            }
        },
        created() {
            this.loadTweets()
        },
        methods: {
            loadTweets() {
                $.ajax({
                    url: this.$store.getters.get_url_server + this.url,
                    type: "GET",
                    success: (response) => {
                        this.tweets = response
                    }
                })
            }
        },
    }
</script>

<style scoped>

</style>