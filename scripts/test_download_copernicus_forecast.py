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

# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #

http = urllib3.PoolManager()

def download(mes, anio, nxtanio):
    nxtmes = str(int(mes) + 1)

    # temperatura ------------------------------------------------------------ #
    data_html = http.request('GET',
                         'https://charts.ecmwf.int/opencharts-api/v1/'
                         'products/c3s_seasonal_spatial_mm_2mtm_3m/'
                         '?valid_time=' + nxtanio + '-'+ nxtmes +
                             '-01T00%3A00%3A00Z&base_time=' + anio + '-' + mes +
                             '-01T00%3A00%3A00Z&area=area13')

    data_dict = json.loads(data_html.data)
    enlace = data_dict['data']['link']['href']

    print('Descargando Prono_Temp_copernicus.png')
    os.system('wget --no-cache -O Prono_Temp_copernicus.png ' + enlace)


    # precipitacion ---------------------------------------------------------- #
    data_html = http.request('GET',
                         'https://charts.ecmwf.int/opencharts-api/v1/'
                         'products/c3s_seasonal_spatial_mm_rain_3m/'
                         '?valid_time=' + nxtanio + '-'+ nxtmes +
                             '-01T00%3A00%3A00Z&base_time=' + anio + '-' + mes +
                             '-01T00%3A00%3A00Z&area=area13')

    data_dict = json.loads(data_html.data)
    enlace = data_dict['data']['link']['href']

    print('Descargando Prono_Precip_copernicus.png')
    os.system('wget --no-cache -O Prono_Precip_copernicus.png ' + enlace)

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

    args = parser.parse_args()

    download(args.mes[0], args.anio[0], args.nxtanio[0])

if __name__ == '__main__':
    main()