function editar(email, nombre, telefono){
    var respuesta = confirm("¿Estas seguro de actualizar el contacto?");

    if (respuesta){
        const URL = "https://heroku-python-3act-62ad9044fdb9.herokuapp.com/contactos"
        //const URL = "http://localhost:8000/contactos";
        var request = new XMLHttpRequest;
        request.open('PUT',URL +"/" +email,true);
        request.setRequestHeader("Content-Type", "application/json");
        data = JSON.stringify( {
            "email": email,
            "nombre": nombre,
            "telefono": telefono})
        request.send(data)

        request.onload = (e) => {
            const response = request.responseText;
            const json = JSON.parse(response);
            console.log(json);
            console.log("status_code: " + request.status);
            window.location.href = "../templates/index.html"
        }
    }else{ 
        console.log("El usuario ha cancelado.");
    }
}