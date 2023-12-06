var profesores = [
    {
        "rut": "12.123.456-9",
        "nombre": "Freddy Campos",
        "titulo": "Ingeniería En Informática",
        "correo": "fre.campos@duocuc.cl",
        "contraseña": "JuanitoSimio"
    }
];

var profesoresAlmacenados = localStorage.getItem('profesores');
var profesoresRecuperados = JSON.parse(profesoresAlmacenados);
var primerProfesor = profesoresRecuperados[0];
var correoRecuperado = primerProfesor.correo;
var contraseñaRecuperada = primerProfesor.contraseña;

console.log('Correo recuperado:', correoRecuperado);
console.log('Contraseña recuperada:', contraseñaRecuperada);


iniciarSesion("fre.campos@duocuc.cl", "JuanitoSimio");
