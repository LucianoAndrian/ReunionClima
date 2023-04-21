import argparse

def output(x):
    dia = int(x)
    import os
    from datetime import datetime

    cumes = datetime.now().month
    cuanio = datetime.now().year

    def check0_and_str(x):
        if x < 10:
            x = '0' + str(x)
        else:
            x = str(x)
        return x

    anio = check0_and_str(cuanio)
    cumes = check0_and_str(cumes)
    pronoiod_ok = True
    pronoiod_nmonth_ok = True
    
    dia_aux = dia
    try_day = 0
    while(pronoiod_ok):
        dia_latest = check0_and_str(dia_aux)
        os.system('wget --no-cache -U "Mozilla" -O PronoIOD.png http://www.bom.gov.au/climate/ocean/outlooks/archive/' + anio + cumes + dia_latest + '//plumes/sstOutlooks.iod.hr.png')
        aux_file = os.stat('PronoIOD.png')
        if (aux_file.st_size > 0) | (try_day == 3):
            pronoiod_ok=False
        else:
            try_day +=1
            dia_aux -= 7

    try_day = 0

    dia = int(x) - 4 #este sigue siendo martes
    print(dia)
    while(pronoiod_nmonth_ok):
        dia_latest = check0_and_str(dia)
        os.system('wget --no-cache -U "Mozilla" -O PronoIOD_NextMon.png http://www.bom.gov.au/climate/model-summary/archive/' + anio + cumes + dia_latest + '.iod_summary_2.png')
        aux_file = os.stat('PronoIOD_NextMon.png')
        if (aux_file.st_size > 0) | (try_day == 3):
            pronoiod_nmonth_ok=False
        else:
            try_day +=1
            dia -= 7


def main():
    parser = argparse.ArgumentParser(description='ghostbird')
    parser.add_argument('--x', dest='x', metavar='x', type=str, nargs=1)

    args = parser.parse_args()
    output(args.x[0])

if __name__ == '__main__':
    main()

