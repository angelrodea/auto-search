# Auto-Search Bing

## DESCRIPCIÓN
Este es un script de Python que utiliza la biblioteca Selenium para automatizar búsquedas en el motor de búsqueda Bing. El script lee una lista de palabras clave desde un archivo de texto y realiza búsquedas en Bing para cada palabra en la lista. También maneja errores y proporciona mensajes de error si hay algún problema al realizar una búsqueda. Además, se ha agregado una opción para desactivar los registros innecesarios de Selenium en la consola. Este script es útil para cualquier persona que necesite automatizar búsquedas en Bing.

## REQUISITOS
- Python
- Instalar `requirements.txt`
- Descargar [WebDriver de Microsoft Edge](https://developer.microsoft.com/es-es/microsoft-edge/tools/webdriver/)
    - Descargar el driver segun la versión del navegador. Para ver la version de Edge entrar a `edge://settings/help`
    - Agregar ruta del driver al PATH
    - Reiniciar

## INSTALACIÓN
```python
pip install -r requirements.txt
```

## USO
```python
python.exe autoSearch.py
```