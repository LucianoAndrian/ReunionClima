import matplotlib.pyplot as plt
from datetime import datetime

# Functions ############################################################################################################
def MonthsName(cumonth, month, year):
    months_name = ['Enero', 'Febrero', 'Marzo', ' Abril', ' Mayo', 'Junio',
                   'Julio', 'Agosto', ' Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    if (cumonth - month) < 0:
        year -= 1

    mname = months_name[month-1]

    titlemonth = mname + '\n' + str(year)

    return titlemonth


def SeasonName(month_2, cuyear):
    seasons_name = ['DEF', 'EFM', 'FMA', 'MAM', 'AMJ', 'MJJ', 'JJA',
                    'JAS', ' ASO', 'SON', 'OND', 'NDE']

    if (month_2 == 12) or (month_2 == 1):
        year_title = str(cuyear-1) + '/' + str(cuyear)
    else:
        year_title = str(cuyear)

    if month_2 > 12:
        return seasons_name[month_2 - 13] + ' - ' + year_title
    else:
        return seasons_name[month_2-1] + ' - ' + year_title

########################################################################################################################

cuyear = datetime.now().year
year_1 = cuyear

cumonth = datetime.now().month
month_1 = cumonth - 1
month_2 = cumonth - 2
month_3 = cumonth - 3

if cumonth == 1:
    month_1 = 12
    month_2 = 11
    month_3 = 10
elif cumonth == 2:
    month_2 = 12
    month_3 = 11
elif cumonth == 3:
    month_3 = 12

try:
    import colorama
    from colorama import Fore, Style, Back
    colorama.init()
    RED = "\x1b[1;31m"
    day = input(f'{RED} Dia de la reunion: ' + Style.RESET_ALL)
except:
    day = input('Dia de la reunion: ')

if cumonth < 10:
    titledate = day + '/' + '0' + str(cumonth) + '/' + str(cuyear)
else:
    titledate = day + '/' + str(cumonth) + '/' + str(cuyear)

month_1_name = MonthsName(cumonth, month_1, cuyear)
month_2_name = MonthsName(cumonth, month_2, cuyear)
month_3_name = MonthsName(cumonth, month_3, cuyear)

season_year_name = SeasonName(month_2, cuyear)
forecast_season_name = SeasonName(cumonth+2, cuyear).split()[0]

fig = plt.figure(figsize=(1.5,0.4), dpi=200)
plt.text(.0,.5, titledate, fontsize=15, color='Red', fontweight ='bold')
plt.axis('off')
plt.savefig('titledate.png')
plt.close()

fig = plt.figure(figsize=(1.5,0.8), dpi=200)
plt.text(0,.3, month_1_name, fontsize=15, color='Red')
plt.axis('off')
plt.savefig('month-1_name.png')
plt.close()

fig = plt.figure(figsize=(1.5,0.8), dpi=200)
plt.text(0,.3, month_2_name, fontsize=15, color='Red')
plt.axis('off')
plt.savefig('month-2_name.png')
plt.close()

fig = plt.figure(figsize=(1.5,0.8), dpi=200)
plt.text(0,.3, month_3_name, fontsize=15, color='Red')
plt.axis('off')
plt.savefig('month-3_name.png')
plt.close()


fig = plt.figure(figsize=(1.7,0.7), dpi=200)
plt.text(.0,.4, season_year_name, fontsize=15, color='Red')
plt.axis('off')
plt.savefig('season_year_name.png')
plt.close()


fig = plt.figure(figsize=(.8,.4), dpi=200)
plt.text(0,.3, forecast_season_name, fontsize=20, fontweight ='bold')
plt.axis('off')
plt.savefig('forecast_season_name.png')
plt.close()
