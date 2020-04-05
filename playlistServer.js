//jshint esversion:6
//const bodyParser = require("body-parser");
const express = require("express");
const app = express();
const bodyParser = require("body-parser")

app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended:true}))
 
app.route('/playlist')
    .get(function(req, res) {
        params = req.query
        
        console.log('get request')
        console.log('Query Params: ')
        console.log(params)
    })
    .post(function(req, res) {
        console.log('post request')
    });

app.listen(3000, function() {
    console.log("Server started on port 3000");
});

