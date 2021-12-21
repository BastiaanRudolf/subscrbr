<template>

    <div class="container mx-auto pt-40 lg:pt-52 2xl:pt-64 pb-16 lg:pb-20 xl:pb-28 2xl:pb-52 flex flex-col px-5 py-24 justify-center items-center max-w-7xl">
        <div class="w-full md:w-2/3 flex flex-col mb-6 text-center">
            <!-- Header text -->
            <h1 class="title-font tracking-tight font-extrabold text-2xl xs:text-3xl lg:text-4xl 2xl:text-6xl mb-4 text-gray-800">Collecting Emails <span style="color: #6666FF;">Made Easy</span></h1>
            
            <!-- Sub text -->
            <p class="mb-8 leading-relaxed text-xs sm:text-sm lg:text-lg xl:text-xl 2xl:text-2xl">
                Quickly and easily collect & store emailaddresses with an Azure Static Web App.
                <br>
                <br>
                Try it out now. 👇
            </p>

            <!-- Form with button -->
            <div>
                <div class="flex w-full justify-center items-end">

                    <div class="relative mr-4 lg:w-full xl:w-1/2 w-2/4 md:w-full text-left">
                        <!-- Binding a placeholder from the Vuex store, just to show how it interacts -->
                        <input v-model="email" type="text" :placeholder="exampleEmail" name="hero-field" class="w-full bg-opacity-50 rounded placeholder-gray-600 placeholder-opacity-50 focus:ring-2 focus:bg-transparent border border-gray-300 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
                    </div>
                    <button id="heroEmailSubscribe" @click="subscribeEmail" type="button" style="background: #6666FF;" class="flex-wrap relative my-auto disabled:opacity-50 text-sm xl:text-xl text-white justify-start rounded-full py-2 px-8 shadow-lg focus:outline-none focus:shadow-outline transform transition hover:shadow-xl hover:scale-105 duration-300 ease-in-out">Subscribe</button>
                </div>
                
                <!-- Response messages -->
                <p v-if="responseType === 'error'" class="text-xs text-red-500 mt-6 ml-1"> ❌ {{this.$store.state.responseMessage}} </p>
                <p v-if="responseType === 'success'" class="text-xs text-green-500 mt-6 ml-1"> ✅ {{this.$store.state.responseMessage}} </p>
            </div>
        </div>
    </div>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'

export default ({
    data() {
        return {
            // This is the local version of the email,
            // this is mounted to the input
            email: '',
        }
    },
    computed: {
        ...mapGetters({
        // This is how you rename a getter, value is accessible
        // via exampleEmail now.
        exampleEmail: 'getExampleEmail',
        responseMsg: 'getResponseMessage',
        responseType: 'getResponseType'
        })
    },
    methods: {
        ...mapActions(["subscribe"]),
        subscribeEmail: function(){
            this.subscribe(this.email)
        },
    },
    watch: {
        responseMsg(newVal, oldVal) {
            return newVal, oldVal
        },
        responseType(newVal, oldVal) {
            return newVal, oldVal
        }
    }
})
</script>
