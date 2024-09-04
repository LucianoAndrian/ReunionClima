#!/bin/bash

echo "========================================"
echo "Se pedirá contraseña para mover archivos"
echo "========================================"

# Mostrar advertencia y esperar confirmación
echo "ATENCION:"
echo "1. Se instalaran las librerias imagemagick-6.q16, cutycapt si no estan instaladas"
echo "2. Se modificará el archivo /etc/ImageMagick-6/policy.xml agregando la siguiente línea:"
echo '<policy domain="coder" rights="read|write" pattern="PDF" />'
echo " este cambio es necesario para convertir PDF a PNG"
read -p "Enter para continuar o Ctrl+C para cancelar..."


if command -v convert &> /dev/null; then
    echo "ImageMagick está instalado."
else
    echo "ImageMagick no está instalado."
    echo "Instalando imagemagick-6.q16"
    sudo apt install imagemagick-6.q16
fi
# Esto si ya esta no cambia nada
sudo sed -i '$i <policy domain="coder" rights="read|write" pattern="PDF" />' /etc/ImageMagick-6/policy.xml


if command -v cutycapt &> /dev/null; then
    echo "CutyCapt está instalado."
else
    echo "CutyCapt no está instalado."
    echo "Instalando CutyCapt..."
    sudo apt install cutycapt
fi


# Verificar e instalar qpdf
if command -v qpdf &> /dev/null; then
    echo "qpdf está instalado."
else
    echo "qpdf no está instalado."
    echo "Instalando qpdf..."
    sudo apt install qpdf
fi

# Verificar e instalar pdfcrop
if command -v pdfcrop &> /dev/null; then
    echo "pdfcrop está instalado."
else
    echo "pdfcrop no está instalado."
    echo "Instalando texlive-extra-utils, puede tardar..."
    sudo apt install texlive-extra-utils
fi

# Verificar e instalar ncal
if command -v ncal &> /dev/null; then
    echo "ncal está instalado."
else
    echo "ncal no está instalado."
    echo "Instalando ncal..."
    sudo apt install ncal
fi

echo "Done"