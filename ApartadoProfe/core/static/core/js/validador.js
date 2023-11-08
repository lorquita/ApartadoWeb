function iniciarclases(claseId) {
    if (claseId === 'clase1') {
        window.location.href = "clase1.html";
    } else if (claseId === 'clase2') {
        window.location.href = "clase2";
    } else {
        console.error('ID de clase no reconocido');
    }
}
function login(){
    let user = document.getElementById('username').value;
    let pass = document.getElementById('password').value;

    if(user=="fre.campos@duocuc.cl" && pass=="JuanitoSimio"){
        window.location = 'home'; 
    }else{
        alert("Usuario Incorrecto");
    }
}