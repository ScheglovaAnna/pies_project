<template>
  <div>
    <headerMain />
    <div class="container">
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md6>
            <v-card class="elevation-12">
              <v-toolbar dark-color="primary">
                <v-toolbar-title>Авторизация </v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    v-model="username"
                    id="username"
                    name="username"
                    label="username"
                    type="username"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="password"
                    id="password"
                    name="password"
                    label="password"
                    type="password"
                    required
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="#8e8b99" @click="setLogin()"
                  >Продолжить</v-btn
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
export default {
  components: { HeaderMain },
  name: "Login",
  data: () => ({
    username: undefined,
    form: false,
    isLoading: false,
    password: undefined,
  }),
  methods: {
    async setLogin() {
      $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/auth/token/login/",
        data: {
          username: this.username,
          password: this.password,
        },
        success: (response) => {
          localStorage.setItem("auth_token", response.auth_token);
          window.location.replace("/");
        },
        error: (response) => {
          if (response.status === 400) {
            alert("Логин или пароль неверный");
          }
        },
      });

      //   getAPI
      //     .get(`auth/token/login/`)
      //     .then((response) => {
      //      this.username =  response.username;
      //      this.password = response.password;
      //     })
      //     .success((response) => {
      //       localStorage.setItem("auth_token", response.auth_token);
      //       window.location.replace("/");
      //     })
      //     .catch((error) => {
      //       console.log(error);
      //     });
    },
  },
};
</script>
