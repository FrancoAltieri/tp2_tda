# TP 2: Programación Dinámica

## Información de los estudiantes

* Nombre: Altieri Franco | Padrón: 105400
* Nombre: Claudia Lis Ramos Sarzuri | Padrón: 104596
* Nombre: Santino Federico Bouza | Padrón: 113991

## Sobre el trabajo

Este proyecto contiene la implementación de la solución algorítmica para la problemática planteada en el TP2.

## Instrucciones

### 1. Uso para un archivo

Para usar el programa, se debe ejecutar el archivo `solucion.py` y especificar qué archivo .txt se quiere utilizar. Los valores deben estar escritos como en un archivo .csv, separando cada valor con `;`.

```bash
python3 solucion.py <ruta_del_archivo.txt>
```

Los datos mostrados por terminal serán el paso a paso de las extracciones de monedas de Mateo y Sofia, el conjunto de monedas totales de cada uno y sus ganancias.

### 2. Uso del archivo de tests automatizado

El archivo de tests automatizado, a diferencia del archivo principal de nuestra solución, ejecuta toda la lógica computacional de los archivos del directorio `Set_Datos_Catedra` y solo muestra si pasan las verificaciones, los resultados obtenidos, y los resultados esperados. La decisión de no mostrar los pasos ni los conjuntos de monedas de Sofia y Mateo, es debido a que floodea la terminal, haciendo tediosa la comparativa de resultados finales. Para más detalle de la solucion de archivos especificos, se debe usar [1. Uso para un archivo](#1-uso-para-un-archivo)

```bash
python3 test.py
```
