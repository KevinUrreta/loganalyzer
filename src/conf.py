""" Configuración de variables globales """


""" RUTAS A LOS FICHEROS """
# Fichero para comprobar datos faltantes.
RUTA_MUTABLE = "./data/cron_userbackup_01.04.24.00.00cnx_2181.txt"
# Fichero para hacer la comparacion.
RUTA_INMUTABLE = "./data/userbackup.txt"
# Fichero donde escribir y enviar los datos.
RUTA_LOGS = "./logs/clientes.log"

""" DATOS DEL REMITENTE, Y ENVIO AL DESTINATARIO """
# Correo y contraseña del remitente.
REMITE_EMAIL = "kurretavizcaya168@ieszaidinvergeles.org"
CONTRASEÑA_EMAIL = "yvtu ensh ycra ismp"
# Correo del destinatario.
DESTINATARIO_EMAIL = "kurretavizcaya168@ieszaidinvergeles.org"

""" DEFINIR INTERVALOS DE TIEMPO. """
# INTERVALO: Este intervalo es el tiempo entre la ejecucion
# en un programa síncrono
INTERVALO = 60 * 5

# INTERVALOS_*: Estos intervalos son el tiempo entre ejecucion
# en un programa asíncrono.
INTERVALO_LECTURA = 60 * 0.05
INTERVALO_ESCRITURA = 60 * 0.15
INTERVALO_ENVIO = 60 * 5
