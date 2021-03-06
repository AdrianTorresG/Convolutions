# Convolutions
 Repositorio que contiene la actividad final de la materia "Herramientas computacionales"

## Función 

_Este código aplica convoluciones con distintos kernels a una imagen. Y tiene el propósito de servir como introducción al manejo e interpretación de imágenes a través de matrices con redes neuronales ._

Ver **Ejecución** para conocer cómo ejecutar el proyecto.

## Convolución

_Una convolución es el tratamiento de una matriz (en este caso una imagen ya que es una colección bidimensional de píxeles ordenados en forma de coordenadas) por otra que se llama "kernel" que será diferente dependiendo del efecto que se quiera aplicar._
_En este proyecto se le agrega un padding a las imágenes para que no se pierda la información de los bordes._

### Conformación 📋

_Son dos archivos los que conforman este proyecto:_

* “LIB.py” que contiene todas las funciones de creación de kernels y de los paddings.
* “main.py” que ejecuta todos los procesos.

## Ejecución ⚙️

_Para la ejecución se necesita el nombre (y ruta si es necesario) del archivo donde se encuentra la imagen a la que se le quiere aplicar las convoluciones._
```
python main.py miImagen.png
```
_Con ruta:_
```
python main.py /Usuario/miUsuario/Descargas/miImagen.png
```

### Kernels

_Hay 5 kernels utilizados en este proyecto para generar las convoluciones:_
* “Gaussian Blur” que es muy utilizado en software gráficos y que tiene el objetivo de disminuir el ruido en imágenes y también los detalles.
* ”Laplacian of Gauss” que tiene el fin de detectar bordes en imágenes, la única desventaja de este es que es muy sensible al ruido por lo que se recomienda usar siempre una matriz 5x5.
* ”Simple Box Blur” que tiene la misma finalidad que “Gaussian Blur” solo que este es más fácil de implementar y se utiliza solo cuando se quiere obtener una aproximación del antes mencionado  “Gaussian Blur”.
* ”Horizontal Line Detection” que, como su nombre lo indica, sirve para detectar fácilmente líneas horizontales.
* ”Vertical Line Detection” que sirve para detectar fácilmente líneas verticales.

### Librerías utilizadas 🛠️

* “numpy” - para la creación de matrices.
* ”argparse” - para la obtención de argumentos a través de la línea de comandos.
* ”PIL” - para el manejo de imágenes.
* ”scipy” - para la creación de convoluciones.
* ”matplotlib” - para la graficación de las imágenes con convoluciones.

### Ejemplo de salida

![alt text](https://github.com/AdrianTorresG/Convolutions/blob/main/Imagenes/ejemploSalida.png?raw=true)

### Autor ✒️

_Adrián Torres González A01369810_

---
Creado por [AdrianTorresG](https://github.com/AdrianTorresG)

