<template>
    <div class="home">
        <Tweets :tweet="tweets" @reload="loadTweets"></Tweets>
    </div>
</template>

<script>
    import Tweets from "../components/Tweets";

    export default {
        name: 'Home',
        components: {
            Tweets
        },
        data() {
            return {
                tweets: "",
                url: 'api/v1/app/',
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
        }
    }
</script>
