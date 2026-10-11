import sys
import time
sys.setrecursionlimit(6000)


def obtener_monedas_de_archivo(file: str):
    """
    Lee el archivo de texto con las monedas y las almacena en una lista.
    Complejidad: O(n), siendo n la cantidad de monedas.
    """
    with open(file, "r") as archivo:
        archivo.readline()
        monedas = list(map(int, archivo.readline().strip().split(';')))
    return monedas


def reconstruir_solucion(monedas, matriz, inicio, fin, solucion, lados):
    """
    Reconstruye la solución óptima a partir de la matriz de soluciones.
    Complejidad: O(n), siendo n la cantidad de monedas.
    """
    if fin == inicio:
        solucion.append(monedas[inicio])
        lados.append("inicio")
        return solucion

    if fin - inicio == 1:
        if monedas[fin] > monedas[inicio]:
            solucion.append(monedas[fin])
            lados.append("fin")
            return solucion

        solucion.append(monedas[inicio])
        lados.append("inicio")
        return solucion

    opt_1 = monedas[fin] + (matriz[fin-2][inicio] if monedas[fin-1] >= monedas[inicio] else matriz[fin-1][inicio+1])
    opt_2 = monedas[inicio] + (matriz[fin-1][inicio+1] if monedas[fin] >= monedas[inicio+1] else matriz[fin][inicio+2])

    if opt_1 > opt_2:
        solucion.append(monedas[fin])
        lados.append("fin")
        if monedas[fin-1] >= monedas[inicio]:
            return reconstruir_solucion(monedas, matriz, inicio, fin-2, solucion, lados)
        return reconstruir_solucion(monedas, matriz, inicio+1, fin-1, solucion, lados)

    solucion.append(monedas[inicio])
    lados.append("inicio")
    if monedas[fin] >= monedas[inicio+1]:
        return reconstruir_solucion(monedas, matriz, inicio+1, fin-1, solucion, lados)
    return reconstruir_solucion(monedas, matriz, inicio+2, fin, solucion, lados)


def mostrar_pasos(lados, monedas):
    """
    Muestra los pasos realizados por Sofia para obtener la máxima ganancia.
    Complejidad: O(n^2), siendo n la cantidad de monedas.
    """

    print("\nMONEDAS TOMADAS EN CADA TURNO")
    print("-----------------------------\n")
    inicio = 0
    fin = len(monedas) - 1
    i = 0
    while inicio <= fin:
        print("Monedas restantes: ", monedas[inicio:fin+1])
        if lados[i] == "fin":
            print(f"Sofia toma la moneda {monedas[fin]}")
            fin -= 1
        else:
            print(f"Sofia toma la moneda {monedas[inicio]}")
            inicio += 1

        i += 1
        if inicio > fin:
            print()
            break

        if monedas[fin] >= monedas[inicio]:
            print(f"Mateo toma la moneda {monedas[fin]}\n")
            fin -= 1
        else:
            print(f"Mateo toma la moneda {monedas[inicio]}\n")
            inicio += 1


def maxima_ganancia_sofia(monedas, mostrar_detalle=False):
    """
    Calcula la máxima ganancia que Sofia puede obtener.
    Complejidad: O(n^2), siendo n la cantidad total de monedas.
    """
    n = len(monedas)

    # matriz_solucion: matriz_solucion[i][j] almacena la ganancia máxima que
    # Sofia puede obtener en el rango [i, j]
    matriz_solucion = [[None] * n for _ in range(n)]

    # Caso base: cuando solo hay una moneda disponible
    # inicializa la diagonal principal de la matriz_solucion
    for i in range(n):
        matriz_solucion[i][i] = monedas[i]

    for i in range(n - 1):
        matriz_solucion[i+1][i] = max(monedas[i], monedas[i+1])

    for i in range(2, n):
        k = i
        for j in range(n - i):

            opt_1 = monedas[k] + (matriz_solucion[k-2][j] if monedas[k-1] >= monedas[j] else matriz_solucion[k-1][j+1])
            opt_2 = monedas[j] + (matriz_solucion[k-1][j+1] if monedas[k] >= monedas[j+1] else matriz_solucion[k][j+2])

            matriz_solucion[k][j] = max(opt_1, opt_2)
            k += 1

    solucion = []
    lados = []
    reconstruir_solucion(monedas, matriz_solucion, 0, n-1, solucion, lados)
    if mostrar_detalle:
        mostrar_pasos(lados, monedas)

    return solucion


def obtener_resultados_mateo(monedas, solucion_sofia):
    """
    Calcula las monedas y la ganancia de Mateo por diferencia
    """
    solucion_mateo = monedas.copy()
    for moneda in solucion_sofia:
        solucion_mateo.remove(moneda)

    return solucion_mateo


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("La cantidad de argumentos es incorrecta")
        print("Uso: python3 solucion.py <archivo_prueba>")
        sys.exit()

    monedas = obtener_monedas_de_archivo(sys.argv[1])
    start_time = time.time()
    solucion = maxima_ganancia_sofia(monedas, True)
    end_time = time.time()
    solucion_mateo = obtener_resultados_mateo(monedas, solucion)

    print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
    print(f"Monedas sacadas por Mateo: {solucion_mateo}")
    print(f"Monto obtenido por Mateo: {sum(solucion_mateo)}")
    print(f"\nMonedas sacadas por Sofia: {solucion}")
    print(f"Monto obtenido por Sofia: {sum(solucion)}")
    print(f"\nTiempo de ejecución: {end_time - start_time:.6f} segundos")
