const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
  transpileDependencies: true,

  devServer: {
    host: "0.0.0.0", // ou "localhost", dependendo das suas necessidades
    allowedHosts: [
      "localhost",
      "127.0.0.1",
      "140.1.53.59",
    ],
  },

  pluginOptions: {
    vuetify: {
      // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
    },
  },
});
