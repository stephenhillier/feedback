<template>
  <nav class="flex items-center justify-between flex-wrap bg-teal-600 p-4">
    <div class="flex items-center flex-shrink-0 text-white mr-6">
      <symbol id="icon-send" viewBox="0 0 24 24">
        <title>send</title>
        <!-- eslint-disable --> 
        <path
          d="M22.963 2.269c0.043-0.151 0.050-0.314 0.015-0.476-0.024-0.113-0.068-0.224-0.131-0.325-0.064-0.102-0.145-0.19-0.238-0.262-0.117-0.090-0.249-0.15-0.386-0.181s-0.282-0.034-0.426-0.004c-0.042 0.009-0.085 0.021-0.126 0.035l-0.021 0.007-19.98 6.993c-0.252 0.088-0.467 0.276-0.584 0.538-0.224 0.505 0.003 1.096 0.508 1.32l8.649 3.844 3.844 8.649c0.108 0.243 0.313 0.443 0.583 0.538 0.521 0.182 1.092-0.092 1.274-0.614l6.993-19.979c0.010-0.027 0.019-0.054 0.027-0.082zM10.779 11.807l-6.068-2.696 13.483-4.72zM19.609 5.806l-4.72 13.483-2.696-6.068z"
        ></path>
        <!-- eslint-enable -->
      </symbol>
      <svg class="icon icon-send"><use xlink:href="#icon-send"></use></svg>
      <span class="font-semibold text-xl tracking-tight">Feedback</span>
    </div>

    <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
      <div class="text-sm lg:flex-grow">
        <!-- <a
          href="#responsive-header"
          class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4"
        >
          Features
        </a>
        <a
          href="#responsive-header"
          class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4"
        >
          Docs
        </a> -->
      </div>
    </div>
  </nav>
</template>
<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class Header extends Vue {}
</script>

<style scoped lang="scss">
.icon {
  display: inline-block;
  width: 1.2em;
  height: 1.2em;
  stroke-width: 0;
  stroke: currentColor;
  fill: currentColor;
}
</style>
