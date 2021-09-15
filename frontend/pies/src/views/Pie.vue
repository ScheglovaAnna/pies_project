<template>
  <div>
    <headerMain />
    <div class="container">
      <div class="pie">
        <div class="pie-image">
          <img :src="pie.image_pies" alt="" />
        </div>
        <div class="pie-info">
          <h1 class="pie-title">{{ pie.name }}</h1>

          <div class="decription">
            <div class="item">
              <p>Вес:</p>
              <span>{{ pie.weight }}</span>
            </div>
            <div class="item">
              <p>Изготовитель:</p>
              <span>{{ pie.produser }}</span>
            </div>
            <div class="item">
              <p>Цена:</p>
              <span>{{ pie.price }}</span>
              <span>/{{ pie.have }}</span>
            </div>
            <div class="item">
              <p>Информация:</p>
              <span>{{ pie.information }}</span>
            </div>
            <!-- <div class="plus-minus">
              <span class="minus"
                ><v-icon>
                  mdi-minus
                </v-icon></span> -->
            <div class="item">
              <p>Количество:</p>
              <v-text-field
                v-model="blue"
                class="mt-0 pt-0"
                type="number"
                style="width: 60px"
                min="1"
                max="100"
              ></v-text-field>
            </div>
            <!-- <span class="plus"
                ><v-icon>
                  mdi-plus
                </v-icon></span>
            </div> -->
            <v-btn class="card-cart" color="#8e8b99">
              Добавить в корзину
            </v-btn>
            <!-- <div class="item">
              <span>{{ pie.information_2 }}</span>
            </div> -->
          </div>
        </div>
      </div>
      <div class="item-information">
        <div>Состав:</div>
        <span>{{ pie.information_2 }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pie {
  display: flex;
  flex-direction: row;
}
.decription {
  margin-top: 25px;
}
.card-card {
  color: #8e8b99 !important;
}
.pie-image {
  border-radius: 15px;
  /* overflow: hidden; */
}
/* .plus-minus{

} */
/* .plus:target {
  cursor: pointer;
}
.minus {
  cursor: pointer;
} */
.pie-info {
  margin-left: 60px;
  display: block;
}

.item {
  display: flex;
  margin-bottom: 7px;
}
.item-information {
  display: block;
  margin-bottom: 20px;
  margin-top: 20px;
  justify-content: space-around;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 28px;
  color: #000000;
}
.item-information div {
  margin-bottom: 7px;
}
.quantity {
  width: 50px;
  text-align: center;
  font-size: 26px;
  border: 1px solid #ddd;
  border-radius: initial;
  display: inline-block;
  vertical-align: middle;
}
.item p {
  margin-right: 20px;
  color: rgb(156, 156, 156);
}
.item span {
  color: black;
  font-weight: 900;
}

.pie-title {
  font-weight: 900;
  font-size: 28px;
  line-height: 34px;
  color: black;
}

.pie-image img {
  width: 600px;
  height: 400px;
  border-radius: 15px;
}
</style>

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
        .get(`onePies/${this.id}`)
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
