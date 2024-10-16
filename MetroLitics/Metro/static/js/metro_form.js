$(document).ready(function(){
    $("#boton-submit").click(function(event){
        linea = $("#linea").val();
        cantidad = $("#aglomeracion").val();
        fecha = $("#fecha").val();
        linea2 = $("#linea2").val();
        cantidad2 = $("#personas").val();
        fecha2 = $("#fecha2").val();
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

        if(fecha == ""){
            $("#fecha").css("border-color","red");
            $("#mensaje_error1").fadeIn();
            valid = false;
        }else{
            $("#fecha").css("border-color","#ced4da");
            $("#mensaje_error1").fadeOut();
        }


        if(linea2 === null){
            $("#linea2").css("border-color","red");
            $("#mensaje_error3").fadeIn();
            valid = false;
        } else {
            $("#linea2").css("border-color","#ced4da"); 
            $("#mensaje_error3").fadeOut();
        }

        if(cantidad2 === ""){
            $("#personas").css("border-color","red");
            $("#mensaje_error5").fadeIn();
            valid = false;
        } else {
            $("#personas").css("border-color","#ced4da");
            $("#mensaje_error5").fadeOut();
        }

        if(fecha2 == ""){
            $("#fecha2").css("border-color","red");
            $("#mensaje_error4").fadeIn();
            valid = false;
        }else{
            $("#fecha2").css("border-color","#ced4da");
            $("#mensaje_error4").fadeOut();
        }

        if (!valid) {
            event.preventDefault();
        }

    });
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

    $("#fecha").blur(function(){
        fecha = $("#fecha").val();
        if(fecha == ""){
            $("#fecha").css("border-color","red");
            $("#mensaje_error1").fadeIn();
            valid = false;
        }else{
            $("#fecha").css("border-color","#ced4da");
            $("#mensaje_error1").fadeOut();
        }
    })

    $("#linea2").blur(function() {
        linea2 = $("#linea2").val();
        if(linea2 === null){
            $("#linea2").css("border-color","red");
            $("#mensaje_error3").fadeIn();
            valid = false;
        } else {
            $("#linea2").css("border-color","#ced4da"); 
            $("#mensaje_error3").fadeOut();
        }
    });

    $("#personas").blur(function() {
        cantidad2 = $("#personas").val();
        if(cantidad2 === ""){
            $("#personas").css("border-color","red");
            $("#mensaje_error5").fadeIn();
            valid = false;
        } else {
            $("#personas").css("border-color","#ced4da");
            $("#mensaje_error5").fadeOut();
        }
    });

    $("#fecha2").blur(function() {
        fecha2 = $("#fecha2").val();
        if(fecha2 == ""){
            $("#fecha2").css("border-color","red");
            $("#mensaje_error4").fadeIn();
            valid = false;
        }else{
            $("#fecha2").css("border-color","#ced4da");
            $("#mensaje_error4").fadeOut();
        }
    });
});
