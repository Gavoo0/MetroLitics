$(document).ready(function(){
    $("#boton-submit").click(function(event){
        linea = $("#linea").val();
        cantidad = $("#aglomeracion").val();
        fecha = $("#fecha").val();
        cantidad2 = $("#personas_bus").val();
        fecha2 = $("#fecha_bus").val();
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

        if(cantidad2 === ""){
            $("#personas_bus").css("border-color","red");
            $("#mensaje_error5").fadeIn();
            valid = false;
        } else {
            $("#personas_bus").css("border-color","#ced4da");
            $("#mensaje_error5").fadeOut();
        }

        if(fecha2 == ""){
            $("#fecha_bus").css("border-color","red");
            $("#mensaje_error4").fadeIn();
            valid = false;
        }else{
            $("#fecha_bus").css("border-color","#ced4da");
            $("#mensaje_error4").fadeOut();
        }

        if(parseInt(cantidad)<parseInt(cantidad2)){
            $("#aglomeracion").css("border-color","red");
            $("#personas_bus").css("border-color","red");
            console.log(cantidad + " <" + cantidad2)
            console.log("menor que")
            valid = false;
        }else{
            $("#personas_bus").css("border-color","#ced4da");
            $("#aglomeracion").css("border-color","#ced4da");
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

    $("#personas_bus").blur(function() {
        cantidad2 = $("#personas_bus").val();
        if(cantidad2 === ""){
            $("#personas_bus").css("border-color","red");
            $("#mensaje_error5").fadeIn();
            valid = false;
        } else {
            $("#personas_bus").css("border-color","#ced4da");
            $("#mensaje_error5").fadeOut();
        }
    });

    $("#fecha_bus").blur(function() {
        fecha2 = $("#fecha_bus").val();
        if(fecha2 == ""){
            $("#fecha_bus").css("border-color","red");
            $("#mensaje_error4").fadeIn();
            valid = false;
        }else{
            $("#fecha_bus").css("border-color","#ced4da");
            $("#mensaje_error4").fadeOut();
        }
    });
});
