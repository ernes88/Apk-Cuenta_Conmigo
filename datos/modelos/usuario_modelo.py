from datos.base_de_datos import BaseDeDatos

#CREATE
def crear_usuario(nombre, clave, fecha_nacimiento, genero, rol):
    crear_usuario_sql = f"""
        INSERT INTO USUARIOS(NOMBRE, CLAVE, FECHA_NACIMIENTO, GENERO, ROL)
        VALUES ('{nombre}','{clave}','{fecha_nacimiento}','{genero}','{rol}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)

#READ
def obtener_usuarios():
    obtener_usuarios_sql = f"""
        SELECT ID_USUARIO, NOMBRE, CLAVE, FECHA_NACIMIENTO, GENERO, ROL FROM USUARIOS
    """
    bd = BaseDeDatos()
    return [{"ID_USUARIO": registro[0],
             "NOMBRE": registro[1],
             "CLAVE": registro[2],
             "FECHA_NACIMIENTO": registro[3],
             "GENERO": registro[4],
             "ROL": registro[5]
             } for registro in bd.ejecutar_sql(obtener_usuarios_sql)]

def obtener_usuario(id_usuario):
    obtener_usuario_sql = f"""
        SELECT ID_USUARIO, NOMBRE, CLAVE, FECHA_NACIMIENTO, GENERO, ROL FROM USUARIOS
        WHERE ID_USUARIO = {id_usuario}
    """
    bd = BaseDeDatos()
    return [{"ID_USUARIO": registro[0],
             "NOMBRE": registro[1],
             "CLAVE": registro[2],
             "FECHA_NACIMIENTO": registro[3],
             "GENERO": registro[4],
             "ROL": registro[5]
             } for registro in bd.ejecutar_sql(obtener_usuario_sql)]


def obtener_usuario_por_nombre_y_clave(nombre, clave):
    obtener_usuario_por_nombre_y_clave_sql = f"""
            SELECT ID_USUARIO, NOMBRE, CLAVE FROM USUARIOS 
            WHERE NOMBRE='{nombre}' and CLAVE='{clave}'  
        """
    bd = BaseDeDatos()
    return [{"ID_USUARIO": registro[0],
             "NOMBRE": registro[1],
             "CLAVE": registro[2]
             } for registro in bd.ejecutar_sql(obtener_usuario_por_nombre_y_clave_sql)]


#UPDATE
def modificar_usuario(id_usuario, datos_usuario):
    modificar_usuario_sql = f"""
        UPDATE USUARIOS
        SET NOMBRE='{datos_usuario["nombre"]}', 
            CLAVE='{datos_usuario["clave"]}', 
            FECHA_NACIMIENTO='{datos_usuario["fecha_nacimiento"]}', 
            GENERO='{datos_usuario["genero"]}', 
            ROL='{datos_usuario["rol"]}'
        WHERE ID_USUARIO='{id_usuario}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_usuario_sql)


#DELETE
def borrar_usuario(id_usuario):
    borrar_usuario_sql = f"""
        DELETE
        FROM USUARIOS 
        WHERE ID_USUARIO = {id_usuario}
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(borrar_usuario_sql)


#OBTENER CANTIDAD DE USUARIOS
def obtener_cantidad_de_usuarios():
    obtener_cantidad_de_usuarios_sql = f"""
        SELECT COUNT(*) FROM USUARIOS
    """
    bd = BaseDeDatos()
    return [{"CANTIDAD_DE_USUARIOS:": registro[0],
             } for registro in bd.ejecutar_sql(obtener_cantidad_de_usuarios_sql)]


#OBTENER USUARIO POR CUALQUIER CAMPO QUE NO SEA EL ID PARA EL CUAL YA EXISTE
def obtener_usuarios_por_campo(campo_usuario, valor_campo):
    if campo_usuario == "nombre":
        obtener_usuario_sql = f"""
            SELECT ID_USUARIO, NOMBRE, CLAVE, FECHA_NACIMIENTO, GENERO, ROL FROM USUARIOS
            WHERE NOMBRE = '{valor_campo}'
        """
    elif campo_usuario == "clave":
        obtener_usuario_sql = f"""
            SELECT ID_USUARIO, NOMBRE, CLAVE, FECHA_NACIMIENTO, GENERO, ROL FROM USUARIOS
            WHERE CLAVE = '{valor_campo}'
        """
    elif campo_usuario == "fecha_nacimiento":
        obtener_usuario_sql = f"""
            SELECT ID_USUARIO, NOMBRE, CLAVE, FECHA_NACIMIENTO, GENERO, ROL FROM USUARIOS
            WHERE FECHA_NACIMIENTO = '{valor_campo}'
        """
    elif campo_usuario == "genero":
        obtener_usuario_sql = f"""
            SELECT ID_USUARIO, NOMBRE, CLAVE, FECHA_NACIMIENTO, GENERO, ROL FROM USUARIOS
            WHERE GENERO = '{valor_campo}'
        """
    elif campo_usuario == "rol":
        obtener_usuario_sql = f"""
            SELECT ID_USUARIO, NOMBRE, CLAVE, FECHA_NACIMIENTO, GENERO, ROL FROM USUARIOS
            WHERE ROL = '{valor_campo}'
        """

    bd = BaseDeDatos()
    return [{"ID_USUARIO": registro[0],
             "NOMBRE": registro[1],
             "CLAVE": registro[2],
             "FECHA_NACIMIENTO": registro[3],
             "GENERO": registro[4],
             "ROL": registro[5]
             } for registro in bd.ejecutar_sql(obtener_usuario_sql)]


#OBTENER DATOS DE UN CAMPO
def obtener_datos_de_un_campo(campo):
    obtener_datos_de_un_campo_sql = f"""
            SELECT '{campo}' FROM USUARIOS
        """
    bd = BaseDeDatos()
    return [{campo: registro[0],
             } for registro in bd.ejecutar_sql(obtener_datos_de_un_campo_sql)]


#SESIONES
def crear_sesion(id_usuario, dt_string):
    print("modelo")
    """
    crear_sesion_sql = f"""
     #   INSERT INTO SESIONES(ID_USUARIO, FECHA_HORA)
     #   VALUES ('{id_usuario}','{dt_string}')
    """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(crear_sesion_sql, True)  #Parámetro True devuelve el id del registro insertado
    """
    return "hola"

def obtener_sesion(id_sesion):
    obtener_sesion_sql = f"""
        SELECT ID, ID_USUARIO, FECHA_HORA FROM SESIONES WHERE ID = {id_sesion}
    """
    bd = BaseDeDatos()
    return [{"id": registro[0],
             "id_usuario": registro[1],
             "fecha_hora": registro[2]}
            for registro in bd.ejecutar_sql(obtener_sesion_sql)]