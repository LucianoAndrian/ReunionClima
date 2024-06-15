#!/bin/bash

# Directorio de este script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# archivo .yml 
ENV_FILE="$SCRIPT_DIR/py_clima_env.yml"

# por las dudas, si existe el archivo *.yml
if [ ! -f "$ENV_FILE" ]; then
    echo "El archivo $ENV_FILE no existe en el directorio del script."
    exit 1
fi

# que conda hay?
ANACONDA_DIR="$HOME/anaconda3"
MINICONDA_DIR="$HOME/miniconda3"

CONDA_FOUND=false

# anaconda o miniconda
if [ -d "$ANACONDA_DIR" ]; then
    echo "Anaconda3 encontrado. Creando el entorno desde $ENV_FILE..."
    source "$ANACONDA_DIR/etc/profile.d/conda.sh"
    CONDA_FOUND=true
elif [ -d "$MINICONDA_DIR" ]; then
    echo "Miniconda3 encontrado. Creando el entorno desde $ENV_FILE..."
    source "$MINICONDA_DIR/etc/profile.d/conda.sh"
    CONDA_FOUND=true
else
    echo "Ni Anaconda3 ni Miniconda3 encontrados. No se puede crear el entorno."
    exit 1
fi

# Se crea el env a partir del archivo .yml
if [ "$CONDA_FOUND" = true ]; then
    echo "Ejecutando conda env create..."
    conda env create -f "$ENV_FILE"

    # Verificar si el entorno se creó correctamente
    if [ $? -eq 0 ]; then
        echo "El entorno ha sido creado exitosamente."
    else
        echo "Hubo un error al crear el entorno."
        exit 1
    fi
fi
