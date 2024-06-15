#!/bin/sh

# Igual que descarga gráficos pero solo para los pronos estacionales de PP  y T.

# que conda hay?
ANACONDA_DIR="$HOME/anaconda3"
MINICONDA_DIR="$HOME/miniconda3"
# anaconda o miniconda
if [ -d "$ANACONDA_DIR" ]; then
    source "$ANACONDA_DIR/etc/profile.d/conda.sh"
    CONDA_FOUND=true
elif [ -d "$MINICONDA_DIR" ]; then
    source "$MINICONDA_DIR/etc/profile.d/conda.sh"
    CONDA_FOUND=true
else
    echo "Ni Anaconda3 ni Miniconda3 encontrados. No se puede crear el entorno."
    exit 1
fi

conda activate py_clima
# Hay que correr esto desde la carpeta raiz del repositorio,
enlace=./scripts/

# elegir que descargar
echo "Seleccione el pronóstico a descargar (nmme, iri, divar, copernicus, todos):"
read -r pronostico

anio=$(date -d "$date" +"%Y")
mes1=$(date -d "$date -3 month" +"%m")
anio1=$(date -d "$date -3 month" +"%Y")
mes2=$(date -d "$date -2 month" +"%m")
anio2=$(date -d "$date -2 month" +"%Y")
mes3=$(date -d "$date -1 month" +"%m")
anio3=$(date -d "$date -1 month" +"%Y")

# ultimo día del mes. Mes 3 es el anterior.
dfm1=$(cal $(date -d "$date -3 month" +"%m %Y") | awk 'NF {DAYS = $NF}; END {print DAYS}')
dfm2=$(cal $(date -d "$date -2 month" +"%m %Y") | awk 'NF {DAYS = $NF}; END {print DAYS}')
dfm3=$(cal $(date -d "$date -1 month" +"%m %Y") | awk 'NF {DAYS = $NF}; END {print DAYS}')

#current month
cumes=$(date -d "$date" +"%m")

#next month
nxtmes=$(date -d "$date +1 month" +"%m")
#next year
nxtanio=$(date -d "$date +1 month" +"%Y")

##########################################################################
mes_nmme=$(python $enlace"pronos_update.py" --x "nmme_month_ic")
mes1_nmme=$(python $enlace"pronos_update.py" --x "nmme_month_1")
mes3_nmme=$(python $enlace"pronos_update.py" --x "nmme_month_3")
mes_iri=$(python $enlace"pronos_update.py" --x "iri_month_ic")
season_iri_divar=$(python $enlace"pronos_update.py" --x "season")
season_iri_divar_en=$(python $enlace"pronos_update.py" --x "season_en")
mes_divar=$(python $enlace"pronos_update.py" --x "divar_month_ic")
anio_i=$(python $enlace"pronos_update.py" --x "anio_i")
anio_i_nmme=$(python $enlace"pronos_update.py" --x "anio_i_nmme")
anio_f=$(python $enlace"pronos_update.py" --x "anio_f")
anio_i_abrev=`expr $anio_i - 2000`
anio_f_abrev=`expr $anio_f - 2000`

