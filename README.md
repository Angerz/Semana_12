# Programa de Cálculo y Selección de Bandas o Fajas

Este programa tiene como objetivo calcular y seleccionar bandas o fajas para distintas aplicaciones. Contiene diferentes archivos y funcionalidades para facilitar el proceso de cálculo y selección. Además de permitir guardar los resultados en un archivo excel.

## Archivos del Proyecto

- **interfaz.py**: Es el programa principal que abre una interfaz gráfica con 4 botones. Permite ingresar parámetros como potencia en HP, RPM, diámetros de las poleas, etc. El segundo botón muestra los resultados obtenidos, el tercer botón abre una tabla para elegir el factor de servicio de la máquina y el cuarto botón llama al archivo interfaz_tablas.py.

- **interfaz_tablas.py**: Es una interfaz sencilla que muestra tablas adicionales para el cálculo y selección de las fajas. Permite visualizar información adicional sobre las fajas.

- **tablas_fajas.py**: Contiene todas las tablas requeridas para el cálculo y selección de las fajas. Las tablas están organizadas en listas de diccionarios.

- **main.py**: Es el archivo base para la selección de bandas y fajas. Permite ingresar los datos mediante la terminal y muestra los cálculos comprimidos allí. No tiene una interfaz gráfica, pero los cálculos son los mismos que en el archivo interfaz.py.

- **Imágenes**: Contiene las imágenes que se muestran en la interfaz del archivo interfaz_tablas.py.

## Uso del Programa

1. Ejecuta el archivo interfaz.py para abrir la interfaz principal.
2. En la interfaz, ingresa los parámetros requeridos para el cálculo y selección de las bandas o fajas.
3. Utiliza los botones correspondientes para ver los resultados, acceder a la tabla de factores de servicio o abrir la interfaz de tablas adicionales.
4. También puedes utilizar el archivo main.py para realizar los cálculos y obtener los resultados directamente en la terminal.

## Requisitos del Sistema

- Python 3.x
- PyQt5
- NumPy

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar o agregar funcionalidades al programa, puedes realizar un *fork* del repositorio, realizar los cambios en tu propio repositorio y luego enviar un *pull request* para revisar y fusionar los cambios.

## Licencia

Este programa se encuentra bajo la [licencia MIT](LICENSE).
