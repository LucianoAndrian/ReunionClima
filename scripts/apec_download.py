
"""
Descarga de productos de APEC
"""
# ---------------------------------------------------------------------------- #
from datetime import datetime
import os
# ---------------------------------------------------------------------------- #
def Download(season, anio):
    link_flechita = (f"https://www.apcc21.org/apcc_images/MME_FIG/ENSO_OUT/"
                     f"{season}/{anio}/Alert/ENSO_Alert.png")
    os.system('wget --no-cache -O enso_flechita_apec.png ' + link_flechita)

    link_prono_enso = (f'https://www.apcc21.org/apcc_images/MME_FIG/ENSO_OUT/'
                  f'{season}/{anio}/Probability/Prob_ENSO_Probability.png')
    os.system('wget --no-cache -O PronoENSO_APEC.png ' + link_prono_enso)

    link_prono_iod = (f"https://www.apcc21.org/apcc_images/MME_FIG/ENSO_OUT/"
                      f"{season}/{anio}/Timeseries/sst_IOD.png")
    os.system('wget --no-cache -O PronoIOD_APEC.png ' + link_prono_iod)

# ---------------------------------------------------------------------------- #
meses = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D',
         'J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
# lo de arriba es para no tener problemas con el cambio de año

cumes = datetime.now().month
anio = datetime.now().year

season = ''.join(meses[cumes-1:cumes-1+6])
Download(season, anio)


# ---------------------------------------------------------------------------- #
print('# ------------------------------------------------------------------- #')
print('apec_download.py DONE')
print('# ------------------------------------------------------------------- #')
# ---------------------------------------------------------------------------- #
