#!/bin/bash

echo "========================================"
echo "Se pedirá contraseña para mover archivos"
echo "========================================"


# Conda está instalado?
if ! command -v conda &> /dev/null; then
    echo "conda no está instalado."
    exit 1
fi

# Verificar si tar está instalado
if ! command -v tar &> /dev/null; then
    echo "tar no está instalado. Es necesario para descomprimir, instalar con:"
    echo "sudo apt-get install tar"
    exit 1
fi


# que conda hay?
ANACONDA_DIR="$HOME/anaconda3"
MINICONDA_DIR="$HOME/miniconda3"
# anaconda o miniconda
if [ -d "$ANACONDA_DIR" ]; then
    source "$ANACONDA_DIR/etc/profile.d/conda.sh"
    CONDA_FOUND=true
elif [ -d "$MINICONDA_DIR" ]; then
    source "$MINICONDA_DIR/etc/profile.d/conda.sh"
    CONDA_FOUND=true
else
    echo "Ni Anaconda3 ni Miniconda3 encontrados. No se puede crear el entorno."
    exit 1
fi


# Activar el entorno conda
echo "Activando el entorno conda 'py_clima'..."
conda activate py_clima
if [ $? -ne 0 ]; then
    echo "Error: Env. py_clima no encontrado."
    echo "Ejecutar primero create_conda_env.sh"
    exit 1
fi

# ---------------------------------------------------------------#
# Instalacion de selenium con pip
# Instalar selenium con pip
echo "Instalando selenium con pip..."
pip install selenium
if [ $? -ne 0 ]; then
    echo "Hubo un problema al instalar selenium."
    exit 1
fi

# eckodriver
FILE="geckodriver-v0.34.0-linux64.tar.gz"

if [ -f "$FILE" ]; then
    echo "geckodriver-v0.34.0-linux64.tar.gz encontrado"
else
    # Descargar geckodriver
    echo "Descargando geckodriver."
    echo "Es necesario para ejecutar selenium con la versión"
    echo "de firefox instalada por defecto en Linux. La versión snap"
    wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/$FILE
    if [ $? -ne 0 ]; then
        echo "Error en la descarga de geckodriver."
        echo "Revisar existencia de:"
        echo "https://github.com/mozilla/geckodriver/releases/download/v0.34.0/$FILE"
        exit 1
    fi
fi
# Extraer geckodriver
echo "Extrayendo geckodriver..."
tar -xvzf geckodriver-v0.34.0-linux64.tar.gz 
if [ $? -ne 0 ]; then
    echo "Error al extraer geckodriver."
    exit 1
fi

# Mover geckodriver a /usr/local/bin
echo "Moviendo geckodriver a /usr/local/bin..."
sudo mv geckodriver /usr/local/bin
if [ $? -ne 0 ]; then
    echo "Hubo un problema al mover geckodriver a /usr/local/bin."
    exit 1
fi

echo "Done"
