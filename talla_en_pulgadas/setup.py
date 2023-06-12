# Importa los módulos necesarios
import sys
from cx_Freeze import setup, Executable

# Lista de módulos adicionales requeridos por el script principal
additional_modules = [
    'tallaBackend',  # Importa el módulo tallaBackend.py
    # Agrega aquí otros módulos adicionales si los hay
]

# Lista de archivos adicionales requeridos por el programa
include_files = [
    'unidades_de_medida.jpg',  # Incluye el archivo de imagen unidades_de_medida.jpg
    # Agrega aquí otros archivos adicionales si los hay
]

# Determina el tipo de interfaz de usuario (si corresponde)
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Utiliza la interfaz gráfica en Windows

# Configuración de cx_Freeze
setup(
    name="Conversion de tallas a cm",  # Nombre del programa
    version="1.0",  # Versión del programa
    # Descripción del programa
    description="Conversor de unidades pulgadas y pies a centimetros",
    # Archivo principal y tipo de interfaz
    executables=[Executable("tallaApp.py", base=base)],
    options={
        'build_exe': {
            'includes': additional_modules,  # Módulos adicionales a incluir
            'include_files': include_files  # Archivos adicionales a incluir
        }
    }
)
