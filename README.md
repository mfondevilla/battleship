#  Battleship 🚢 Hundir la flota

Battleship es un pequeño juego de consola escrito en Python. El objetivo es adivinar la posición de todos los barcos generada aleatoriamente por el programa.

## Requisitos

- Python 3.0 o superior

## Características

- Posiciones de los barcos generadas de forma aleatoria
- Variables y constantes configurables en un fichero variables.py
- Ejecución desde consola
- Modalidad de jugador vs. ordenador

## Estructura del proyecto
El código fuente del proyecto se encuentra organizado dentro del directorio `src`, mientras que los ficheros `main.py` y `README.md` permanecen en el nivel raíz del repositorio.  

Dentro de `src` el código se organiza en los siguientes directorios:  

`clases`: Definición de la clase tablero y sus métodos

`functions`: Definición de las funciones relativas a las acciones de: crear tableros, colocar barcos, disparar, acciones por turno

`notebooks`: notebooks Jupyter para probar funciones de forma independiente y encapsulada

`variables` : Definición de variables y constantes que se usarán en la diferentes funciones y clases del proyecto

            
## Guía de usuario
* Se requiere tener instalada una versión 3.0 de Python o superior
* Clonar el proyecto el local
* Abrir una terminal en la carpeta raíz del proyecto
* Ejecutar el programa con el comando: `python py main.py` o `py main.py`
* Se mostrará un menú con tres opciones
    1. Nueva partida
    2. Instrucciones
    3. Salir
* Introducimos `1` para inciar la partida, en ese momento iremos introduciendo coordenadas de disparos turnándonos con los disparos aleatorios del juego sobre nuestro tablero, hasta que uno de los dos haya hundido todos los barcos del contrincante.


## Autores

Ana Corrochano  
Melania Fondevilla  
María Rodríguez  
William Walker
