import qrcode
from PIL import Image
import json


# Create your views here.

contenido = '''{
    "Clase": [
        {
            "Clase": "Programacion Java Escritorio",
            "Profe": "Freddy Campos",
            "Seccion": "013D",
            "Hora": "8:30"
        }
    ]
}'''

# Crear el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(contenido)
qr.make(fit=True)

# Crear una imagen del código QR
imagen = qr.make_image(fill_color="black", back_color="white")

# Guardar el código QR en un archivo
imagen.save("Java.png")