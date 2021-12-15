import requests                                     #Permite invocar funcionalidades que están en otro servidor.
from web.servicios import rest_api


#################################################CRUD ENDPOINTS#########################################
#CREAR REGISTRO
def crear_usuario(nombre, clave, fecha_nacimiento, genero, rol):
    body = {"nombre": nombre,
            "clave": clave,
            "fecha_nacimiento": fecha_nacimiento,
            "genero": genero,
            "rol": rol}
    nombre_tabla = 'usuarios'
    respuesta = requests.post(f'{rest_api.API_URL}/crear_registro/{nombre_tabla}', json=body)
    return respuesta.status_code == 200

def crear_actividad(tipo, valor, realizada, intensidad):
    body = {"tipo": tipo,
            "valor": valor,
            "realizada": realizada,
            "intensidad": intensidad}
    nombre_tabla = 'actividades'
    respuesta = requests.post(f'{rest_api.API_URL}/crear_registro/{nombre_tabla}', json=body)
    return respuesta.status_code == 200

def crear_rol(rol):
    body = {"rol": rol}
    nombre_tabla = 'roles'
    respuesta = requests.post(f'{rest_api.API_URL}/crear_registro/{nombre_tabla}', json=body)
    return respuesta.status_code == 200

def crear_tarjeta_de_humor(fecha_actual, valor, promedio):
    body = {"fecha_actual": fecha_actual,
            "valor": valor,
            "promedio": promedio}
    nombre_tabla = 'tarjetas_de_humor'
    respuesta = requests.post(f'{rest_api.API_URL}/crear_registro/{nombre_tabla}', json=body)
    return respuesta.status_code == 200

#LEER DE CUALQUIER TABLA TODOS LOS REGISTROS
def leer_tabla(nombre_tabla):
    respuesta = requests.get(f'{rest_api.API_URL}/leer_tabla/{nombre_tabla}')
    return respuesta.json()

#LEER DE UNA TABLA UN NÚMERO DETERMINADO DE REGISTROS
def leer_tabla_con_limite(nombre_tabla, limite):
    respuesta = requests.get(f'{rest_api.API_URL}/leer_tabla/{nombre_tabla}/{limite}')
    return respuesta.json()

#LEER TODOS LOS REGISTROS DE UNA TABLA QUE CUMPLAN UNA CONDICION
def leer_tabla_filtrada(nombre_tabla, condicion):
    respuesta = requests.get(f'{rest_api.API_URL}/leer_tabla_filtrada/{nombre_tabla}/{condicion}')
    return respuesta.json()

#LEER DE CUALQUIER TABLA UN REGISTRO EN PARTICULAR
def leer_registro(nombre_tabla, id_registro):
    respuesta = requests.get(f'{rest_api.API_URL}/leer_registro/{nombre_tabla}/{id_registro}')
    return respuesta.json()

#ACTUALIZAR UN REGISTRO
def modificar_usuario(id_registro, nombre, clave, fecha_nacimiento, genero, rol):
    body = {
            "id_registro" : id_registro,
            "nombre": nombre,
            "clave": clave,
            "fecha_nacimiento": fecha_nacimiento,
            "genero": genero,
            "rol": rol}
    nombre_tabla = 'usuarios'
    respuesta = requests.put(f'{rest_api.API_URL}/modificar_registro/{nombre_tabla}/{id_registro}', json=body)
    return respuesta.status_code == 200

def modificar_actividad(id_registro, tipo, valor, realizada, intensidad):
    body = {
            "id_registro": id_registro,
            "tipo": tipo,
            "valor": valor,
            "realizada": realizada,
            "intensidad": intensidad}
    nombre_tabla = 'actividades'
    respuesta = requests.put(f'{rest_api.API_URL}/modificar_registro/{nombre_tabla}/{id_registro}', json=body)
    return respuesta.status_code == 200

def modificar_rol(id_registro, rol):
    body = {
            "id_registro" : id_registro,
            "rol": rol}
    nombre_tabla = 'roles'
    respuesta = requests.put(f'{rest_api.API_URL}/modificar_registro/{nombre_tabla}/{id_registro}', json=body)
    return respuesta.status_code == 200

def modificar_tarjeta_de_humor(id_registro, fecha_actual, valor, promedio):
    body = {
            "id_registro" : id_registro,
            "fecha_actual": fecha_actual,
            "valor": valor,
            "promedio": promedio}
    nombre_tabla = 'tarjetas_de_humor'
    respuesta = requests.put(f'{rest_api.API_URL}/modificar_registro/{nombre_tabla}/{id_registro}', json=body)
    return respuesta.status_code == 200

#BORRAR UNA TABLA COMPLETAMENTE
def borrar_tabla(nombre_tabla):
    respuesta = requests.delete(f'{rest_api.API_URL}/borrar_tabla/{nombre_tabla}')
    return respuesta.status_code == 200

#BORRAR DE CUALQUIER TABLA UN REGISTRO EN PARTICULAR
def borrar_registro(nombre_tabla, id_registro):
    respuesta = requests.delete(f'{rest_api.API_URL}/borrar_registro/{nombre_tabla}/{id_registro}')
    return respuesta.status_code == 200

#OBTENER CANTIDAD DE REGISTROS
def obtener_cantidad_de_registros(nombre_tabla):
    respuesta = requests.get(f'{rest_api.API_URL}/contar_registros/{nombre_tabla}')
    return respuesta.json()

#OBTENER CANTIDAD DE REGISTROS QUE CUMPLAN UNA DETERMINADA CONDICIÓN
def obtener_cantidad_de_registros_filtrados(nombre_tabla, condicion):
    respuesta = requests.get(f'{rest_api.API_URL}/contar_registros/{nombre_tabla}/{condicion}')
    return respuesta.json()

#ORDENAR REGISTROS
def ordenar_registros(nombre_tabla, campo_de_ordenacion, tipo):
    respuesta = requests.get(f'{rest_api.API_URL}/ordenar_registros/{nombre_tabla}/{campo_de_ordenacion}/{tipo}')
    return respuesta.json()

#ORDENAR REGISTROS QUE CUMPLAN UNA DETERMINADA CONDICIÓN
def ordenar_registros_filtrados(nombre_tabla, campo_de_ordenacion, tipo, condicion):
    respuesta = requests.get(f'{rest_api.API_URL}/ordenar_registros/{nombre_tabla}/{campo_de_ordenacion}/{tipo}/{condicion}')
    return respuesta.json()



