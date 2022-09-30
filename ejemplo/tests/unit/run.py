from pathlib import Path

import sys

path_root = Path(__file__).parents[3]
sys.path.append(str(path_root))
print(sys.path)

from ejemplo.app.funciones import procesar_apellido_paterno

print("Imported!")