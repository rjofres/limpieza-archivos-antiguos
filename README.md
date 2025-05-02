# Script de Limpieza de Archivos Antiguos en Python

[![Python 3](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Mantiene tu disco limpio](https://img.shields.io/badge/Estado-Activo-success)

Este script en Python 3 automatiza la eliminación de archivos antiguos de una carpeta específica, basado en la antigüedad en días. Se recomienda el uso de `virtualenv` para un entorno aislado.

## Uso

1.  **Clonar (opcional):**
    ```bash
    git clone git@github.com:rjofres/limpieza-archivos-antiguos.git
    cd limpieza-archivos-antiguos
    ```
2.  **Entorno Virtual (recomendado):**
    ```bash
    python3 -m virtualenv venv
    source venv/bin/activate            # macOS/Linux
    pip install -r requirements.txt
    ```
3.  **Configurar `main.py`:**
    
    Modifica las variables `carpeta` (ruta a la carpeta) y `dias` (antigüedad máxima en días).

4.  **Ejecutar:**
    ```bash
    python main.py
    ```

## Notas

* Asegúrate de configurar la carpeta correcta.
* Se recomienda probar en un entorno de prueba primero.

## Licencia

MIT License. Consulta el archivo `LICENSE`.

## Video del tutorial
Puedes seguir un paso a paso completo en el siguiente video:

[![Ver el tutorial en YouTube](https://img.youtube.com/vi/r1KrsChmNgw/hqdefault.jpg)](https://www.youtube.com/watch?v=r1KrsChmNgw)

> 🔗 [https://www.youtube.com/watch?v=r1KrsChmNgw](https://www.youtube.com/watch?v=r1KrsChmNgw)
