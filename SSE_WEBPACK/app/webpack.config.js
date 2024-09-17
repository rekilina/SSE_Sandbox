const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
	mode: 'development',
	entry: './src/index.js',
	output: {
		path: path.resolve(__dirname, 'dist'),
		filename: 'bundle.js',
	},
	module: {
		rules: [
			{
				test: /\.js$/,
				exclude: /node_modules/,
				use: {
					loader: 'babel-loader',
					options: {
						presets: ['@babel/preset-env', '@babel/preset-react'],
					},
				},
			},
		],
	},
	plugins: [
		new HtmlWebpackPlugin({
			template: './src/index.html',
		}),
	],
	devServer: {
		static: {
			directory: path.join(__dirname, 'dist'),
		},
		compress: true,
		port: 9000,
		proxy: [
			{
				context: ['/stream'],
				target: 'http://localhost:5000',
				changeOrigin: true,
				ws: true,
				secure: false,
				onProxyReq: (proxyReq, req, res) => {
					proxyReq.setHeader('Connection', 'keep-alive'); 
				},
				bypass: function (req, res, proxyOptions) {
					if (req.headers.accept && req.headers.accept.indexOf('text/event-stream') !== -1) {
						console.log('Skipping proxy for SSE request');
						return false;
					}
				}
			}
		],
	},
};
