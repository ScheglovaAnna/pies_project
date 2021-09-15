import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/registration",
    name: "Registration",
    component: () =>
      import(/* webpackChunkName: "registration" */ "../views/Registration.vue"),
  },
  {
    path: "/authorization",
    name: "Authorization",
    component: () =>
      import(/* webpackChunkName: "authorization" */ "../views/Authorization.vue"),
  },
  {
    path: "/orders",
    name: "Orders",
    component: () =>
      import(/* webpackChunkName: "oreders" */ "../views/Orders.vue"),
  },
  {
    path: "/basket",
    name: "Basket",
    component: () =>
      import(/* webpackChunkName: "basket" */ "../views/Basket.vue"),
  },
  {
    path: "/admin_pies",
    name: "Admin_pies",
    component: () =>
      import(/* webpackChunkName: "admin_pies" */ "../views/Admin_pies.vue"),
  },
  {
    path: "/pie/:id",
    name: "Pie",
    component: () =>
      import(/* webpackChunkName: "pie" */ "../views/Pie.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
