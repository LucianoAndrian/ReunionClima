# Primera vez

1. En la carpeta `set_up` correr:

   a. `create_conda_env.sh`
   
      A partir del archivo `py_clima_env.yml` va a crear un entorno de conda.
      No importa si está instalado Anaconda o Miniconda.
      
      > **Nota:** Si surge el error: `AttributeError: module 'importlib_metadata' has no attribute 'version'`, mala suerte... En mi caso se solucionó desinstalando Anaconda e instalando Miniconda, pero no conozco la causa.

      **SI NO SE QUIERE CREAR UN NUEVO ENTORNO Y USAR UNO YA EXISTENTE:** Está bien.  
      Hay que cambiar el nombre por el entorno deseado en `descarga_graficos.sh` y en `install_selenium.sh`.

   b. `install_selenium.sh`
   
      Instala Selenium con `pip` en el entorno creado, rápido y sin problemas (por ahora).

      Además, instala Selenium con Firefox para asegurar que siempre funcione en Linux.  
      El problema es que la versión por defecto en Ubuntu fue instalada vía `snap` y eso complica.

      Para eso, este script también instala `geckodriver` a partir de `geckodriver-v0.34.0-linux64.tar.gz` incluido en la carpeta `set_up`.  
      > **Nota:** Si por algún motivo no funciona, borrar el archivo y correr el código otra vez.  
      > Va a descargar el archivo desde el repositorio de GitHub [geckodriver releases](https://github.com/mozilla/geckodriver/releases/download/v0.34.0).

      Se va a pedir la contraseña para mover lo extraído de `geckodriver-v0.34.0-linux64.tar.gz` a una carpeta del sistema.

   c. `set_up_varios.sh`
   
      Si no existen, va a instalar ImageMagick y CutyCapt.

      Se va a pedir la contraseña para modificar el archivo `/etc/ImageMagick-6/policy.xml`  
      para que pueda convertir de PDF a PNG.  
      > **Nota:** Si el archivo ya fue modificado, solo agrega otra línea y no afecta.

## Una vez finalizado lo anterior

Desde `Reunion_Clima-master` ejecutar `bash scripts/descarga_graficos.sh`.

Por pantalla:

- Va a pedir el día de la reunión (número) para actualizar la fecha.
- Va a preguntar sobre usar Selenium o no. Selenium va a ser usado como método alternativo si falla la descarga a partir de los links de Copernicus (por ahora no funcionan).

## En caso de no estar disponibles algunos de los pronósticos estacionales de T o PP

Se puede ejecutar `bash scripts/AUX_descarga_pronos.sh` en otro momento.  
Es igual a `descarga_graficos.sh` pero solo con la descarga de pronósticos,  
para evitar tener que correr todo otra vez o buscarlos a mano.

Por pantalla va a preguntar qué pronóstico se quiere descargar (NMME, IRI, DIVAR, Copernicus, todos).

---

## Se debe actualizar a mano

- Figuras CRC-SAS de precipitación (voto por hacer las nuestras con CMAP o CHIRPS).
- Flechita ENSO BoM.

## Prestar atención

- Pronósticos ENSO, pluma y barras, del IRI. Hace más de un año (06/2024) que los links cambian mes a mes.
- Pronósticos BoM: Links más estables que los del IRI, pero pasaron de actualizarlos los martes, a los sábados, y ahora (06/2024) los miércoles. El código de Python que descarga esos pronósticos actualmente chequea los últimos 30 días previos a la fecha donde se corre el código. No debería haber problemas.

