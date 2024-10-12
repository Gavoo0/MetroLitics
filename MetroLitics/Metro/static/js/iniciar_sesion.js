$(document).ready(function(){
    $("#submit").click(function(){
        var correo = $("#correo").val();
        var contrasena = $("#contrasena").val();
        var checkbox = $("#checkbox").is(':checked');
        var validarCorreo = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        var valido = true;
    
        if(validarCorreo.test(correo)){
            valido = true;
        }else{
            console.log("hols")
            valido = false;
            event.preventDefault();
        }
    })
})