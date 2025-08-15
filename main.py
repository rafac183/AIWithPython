# Programa para contar palabras en un archivo de texto

import os
import re
from collections import Counter


def main():
    print("=== CONTADOR DE PALABRAS EN ARCHIVOS DE TEXTO ===")

    # 1. Pedir al usuario la ruta de un archivo de texto
    while True:
        ruta_archivo = input("\nIngresa la ruta del archivo de texto: ").strip()

        if not ruta_archivo:
            ruta_archivo = "ejemplo.txt"
            print(f"Usando archivo de ejemplo: {ruta_archivo}")

        if os.path.exists(ruta_archivo):
            break
        else:
            print(f"Error: No se encontró el archivo '{ruta_archivo}'")
            print("Puedes usar 'ejemplo.txt' que viene incluido.")

    # 2. Leer el contenido del archivo
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        print(f"\n=== CONTENIDO DEL ARCHIVO '{ruta_archivo}' ===")
        print(contenido)
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    # 3. Separar en palabras
    palabras = re.findall(r"\b\w+\b", contenido.lower())
    print(f"\n=== PALABRAS EXTRAÍDAS ===")
    print(f"Total de palabras encontradas: {len(palabras)}")
    print("Primeras 10 palabras:", palabras[:10])

    # 4. Contar número total de palabras
    total_palabras = len(palabras)
    contador = Counter(palabras)
    print(f"\n=== CONTEO DE PALABRAS ===")
    print(f"Total de palabras: {total_palabras}")
    print(f"Palabras únicas: {len(contador)}")

    # 5. Mostrar las 10 palabras más frecuentes y su conteo
    print(f"\n=== TOP 10 PALABRAS MÁS FRECUENTES ===")
    print("Posición | Palabra | Frecuencia")
    print("-" * 35)

    for i, (palabra, frecuencia) in enumerate(contador.most_common(10), 1):
        print(f"{i:8d} | {palabra:7s} | {frecuencia:10d}")


if __name__ == "__main__":
    main()
