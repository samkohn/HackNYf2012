var http = require('http');
/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index', { title: 'Hey There!' });
};

exports.result = function(req, res){
  
  // Get the response parameters
  var response = {};

  response.title= 'Results';
  response.api = req.query.api;
  response.value = req.query.value;
  response.factor = req.query.factor;
  response.comparison = req.query.comparison;
  response.comparisonValue = req.query.comparisonValue; 
  response.imageLink = req.query.image;

  res.render('result', response);

};

exports.query = {};

exports.query.etsy = function(req, res){
  res.render('queryetsy', { title: 'Etsy', api: 'Etsy' });
};

exports.sendquery = function(req, res){
  var type = req.query.type;
  var api = req.query.api;
  var search = req.query.search;

  var path = '/query/?';
  path += 'api=' + api + '&';
  path += 'type=' + type + '&';
  path += 'search=' + search;

  var host = 'ec2.rjehlers.com';
  var port = 8080;
  
  var options = {host : host, port : port, path : path};

  http.get(options, function(response) {
    response.on('data', function(data) {
      var response = JSON.parse(data);
      console.log('data = ' + data);
      console.log('JSON.stringify(response) = ' + JSON.stringify(response));
      res.render('queryetsy', { title: 'Etsy', api: 'Etsy' });
    });
  });
};
