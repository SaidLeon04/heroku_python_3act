function insert(email, nombre, telefono){
    const URL = "https://heroku-python-3act-62ad9044fdb9.herokuapp.com/contactos"
    //const URL = "http://localhost:8000/contactos";
    var request = new XMLHttpRequest;
    request.open('POST',URL)
    request.setRequestHeader("Content-Type", "application/json");
    post = JSON.stringify( {
        "email": email,
        "nombre": nombre,
        "telefono": telefono})
    console.log(post)
    request.send(post)

    request.onload = (e) => {
        if(request.status == 200){
            alert("Email ya registrado")
        }else{
            const response = request.responseText;
            const json = JSON.parse(response);
            console.log("response: " + response);
            console.log("json: " + json);
            console.log("status_code: " + request.status);
            window.location.href = "../templates/index.html";
        }
    }
    
}


