$(document).ready(function(){
    $("#boton-submit").click(function(event){
        linea = $("#linea").val();
        cantidad = $("#aglomeracion").val();
        valid = true;

        if(linea === null){
            $("#linea").css("border-color","red");
            $("#mensaje_error").fadeIn();
            valid = false;
        } else {
            $("#linea").css("border-color","#ced4da"); 
            $("#mensaje_error").fadeOut();
        }

        if(cantidad === ""){
            $("#aglomeracion").css("border-color","red");
            $("#mensaje_error2").fadeIn();
            valid = false;
        } else {
            $("#aglomeracion").css("border-color","#ced4da");
            $("#mensaje_error2").fadeOut();
        }


        $("#linea").blur(function() {
            linea = $("#linea").val();
            if(linea === null){
                $("#linea").css("border-color","red");
                $("#mensaje_error").fadeIn();
                valid = false;
            } else {
                $("#linea").css("border-color","#ced4da"); 
                $("#mensaje_error").fadeOut();
            }
        });

        $("#aglomeracion").blur(function(){
            cantidad = $("#aglomeracion").val();
            if(cantidad === ""){
                $("#aglomeracion").css("border-color","red");
                $("#mensaje_error2").fadeIn();
                valid = false;
            } else {
                $("#aglomeracion").css("border-color","#ced4da");
                $("#mensaje_error2").fadeOut();
            }
        })

        if (!valid) {
            event.preventDefault();
        }
    });
});
