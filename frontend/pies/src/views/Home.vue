<template>
  <div>
    <headerMain />
    <pies />
    <footerMain />
  </div>
</template>

<script>
import Pies from "../components/Pies";
import HeaderMain from "../components/Header";
import FooterMain from "../components/Footer";

export default {
  name: "Home",

  components: {
    Pies,
    HeaderMain,
    FooterMain,
  },
};
</script>
