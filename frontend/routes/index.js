var http = require('http');

var imageFor = {};
imageFor['etsy'] = 'https://s3.amazonaws.com/siteassets.etsy.com/press/Website/etsy-logo.png';
imageFor['donorschoose'] = 'http://cdn.donorschoose.net/images/link/dc_banner_280_60.jpg';
imageFor['behance'] = 'http://www.veryicon.com/icon/png/Internet%20%26%20Web/Pretty%20Social%20Media/behance.png';

var apiQueriesFor = {};
apiQueriesFor['etsy'] = [
  { 'type' : 'color',
    'display' : 'Color'},
  { 'type' : 'category',
    'display' : 'Etsy Category'},
  { 'type' : 'min_price',
    'display' : 'Minimum Price'},
  { 'type' : 'max_price',
    'display' : 'Maximum Price'},
  { 'type' : 'materials',
    'display' : 'Material'},
  { 'type' : 'private',
    'display' : 'Number of Items in API'},
  { 'type' : 'keywords',
    'display' : 'Item Description'}];

apiQueriesFor['donorschoose'] = [
  { 'type' : 'null',
    'display' : 'Search by Keyword'}];

apiQueriesFor['behance'] = [
  { 'type' : 'projects?q',
    'display' : 'Keyword (Project)'},
  { 'type' : 'projects?city',
    'display' : 'City (Project)'},
  { 'type' : 'projects?tags',
    'display' : 'Project Tag'},
  { 'type' : 'users?q',
    'display' : 'Keyword (User)'},
  { 'type' : 'users?city',
    'display' : 'City (User)'},
  { 'type' : 'users?tags',
    'display' : 'User Tag'}];


/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index', { title: 'Order of Magnitude!', apis : imageFor });
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

exports.query = function(req, res){
  var api = req.params.api;
  var image = imageFor[api];
  res.render('query', { 
    title: 'Query ' + api + '!',
    api: api,
    image: image,
    options: apiQueriesFor[api],
  });
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
      response.title = 'Results';

      for(var i = 0; i < apiQueriesFor[api].length; i++) {
        if(apiQueriesFor[api][i]['type'] === type)
        {
          console.log('type = ' + type);
          type = apiQueriesFor[api][i]['display'];
          break;
        }
      }

      response.type = type;
      response.search = search;

      res.render('result', response);
    });
  });
};