# Función para descargar imágenes
descargar_imagenes() {
  #Imagen Prono Precip NMME
  wget -O Prono_Precip_NMME.png http://www.cpc.ncep.noaa.gov/products/international/nmme/probabilistic_seasonal/samerica_nmme_prec_3catprb_${mes_nmme}IC_${mes1_nmme}${anio_i_nmme}-${mes3_nmme}${anio_f}.png

  #Imagen Prono Temp NMME
  wget -O Prono_Temp_NMME.png http://www.cpc.ncep.noaa.gov/products/international/nmme/probabilistic_seasonal/samerica_nmme_tmp2m_3catprb_${mes_nmme}IC_${mes1_nmme}${anio_i_nmme}-${mes3_nmme}${anio_f}.png

  #Imagen Prono Precip IRI
  wget -O Prono_Precip_IRI.gif https://iri.columbia.edu/climate/forecast/net_asmt_nmme/$anio_i/${mes_iri}${anio_i}/images/${season_iri_divar_en}${anio_f_abrev}_SAm_pcp.gif

  #Imagen Prono Temp IRI
  wget -O Prono_Temp_IRI.gif https://iri.columbia.edu/climate/forecast/net_asmt_nmme/$anio/${mes_iri}${anio_i}/images/${season_iri_divar_en}${anio_f_abrev}_SAm_tmp.gif

  #Imagen Prono DIVAR
  wget --tries=1 -O Prono_Precip_DIVAR.png http://climar.cima.fcen.uba.ar/grafEstacional/for_prec_${season_iri_divar_en}_ic_${mes_divar}_${anio_i}_wsereg_mean_cor.png

  #Imagen Prono DIVAR
  wget --tries=1 -O Prono_Temp_DIVAR.png http://climar.cima.fcen.uba.ar/grafEstacional/for_tref_${season_iri_divar_en}_ic_${mes_divar}_${anio_i}_wsereg_mean_cor.png
	
  # TEST DESCARGA AUTOMATICA COPERNICUS

  # Preguntar por SELENIUM para Copernicus
  echo "-----------------------------------------------------------"
  echo "-----------------------------------------------------------"
  echo "En caso de no funcionar la descarga tradicional para los"
  echo "pronósticos de Copernicus, ¿Desea usar SELENIUM en python? (si/no):"
  read -r respuesta

  # Compara la respuesta
  if [ "$respuesta" = "si" ]; then
      use_selenium=true
  else
      use_selenium=false
  fi

  python $enlace"test_download_copernicus_forecast.py" --mes "$cumes" --anio "$anio" --nxtanio "$nxtanio" --use_selenium "$use_selenium"
}

# Descargar según selección
case $pronostico in
  "nmme")
    wget -O Prono_Precip_NMME.png http://www.cpc.ncep.noaa.gov/products/international/nmme/probabilistic_seasonal/samerica_nmme_prec_3catprb_${mes_nmme}IC_${mes1_nmme}${anio_i_nmme}-${mes3_nmme}${anio_f}.png
    wget -O Prono_Temp_NMME.png http://www.cpc.ncep.noaa.gov/products/international/nmme/probabilistic_seasonal/samerica_nmme_tmp2m_3catprb_${mes_nmme}IC_${mes1_nmme}${anio_i_nmme}-${mes3_nmme}${anio_f}.png
    ;;
  "iri")
    wget -O Prono_Precip_IRI.gif https://iri.columbia.edu/climate/forecast/net_asmt_nmme/$anio_i/${mes_iri}${anio_i}/images/${season_iri_divar_en}${anio_f_abrev}_SAm_pcp.gif
    wget -O Prono_Temp_IRI.gif https://iri.columbia.edu/climate/forecast/net_asmt_nmme/$anio/${mes_iri}${anio_i}/images/${season_iri_divar_en}${anio_f_abrev}_SAm_tmp.gif
    ;;
  "divar")
    wget --tries=1 -O Prono_Precip_DIVAR.png http://climar.cima.fcen.uba.ar/grafEstacional/for_prec_${season_iri_divar_en}_ic_${mes_divar}_${anio_i}_wsereg_mean_cor.png
    wget --tries=1 -O Prono_Temp_DIVAR.png http://climar.cima.fcen.uba.ar/grafEstacional/for_tref_${season_iri_divar_en}_ic_${mes_divar}_${anio_i}_wsereg_mean_cor.png
    ;;
  "copernicus")

    echo "-----------------------------------------------------------"
    echo "-----------------------------------------------------------"
    echo "En caso de no funcionar la descarga tradicional para los"
    echo "pronósticos de Copernicus, ¿Desea usar SELENIUM en python? (si/no):"
    read -r respuesta

    # Compara la respuesta
    if [ "$respuesta" = "si" ]; then
        use_selenium=true
    else
        use_selenium=false
    fi
      python $enlace"test_download_copernicus_forecast.py" --mes "$cumes" --anio "$anio" --nxtanio "$nxtanio" --use_selenium "$use_selenium"
    ;;
  "todos")
    descargar_imagenes
    ;;
  *)
    echo "Opción no válida. Saliendo..."
    exit 1
    ;;
esac
