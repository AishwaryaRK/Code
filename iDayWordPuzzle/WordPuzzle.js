/**
 * Created by akaneri on 9/22/16.
 */


var http = require("http");
var async = require("async");

//    http://api.pearson.com/v2/dictionaries/entries?headword=bus

var url = "/v2/dictionaries/entries?headword=";
var words = ['INITIATI'];

var options = {
    hostname: "api.pearson.com",
    port: 80,
    path: "",
    headers: {
        "Content-Type": "application/json"
    },
    method: "GET"
};

console.log("------------------BEFORE-----------");
console.log(words.length);

var validEnglishWords = [];

async.each(words, function (word, callback) {
    options.path = url + word;
    var body = "";
    http.request(options, function (response) {
        response.setEncoding("utf-8");
        response.on("data", function (chunk) {
            body += chunk;
        });
        response.on("end", function () {
            body = JSON.parse(body);
            console.log(body);
            if (body.results.length > 0) {
                validEnglishWords.push(word);
            }
            callback(null);
        });
        response.on("error", function () {
            callback(null);
        });
    }).end();
}, function () {
    console.log("------------------AFTER-----------");
    console.log(validEnglishWords.length);
});

