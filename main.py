# Script para limpieza automática de archivos antiguos
# Copyright (c) 2025 Camino del Dev
#
# Este script está licenciado bajo la Licencia MIT.
# Consulta el archivo LICENSE para obtener más detalles.

import os
import time


# Define la ruta de la carpeta a limpiar.
carpeta = "/ruta/a/la/carpeta/a/limpiar"
# Define el número de días de antigüedad como umbral para la eliminación.
dias = 30
# Inicializa un contador para el número de archivos eliminados.
borrados = 0
# Calcula el timestamp límite para la eliminación (antigüedad en segundos).
limite = time.time() - (dias * 86400)

# Itera sobre cada elemento dentro de la carpeta especificada.
for archivo in os.listdir(carpeta):
    # Construye la ruta completa al elemento.
    ruta_completa = os.path.join(carpeta, archivo)

    # Verifica si el elemento actual es un archivo.
    if os.path.isfile(ruta_completa):
        # Comentado: Posible condición adicional para filtrar por extensión de archivo (ejemplo: .jpg).
        # and archivo.endswith('.jpg')
        
        # Verifica si la fecha de última modificación del archivo es anterior al límite calculado.
        if (os.path.getmtime(ruta_completa) < limite):
            # Bloque try-except para manejar posibles errores durante la eliminación del archivo.
            try:
                # Intenta eliminar el archivo.
                os.remove(ruta_completa)
                # Imprime un mensaje indicando el archivo eliminado.
                print(f"Archivo eliminado: {archivo}")
                # Incrementa el contador de archivos eliminados.
                borrados += 1
            except Exception as e:
                # Imprime un mensaje de error si la eliminación falla.
                print(f"Error al intentar eliminar {archivo}: {e}")

# Imprime el número total de archivos que fueron eliminados.
print(f"Se han eliminado {borrados} archivos")
