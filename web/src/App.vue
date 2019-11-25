<template>
  <div id="app">
    <Header></Header>
    <router-view/>
  </div>
</template>
<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import Header from '@/components/Header.vue';

@Component({
  components: {
    Header,
  },
})
export default class App extends Vue {}
</script>
<style lang="scss">
</style>
