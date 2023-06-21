# CourseraPractice

Este repositorio muestra las prácticas para el certificado de Python impartido por Coursera. Comparto para aquellos que están haciendo el curso, es básicamente como los he pensado, si tienen alguna sugerencia para mejorar el código pues bienvenido sea. 

Esto es una guía, el código debe ser adaptado a lo que pide cada evaluación. 

## Primera Semana ##
Se solicita crear una aplicación que lea un grupo de imágenes de una carpeta, se roten la imagen, se redimensiona y se almacenen en una nueva carpeta. Carpeta firstweek contiene el archivo rotateimg.py

Recomendaciones, validar la carpeta en donde se pide se guarde las imagenes. La ruta dentro del código en referencial. 

## Segunda Semana ##
Se solicita convertir varios archivos txt que son parte de las revisiones de compra de clientes de vehículos y colocarlos de forma automática en la página. Para ello es necesario convertir la información contenida dentro de cada TXT en un diccionario que luego será enviado al servicio web por un POST. 

## Tercera Semana ##
En esta ocasión solicitan modificar un script que lee un documento .json con una lista de venta de modelos de carros. Hay que totalizar esta lista en tres forma. Modelo con las ganancias mayores, el vehículo que tuvo más cantidad de ventas y el año que tuvo más cantidad de ventas. Luego de totalizado hay que enviar esta información por correo adjuntando la tabla de los carros parseado de una forma específica. Mucho del código ya está suministrado pero hay que unir las piezas y agregar un poco más de código para que funcione correctamente. 

## Cuarta Semana ##
En esta oportunidad se pide realizar varios scripts que realicen la carga de imagenes y sus respectivas descripciones en una página web, envíe un reporte de los archivos cargados y sea enviado por correo electrónico y exista un monitoreo de salud del servidor que muestra la información. Los scripts realizados son los siguientes:

    * Change_Image.py -> Realiza el re dimensionamiento y transforma archivos de imagen en .jpeg y almacena la información en una carpeta.
    * supplier_image_upload.py -> Carga las imágenes .jpeg en un servicio web para que sea desplegado en la página.
    * Run.py -> A partir de varios archivos TXT extrae la información de las imágenes cargadas en el script anterior, lo organiza en un diccionario y es enviado a un servicio web mediante el método post para su publicación.
    * reports.py -> Contiene todas las librerías necesarias para crear un archivo PDF. 
    * emails.py -> Contiene todas las librerías para crear la estructura de un email y luego enviarlo. 
    * report_email.py -> Script que se encarga de crear un archivo PDF de acuerdo al resumen de producto que se han subido a la página web y enviarlo vía correo. 
