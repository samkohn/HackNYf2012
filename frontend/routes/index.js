
/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index', { title: 'Hey There!' });
};

exports.query = {};

exports.query.etsy = function(req, res){
  res.render('queryetsy', { title: 'Etsy', api: 'Etsy' });
};
