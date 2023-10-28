const contenedorQR = document.getElementById("contenedorQR");

new QRCode(contenedorQR, 'asistencia')

var qr = new QRCode(qrContainer, {
    text: datosQR,
    width: 128,
    height: 128,
    });