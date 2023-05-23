<template>
  <v-app>
    <v-app-bar
      :elevation="2"
      size="small"
      theme="dark"
      :style="{
        background:
          'linear-gradient(to right, #1e5799, #5164a7, #7571b3, #967ebf, #b48dc9)',
      }"
    >
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>THOTH</v-toolbar-title>
      <v-breadcrumbs divider="." :items="items"> </v-breadcrumbs>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" theme="dark" app>
      <v-list density="compact" class="list-group list-group-flush">
        <v-list-subheader color="white">Administrativo:</v-list-subheader>
        <v-divider class="border-opacity-50 ms-2 me-2" color="dark"></v-divider>
        <v-list-item
          v-for="link in links"
          :key="link.title"
          :to="link.path"
          class="list-group-item list-group-item-action mt-1 mb-0 ms-0 me-1 bg-transparent"
          style="border: 2px solid light; border-radius: 10px"
        >
          <template v-slot:prepend>
            <v-icon> {{ link.icon }} </v-icon>
          </template>
          <v-list-item-content>
            <v-list-item-title>{{ link.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-divider class="border-opacity-50" color="dark"></v-divider>
    </v-navigation-drawer>
    <v-main class="bg-grey-lighten-2">
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawer: null,
    items: [
      {
        title: "CNGR",
        disabled: false,
        href: "/cngr",
      },
      {
        title: "REDES",
        disabled: false,
        href: "/redes",
      },
      {
        title: "VOIP",
        disabled: false,
        href: "/voip",
      },
    ],
    homeLinks: [
      {
        title: "Contatos Internos",
        path: "/contatos-uteis",
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
    aboutLinks: [
      {
        title: "Sobre",
        href: "/sobre",
      },
      {
        title: "Versão",
        href: "/versao",
      },
      {
        title: "Reportar",
        href: "/reportar",
      },
    ],
  }),
  computed: {
    links() {
      if (this.$route.name === "home") {
        return this.homeLinks;
      } else if (this.$route.name === "about") {
        return this.$route.meta.links;
      } else if (this.$route.name === "cngr") {
        console.log(this.$route.title);
        return this.$route.meta.links;
      } else {
        return this.$route.meta.links;
      }
    },
  },
};
</script>
