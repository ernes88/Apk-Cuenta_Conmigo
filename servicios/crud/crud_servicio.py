from datos.modelos import crud_modelo as modelo_crud
from datetime import datetime

#CREAR REGISTRO
def crear_registro(nombre_tabla, datos_registro):
    if not _existe_registro(nombre_tabla, datos_registro):
        modelo_crud.crear_registro(nombre_tabla, datos_registro)
    else:
        raise Exception("El registro ya existe")

#CREAR USUARIO
def crear_usuario(nombre, clave, fecha_nacimiento, genero, rol):
    if not _existe_usuario(nombre, clave):
        modelo_crud.crear_usuario(nombre, clave, fecha_nacimiento, genero, rol)
    else:
        raise Exception("El usuario ya existe")

#CREAR ACTIVIDAD
def crear_actividad(tipo, valor, realizada, intensidad):
    if not _existe_actividad(tipo, valor):
        modelo_crud.crear_actividad(tipo, valor, realizada, intensidad)
    else:
        raise Exception("La actividad ya existe")

#CREAR ROL
def crear_rol(rol):
    if not _existe_rol(rol):
        modelo_crud.crear_rol(rol)
    else:
        raise Exception("El rol ya existe")

#CRAR TARJETA DE HUMOR
def crear_tarjeta_de_humor(fecha_actual, valor, promedio):
    if not _existe_tarjeta_de_humor(valor, promedio):
        modelo_crud.crear_tarjeta_de_humor(fecha_actual, valor, promedio)
    else:
        raise Exception("La atarjeta de humor ya existe")

#LEER TABLA
def leer_tabla(nombre_tabla):
    return modelo_crud.leer_tabla(nombre_tabla)

#LEER TABLA CON LIMITE
def leer_tabla_con_limite(nombre_tabla, limite):
    return modelo_crud.leer_tabla_con_limite(nombre_tabla, limite)

#LEER TODOS LOS REGISTROS DE UNA TABLA QUE CUMPLAN UNA CONDICION
def leer_tabla_filtrada(nombre_tabla, condicion):
    return modelo_crud.leer_tabla_filtrada(nombre_tabla, condicion)

#LEER UN REGISTRO
def leer_registro(nombre_tabla, id_registro):
    registro = modelo_crud.leer_registro(nombre_tabla, id_registro)
    if len(registro) == 0:
        raise Exception("El registro no existe")
    return registro[0]


#ACTUALIZAR REGISTRO
def modificar_registro(nombre_tabla, id_registro, datos_registro):
   modelo_crud.modificar_registro(nombre_tabla, id_registro, datos_registro)


#BORRAR TABLA
def borrar_tabla(nombre_tabla):
    modelo_crud.borrar_tabla(nombre_tabla)


#BORRAR UN REGISTRO
def borrar_registro(nombre_tabla, id_registro):
    modelo_crud.borrar_registro(nombre_tabla, id_registro)


#OBTENER CANTIDAD DE REGISTROS
def contar_registros(nombre_tabla):
    return modelo_crud.contar_registros(nombre_tabla)

#OBTENER CANTIDAD DE REGISTROS FILTRADOS
def contar_registros_filtrados(nombre_tabla, condicion):
    return modelo_crud.contar_registros_filtrados(nombre_tabla, condicion)

#ORDENAR REGISTROS
def ordenar_registros(nombre_tabla, campo_de_ordenacion, tipo):
    return modelo_crud.ordenar_registros(nombre_tabla, campo_de_ordenacion, tipo)

#ORDENAR REGISTROS FILTRADOS
def ordenar_registros_filtrados(nombre_tabla, campo_de_ordenacion, tipo, condicion):
    return modelo_crud.ordenar_registros_filtrados(nombre_tabla, campo_de_ordenacion, tipo, condicion)

#VALIDACIONES
def _existe_registro(nombre_tabla, datos_registro):
    registro = modelo_crud.validar_registro(nombre_tabla, datos_registro)
    return not len(registro) == 0

def _existe_usuario(nombre, clave):
    usuarios = modelo_crud.obtener_usuario_por_nombre_y_clave(nombre, clave)
    return not len(usuarios) == 0

def _existe_actividad(tipo, valor):
    actividades = modelo_crud.obtener_actividad_por_tipo_y_valor(tipo, valor)
    return not len(actividades) == 0

def _existe_rol(rol):
    roles = modelo_crud.obtener_rol(rol)
    return not len(roles) == 0

def _existe_tarjeta_de_humor(valor, promedio):
    tarjetas_de_humor = modelo_crud.obtener_tarjeta_de_humor_por_valor_y_promedio(valor, promedio)
    return not len(tarjetas_de_humor) == 0


