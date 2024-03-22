"""
Descarga los pronosticos trimestrales de copernicus
inicializados en el mes actual
Utiliza herramientas que todavia estan en etapA BETA en copernicus

"""
# ---------------------------------------------------------------------------- #
import argparse
from bs4 import BeautifulSoup
import re
import urllib3
import json
import os
import shutil
import time
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


def download_with_selenium(url, nombre_figura):

    try:
        from selenium import webdriver
        from selenium.common.exceptions import WebDriverException
        print('Se intentara la descarga a travez del navegador firefox')
    except:
        print('Selenium no instalada')
        print('instalar con: ')
        print('pip install selenium')
        return

    # Para funcionar con firefox instalado por defecto en linux a partir de snap
    # es necesario lo siguiente
    temp_dir = "tmp_selenium"
    try:
        shutil.rmtree(temp_dir)
    except:
        pass
    os.makedirs(temp_dir)
    os.environ["TMPDIR"] = temp_dir
    #

    try:
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)

        time.sleep(20)  # puede tardar en abrir firefox

        driver.get(url)

        time.sleep(10)  # esperando que cargue la pagina, normalmente tarda menos

        imagen = driver.find_element("xpath",
                                     "//img[contains(@src, 'charts.ecmwf')]")
        enlace = imagen.get_attribute("src")
        os.system('wget --no-cache -O ' + nombre_figura + ' ' + enlace)
        driver.quit()  # cierra firefox

        print('Descarga via selenium ok')

    except WebDriverException as e:
        if "Service /snap/bin/geckodriver unexpectedly exited." in str(e):
            print('# ------------------------------------------------------- #')
            print("geckodriver no instalado")
            print('Descargar geckodriver desde el siguiente link:')
            print("https://github.com/mozilla/geckodriver/releases/download/"
                  "v0.34.0/geckodriver-v0.34.0-linux64.tar.gz")
            print("descomprimir el archivo .tar.gz y ejecutar por terminal:")
            print("sudo mv geckodriver /usr/local/bin")
            print('# ------------------------------------------------------- #')
        else:
            print('Error: ' + str(e))
            return

def download(mes, anio, nxtanio, use_selenium):

    print('#-----------------------------------------------------------------#')
    print('Descarga pronos copernicus')
    print('#-----------------------------------------------------------------#')
    nxtmes = int(mes) + 1
    if nxtmes < 10:
        nxtmes = f"0{nxtmes}"

    # Marzo 2024: los links no parecen estar definidos todavia.
    # La version la api deberia usar url1 pero en este momento no anda
    # la version web usa url2

    valid_time1 = f"{nxtanio}-{nxtmes}"
    base_time1 = f"{anio}-{mes}"

    valid_time2 = f"{nxtanio}{nxtmes}"
    base_time2 = f"{anio}{mes}"

    http = urllib3.PoolManager()

    for variable, var_name_pic in zip(['rain', '2mtm'], ['Precip', 'Temp']):
        print('inicio iteracion')
        url1 = (f"https://charts.ecmwf.int/opencharts-api/v1/products/"
                f"c3s_seasonal_spatial_mm_{variable}_3m/?"
                f"valid_time={valid_time1}-01T00%3A00%3A00Z&"
                f"base_time={base_time1}-01T00%3A00%3A00Z&area=area13")

        url2 = (f"https://climate.copernicus.eu/charts/packages/c3s_seasonal/"
                f"products/c3s_seasonal_spatial_mm_{variable}_3m?area=area13&"
                f"base_time={base_time2}010000&type=tsum&"
                f"valid_time={valid_time2}010000/")

        nombre_figura = f"Prono_{var_name_pic}_copernicus.png"

        # -------------------------------------------------------------------- #

        data_html = http.request('GET', url1)
        try:
            data_dict = json.loads(data_html.data)
            enlace = data_dict['data']['link']['href']
            print('Descargando ' + nombre_figura_temp)
            os.system('wget --no-cache -O '+ nombre_figura_temp + enlace)
        except:

            if use_selenium:
                try:
                    from selenium import webdriver
                    import os
                    import shutil
                except:
                    print('Selenium no instalado')
                    return

                download_with_selenium(url2, nombre_figura)

            else:
                print('# ---------------------------- #')
                print(f"Error Link prono {var_name_pic} copernicus no funciona")
                print("Descargar manualmente:")
                print(url2)
                print('# ---------------------------- #')

        time.sleep(10) # por si la descarga toma tiempo

# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #

def main():
    parser = argparse.ArgumentParser(description='ghostbird')
    parser.add_argument('--mes', dest='mes',
                        metavar='mes',
                        type=str, nargs=1)
    parser.add_argument('--anio', dest='anio',
                        metavar='anio',
                        type=str, nargs=1)
    parser.add_argument('--nxtanio', dest='nxtanio',
                        metavar='nxtanio',
                        type=str, nargs=1)
    parser.add_argument('--use_selenium', dest='use_selenium',
                        metavar='nxtanio',
                        type=bool, nargs=1)

    args = parser.parse_args()

    download(args.mes[0], args.anio[0], args.nxtanio[0], args.use_selenium[0])

if __name__ == '__main__':
    main()
