<template>
  <div>
    <headerMain />
    <div class="container">
      <!-- <div class="row"> -->
      <!-- <div class="col-sm-10"> -->
      <h1>Pies</h1>
      <hr />
      <br /><br />
      <v-btn color="#8e8b99" dark class="mb-2" v-bind="attrs" @click="$router.push(`/admin_pies/`)">
        Редактирование тортиков
      </v-btn>
      <br /><br />
    </div>
    <v-container>
      <v-data-table
        :headers="headers"
        :items="orders"
        sort-by="id"
        class="elevation-1"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title>Orders</v-toolbar-title>
            <v-divider class="mx-4" inset vertical></v-divider>
            <v-spacer></v-spacer>
            <v-dialog v-model="dialog" max-width="500px">
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  color="#8e8b99"
                  dark
                  class="mb-2"
                  v-bind="attrs"
                  v-on="on"
                >
                  New Order
                </v-btn>
              </template>
              <v-card>
                <v-card-title>
                  <span class="text-h5">{{ formTitle }}</span>
                </v-card-title>

                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.id"
                          label="Номер заказа"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.buying_type"
                          label="Тип заказа"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.status_type"
                          label="Статус"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.quantity"
                          label="Количество"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.comment"
                          label="Комментарий"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.date_create"
                          label="Дата заказа"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.data_order"
                          label="Дата доставки"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="close">
                    Cancel
                  </v-btn>
                  <v-btn color="blue darken-1" text @click="save">
                    Save
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
            <v-dialog v-model="dialogDelete" max-width="500px">
              <v-card>
                <v-card-title class="text-h5"
                  >Are you sure you want to delete this item?</v-card-title
                >
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="closeDelete"
                    >Cancel</v-btn
                  >
                  <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                    >OK</v-btn
                  >
                  <v-spacer></v-spacer>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-toolbar>
        </template>
        <template v-slot:item.actions="{ item }">
          <v-icon small class="mr-2" @click="editItem(item)">
            mdi-pencil
          </v-icon>
          <v-icon small @click="deleteItem(item)">
            mdi-delete
          </v-icon>
        </template>
        <template v-slot:no-data>
          <v-btn color="primary">
            Reset
          </v-btn>
        </template>
      </v-data-table>
    </v-container>
  </div>
</template>
<script>
import getAPI from "@/api/getApi.js";
import HeaderMain from "../components/Header";

export default {
  components: { HeaderMain },
  data: () => ({
    dialog: false,
    dialogDelete: false,
    headers: [
      { text: "Номер заказа", value: "order" },
      { text: "Дата заказа", value: "date_create" },
      { text: "Статус заказа", value: "status_type" },
      { text: "Обработчик заказа", value: "buying_type" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    orders: [],
    editedIndex: -1,
    editedItem: {
      id: 0,
      date_create: "",
      status_type: "",
      buying_type: "",
    },
    defaultItem: {
      id: 0,
      date_create: "",
      status_type: "",
      buying_type: "",
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Order" : "Edit Order";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },
  created() {
    this.fetchOrders();
  },

  methods: {
    async fetchOrders() {
      getAPI
        .get(`orders/`)
        .then((response) => {
          this.orders = response.data;
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    editItem(item) {
      this.editedIndex = this.orders.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.orders.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      this.orders.splice(this.editedIndex, 1);
      this.closeDelete();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.orders[this.editedIndex], this.editedItem);
      } else {
        this.orders.push(this.editedItem);
      }
      this.close();
    },
  },
};
</script>
