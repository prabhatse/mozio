$( document ).ready(function() {
  //save the service area..
  $("form").submit(function(e) {
    e.preventDefault();
    $(".errors").html("");
    $(".success").text("");
    var data = {
      'name': $("#id_name").val(), 
      'email': $("#id_email").val(), 
      'phone_no': $("#id_phone_no").val(), 
      'language': $("#id_language").val(), 
      'currency': $("#id_currency").val(), 
    };
    jQuery.ajax({
      url : $(this).attr("action"),
      dataType: 'json',
      type: 'POST',
      data: JSON.stringify(data),
      success:function(data) {
        if ('errors' in data) {
            var errors = "";
            for(var i=0; i<data.errors.length; i++) {
                errors += "<span>"+data.errors[i][0]+"</span> <br />"
            }
            $(".errors").html(errors);
        } else if ('saved' in data) {
            $(".success").text(data.saved);
        }
      },
    });
  });
});
