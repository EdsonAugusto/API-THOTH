<template>
  <HomeVoip />
</template>

<script>
import { defineComponent } from "vue";

import HomeVoip from "../components/HomeVoip.vue";

export default defineComponent({
  name: "base-voip",
  links: [
    {
      title: "Exemplo Botão",
      path: "/exemplo",
      icon: "mdi mdi-card-account-phone-outline",
    },
  ],
  components: {
    HomeVoip,
  },
});
</script>
