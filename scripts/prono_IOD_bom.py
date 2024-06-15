"""
el código inicialmente testeaba si el prono estaba disponible los sabados previos
actualmente el BoM los actualiza un miercoles y antes era un martes...
Para evitar problemas, toma el dia actual y va para atras hasta encontrar el prono. 
Prueba hasta 30 dias para atras. En cuanto puede descargar el archivo ya corta.
"""

import argparse

def output():
    
    import os
    from datetime import datetime
    
    cumes = datetime.now().month
    cuanio = datetime.now().year
    today = datetime.now().day
    
    def check0_and_str(x):
        if x < 10:
            x = '0' + str(x)
        else:
            x = str(x)
        return x
    
    anio = check0_and_str(cuanio)
    cumes = check0_and_str(cumes)
    
    pronoiod_ok = True
    pronoiod_ok2 = True
    
    dia_aux = today
    try_day = 0
    while(pronoiod_ok):
        dia_lastest = check0_and_str(dia_aux)
        os.system('wget --no-cache -U "Mozilla" -O PronoIOD.png http://www.bom.gov.au/climate/ocean/outlooks/archive/' + anio + cumes + dia_lastest + '//plumes/sstOutlooks.iod.hr.png')
        aux_file = os.stat('PronoIOD.png')
        if (aux_file.st_size > 0) | (try_day == 30):
            pronoiod_ok=False
        else:
            try_day +=1
            dia_aux -= 1
    
    dia_aux = today
    try_day = 0
    while(pronoiod_ok2):
        dia_lastest = check0_and_str(dia_aux)
        os.system('wget --no-cache -U "Mozilla" -O PronoIOD_NextMon.png http://www.bom.gov.au/climate/model-summary/archive/' + anio + cumes + dia_lastest + '.iod_summary_2.png')
        aux_file = os.stat('PronoIOD_NextMon.png')
        if (aux_file.st_size > 0) | (try_day == 30):
            pronoiod_ok2=False
        else:
            try_day +=1
            dia_aux -= 1

def main():
    output()

if __name__ == '__main__':
    main()

