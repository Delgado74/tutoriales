import os

# Configura el nombre base y el número inicial
nombre_base = "cashubasic"
contador = 13

# Obtiene la lista de archivos en el directorio actual
archivos = os.listdir()
print("Archivos encontrados en el directorio:")
print(archivos)

# Filtra los archivos que empiezan con "Screenshot" y terminan en .png
archivos_screenshot = sorted([f for f in archivos if f.startswith("Screenshot") and f.endswith(".jpg")])
print("\nArchivos que serán renombrados:")
print(archivos_screenshot)

# Renombra los archivos
for archivo in archivos_screenshot:
    nuevo_nombre = f"{nombre_base}{contador}.png"
    os.rename(archivo, nuevo_nombre)
    print(f"Renombrado: {archivo} -> {nuevo_nombre}")
    contador += 1

if not archivos_screenshot:
    print("\nNo se encontraron archivos que empiecen con 'Screenshot' y terminen en '.png'.")

