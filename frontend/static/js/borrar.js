function borrar(email){
    respuesta = confirm("¿Estas seguro de borrar el contacto?");

    if (respuesta){
        // const URL = "http://localhost:8000/contactos";
        const URL = "https://heroku-python-3act-62ad9044fdb9.herokuapp.com/contactos"
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