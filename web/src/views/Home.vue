<template>
  <div class="container w-full pt-10 mx-auto">
      <div class="flex flex-wrap">
        <div class="w-full lg:w-1/3 p-3">
          <!--Metric Card-->
          <div class="bg-white border rounded shadow p-2">
            <div class="flex flex-row items-center">
              <div class="flex-1 text-center">
                <h5 class="uppercase text-teal-800">Overall positive / neutral / negative</h5>
                <h3 class="text-3xl text-gray-800">
                  {{summary.overall_positive}}% /
                  {{summary.overall_neutral}}% /
                  {{summary.overall_negative}}%
                </h3>
              </div>
            </div>
          </div>
          <!--/Metric Card-->
        </div>
        <div class="w-full lg:w-1/3 p-3">
          <!--Metric Card-->
          <div class="bg-white border rounded shadow p-2">
            <div class="flex flex-row items-center">
              <div class="flex-1 text-center">
                <h5 class="uppercase text-teal-800">Most loved feature</h5>
                <h3 class="text-3xl text-gray-800">
                  {{summary.most_positive.feature_name}}
                  ({{summary.most_positive.ratings_count}})
                </h3>
              </div>
            </div>
          </div>
          <!--/Metric Card-->
        </div>
        <div class="w-full lg:w-1/3 p-3">
          <!--Metric Card-->
          <div class="bg-white border rounded shadow p-2">
            <div class="flex flex-row items-center">
              <div class="flex-1 text-center">
                <h5 class="uppercase text-teal-800">Could use some work</h5>
                <h3 class="text-3xl text-gray-800">{{summary.most_negative.feature_name}}
                  ({{summary.most_negative.ratings_count}})</h3>
              </div>
            </div>
          </div>
          <!--/Metric Card-->
        </div>
      </div>
  </div>
</template>

<script>
import { Component, Prop, Vue } from 'vue-property-decorator';
import axios from 'axios';
@Component({
  components: {
  },
})
export default class FeedbackHome extends Vue {
  summary = {}

  fetchSummary() {
    axios
      .get('http://localhost:8000/ratings')
      .then((r) => {
        this.summary = r.data;
      })
      .catch((e) => {});
  }

  created() {
    this.fetchSummary();
  }
}
</script>
