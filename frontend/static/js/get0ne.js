function get_one(email) {
    const URL = "https://heroku-python-3act-62ad9044fdb9.herokuapp.com/contactos"
    // const URL = "http://localhost:8000/contactos";
    var request = new XMLHttpRequest;
    request.open('GET',URL +"/" +email,true);
    request.send();
    request.onload = () => {
        if(request.status == 404){
            alert("No se encontro el contacto");
        }else{
            const response = request.responseText;
            const json = JSON.parse(response);
            console.log("response: " + response);
            console.log("json: " + json);
            console.log("status_code: " + request.status);

            const tbody_contactos = document.getElementById("tbody_contactos");

            tbody_contactos.innerHTML = null;

            var tr = document.createElement("tr");
            var td_email = document.createElement("td");
            var td_nombre = document.createElement("td");
            var td_telefono = document.createElement("td");

            td_email.innerHTML = json["email"];
            td_nombre.innerHTML = json["nombre"];
            td_telefono.innerHTML = json["telefono"];

            tr.appendChild(td_email);
            tr.appendChild(td_nombre);
            tr.appendChild(td_telefono);

            tbody_contactos.appendChild(tr);
        }
    }
};
