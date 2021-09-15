<template>
  <!-- <v-parallax src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"> -->
  <div class="container">
    <div class="v-list-items" v-for="pie in pies" :key="pie.pies_id">
      <div class="card">
        <!-- <v-img class="card-image">{{ pie.image_pies }}</v-img> -->
        <div class="card-image">
          <img :src="pie.image_pies" alt="" />
        </div>
        <div class="card-text">
          <span class="card-name">{{ pie.name }}</span>
          <div class="card-inform">{{ pie.information }}</div>
          <div class="card-price">{{ pie.price }}</div>
          <span class="card-sale" v-if= "!null" > {{ pie.sale }}</span>
        </div>

        <div class="card-buttons">
          <v-btn class="card-cart" :key="pie.pies_id" @click="$router.push(`/basket/`)">
            В корзину
          </v-btn>
          <v-btn class="card-more" @click="$router.push(`/pie/${pie.pies_id}`)">Подробнее</v-btn>
        </div>
      </div>
    </div>
  </div>
  <!-- </v-parallax> -->
</template>

<style scoped>
.container {
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: space-between;
  /* overflow: hidden; */
}

.card {
  display: block;
  align-items: center;
  justify-content: space-between;
  width: 300px;
  height: 400px;
  background: white;
  border-radius: 18px;
  overflow: hidden;

  transition: 0.6s ease;
  cursor: pointer;
}

.card-price{
  font-size: 18px;
  font-weight: 500;
}

.card-buttons{
  padding: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-more{
  color:#8e8b99!important;
}
.card-card{
  color:#7a719b!important;
}

.card-image img {
  width: 300px;
}
.card-text {
  text-align: center;
  padding: 10px;
}

.card-name {
  color: rgb(27, 27, 27);
  font-size: 18px;
  font-weight: 500;
  line-height: 22px;
}
.card-inform {
  color: rgb(88, 86, 86);
  font-size: 18px;
  font-weight: 500;
  line-height: 22px;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.6);
}
/* .v-list-items {
  display: flex!important;
} */
/* .container {
  display: flex !important;
  
} */
h1 {
  color: white;
}
</style>

<script>
import getAPI from "@/api/getApi.js";
export default {
  name: "Home",
  components: {},
  data() {
    return {
      pies: [],
    };
  },
  methods: {
    async fetchPies() {
      getAPI
        .get("pies/")
        .then((response) => {
          this.pies = response.data;
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
          alert('Сервер не получил данные');
        });
    },
  },
  created() {
    this.fetchPies();
  },
};
</script>
