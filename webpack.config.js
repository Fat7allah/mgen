const path = require('path');
const webpack = require('webpack');

module.exports = {
    entry: {
        'mgen': './mgen/public/js/mgen.js'
    },
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'mgen/public/dist')
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader'
                }
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            }
        ]
    }
};
