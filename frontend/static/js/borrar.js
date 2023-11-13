function borrar(email){
    respuesta = confirm("¿Estas seguro de borrar el contacto?");

    if (respuesta){
        const URL = "http://localhost:8000/contactos";
        var request = new XMLHttpRequest;
        request.open('DELETE',URL +"/" +email,true);
        request.send();
        request.onload = () => {
            const response = request.responseText;
            window.location.href = "../templates/index.html"
        }
    }else{
        console.log("El usuario ha cancelado.");
    }
}