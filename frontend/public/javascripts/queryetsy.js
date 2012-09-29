$('document').ready( function() {
  $('#submit').click( function() {
    var $form = $('#etsyquery');
    $form.attr('action', 'http://ec2.rjehlers.com:8080/');
    $form.attr('method', 'GET');
    $form.submit();
    console.log('submitted');
  });



});
