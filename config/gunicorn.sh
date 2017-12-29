#!/bin/bash
#******************************************#
# Configuración gunicorn_start             #
# esto debe estar en:                      #
#  /carpeta_base/carpeta_virtualenv/bin/   #
#******************************************#

NAME="geolocaliza"                                  # Nombre del proyecto
ENVDIR=/home/davis18/geolocalizacion/env                  # Ruta del entorno virual
DJANGODIR=/home/davis18/geolocalizacion/geolocaliza                  # Ruta del proyecto
SOCKFILE=/home/davis18/run/gunicorn.sock  # ruta del unix socket esto para conexión con nginx si no existe crea la carpeta autoamtico
USER=root                                        # usuario que ejecuta
GROUP=root                                       # grupo que ejecuta
NUM_WORKERS=3                                    # el número de procesos de trabajo de Gunicorn
DJANGO_SETTINGS_MODULE=geolocaliza.settings         # Archivo de configuración de django
DJANGO_WSGI_MODULE=geolocaliza.wsgi                 # nombre del modulo WSGI

echo "Iniciando proyecto $NAME como `whoami`"

# Entorno virtual/trabajo
cd $DJANGODIR
source $ENVDIR"/bin/activate"
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Crea el directorio/archivo del unix socket si no existe
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Inicia django + gunicon

exec $ENVDIR"/bin/gunicorn" ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
