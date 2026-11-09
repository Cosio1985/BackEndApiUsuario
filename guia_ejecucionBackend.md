# Guía del Alumno: Puesta en Marcha del Backend con Docker y Postman

Esta guía detalla los pasos exactos que debes seguir, desde la obtención del proyecto backend desde el repositorio de GitHub hasta la verificación completa de su funcionamiento mediante pruebas de API en Postman.

## Paso 1: Obtención del Proyecto desde GitHub

Para descargar el código fuente del servidor backend en tu computadora, puedes elegir cualquiera de los dos métodos siguientes:

### Opción A: Clonar el repositorio mediante Git (Recomendado)

1. Abre tu terminal (CMD, PowerShell, Git Bash o la terminal de tu preferencia).

2. Navega hasta la carpeta en tu disco duro donde almacenas tus proyectos de desarrollo.

3. Copia y ejecuta el siguiente comando para clonar el repositorio:

   ```bash
   git clone https://github.com/Cosio1985/BackEndApiUsuario.git
   ```

4. Entra a la carpeta recién creada:

   ```bash
   cd BackEndApiUsuario
   ```

### Opción B: Descarga directa en archivo ZIP

1. Ingresa a la página web del repositorio en GitHub: [BackEndApiUsuario](https://github.com/Cosio1985/BackEndApiUsuario).

2. Haz clic en el botón verde **`<> Code`**.

3. Selecciona la opción **Download ZIP**.

4. Una vez descargado el archivo comprimido, descomprímelo en una carpeta de fácil acceso en tu computadora.

## Paso 2: Ambientación y Apertura en Visual Studio Code

1. Abre la aplicación **Visual Studio Code (VSC)** en tu equipo.

2. Ve al menú superior y selecciona **Archivo > Abrir carpeta...** (o *File > Open Folder*).

3. Selecciona la carpeta del proyecto (`BackEndApiUsuario` o la carpeta descomprimida).

4. Verifica en el panel lateral izquierdo del explorador que los archivos principales se encuentren visibles y organizados en la raíz:

   * `Dockerfile`
   * `docker-compose.yml`
   * `manage.py`
   * `requirements.txt`
   * `db.sqlite3` (base de datos precargada con datos de prueba)
   * Carpetas de aplicaciones (`LoginUser/`, `backend1_login/`)

## Paso 3: Encendido de Docker Desktop (Requisito Indispensable)

Antes de ejecutar comandos en la terminal de tu editor, debes asegurarte de que el motor de contenedores esté activo:

1. Busca y abre la aplicación **Docker Desktop** en tu sistema operativo (Windows o Mac).

2. Espera unos segundos a que la interfaz indique que el servicio está completamente encendido y en ejecución (el indicador visual o ícono en la barra de tareas suele ponerse en verde).

   >  **Nota:** Si intentas ejecutar comandos de Docker sin haber abierto esta aplicación previamente, la terminal te devolverá un error de conexión (*daemon not running*).

##  Paso 4: Ejecución del Contenedor desde la Terminal

1. En Visual Studio Code, abre la terminal integrada utilizando el atajo de teclado `Ctrl + Ñ` (o `Ctrl + ~`), o bien desde el menú superior en **Terminal > Nueva terminal**.

2. Asegúrate de que la ruta activa en la terminal corresponda exactamente a la raíz del proyecto (debes ver los archivos de configuración de Docker).

3. Escribe y ejecuta el siguiente comando para construir y levantar el servidor backend:

   ```bash
   docker compose up --build
   ```

4. **¿Qué sucede en este punto?**
   * Docker leerá el `Dockerfile` y el `requirements.txt` para empaquetar el entorno de Python de forma aislada.
   * Montará la base de datos `db.sqlite3` ya precargada con los usuarios de prueba.
   * La primera ejecución puede tardar un par de minutos mientras descarga la imagen base; las siguientes serán casi instantáneas.

5. Sabrás que el servidor está listo y operando cuando en la terminal visualices mensajes de Django similares a:

   ```text
   backend-1  | Starting development server at http://0.0.0.0:8000/
   backend-1  | Quit the server with CONTROL-C.
   ```

   >  **Importante:** Deja esta ventana de terminal abierta. Si la cierras o presionas `Ctrl + C`, el contenedor se detendrá y el servidor dejará de responder.

##  Paso 5: Pruebas de Verificación y Registro con Postman

Para interactuar con la API REST y verificar que el servidor acepta operaciones (como el registro de nuevos usuarios), es necesario utilizar la herramienta **Postman**. Si no la tienes instalada en tu equipo, descárgala y ábrela antes de continuar.

### Pasos para probar el registro de un nuevo usuario:

1. Abre la aplicación **Postman**.
2. Crea una nueva pestaña de solicitud HTTP haciendo clic en el botón `+`.
3. Cambia el método HTTP a **`POST`** utilizando el selector desplegable situado junto a la barra de direcciones.
4. Introduce la URL completa del endpoint de registro del backend:
   ```text
   http://127.0.0.1:8000/api/registro/
   ```
5. Dirígete a la pestaña **Headers** (Cabeceras) debajo de la URL y asegúrate de agregar:
   * Key: `Content-Type`
   * Value: `application/json`
6. Dirígete a la pestaña **Body** (Cuerpo), selecciona la opción **`raw`** y asegúrate de que el formato a la derecha esté configurado como **JSON**.
7. Copia y pega el siguiente objeto JSON con los datos de prueba en el área de texto:
   ```json
   {
     "username": "alumno2",
     "password": "PasswordSegura124",
     "email": "alumno1@correo.com",
     "first_name": "Juan",
     "last_name": "Pérez"
   }
   ```
8. Haz clic en el botón **Send** (Enviar).

### Resultados esperados:
* Recibirás una respuesta HTTP con código **`201 Created`** (o el estado de éxito correspondiente configurado en tu API) junto con un objeto JSON confirmando la creación del usuario.
* Esto valida que el contenedor Docker está respondiendo correctamente, procesa los datos y está listo para enlazarse con tu cliente frontend en Vite.