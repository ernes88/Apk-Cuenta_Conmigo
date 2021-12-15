from datos.modelos import actividades_modelo as modelo_actividad
from datetime import datetime

#CREATE
def crear_actividad(tipo, valor, realizada, intensidad):
    if not _existe_actividad(tipo, valor):
        modelo_actividad.crear_actividad(tipo, valor, realizada, intensidad)
    else:
        raise Exception("La actividad ya existe")

#VALIDACIONES
def _existe_actividad(tipo, valor):
    actividades = modelo_actividad.obtener_actividad_por_tipo_y_valor(tipo, valor)
    return not len(actividades) ==0

#READ
def obtener_actividades():
    return modelo_actividad.obtener_actividades()