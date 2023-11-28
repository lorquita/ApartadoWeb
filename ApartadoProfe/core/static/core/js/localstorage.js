var profesores = [
    {
        "rut": "12.123.456-9",
        "nombre": "Freddy Campos",
        "titulo": "Ingeniería En Informática"
    }
];

localStorage.setItem('profesores', JSON.stringify(profesores));

console.log('Datos de profesores almacenados en localStorage.');

var profesoresAlmacenados = localStorage.getItem('profesores');

var profesoresRecuperados = JSON.parse(profesoresAlmacenados);

console.log('Datos de profesores recuperados de localStorage:', profesoresRecuperados);
