from datos.modelos import sesiones_modelo as modelo_sesiones
from datos.modelos import crud_modelo as modelo_crud
from datetime import datetime


#LOGIN
def login(nombre, clave):
    if _existe_usuario(nombre, clave):
        usuario = modelo_crud.obtener_usuario_por_nombre_y_clave(nombre, clave)[0]
        return _crear_sesion(usuario['ID_USUARIO'])
    else:
        raise Exception("El usuario no existe o la clave es invalida")


#SESIONES
def _crear_sesion(id_usuario):
    hora_actual = datetime.now()
    dt_string = hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    return modelo_sesiones.crear_sesion(id_usuario, dt_string)



def validar_sesion_por_id(id_sesion):
    sesion = modelo_sesiones.obtener_sesion_por_id(id_sesion)
    if len(sesion) == 0:
        print('No hay una sesión activa para este usuario')
        return False
    elif (datetime.now() - datetime.strptime(sesion[0]['FECHA_HORA'], "%d/%m/%Y %H:%M:%S")).total_seconds() > 3600:
        # Sesion expirada
        print('Hubo una sesión activa pero está expirada')
        return False
    else:
        print('Hay una sesión activa para este usuario')
        return True

def obtener_sesiones():
    return modelo_sesiones.obtener_sesiones()


def _existe_usuario(nombre, clave):
    usuarios = modelo_crud.obtener_usuario_por_nombre_y_clave(nombre, clave)
    return not len(usuarios) == 0


