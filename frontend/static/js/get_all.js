function getAll(){
    //const URL = "http://localhost:8000/contactos";
    const URL = "https://heroku-python-3act-62ad9044fdb9.herokuapp.com/contactos"
    var request = new XMLHttpRequest;
    request.open('GET',URL);
    request.send();

    request.onload = (e) => {
        const response = request.responseText;
        const json = JSON.parse(response);
        console.log("response: " + response);
        console.log("json: " + json);
        console.log("status_code: " + request.status);

        console.log("Email: " + json[0]["email"]);
        console.log("Nombre: " + json[0]["nombre"]);
        console.log("Telefono: " + json[0]["telefono"]);

        const tbody_contactos = document.getElementById("tbody_contactos");
        for (var i = 0; i < Object.keys(json).length; i++) {
            var tr = document.createElement("tr");
            var td_email = document.createElement("td");
            var td_nombre = document.createElement("td");
            var td_telefono = document.createElement("td");
            var td_ver = document.createElement("td");
            var td_editar = document.createElement("td");
            var td_borrar = document.createElement("td");

            td_email.innerHTML = json[i]["email"];
            var emailCodificado = encodeURIComponent(json[i]["email"]);
            td_nombre.innerHTML = json[i]["nombre"];
            td_telefono.innerHTML = json[i]["telefono"];
            td_ver.innerHTML = '<a href="../templates/ver.html?email=' + emailCodificado + '">Ver</a>';
            td_editar.innerHTML = '<a href="../templates/editar.html?email='+ emailCodificado +'">Editar</a>';
            td_borrar.innerHTML = '<a href="../templates/borrar.html?email='+ emailCodificado +'">Borrar</a>';

            // console.log("Email: " + json[i]["email"]);

            tr.appendChild(td_email);
            tr.appendChild(td_nombre);
            tr.appendChild(td_telefono);
            tr.appendChild(td_ver);
            tr.appendChild(td_editar);
            tr.appendChild(td_borrar);
            tbody_contactos.appendChild(tr);
        }
    };
};
