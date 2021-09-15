<template>
  <div>
    <headerMain />
    <div class="container">
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md6>
            <v-card class="elevation-12">
              <v-toolbar dark-color="primary">
                <v-toolbar-title>Регистрация </v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    v-model="username"
                    id="username"
                    name="username"
                    label="Username"
                    type="username"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="email"
                    id="email"
                    name="email"
                    label="Email"
                    type="email"
                    required
                  ></v-text-field>
                  <v-text-field
                    id="password"
                    v-model="password"
                    name="password"
                    label="Password"
                    type="password"
                    required
                  ></v-text-field>
                  <v-text-field
                    id="first_name"
                    v-model="first_name"
                    name="first_name"
                    label="Name"
                    type="text"
                    required
                  ></v-text-field>
                  <v-text-field
                    id="last_name"
                    v-model="last_name"
                    name="last_name"
                    label="Last_name"
                    type="text"
                    required
                  ></v-text-field>
                  <v-text-field
                    id="telephone_number"
                    v-model="telephone_number"
                    name="telephone_number"
                    label="Telephone"
                    type="text"
                    required
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="#8e8b99"
                  @click="setSignup()"
                  class="white--text"
                  depressed
                  style="
            width: 470px;
            height: 45px;
            margin-bottom: 15px;
            display: flex;
            justfy-content: center;
            align-items: center;
            border-radius: 10px;
          "
                  >Зарегистрироваться</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </div>
  </div>
</template>

<script>
import $ from "jquery";
import HeaderMain from "../components/Header";
// import getAPI from "@/api/getApi.js";
export default {
  name: "Registration",
  components: { HeaderMain },

  data: () => ({
    username: undefined,
    password: undefined,
    telephone_number: undefined,
    last_name: undefined,
    first_name: undefined,
    email: undefined,
  }),
  methods: {
    async setSignup() {
      $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/auth/users/",

        data: {
          username: this.username,
          first_name: this.first_name,
          password: this.password,
          email: this.email,
          telephone_number: this.telephone_number,
          last_name: this.last_name,
        },
        success: (response) => {
          window.location.replace("/");
          console.log(response);
        },
        error: (response) => {
             if (response.status === 400) {
          alert("Ошибка");}
        },
      });
    },
  },
};
</script>
