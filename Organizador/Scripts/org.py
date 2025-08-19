from pathlib import Path
import os

carpeta = Path(__file__).parent
print(f"Organizando archivos en: {carpeta}")

categorias = {
    "Imagenes": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Datos": [".csv", ".xlsx", ".json"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Scripts": [".py", ".js", ".sh"],
    "Musica": [".mp3", ".flac", ".aac", ".wav"],
}
categorias_predeterminadas = ["Otros"]

extend_category = {}
for category, exts in categorias.items():
    for ext in exts:
        extend_category[ext.lower()] = category
        
items = [i for i in carpeta.iterdir() if i.is_file()]
for item in items:
    ext = item.suffix.lower()
    categoria = extend_category.get(ext, "Otros")
    nueva_carpeta = carpeta / categoria
    nueva_carpeta.mkdir(exist_ok=True)
    nuevo_path = nueva_carpeta / item.name
    item.rename(nuevo_path)
    print(f"Movido: {item.name} -> {nueva_carpeta}/")