<template>
  <div class="container w-full pt-10 mx-auto">
      <div class="flex flex-wrap">
        <div class="w-full lg:w-1/3 p-3">
          <!--Metric Card-->
          <div class="bg-white border rounded shadow p-2">
            <div class="flex flex-row items-center">
              <div class="flex-1 text-center">
                <h5 class="uppercase text-teal-800">Overall positive / neutral / negative</h5>
                <h3 class="text-3xl text-gray-800" v-if="summary.overall_ratings">
                  {{(summary.overall_positive / summary.overall_ratings * 100).toFixed(0)}}% /
                  {{(summary.overall_neutral / summary.overall_ratings * 100).toFixed(0)}}% /
                  {{(summary.overall_negative / summary.overall_ratings * 100).toFixed(0)}}%
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
                  {{summary.most_positive}}
                  ({{summary.most_positive_rating}})
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
                <h3 class="text-3xl text-gray-800">{{summary.most_negative}}
                  ({{summary.most_negative_rating}})</h3>
              </div>
            </div>
          </div>
          <!--/Metric Card-->
        </div>
      </div>
      <div class="flex mt-5">
        <div class="w-1/2 text-center">
          <v-popover offset="16">
            <button
              class="bg-transparent hover:bg-blue-500 text-blue-700
              font-semibold hover:text-white py-2 px-4 border border-blue-500
              hover:border-transparent rounded">
              Puppy pictures
            </button>
            <template slot="popover">
              <div class="border-r border-b border-l border-gray-400
                  lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b
                  lg:rounded-b-none lg:rounded-r p-4 flex flex-col
                  justify-between leading-normal">
              Did you like this feature?
                <button v-close-popover
                  @click="handleFeedback('Puppy pictures', 'positive')"
                  class="bg-transparent hover:bg-blue-500 text-blue-700 mt-3
                    font-semibold hover:text-white py-2 px-4
                    border border-blue-500 hover:border-transparent">
                  Yes
                </button>
                <button v-close-popover
                  @click="handleFeedback('Puppy pictures', 'negative')"
                  class="bg-transparent hover:bg-orange-500 text-orange-700 mt-3
                    font-semibold hover:text-white py-2 px-4
                    border border-orange-500 hover:border-transparent">
                  No
                </button>
                <button v-close-popover class="bg-transparent hover:bg-grey-500 text-grey-700 mt-5
                  font-semibold hover:text-white py-2 px-4
                  border border-grey-500 hover:border-transparent">
                  Close
                </button>
              </div>
            </template>
          </v-popover>
        </div>
        <div class="w-1/2 text-center">
          <v-popover offset="16">
            <button
              class="bg-transparent hover:bg-blue-500 text-blue-700
              font-semibold hover:text-white py-2 px-4 border border-blue-500
              hover:border-transparent rounded">
              Cat pictures
            </button>
            <template slot="popover">
              <div class="border-r border-b border-l border-gray-400
                  lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b
                  lg:rounded-b-none lg:rounded-r p-4 flex flex-col
                  justify-between leading-normal">
              Did you like this feature?
                <button v-close-popover
                  @click="handleFeedback('Cat pictures', 'positive')"
                  class="bg-transparent hover:bg-blue-500 text-blue-700 mt-3
                    font-semibold hover:text-white py-2 px-4
                    border border-blue-500 hover:border-transparent">
                  Yes
                </button>
                <button v-close-popover
                  @click="handleFeedback('Cat pictures', 'negative')"
                  class="bg-transparent hover:bg-orange-500 text-orange-700 mt-3
                    font-semibold hover:text-white py-2 px-4
                    border border-orange-500 hover:border-transparent">
                  No
                </button>
                <button v-close-popover class="bg-transparent hover:bg-grey-500 text-grey-700 mt-5
                  font-semibold hover:text-white py-2 px-4
                  border border-grey-500 hover:border-transparent">
                  Close
                </button>
              </div>
            </template>
          </v-popover>
        </div>
      </div>
      <div class="mt-5">

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

  handleFeedback(feature, rating) {
    if (!feature || !rating) {
      return;
    }
    const body = {
      rating_code: rating,
      feature,
    };
    axios.post('http://localhost:8000/ratings', body)
      .then((r) => {
        this.fetchSummary();
      })
      .catch((e) => {
        console.error(e);
      });
  }

  created() {
    this.fetchSummary();
  }
}
</script>
<style lang="scss">
.tooltip {
  &.popover {
    $color: #f9f9f9;

    .popover-inner {
      background: $color;
      color: black;
      padding: 24px;
      border-radius: 5px;
      box-shadow: 0 5px 30px rgba(black, .1);
    }

    .popover-arrow {
      border-color: $color;
    }
  }
}
</style>
