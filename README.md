**BIENVENIDOS A EL PROYECTO INTEGRADOR DE SABERES "PIS"**  

INTEGRANTES:  
- Josue Torres (@josuetrres)
- Alexis Roman (@vinirmn007)
- Emilio Jaramillo (@emilioj04)
- Benito Minga (@manuelminga)
- Daniel Sanchez (@DanielS110)

---
**DIAGRAMA DE CLASES:**  
  ![Diagrama_clases](https://github.com/user-attachments/assets/00072377-32f3-438f-8f13-e1c79aac015b)


---
# Carácteristicas del sitio web
![udgh](https://github.com/josuetrres/PIS/assets/166523434/ecbdf20c-06dc-48d4-bd73-fd9557c88804)

---
- El programa te permite agregar nuevos componentes electronicos, desde el admin.
    Usuario: admin
    Contraseña: 12345678
  
  ![Imagen de WhatsApp 2024-06-07 a las 14 27 29_986f569a](https://github.com/josuetrres/PIS/assets/166523434/2b965c9e-cdc0-40b6-a0d9-a9a380b60446)
  
  ![Imagen de WhatsApp 2024-06-07 a las 14 27 30_b5a0d824](https://github.com/josuetrres/PIS/assets/166523434/529a7bcd-104d-4d72-848f-5625fc7c749d)

  ---

- El sitio web permite navegar a traves de los apartados: Inicio, Desarrolladores, Documentación, Testimonios, y Control, esto permitira al usuario una mejor visualizacion y navegación intuitiva, mediante el cual al usuario le permitirá  conocer de lo que se trata nuestro proyecto Telerobob y su respectivo funcionamiento del mismo.
  ![rgrg](https://github.com/josuetrres/PIS/assets/166523434/6a181809-08de-4b16-aa14-9211a677326a)

  ---

- Exite una opcion para acceder al link del repsitorio de GitHub, haciendo clik en el icono del mismo.
  
![tr](https://github.com/josuetrres/PIS/assets/166523434/35a7900f-9b58-4ea8-a551-7fdbf71d9d82)

---
  
- Permite a los usuarios en el apartado de testimonio dejar un comentario de como apreciaron la plataforma.
  ![erer](https://github.com/josuetrres/PIS/assets/166523434/d9b03ef4-61ad-4343-a778-255c0a470bc2)

- Mediante el apartado de la documentación el usuario podra conocer cada detalle de como se realizo el proyecto PIS:
  Materiales.- En este aparatdo se encuentran todos los materiales utilizados para la realización de nuestro Telerobot, con su respectiba implementacion y funcionamiento.
  Funcionamiento: Se encuentran videos recopialdos, que se realizo al momento de hacer prubas de movimiento del brazo.
  Integración de materias: Conjunto de conocimientos que se aplicaran segmentados por materias.
  Diagrama de clases: Se observa el diagrama UML de clases, donde se puede observar la logica detras del sitio web, las relaciones que tiene cada clase para el correcto funcionamiento.
  Historias de usuario: El historial de usuario describe las funcionalidades que se desean implementar en un proyecto de control de un brazo robótico a través de una interfaz web.
  ![sfad](https://github.com/josuetrres/PIS/assets/166523434/aa6cf16f-e3e9-4a56-9690-1917ffc32faf)

---
- En la parte inferior de la plataforma (footer), se vusualiza los apartados de la ubicación del proyecto, como también el numero de teléfono y el correo del proyecto denominado JABED, para consultar cualquier inquietud mas personalisada.
![dewtgewr](https://github.com/josuetrres/PIS/assets/166523434/a1821614-d4b7-4fdd-9206-ddfb6e7145c0)
  
---
**##Integración de materias**  
- **Análisis Matemático:** Los conocimientos de esta materia se utlizara para automatizar el movimiento del brazo robotico mediante ecuaciones diferenciales e integrales, ademas de apoyar al algoritmo estadistico.
  
- **Diseño de Circuitos:** En esta materia utilizaremos los conocmientos obtenidos para lograr crear y optimizar diseños electronicos necesarios, para el correcto funcionamiento del proyecto, asi mismo, de esta manera lograr entender y preveer errores que genewren los componentes desde bajo nivel.
   
- **Teoria de la Distribución y Probabilidad:** Se pretende utilizar los concimientos de esta materia para lograr implementar estadisticas de uso del brazo robotico. Caracteristicas tales como el peso de cada objeto recolectado, la temperatura ambiente en el sitio donde esta ubicado, ademas de su posición en el GPS. Todo esto nos ayudara a realizar graficos estadisticos.
   
- **Programación Orientada a Objetos:** Implementaremos los conocimientos adquiridos en POO, para planificar y desarrollar aplicaciones web, y de esta manera darle su respectivo fucionamiento al Hardware. El mismo se lograra mediante la implementación de modelado UML, y lenguajes de programación con sus respectivos frameworks, aprendidos durante el ciclo.
  
- **Emprendimiento e Innovación Técnologica:** Los conocimientos adquiridos en esta meteria se hara uso para poder gestionar la imagen del proyecto, gastos e inversiones que se realizaran al momento del desarrollo del proyecto.
  
---
**##Historias de usuario**  
**Historia 1**  
Como usuario, quiero poder controlar el movimiento del brazo robótico a través de la interfaz web para realizar tareas específicas.
  
**Historia 2**  
Como usuario, quiero poder programar secuencias de movimientos para que el brazo robótico los ejecute automáticamente.
  
**Historia 3**  
Como usuario, quiero recibir feedback en tiempo real del estado y posición del brazo robótico para asegurarme de que está funcionando correctamente.
  
**Historia 4**  
Como usuario me gustaria que la aplicacion de control del brazo robotico cuente con imagen de video en vivo.
  
---
  
**##Casos de uso**  
    
**Título:** Recolectar desechos peligrosos  
**Actor:** Usuario  
**Precondiciones:** El usuario debe estar registrado y debe estar familiarizado con los controles del robot.  
**Flujo principal:**
- El usuario  debe escoger seleccionar los desechos destinados a recolectar.
- El usuario debe iniciar seción.
- Una vez dentro de la pagina principal debe dirigirce al apartado control remoto.
- Ya familiarizado con los controles, procede a manipular el brazo robotico y de igual manera observalo en la camara integrada.
- Recoge la basura para posteriormente colocar en el sensor de peso.
**Flujos alternativos:** 
- Si el cliente no tiene una cuenta, se le solicita que se registre.
- Si el usuario no esta familiarizado, procedera a seguir el tutorial de como usarlo.


**Título:** Automatizar un movimiento  
**Actor:** Usuario  
**Precondiciones:** El usuario debe estar registrado y debe estar familiarizado con los controles del robot.  
**Flujo principal:**
- El usuario  debe realizar el movimiento deseado con el brazo.
- Luego el usuario debe guardarlo mediante un boton integrado al sitio web.
**Flujos alternativos:**
- Si el cliente no tiene una cuenta, se le solicita que se registre.
- Si el usuario no esta familiarizado, procedera a seguir el tutorial de como usarlo.


## GitHub Pages

GitHub Pages es un servicio ofrecido por GitHub que permite a los usuarios publicar sitios web directamente desde un repositorio en GitHub; esto es especialmente útil para alojar páginas web estáticas, como blogs, sitios personales, documentación de proyectos y páginas de portafolio.

---

### Características de GitHub Pages

1. **Alojamiento de Páginas Web Estáticas**: GitHub Pages está diseñado para alojar contenido estático, como HTML, CSS, JavaScript y archivos de imágenes.

2. **Integración con Repositorios**: Los sitios de GitHub Pages se publican directamente desde los repositorios de GitHub, el cual significa que cualquier cambio realizado en el repositorio (en una rama específica) puede desencadenar una actualización del sitio web.

3. **Soporte para Jekyll**: GitHub Pages tiene soporte integrado para Jekyll, un generador de sitios estáticos. Esto permite a los usuarios crear sitios web con plantillas y contenido dinámico generado estáticamente.

4. **Subdominio Gratuito**: GitHub Pages proporciona un subdominio gratuito en la forma `username.github.io` para los sitios de usuario o `username.github.io/reponame` para sitios de proyectos.

5. **Configuración de Dominios Personalizados**: Los usuarios pueden configurar dominios personalizados para sus sitios de GitHub Pages, permitiendo que el sitio esté disponible en su propio dominio.

---

**## Cómo Funciona GitHub Pages**

1. **Creación del Repositorio**:
   - Para un sitio de usuario, crea un repositorio llamado `username.github.io`.
   - Para un sitio de proyecto, crea un repositorio con el nombre del proyecto.

2. **Agregar Contenido**:
   - Agrega archivos HTML, CSS, JavaScript y otros contenidos estáticos al repositorio.
   - Si usas Jekyll, agrega archivos Jekyll y configura el sitio según tus necesidades.

3. **Seleccionar la Rama**:
   - Para sitios de usuario, GitHub Pages publica contenido desde la rama `main` o `master`.
   - Para sitios de proyecto, puedes configurar GitHub Pages para publicar desde `main`, `master` o una carpeta específica (por ejemplo, `/docs`).

4. **Publicación**:
   - Una vez configurado, GitHub Pages generará y publicará el sitio web automáticamente cada vez que se realicen cambios en el repositorio.

### Ejemplo para crear un sitio web básico

Para crear un sitio web básico con GitHub Pages:

1. **Crear el Repositorio**:
   - Navegamos a GitHub y crea un nuevo repositorio llamado `username.github.io` (reemplaza `username` con tu nombre de usuario de GitHub).

2. **Agregar un Archivo HTML**:
   - En el repositorio, agrega un archivo llamado `index.html` con contenido HTML.

3. **Publicar**:
   - Una vez que el archivo esté en el repositorio, GitHub Pages lo publicará automáticamente.
   - Accede a `https://username.github.io` para ver tu sitio web.

---
