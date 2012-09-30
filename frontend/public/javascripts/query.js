$('document').ready( function() {
  $('#submit').click( function() {
    var $form = $('#etsyquery');
    $form.attr('action', '/sendquery');
    $form.attr('method', 'GET');
    $form.submit();
    console.log('submitted');
    /*
    var type = $('#type').val();
    var api = $('#api').val();
    var search = $('#search').val();



    var url = 'http://ec2.rjehlers.com:8080/query/?';
    url += 'api=' + api + '&';
    url += 'type=' + type + '&';
    url += 'search=' + search;

    console.log('getting url = ' + url);
    $.get(url, function(responseText) {
      var response = JSON.parse(responseText);
      console.log('responseText = ' + responseText);
      console.log('JSON.stringify(response) = ' + JSON.stringify(response));
    });
    */

  });



});
