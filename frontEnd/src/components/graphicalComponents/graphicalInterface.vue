<template>
    <div class="InterfaceWrapper">
        <NavigationBar/>
    </div>
</template>

<script>
import NavigationBar from './NavigationBar.vue';

export default {
    data(){
        return{

        }
    },
    mounted(){
        this.fetchUserDetails()
    },
    components:{
        NavigationBar
    },
    methods: {
        fetchUserDetails(){

        },
        createUserMessage(){

        }
    }
}
</script>

<style>
.InterfaceWrapper > div {
    position:absolute;
}
.InterfaceWrapper .navbar{
    top:0;
    left:0;
    right:0;
}
</style>