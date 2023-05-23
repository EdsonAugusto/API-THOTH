<template>
  <HomeRedes />
</template>

<script>
import { defineComponent } from "vue";

import HomeRedes from "../components/HomeRedes.vue";

export default defineComponent({
  name: "base-redes",
  links: [
    {
      title: "Exemplo Botão",
      path: "/exemplo",
      icon: "mdi mdi-card-account-phone-outline",
    },
  ],
  components: {
    HomeRedes,
  },
});
</script>
