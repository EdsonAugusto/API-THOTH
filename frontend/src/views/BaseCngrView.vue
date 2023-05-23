<template>
  <HelloWorldTwo />
  <HelloWorld />
</template>

<script>
import { defineComponent } from "vue";

import HelloWorldTwo from "../components/HelloWorldTwo.vue";

export default defineComponent({
  name: "base-cngr",
  links: [
    {
      title: "Contatos Internos",
      path: "/contatos-internos",
      icon: "mdi mdi-card-account-phone-outline",
    },
    {
      title: "Grupo Empresas",
      path: "/about",
      icon: "mdi mdi-domain",
    },
    {
      title: "Inf. Datacenters",
      path: "datacenters",
      icon: "mdi mdi-bank",
    },
    {
      title: "Inf. Técnicos",
      path: "tecnicos",
      icon: "mdi mdi-account-supervisor",
    },
  ],
  components: {
    HelloWorldTwo,
  },
});
</script>
