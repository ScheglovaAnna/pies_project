<template>
  <div>
    <headerMain />
    <template>
      <div class="container">
        <!-- <div class="row"> -->
        <!-- <div class="col-sm-10"> -->
        <h1>Basket</h1>
        <hr />
        <br /><br />
         <v-btn class="card-more" @click="$router.push(`//`)">Перейти на главную</v-btn>
        <br /><br />
        <v-simple-table fixed-header height="300px">
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">
                  
                </th>
                <th class="text-left">
                  Название
                </th>
                <th class="text-left">
                  Количество
                </th>
                <th class="text-left">
                  Купить
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="pie in pies" :key="pie.id">
                <td>{{ pie.image_pies }}</td>
                <td>{{ pie.name }}</td>
                <td>{{ pie.have }}</td>
                <td>
                  <v-btn class="card-more">Buy</v-btn>
                </td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </div>
      <!-- </div> -->
      <!-- </div> -->
    </template>
  </div>
</template>

<script>
import getAPI from "@/api/getApi.js";
import HeaderMain from "../components/Header";

export default {
  name: "Pie",
  components: { HeaderMain },
  data() {
    return {
      pie: [],
      id: this.$route.params.id,
    };
  },
  methods: {
    async fetchPies() {
      getAPI
        .get(`/${this.id}`)
        .then((response) => {
          this.pie = response.data;
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.fetchPies();
  },
};
</script>
