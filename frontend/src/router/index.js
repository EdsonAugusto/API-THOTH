import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import BaseCngrView from "../views/BaseCngrView.vue";
import BaseRedesView from "../views/BaseRedesView.vue";
import BaseVoipView from "../views/BaseVoipView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
    meta: {
      title: "Thoth - Home",
      links: [
        {
          title: "Empresas",
          href: "breadcrumbs_link_1",
        },
        {
          title: "Ramais",
          href: "breadcrumbs_link_2",
        },
        {
          title: "Técnicos",
          href: "breadcrumbs_link_3",
        },
        {
          title: "Datacenters",
          href: "breadcrumbs_link_4",
        },
      ],
    },
  },
  {
    path: "/contatos-uteis",
    name: "contatos-uteis",
    component: BaseCngrView,
    meta: {
      title: "Thoth - Contatos Úteis",
      links: BaseCngrView.links,
    },
  },
  {
    path: "/about",
    name: "about",
    component: AboutView,
    meta: {
      title: "Thoth - About",
      links: BaseCngrView.links,
    },
  },
  {
    path: "/cngr",
    name: "cngr",
    component: BaseCngrView,
    meta: {
      title: "Thoth - CNGR",
      links: BaseCngrView.links,
    },
  },
  {
    path: "/redes",
    name: "redes",
    component: BaseRedesView,
    meta: {
      title: "Thoth - Redes",
      links: BaseRedesView.links,
    },
  },
  {
    path: "/voip",
    name: "voip",
    component: BaseVoipView,
    meta: {
      title: "Thoth - VoIP",
      links: BaseVoipView.links,
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || "Thoth";
  next();
});
export default router;
