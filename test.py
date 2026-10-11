import os
import re
from solucion import obtener_monedas_de_archivo, maxima_ganancia_sofia, obtener_resultados_mateo


def leer_resultados_esperados(path):
    """
    Lee el archivo de texto y extrae las ganancias de Sophia.
    """
    resultados = {}
    if not os.path.exists(path):
        print(f"⚠️ Archivo no encontrado en la ruta: {path}")
        return resultados

    with open(path, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    nombre_actual = None
    for linea in lineas:
        linea_s = linea.strip()
        if not linea_s:
            continue

        if linea_s.endswith(".txt") and " " not in linea_s:
            nombre_actual = linea_s
            continue

        valor_match = re.search(r"Ganancia Sophia:\s*(\d+)", linea_s, re.IGNORECASE)
        if valor_match and nombre_actual:
            valor = int(valor_match.group(1))
            resultados[nombre_actual] = {
                "ganancia_esperada": valor
            }

    return resultados


def ejecutar_tests(resultados_esperados, carpeta):
    if not resultados_esperados:
        print(f"No se encontraron resultados esperados en la carpeta '{carpeta}' o el archivo no existe.\n")
        return

    for nombre_archivo, datos in resultados_esperados.items():
        archivo_path = os.path.join(carpeta, nombre_archivo)
        print(f"===== Test: {nombre_archivo} =====")

        if not os.path.exists(archivo_path):
            print(f"❌ No se encontró el archivo de entrada: {archivo_path}\n")
            continue

        try:
            monedas = obtener_monedas_de_archivo(archivo_path)
            solucion_sofia = maxima_ganancia_sofia(monedas)
            ganancia_sofia = sum(solucion_sofia)
            solucion_mateo = obtener_resultados_mateo(monedas, solucion_sofia)
            ganancia_mateo = sum(solucion_mateo)
            esperado = datos["ganancia_esperada"]

            if esperado is not None:
                if ganancia_sofia == esperado:
                    print("✅ Ganancia óptima correcta")
                else:
                    print(f"❌ Ganancia errónea")
                print(f"Resultado esperado para Sofia: {esperado}")
                print(f"Suma total Sofia: {ganancia_sofia}")
                print(f"Suma total Mateo: {ganancia_mateo}")
            else:
                print(f"⚠️ Sin valor esperado definido. Ganancia obtenida: {ganancia_sofia}")
        except Exception as e:
            print(f"❌ Error al procesar {archivo_path}: {e}")
        print()


if __name__ == "__main__":
    ruta_esperados_catedra = "Set_Datos_Catedra/Resultados_Esperados.txt"
    carpeta_catedra = "Set_Datos_Catedra"

    print("--- EJECUTANDO TESTS DE CÁTEDRA ---")
    resultados_catedra = leer_resultados_esperados(ruta_esperados_catedra)
    ejecutar_tests(resultados_catedra, carpeta_catedra)
