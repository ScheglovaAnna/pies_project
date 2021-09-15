<template>
  <div>
    <headerMain />
    <template>
      <div class="container">
        <!-- <div class="row"> -->
        <!-- <div class="col-sm-10"> -->
        <h1>Pies</h1>
        <hr />
        <br /><br />
        <!-- <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
                Add Pies
              </v-btn>
            </template>
            <v-card ref="form">
              <v-form @submit.prevent="submitForm">
                <v-card-title>
                  <span class="headline">{{ formTitle }}</span>
                </v-card-title>

                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          type="number"
                          ref="tournament_id"
                          label="ID tournament"
                          v-model="tournament.tournament_id"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          label="Name"
                          v-model="tournament.name"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-autocomplete
                          label="status"
                          v-model="tournament.status"
                          :items="statuses"
                        ></v-autocomplete>
                      </v-col>

                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          type="number"
                          label="Seats number"
                          v-model="tournament.seats_number"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-textarea
                          class="desc-area"
                          solo
                          rows="1"
                          name="input-7-4"
                          label="Prize"
                          v-model="tournament.prize"
                        ></v-textarea>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-autocomplete
                          label="Limitation"
                          v-model="tournament.limitation"
                          :items="limitations"
                        ></v-autocomplete>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          type="date"
                          label="Start date"
                          v-model="tournament.start_date"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          type="date"
                          label="End date"
                          v-model="tournament.end_date"
                        ></v-text-field>
                      </v-col>

                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          type="number"
                          v-model="tournament.discipline_id"
                          label="Discipline"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          type="number"
                          v-model="tournament.employee_id"
                          label="Employee"
                        ></v-text-field>
                      </v-col>

                      <v-col cols="12" sm="12" md="12">
                        <v-autocomplete
                          label="players"
                          clearable
                          deletable-chips
                          multiple
                          small-chips
                          :items="playersList"
                          item-value="user_id"
                          item-text="username"
                          v-model="tournament.players"
                        ></v-autocomplete>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="close">
                    Cancel
                  </v-btn>
                  <v-btn color="blue darken-1" text type="submit"> Save </v-btn>
                </v-card-actions>
              </v-form>
            </v-card>
          </v-dialog> -->
        <v-btn class="card-more">Add Pies</v-btn>
        <br /><br />
        <v-simple-table fixed-header height="300px">
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">
                  Id торта
                </th>
                <th class="text-left">
                  Название
                </th>
                <th class="text-left">
                  Количество в наличии
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="pie in pies" :key="pie.id">
                <td>{{ pie.pies_id }}</td>
                <td>{{ pie.name }}</td>
                <td>{{ pie.have }}</td>
                <td>
                  <v-btn class="card-more">Update</v-btn>
                  <v-btn class="card-more">Delete</v-btn>
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
  name: "Home",
  components: { HeaderMain },
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
