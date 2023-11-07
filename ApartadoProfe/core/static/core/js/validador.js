function login(){
    let user = document.getElementById('username').value;
    let pass = document.getElementById('password').value;

    if(user=="fre.campos@duocuc.cl" && pass=="JuanitoSimio"){
        window.location = 'home'; 
    }else{
        alert("Usuario Incorrecto");
    }
}