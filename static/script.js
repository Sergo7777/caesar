    $(document).ready(function(){
      $("#encrypt, #decrypt").click(function (event) {
        var postData = {
          "text": $("#text").val(),
          "text2": $("#text2").val(),
          "mode" : event.target.id
       };
        $.ajax({
            url: "encrypted",
            type: "POST",
            data: postData,
            dataType: "json",
            cache: false,
            success: function(response) {
                $("#result").text(response)
            },
            error : function(xhr,errmsg,err) {
             console.log(xhr.status + ": " + xhr.responseText);
            }
        });
        return false;
    });
    });  
$(document).ready(function(){
  $('textarea').on('input', function () {
    var msg = {
      "input_value" : $(this).val(),
    };
      $.ajax({
            url: "diagram",
            type: "POST",
            data: msg,
            dataType: "json",
            cache: false,
            success: function(response) {
                if (response > 0 && response !=26) {
                        $("#key").show().text("Ваш текст зашифрован с ключем: " + response);
                }
                else{
                  $("#key").show().text("Введите текст больше 20 букв");
              }
            }
        });
        return false;
    });
});
