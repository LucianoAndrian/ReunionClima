#!/bin/sh

rm ./*.gif
rm ./*.jpg
rm ./*.pdf
rm ./*.png

# Ruta a los scrips para correr en python
# Hay que correr esto desde la carpeta raiz del repositorio, 
enlace=./scripts/

source ~/anaconda3/etc/profile.d/conda.sh
conda activate py37

#################### PROBANDO #####################
mes_nmme=$(python $enlace"pronos_update.py" --x "nmme_month_ic")
mes1_nmme=$(python $enlace"pronos_update.py" --x "nmme_month_1")
mes3_nmme=$(python $enlace"pronos_update.py" --x "nmme_month_3")
mes_iri=$(python $enlace"pronos_update.py" --x "iri_month_ic")
season_iri_divar=$(python $enlace"pronos_update.py" --x "season")
mes_divar=$(python $enlace"pronos_update.py" --x "divar_month_ic")
anio=$(date -d "$date" +"%Y")
anio_abrev=`expr $anio - 2000`
###################################################
#Imagen Prono Precip NMME (¡¡¡Cambiar!!!)---> probando=FIJA
#wget -O Prono_Precip_NMME.png http://www.cpc.ncep.noaa.gov/products/international/nmme/probabilistic_seasonal/samerica_nmme_prec_3catprb_${mes_nmme}IC_${mes1_nmme}${anio}-${mes3_nmme}${anio}.png

#Imagen Prono Temp NMME (¡¡¡Cambiar!!!)---> probando=FIJA
#wget -O Prono_Temp_NMME.png http://www.cpc.ncep.noaa.gov/products/international/nmme/probabilistic_seasonal/samerica_nmme_tmp2m_3catprb_${mes_nmme}IC_${mes1_nmme}${anio}-${mes3_nmme}${anio}.png


#Imagen Prono Precip IRI (¡¡¡Cambiar!!!)---> probando=FIJA
#wget -O Prono_Precip_IRI.gif https://iri.columbia.edu/climate/forecast/net_asmt_nmme/$anio/${mes_iri}${anio}/images/${season_iri_divar}${anio_abrev}_SAm_pcp.gif

echo "https://iri.columbia.edu/climate/forecast/net_asmt_nmme/$anio/${mes_iri}${anio}/images/${season_iri_divar}${anio_abrev}_SAm_pcp.gif"
 
echo "hola/ASO"
#Imagen Prono Temp IRI (¡¡¡Cambiar!!!)---> probando=FIJA
#wget -O Prono_Temp_IRI.gif https://iri.columbia.edu/climate/forecast/net_asmt_nmme/$anio/${mes_iri}${anio}/images/${season_iri_divar}${anio_abrev}_SAm_tmp.gif


#Imagen Prono DIVAR (¡¡¡Cambiar!!!)---> probando=FIJA
#wget -O Prono_Precip_DIVAR.png http://climar.cima.fcen.uba.ar/grafEstacional/for_prec_${season_iri_divar}_ic_${mes_divar}_${anio}_wsereg_mean_cor.png
 
#Imagen Prono DIVAR (¡¡¡Cambiar!!!)---> probando=FIJA
#wget -O Prono_Temp_DIVAR.png http://climar.cima.fcen.uba.ar/grafEstacional/for_tref_${season_iri_divar}_ic_${mes_divar}_${anio}_wsereg_mean_cor.png


