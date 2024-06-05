# ===== Docstring ============================= #
"""
Este programa ejecuta tareas de forma asíncrona, permitiendo que cada tarea

se ejecute independientemente de si las anteriores han terminado o no 

garantizando el funcionamiento continuo ante acciones inesperadas.

MIT License 

Copyright (c) 2024 Urreta0

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# ===== Importaciones ========================= #

try:
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    from email import encoders

    from datetime import datetime
    import aiosmtplib
    import aiofiles
    import asyncio

    import logging
except ModuleNotFoundError as e:
    print(e)
except ImportError as e:
    print(e)
except ImportWarning as e:
    print(e)

# ===== Variables globales ==================== #

RUTA_MUTABLE = "./data/cron_userbackup_01.04.24.00.00cnx_2181.txt"
RUTA_INMUTABLE = "./data/userbackup.txt"
RUTA_REGISTRO = "./logs/registro.log"

REMITENTE = ""
CONTRASEÑA = ""
DESTINATARIO = ""

INTERVALO_LEER = 60*0.015
INTERVALO_ESCRIBIR = 60*0.1
INTERVALO_ENVIAR = 60*5

logging.basicConfig(
    filename = "./logs/stderr.log",
    level = logging.ERROR,
    format = "%(ascstime)s - %(levelname)s - %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S"
)

# ===== Clase Notificacion ==================== #

class Notificacion:
    """
    ### Notificacion
    Clase que permite gestionar y enviar notificaciones por correo electrónico

    sobre el estado de conexión de clientes, basado en la comparación de dos ficheros.

    :Methods:
        - :func comparar: -- Compara el contenido de dos ficheros de texto
        - :func enviar: -- Envia a un destinatario un correo electrónico
    """

    def __init__(self) -> None:
        """
        Inicializa una instancia de `Notificacion` con una lista vacía de desconexiones.
        """
        self.estado = []

# ===== Método comparar, de la clase Notificacion ===== #

    async def comparar(
        self,
        mutable :str,
        inmutable :str
    ) -> list[str]:
        """
        Compara el contenido de dos ficheros y actualiza el estado de la lista de desconexiones.
        - :param mutable: Ruta al fichero de texto mutable
        - :param inmutable: Ruta al fichero de texto inmutable
        - :return: Lista de desconexiones actualizada
        """
        async with aiofiles.open(mutable, "r") as f:
            fichero = await f.read()
        async with aiofiles.open(inmutable, "r") as f:
            userbackup = await f.read()

        fichero_lineas = fichero.splitlines()
        userbackup_lineas = userbackup.splitlines()

        for lineas in userbackup_lineas:
            cliente = lineas.replace("~", " ").strip()
            if lineas in fichero_lineas and lineas in self.estado:
                self.estado.append( f"Cliente '{cliente}' reconectado" )
            elif lineas in fichero_lineas and lineas not in self.estado:
                pass
            elif lineas not in fichero_lineas and lineas in self.estado:
                pass
            elif lineas not in fichero_lineas and lineas not in self.estado:
                self.estado.append( f"Cliente '{cliente}' desconectado" )
            else:
                pass
        return self.estado

# ===== Método enviar, de la clase Notificacion ===== #

    async def enviar(
        self,
        remitente :str,
        contraseña :str,
        destinatario: str | None = None,
        asunto :str | None = None,
        descripcion :str | None = None,
        fichero :str | None = None,
        server :str = "smtp.gmail.com",
        port :int = 587
    ) -> None:
        """
        Envía un correo electrónico con posibles adjuntos.
        - :param remitente: Dirección de correo del remitente
        - :param contraseña: Contraseña del correo del remitente
        - :param destinatario: Dirección de correo del destinatario
        - :param asunto: Asunto del correo electrónico
        - :param descripcion: Descripcion del correo electrónico
        - :param fichero: Ruta al fichero que se desea adjuntar
        - :param servidor: Servidor SMTP para enviar el correo (por defecto es Gmail)
        - :param puerto: Puerto del servidor SMTP (por defecto es 587)
        """
        if remitente is None or contraseña is None:
            return
        message = MIMEMultipart()
        message["From"] = remitente
        message["To"] = destinatario if destinatario else remitente
        message["Subject"] = asunto if asunto else "Sin asunto"

        if descripcion:
            message.attach(MIMEText(descripcion, "plain"))
        if fichero:
            async with aiofiles.open(fichero, "rb") as attachment:
                file = MIMEBase("application", "octect-stream")
                file.set_payload(await attachment.read())
                encoders.encode_base64(file)
                filename = datetime.now()
                file.add_header(
                    "Content-Disposition",
                    f"attachment; filename= LogAnalyzer {filename}LOG.log"
                )
                message.attach(file)
        await aiosmtplib.send(
            message = message,
            hostname = server,
            port = port,
            start_tls = True,
            username = remitente,
            password = contraseña
        )

# ===== Función =============================== #

def timestamp() -> str:
    """
    Devuelve la marca de tiempo actual en formato de cadena.
    """
    return datetime.now()#.strftime("%Y-%m-%d %H:%M:%S")

# ===== Función asíncrona ===================== #

async def leer( app: Notificacion ) -> None:
    """
    Bucle que lee y compara ficheros de texto periódicamente.
    - :param app: Instancia de la clase Notificacion
    """
    while True:
        await app.comparar(RUTA_MUTABLE, RUTA_INMUTABLE)
        print( f"{timestamp()} - INFO - leer terminado" )
        await asyncio.sleep(INTERVALO_LEER)

# ===== Función asíncrona ===================== #

async def escribir( app: Notificacion ) -> None:
    """
    Bucle que escribe en un fichero texto el contenido de la lista app.desconexion
    - Lee el fichero de registro, divide el texto, siendo una lista de texto,

        esto lo hace para cada línea del registro, añadiendo los elementos a una lista.

    - También añade en la misma linea los elementos de la lista app.desconexion,

        con fin de eliminar repeticiones, posteriormente escribe los datos.
    """
    #   Corregir función, problema: sobreescribe la hora de registro.
    #   Lee el REGISTRO

    #   Crea una lista vacia (elimina duplicados)
    #   Por linea del REGISTRO
    #       Divide la linea por "INFO" y coge la 2º mitad
    #       Añade la 2º mitad a la lista
    #   Por elemento en la lista 'app.estado'
    #       Añade el elemento en la lista

    #   Escribe en el fichero por cada dato en la lista que creamos vacia
    #       Si contiene INFO (también contiene la hora): escribe
    #       Si no: Añade '(timestamp) - INFO - evento'
    
    while True:
        async with aiofiles.open(RUTA_REGISTRO, "r") as f:
            registro = await f.read()
        datos :set[str] = set()
        for lineas in registro.splitlines():
            info = lineas.split(" - INFO - ")[1].strip()
            datos.add(info)
        for elemento in app.estado:
            datos.add(elemento)
        async with aiofiles.open(RUTA_REGISTRO, "w") as f:
            for data in sorted(datos):
                if not data.__contains__(" - INFO - "):
                    await f.write( f"{timestamp()} - INFO - {data}\n" )
                else:
                    f.write( f"{data}\n" )
        print( f"{timestamp()} - INFO - escribir terminado" )
        await asyncio.sleep(INTERVALO_ESCRIBIR)


# ===== Función asíncrona ===================== #

async def enviar( app: Notificacion ) -> None:
    """
    Bucle para enviar un correo electrónico con el estado de la lista de desconexiones.
    - :param app: Instancia de la clase Notificacion
    """
    while True:
        await app.enviar(
            remitente = REMITENTE,
            contraseña = CONTRASEÑA,
            destinatario = DESTINATARIO,
            asunto = str(
                f"Monitoreo del estado de conexión de los clientes - LogAnalyzer | {timestamp()}"
            ),
            descripcion = str(
                f""
            ),
            fichero = RUTA_REGISTRO
        )
        print( f"{timestamp()} - INFO - enviar terminado" )
        await asyncio.sleep(INTERVALO_ENVIAR)

# ===== Función principal ===================== #

async def main( ) -> None:
    """
    Funcion principal del módulo. Completa tareas de forma asíncrona

    Monitorea 2 ficheros de texto, y filtra y escribe los datos en un registro.
    """
    try:
        app = Notificacion()
        await asyncio.gather(leer(app), escribir(app))
    except Exception as e:
        logging.error(f"Error Asíncrono\n{e}\n")

# ===== Ejecución ============================= #

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        exit(0)