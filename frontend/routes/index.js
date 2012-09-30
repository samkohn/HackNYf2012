
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
