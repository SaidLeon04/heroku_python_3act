function ver(email){
    var urlParams = new URLSearchParams(window.location.search);
    var email = urlParams.get('email');
    console.log("email: " + email);
    const URL = "https://heroku-python-3act-62ad9044fdb9.herokuapp.com/contactos"
    //const URL = "http://localhost:8000/contactos";
    var request = new XMLHttpRequest;
    request.open('GET',URL +"/" +email,true);

    request.send();
    request.onload = () => {
        const response = request.responseText;
        const json = JSON.parse(response);
        console.log("response: " + response);
        email = json["email"];
        nombre = json["nombre"];
        telefono = json["telefono"];
        
        var labelEmail = document.createElement("label");
        var labelNombre = document.createElement("label");
        var labelTelefono = document.createElement("label");
        var saltos = document.createElement("br");

        labelEmail.setAttribute("for", "email");
        labelEmail.textContent = "Correo: " + email;
        labelNombre.setAttribute("for", "nombre");
        labelNombre.textContent = "Nombre: " + nombre;
        labelTelefono.setAttribute("for", "telefono");
        labelTelefono.textContent = "Telefono: " + telefono;
      
        document.body.appendChild(labelEmail);
        document.body.appendChild(saltos);
        document.body.appendChild(labelNombre);
        document.body.appendChild(saltos);
        document.body.appendChild(labelTelefono);
    }
}