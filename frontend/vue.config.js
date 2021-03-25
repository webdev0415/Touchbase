// vue.config.js
module.exports = {
  lintOnSave: false,
  pages: {
    index: {
      entry: 'src/main.js',
      template: 'index.html',
      filename: 'index.html',
    },
  },
  // /* to configure ui/public as a static assets folder */
  // configureWebpack: {
  //   plugins: [
  //     new CopyWebpackPlugin([{
  //       from: path.join(__dirname, "ui/public"),
  //       to: path.join(__dirname, "ui/dist"),
  //       toType: "dir",
  //       ignore: [ "index.html", ".DS_Store" ]
  //     }])
  //   ]
  // },

  /* to configure ui/public as the location of the template */
  // chainWebpack: config => {
  //   config.plugin("html")
  //     .tap(args => {
  //       args[0].template = path.join(__dirname,"index.html");
  //       return args;
  //     })
  // },
  devServer: {
    hot: true,
    hotOnly: true,
    disableHostCheck: true,
    historyApiFallback: true,
    public: '0.0.0.0:8000',
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
      'Access-Control-Allow-Headers': 'X-Requested-With, content-type, Authorization'
    },
    watchOptions: {
      poll: 1000,
      ignored: '/app/node_modules/'
    }
  }
}
