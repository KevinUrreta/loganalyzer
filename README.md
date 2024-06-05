# LogAnalyzer - Sistema de Notificación
Notificacion LogAnalyzer es un programa en Python diseñado para ejecutar tareas de manera asíncrona. Permite que cada tarea se ejecute de forma independiente, independientemente de si las tareas anteriores han completado, asegurando un funcionamiento continuo ante acciones inesperadas. Además se añadió el mismo programa pero de ejecución sincrona.

## Características
- Ejecución Sincrona: Permite la ejecución de tareas de manera sincrona, es menos óptimo y eficiente, puede dar problemas a la hora de ejecución del programa.
- Ejecución Asíncrona: Permite la ejecución de tareas de manera independiente, optimizando el rendimiento y la eficiencia del sistema.
- Comparación de Archivos de Texto: Monitorea las conexiones de los clientes mediante la comparación de archivos de texto, manteniendo un registro actualizado de la actividad.
- Notificaciones por Correo Electrónico: Envía notificaciones por correo electrónico para informar sobre el estado de las conexiones, manteniendo a los usuarios actualizados en tiempo real.
- Registro de Eventos: Registra eventos relevantes para análisis y resolución de problemas, facilitando la identificación y corrección de posibles fallos.

## Instalación
Para utilizar el LogAnalyzer, asegúrate de tener Python 3.12 instalado en tu sistema. Luego, clona el repositorio en tu máquina local utilizando el siguiente comando:
```bash
git clone https://github.com/KevinUrreta/loganalyzer.git
```

## Uso
1. Modifica las variables globales en `_async.py` o `_sync.py` según tus requisitos.
2. Ejecuta el programa usando Python:
```bash
python ./main.py
```

## Licencia
**LogAnalyzer - Notification system, bajó licencia MIT.**

MIT License

Copyright (c) 2024 KevinUrreta

Por la presente se concede permiso, libre de cargos, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el "Software"), a utilizar el Software sin restricción, incluyendo sin limitación los derechos a usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar, y/o vender copias del Software, y a permitir a las personas a las que se les proporcione el Software a hacer lo mismo, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "COMO ESTÁ", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A GARANTÍAS DE COMERCIALIZACIÓN, IDONEIDAD PARA UN PROPÓSITO PARTICULAR E INCUMPLIMIENTO. EN NINGÚN CASO LOS AUTORES O PROPIETARIOS DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑOS U OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O CUALQUIER OTRO MOTIVO, DERIVADAS DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O SU USO U OTRO TIPO DE ACCIONES EN EL SOFTWARE.

## Contribuidores
- KevinUrreta - [github.com/KevinUrreta](https://github.com/KevinUrreta/)

## Problemas & Sugerencias
Si detectas algún problema o tienes sugerencias para mejorar, abre un "issue" en GitHub.

- Nota: En el momento en que el programa escribe sobre el archivo de registro o log, sobreescribe las fechas de los eventos. Esto puede afectar la precisión del registro y la capacidad de seguimiento.