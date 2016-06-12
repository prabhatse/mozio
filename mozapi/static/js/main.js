$( document ).ready(function() {
  // init map and set it for drawing
  map = new Map();
  map.init('map-canvas', 28.4818466, 76.9990324);
  map.initPolygonDrawer();
  //save the service area..
  $("form").submit(function(e) {
    e.preventDefault();
    $(".errors").html("");
    $(".success").text("");
    var data = {'mpoly':map.getCoords(), 'name': $("#id_name").val(), 
                'provider_id' : $('#id_provider_id').val(),
                'price' : $('#id_price').val()
    };
    jQuery.ajax({
      url : "/api/polygon/create/",
      contentType: "application/json; charset=utf-8",
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

  // clean the map.
  $("#clear").click(function(e) {
    e.preventDefault();
    map.clearPolygons();
  });

});
