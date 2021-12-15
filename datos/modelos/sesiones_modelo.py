#SESIONES
from datos.base_de_datos import BaseDeDatos

def crear_sesion(id_usuario, dt_string):
    crear_sesion_sql = f"""
        INSERT INTO SESIONES(ID_USUARIO, FECHA_HORA)
        VALUES ('{id_usuario}','{dt_string}')
    """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(crear_sesion_sql, True)


def obtener_sesion_por_id(id_sesion):
    obtener_sesion_sql_por_id = f"""
        SELECT ID_SESIONES, ID_USUARIO, FECHA_HORA FROM SESIONES WHERE ID_SESIONES = '{id_sesion}'
    """
    bd = BaseDeDatos()
    return [{"ID_SESIONES": registro[0],
             "ID_USUARIO": registro[1],
             "FECHA_HORA": registro[2]}
            for registro in bd.ejecutar_sql(obtener_sesion_sql_por_id)]


def obtener_sesiones():
    obtener_sesiones_sql = f"""
        SELECT ID_SESIONES, ID_USUARIO, FECHA_HORA FROM SESIONES 
    """
    bd = BaseDeDatos()
    return [{"ID_SESIONES": registro[0],
             "ID_USUARIO": registro[1],
             "FECHA_HORA": registro[2]}
            for registro in bd.ejecutar_sql(obtener_sesiones_sql)]
