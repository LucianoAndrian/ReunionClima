import argparse

def Output(x):
    from datetime import datetime
    seasons_name = [0 ,'DEF', 'EFM', 'FMA', 'MAM', 'AMJ', 'MJJ', 'JJA' ,'JAS', 'ASO', 'SON', 'OND', 'NDE']
    seasons_name_en = [0 ,'DJF', 'JFM', 'FMA', 'MAM', 'AMJ', 'MJJ', 'JJA' ,'JAS', 'ASO', 'SON', 'OND', 'NDJ']
    Months = [0 ,'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    months2 = [0 ,'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    year_abrev = ['22','23','24','25','26','etc'] #es la unica forma en la q anda

    cumes = datetime.now().month
    if cumes != 12:
        mes1 = cumes +1
    else:
        mes1 = 1

    if cumes < 10:
        mes3 = cumes + 3
    else:
        mes3 = cumes + 3 -12


    anio_i = datetime.now().year
    if mes3 < cumes:
        anio_f = datetime.now().year + 1
    else: 
        anio_f = anio_i


    if x== 'nmme_month_ic' or x == 'divar_month_ic':
        print(Months[cumes])
    elif x == 'nmme_month_1':
        print(Months[mes1])
    elif x == 'nmme_month_3':
        print(Months[mes3])
    elif x == 'iri_month_ic':
        print(months2[cumes])
    elif (x == 'season'):
        if mes3 == 1:
            mes3=13
        print(seasons_name[mes3-1])
    elif (x == 'anio_i'):
        print(anio_i)
    elif (x == 'anio_i_nmme'):
        print(anio_i)
    elif (x == 'anio_f'):
        print(anio_f)
    elif (x == 'season_en'):
        if mes3 == 1:
            mes3=13
        print(seasons_name_en[mes3-1])



def main():
    # Define parser data
    parser = argparse.ArgumentParser(description='ghostbird')
    parser.add_argument('--x', dest='x', metavar='x', type=str,
                        nargs=1)

    # Extract dates from args
    args = parser.parse_args()
    Output(args.x[0])


if __name__ == '__main__':
    main()







