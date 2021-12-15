import requests
from web.servicios import rest_api


def validar_credenciales(login, password):
    body = {"nombre": login,
            "clave": password}
    respuesta = requests.post(f'{rest_api.API_URL}/login', json=body)
    return respuesta.status_code == 200


def crear_usuario(usuario, clave):
    body = {"nombre": usuario,
            "clave": clave}
    respuesta = requests.post(f'{rest_api.API_URL}/usuarios', json=body)
    return respuesta.status_code == 200


def obtener_usuarios():
    respuesta = requests.get(f'{rest_api.API_URL}/usuarios')
    return respuesta.json()


def obtener_sesiones():
    respuesta = requests.get(f'{rest_api.API_URL}/obtener_sesiones')
    return respuesta.json()