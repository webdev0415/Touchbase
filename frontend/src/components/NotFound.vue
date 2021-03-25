<template>
    <div class="white home-div">
        <v-container fluid style="max-height: calc(100vh - 58px); overflow: hidden;">
            <v-layout justify-center align-center column>
                <v-layout justify-center align-center class="mb-5" z-index="-1">
                    <video id="video1" autoplay muted loop>
                        <source src="/video/Crocodile.mp4" type="video/mp4">
                    </video>
                    <img id="image" src="/img/404.svg" alt="" class="mt-0 px-3">
                    <!-- <img id="image" src="../images/404.svg" alt="" width="100%"> -->
                </v-layout>
                <v-layout align-center justify-center column class="mt-5">
                    <v-flex lg12 class="mt-4">
                        <p class="headline font-italic font-weight-bold text-xs-center">Hello There!</p>
                        <p class="display-1 font-weight-light text-xs-center">Error 404. The webpage you came looking for doesn't exist here.</p>
                    </v-flex>
                    <v-layout justify-center align-center class="">
                        <v-btn @click="$router.go(-1)" large depressed color="primary" dark class="font-weight-medium pr-3 pl-3">Go back</v-btn>
                    </v-layout>
                    <v-layout justify-center align-center class="notfound-footer">
                        <span class="mt-5">&copy;Hioz LLC.</span>
                    </v-layout>
                </v-layout>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
export default {
    name: 'NotFound',
    // NOTE change document title to 404
}
</script>

<style scoped>
    /* * {
        font-family: "Roboto", Arial, sans-serif;
    } */
    img {
        background-color: transparent;
        margin-top: -8%;
        position: absolute;
        height: 500px;
        width: 100%;
        transform: scale(1.5);
    }
    video {
        width: 1000px;
        height: 500px;
    }
    @media screen and (max-width: 834px) {
        img {
            transform: scale(1.28);
        }
    }
    @media screen and (max-width: 800px) {
        img {
            transform: scale(1.3);
        }
    }

    @media screen and (max-width: 768px) {
        img {
            height: 400px;
            transform: scale(1.5);
        }
        video {
            height: 400px;
        }
    }
    @media screen and (max-width: 620px) {
        img {
            transform: scale(1.2);
        }
    }
    @media screen and (max-width: 480px) {
        img {
            height: 200px;
            transform: scale(1.42);
        }
        video {
            height: 200px;
        }
    }
    @media screen and (max-width: 414px) {
        img {
            height: 200px;
            transform: scale(1.55);
        }
        video {
            height: 200px;
        }
    }
    @media screen and (max-width: 360px) {
        img {
            transform: scale(1.53);
        }
    }
    @media screen and (max-width: 320px) {
        img {
            transform: scale(1.3);
        }
    }

    .notfound-footer {
        position: absolute;
        bottom: 10px;
    }
</style>
