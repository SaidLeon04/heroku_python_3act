function editar_data(email){
    var urlParams = new URLSearchParams(window.location.search);
    var email = urlParams.get('email');
    console.log("email: " + email);
    // const URL = "http://localhost:8000/contactos";
    const URL = "https://heroku-python-3act-62ad9044fdb9.herokuapp.com/contactos"
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
        
        var inputEmail = document.createElement("input");
        var inputNombre = document.createElement("input");
        var inputTelefono = document.createElement("input");
        var saltos = document.createElement("br");

        inputEmail.setAttribute("type", "email");
        inputEmail.setAttribute("id", "email");
        inputEmail.setAttribute("readonly", true)
|       inputEmail.setAttribute("value", email)

        inputNombre.setAttribute("type", "text");
        inputNombre.setAttribute("id", "nombre");
        inputNombre.setAttribute("value", nombre)

        inputTelefono.setAttribute("type", "number");
        inputTelefono.setAttribute("id", "telefono");
        inputTelefono.setAttribute("value", telefono)
      
        document.body.appendChild(inputEmail);
        document.body.appendChild(inputNombre);
        document.body.appendChild(inputTelefono);
    }
}