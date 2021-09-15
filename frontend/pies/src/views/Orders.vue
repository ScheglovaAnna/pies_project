<template>
  <div>
    <headerMain />
    <div class="container">
    <div class="class">Редактирование тортов</div>
        <v-btn class="card-more" @click="$router.push(`/admin_pies/`)">Редактирование</v-btn>
    <div class="class">Заказы пользователей</div>
    <v-simple-table fixed-header height="300px">
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">
              Номер заказа
            </th>
            <th class="text-left">
              Дата заказа
            </th>
            <th class="text-left">
              Статус заказа
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="orders in orders" :key="orders.id">
            <td>{{ orders.id }}</td>
            <td>{{ orders.date_create }}</td>
            <td>{{ orders.status_type }}</td>
            <td>
                  <v-btn class="card-more">Update</v-btn>
                  <v-btn class="card-more">Delete</v-btn>
                </td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </div>
   </div>
</template>

<script>
import getAPI from "@/api/getApi.js";
import HeaderMain from "../components/Header";
export default {
  name: "Orders",
  components: { HeaderMain },
  data() {
    return {
      orders: [],
    };
  },
  methods: {
    async fetchOrders() {
      getAPI
        .get("orders/")
        .then((response) => {
          this.orders = response.data;
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
          alert("Сервер не получил данные");
        });
    },
  },
  created() {
    this.fetchOrders();
  },
};
</script>

<style scoped>
.class{
  font-weight: 600;
  font-size: 28px;
  line-height: 20px;
  color: black;
  margin-top: 30px;
  margin-bottom: 20px;
}
.text-left{
   line-height: 20px; 
}
.card-more{
  color:#8e8b99!important;
}

</style>