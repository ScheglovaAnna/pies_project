<template>
  <v-card class="overflow-hidden margin">
    <v-app-bar
      absolute
      color="white"
      elevate-on-scroll
      scroll-target="#scrolling-techniques-7"
    >
      <v-toolbar-title>Pies</v-toolbar-title>

      <v-spacer></v-spacer>
      <!-- <div class="profile">
        <div v-if="username == 'admin'">
            <router-link to="administration" class="linkadmin">
              <v-btn depressed color="#8e8b99">
                Admin panel
              </v-btn>
            </router-link>
          </div>
        <div  class="profile d-flex" v-else-if="auth">
          <div class="profile_info">
            <v-btn icon @click="$router.push(`/basket/`)">
              <v-icon>mdi-basket</v-icon>
            </v-btn>
          </div>
          <v-btn depressed color="#8e8b99" @click="logout()">
            Log out
          </v-btn>
        </div> -->

      <!-- <div v-else>
          <v-toolbar-items>
            <div class="my-2">
              <router-link to="/Authorization" class="linksignin"
                ><v-btn class="mr-5" color="#8e8b99" dark>
                  Authorization
                </v-btn></router-link
              >
              <v-btn color="#8e8b99" dark>
                <router-link to="/Registration"
                  ><span class="button_signup">Registration</span></router-link
                >
              </v-btn>
            </div>
          </v-toolbar-items>
        </div>
      </div> -->
      <div class="profile">
        <div v-if="auth" class="profile d-flex">
          <div v-if="username == 'admin'">
            <router-link to="administration" class="linkadmin">
              <v-btn depressed color="#8e8b99">
                Admin panel
              </v-btn>
            </router-link>
          </div>
          <div class="profile_info" v-else></div>
          <v-btn icon @click="$router.push(`/basket/`)">
            <v-icon>mdi-basket</v-icon>
          </v-btn>
          <v-btn depressed color="#8e8b99" @click="logout()">
            Log out
          </v-btn>
        </div>
        <div v-else>
          <v-toolbar-items>
            <div class="my-2">
              <router-link to="/authorization" class="linksignin"
                ><v-btn class="mr-5" color="#8e8b99" dark>
                  Authorization
                </v-btn></router-link
              >
              <v-btn color="#8e8b99" dark>
                <router-link to="/registration"
                  ><span class="button_signup">Registration</span></router-link
                >
              </v-btn>
            </div>
          </v-toolbar-items>
        </div>
      </div>
    </v-app-bar>
    <v-container style="height: 60px;"> </v-container>
  </v-card>
</template>

<script>
import $ from "jquery";
// import getAPI from "@/api/getApi.js";

export default {
  data() {
    return {
      block: 1,
      username: "",
      role: "",
      auth: true,
    };
  },
  created() {
    this.isLogin();
  },
  methods: {
    async isLogin() {
      let token = localStorage.getItem("auth_token");
      if (token) {
        this.auth;
        $.ajax({
          url: "http://127.0.0.1:8000/auth/users/me",
          type: "GET",
          headers: {
            Authorization: "Token " + token,
          },
          success: (response) => {
            this.username = response.username;
            if (response.post) this.role = response.post;
            else if (this.username == "admin") this.role = "Admin account";
            else this.role = "Guest";
          },
          error: (response) => {
            console.log(response);
          },
        });
      } else {
        this.auth = false;
      }
    },
    logout() {
      localStorage.removeItem("auth_token");
      window.location.replace("/");
    },
  },
};
</script>

<style>
.linkadmin {
  text-decoration: none;
  margin-right: 5px;
}
.name {
  color: #8e8b99;
}
.post {
  font-size: 12px;
}
.profile {
  align-items: center !important;
}
.profile_info p {
  margin-bottom: 0px !important;
}
.linksignin {
  text-decoration: none;
}
.b_list {
  text-align: center;
}
.nav-menu {
  border-bottom: 3px solid transparent;
  display: flex;
  transition: 0.4s;
  background: none !important;
  background-color: none !important;
}
.nav-menu:hover {
  background-color: none;
  border-bottom-color: #7b7596;
}
.nav-menu span {
  margin-right: 5px;
}
.cybernm_link {
  text-decoration: none;
  color: white !important;
}
.button_signup {
  color: #221d3b;
}
.header_back {
  background: #50465c !important;
}
.cybernm_header {
  font-size: 28px !important;
  font-weight: 900;
  color: white;
}
</style>
