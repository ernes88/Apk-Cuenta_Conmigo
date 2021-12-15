from datos.base_de_datos import BaseDeDatos

#CREAR REGISTRO
def crear_registro(nombre_tabla, datos_registro):
    validar_registro(nombre_tabla, datos_registro)
    bd = BaseDeDatos()
    crear_registro_sql=None

    if nombre_tabla == 'usuarios':
        if 'nombre' not in datos_registro or datos_registro['nombre'] == '':
            return 'El nombre de usuario es requerido', 412
        if 'clave' not in datos_registro:
            return 'La clave es requerida', 412

        crear_registro_sql = f"""
            INSERT INTO USUARIOS(NOMBRE, CLAVE, FECHA_NACIMIENTO, GENERO, ROL)
            VALUES ('{datos_registro["nombre"]}','{datos_registro["clave"]}',
            '{datos_registro["fecha_nacimiento"]}','{datos_registro["genero"]}',
            '{datos_registro["rol"]}')
         """

    elif nombre_tabla == 'actividades':
        if 'tipo' not in datos_registro or datos_registro['tipo'] == '':
            return 'El tipo de actividad es requerida', 412
        if 'valor' not in datos_registro:
            return 'El valor dado para la actividad es requerida', 412

        crear_registro_sql = f"""
            INSERT INTO ACTIVIDADES(TIPO, VALOR, REALIZADA, INTENSIDAD)
            VALUES ('{datos_registro["tipo"]}','{datos_registro["valor"]}',
            '{datos_registro["realizada"]}','{datos_registro["intensidad"]}')
         """

    elif nombre_tabla == 'roles':
        if 'rol' not in datos_registro or datos_registro['rol'] == '':
            return 'El rol es requerido', 412

        crear_registro_sql = f"""
            INSERT INTO ROLES(ROL)
            VALUES ('{datos_registro["rol"]}')
         """

    elif nombre_tabla == 'tarjetas_de_humor':
        if 'promedio' not in datos_registro or datos_registro['promedio'] == '':
            return 'El promedio es requerido', 412
        if 'valor' not in datos_registro:
            return 'El valor es requerido', 412

        crear_registro_sql = f"""
            INSERT INTO TARJETAS_DE_HUMOR(FECHA_ACTUAL, VALOR, PROMEDIO)
            VALUES ('{datos_registro["fecha_actual"]}','{datos_registro["valor"]}',
            '{datos_registro["promedio"]}')
         """
    bd.ejecutar_sql(crear_registro_sql)



def crear_usuario(nombre, clave, fecha_nacimiento, genero, rol):
    crear_usuario_sql = f"""
        INSERT INTO USUARIOS(NOMBRE, CLAVE, FECHA_NACIMIENTO, GENERO, ROL)
        VALUES ('{nombre}','{clave}','{fecha_nacimiento}','{genero}','{rol}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)

def crear_actividad(tipo, valor, realizada, intensidad):
    crear_actvidad_sql = f"""
        INSERT INTO ACTIVIDADES(TIPO, VALOR, REALIZADA, INTENSIDAD)
        VALUES ('{tipo}','{valor}','{realizada}','{intensidad}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_actvidad_sql)


def crear_rol(rol):
    crear_rol_sql = f"""
        INSERT INTO ROLES(ROL)
        VALUES('{rol}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_rol_sql)

def crear_tarjeta_de_humor(fecha_actual, valor, promedio):
    crear_tarjeta_de_humor_sql = f"""
        INSERT INTO TARJETAS_DE_HUMOR(FECHA_ACTUAL, VALOR, PROMEDIO)
        VALUES ('{fecha_actual}','{valor}','{promedio}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_tarjeta_de_humor_sql)


def validar_registro(nombre_tabla, datos_registro):
    if nombre_tabla == 'usuarios':
        obtener_usuario_por_nombre_y_clave(datos_registro['nombre'], datos_registro['clave'])
    elif nombre_tabla == 'actividades':
        obtener_actividad_por_tipo_y_valor(datos_registro['tipo'], datos_registro['valor'])
    elif nombre_tabla == 'roles':
        obtener_rol(datos_registro['rol'])
    elif nombre_tabla == 'tarjetas_de_humor':
        obtener_tarjeta_de_humor_por_valor_y_promedio(datos_registro['valor'], datos_registro['promedio'])



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


def obtener_actividad_por_tipo_y_valor(tipo, valor):
    obtener_actividad_por_tipo_y_valor_sql = f"""
        SELECT ID_ACTIVIDADES, TIPO, VALOR FROM ACTIVIDADES 
        WHERE TIPO='{tipo}' and VALOR='{valor}'  
    """
    bd = BaseDeDatos()
    return [{"ID_ACTIVIDADES": registro[0],
             "TIPO": registro[1],
             "VALOR": registro[2]
             } for registro in bd.ejecutar_sql(obtener_actividad_por_tipo_y_valor_sql)]


def obtener_rol(rol):
    obtener_rol_sql = f"""
        SELECT ID_ROLES, ROL FROM ROLES 
        WHERE ROL='{rol}'  
    """
    bd = BaseDeDatos()
    return [{"ID_ROLES": registro[0],
             "ROL": registro[1],
             } for registro in bd.ejecutar_sql(obtener_rol_sql)]


def obtener_tarjeta_de_humor_por_valor_y_promedio(valor, promedio):
    obtener_tarjeta_de_humor_por_valor_y_promedio_sql = f"""
        SELECT ID_TARJETAS_DE_HUMOR, VALOR, PROMEDIO FROM TARJETAS_DE_HUMOR 
        WHERE VALOR='{valor}' and PROMEDIO='{promedio}'  
    """
    bd = BaseDeDatos()
    return [{"ID_TARJETAS_DE_HUMOR": registro[0],
             "VALOR": registro[1],
             "PROMEDIO": registro[2]
             } for registro in bd.ejecutar_sql(obtener_tarjeta_de_humor_por_valor_y_promedio_sql)]


def leer_tabla(nombre_tabla):
    bd = BaseDeDatos()
    if nombre_tabla == 'usuarios':
        leer_tabla_sql = f"""
            SELECT ID_USUARIO, NOMBRE, CLAVE, FECHA_NACIMIENTO, GENERO, ROL FROM USUARIOS 
         """
        return [{"ID_USUARIO": registro[0],
             "NOMBRE": registro[1],
             "CLAVE": registro[2],
             "FECHA_NACIMIENTO": registro[3],
             "GENERO": registro[4],
             "ROL": registro[5]
             } for registro in bd.ejecutar_sql(leer_tabla_sql)]

    elif nombre_tabla == 'actividades':
        leer_tabla_sql = f"""
            SELECT ID_ACTIVIDADES, TIPO, VALOR, REALIZADA, INTENSIDAD FROM ACTIVIDADES 
        """
        return [{"ID_ACTIVIDADES": registro[0],
             "TIPO": registro[1],
             "VALOR": registro[2],
             "REALIZADA": registro[3],
             "INTENSIDAD": registro[4]
            } for registro in bd.ejecutar_sql(leer_tabla_sql)]

    elif nombre_tabla == 'roles':
        leer_tabla_sql = f"""
            SELECT ID_ROLES, ROL FROM ROLES
        """
        return [{"ID_ROLES": registro[0],
               "ROL": registro[1]
               }for registro in bd.ejecutar_sql(leer_tabla_sql)]

    elif nombre_tabla == 'tarjetas_de_humor':
        leer_tabla_sql = f"""
            SELECT ID_TARJETAS_DE_HUMOR, FECHA_ACTUAL, VALOR, PROMEDIO FROM TARJETAS_DE_HUMOR 
        """
        return [{"ID_TARJETAS_DE_HUMOR": registro[0],
                 "FECHA_ACTUAL": registro[1],
                 "VALOR": registro[2],
                 "PROMEDIO": registro[3]
                 } for registro in bd.ejecutar_sql(leer_tabla_sql)]




#LEER TABLA CON LIMITE
def leer_tabla_con_limite(nombre_tabla, limite):
    bd = BaseDeDatos()
    if nombre_tabla == 'usuarios':
        leer_tabla_sql = f"""
            SELECT ID_USUARIO, NOMBRE, CLAVE, FECHA_NACIMIENTO, GENERO, ROL FROM USUARIOS LIMIT {limite}
         """
        return [{"ID_USUARIO": registro[0],
             "NOMBRE": registro[1],
             "CLAVE": registro[2],
             "FECHA_NACIMIENTO": registro[3],
             "GENERO": registro[4],
             "ROL": registro[5]
             } for registro in bd.ejecutar_sql(leer_tabla_sql)]

    elif nombre_tabla == 'actividades':
        leer_tabla_sql = f"""
            SELECT ID_ACTIVIDADES, TIPO, VALOR, REALIZADA, INTENSIDAD FROM ACTIVIDADES LIMIT {limite}
        """
        return [{"ID_ACTIVIDADES": registro[0],
             "TIPO": registro[1],
             "VALOR": registro[2],
             "REALIZADA": registro[3],
             "INTENSIDAD": registro[4]
            } for registro in bd.ejecutar_sql(leer_tabla_sql)]

    elif nombre_tabla == 'roles':
        leer_tabla_sql = f"""
            SELECT ID_ROLES, ROL FROM ROLES LIMIT {limite}
        """
        return [{"ID_ROLES": registro[0],
               "ROL": registro[1]
               }for registro in bd.ejecutar_sql(leer_tabla_sql)]

    elif nombre_tabla == 'tarjetas_de_humor':
        leer_tabla_sql = f"""
            SELECT ID_TARJETAS_DE_HUMOR, FECHA_ACTUAL, VALOR, PROMEDIO FROM TARJETAS_DE_HUMOR LIMIT {limite}
        """
        return [{"ID_TARJETAS_DE_HUMOR": registro[0],
                 "FECHA_ACTUAL": registro[1],
                 "VALOR": registro[2],
                 "PROMEDIO": registro[3]
                 } for registro in bd.ejecutar_sql(leer_tabla_sql)]


#LEER TODOS LOS REGISTROS DE UNA TABLA QUE CUMPLAN UNA CONDICION
def leer_tabla_filtrada(nombre_tabla, condicion):
    bd = BaseDeDatos()
    if nombre_tabla == 'usuarios':
        leer_tabla_sql = f"""
                SELECT ID_USUARIO, NOMBRE, CLAVE, FECHA_NACIMIENTO, GENERO, ROL FROM USUARIOS WHERE {condicion}
             """
        return [{"ID_USUARIO": registro[0],
                 "NOMBRE": registro[1],
                 "CLAVE": registro[2],
                 "FECHA_NACIMIENTO": registro[3],
                 "GENERO": registro[4],
                 "ROL": registro[5]
                 } for registro in bd.ejecutar_sql(leer_tabla_sql)]

    elif nombre_tabla == 'actividades':
        leer_tabla_sql = f"""
                SELECT ID_ACTIVIDADES, TIPO, VALOR, REALIZADA, INTENSIDAD FROM ACTIVIDADES WHERE {condicion}
            """
        return [{"ID_ACTIVIDADES": registro[0],
                 "TIPO": registro[1],
                 "VALOR": registro[2],
                 "REALIZADA": registro[3],
                 "INTENSIDAD": registro[4]
                 } for registro in bd.ejecutar_sql(leer_tabla_sql)]

    elif nombre_tabla == 'roles':
        leer_tabla_sql = f"""
                SELECT ID_ROLES, ROL FROM ROLES WHERE {condicion}
            """
        return [{"ID_ROLES": registro[0],
                 "ROL": registro[1]
                 } for registro in bd.ejecutar_sql(leer_tabla_sql)]

    elif nombre_tabla == 'tarjetas_de_humor':
        leer_tabla_sql = f"""
                SELECT ID_TARJETAS_DE_HUMOR, FECHA_ACTUAL, VALOR, PROMEDIO FROM TARJETAS_DE_HUMOR WHERE {condicion}
            """
        return [{"ID_TARJETAS_DE_HUMOR": registro[0],
                 "FECHA_ACTUAL": registro[1],
                 "VALOR": registro[2],
                 "PROMEDIO": registro[3]
                 } for registro in bd.ejecutar_sql(leer_tabla_sql)]


#LEER REGISTRO
def leer_registro(nombre_tabla, id_registro):
    bd = BaseDeDatos()
    if nombre_tabla == 'usuarios':
        leer_tabla_sql = f"""
            SELECT ID_USUARIO, NOMBRE, CLAVE, FECHA_NACIMIENTO, GENERO, ROL FROM USUARIOS
            WHERE ID_USUARIO = {id_registro}
        """
        return [{"ID_USUARIO": registro[0],
                 "NOMBRE": registro[1],
                 "CLAVE": registro[2],
                 "FECHA_NACIMIENTO": registro[3],
                 "GENERO": registro[4],
                 "ROL": registro[5]
                 } for registro in bd.ejecutar_sql(leer_tabla_sql)]

    elif nombre_tabla == 'actividades':
        leer_tabla_sql = f"""
            SELECT ID_ACTIVIDADES, TIPO, VALOR, REALIZADA, INTENSIDAD FROM ACTIVIDADES
            WHERE ID_ACTIVIDADES = {id_registro}
        """
        return [{"ID_ACTIVIDADES": registro[0],
                 "TIPO": registro[1],
                 "VALOR": registro[2],
                 "REALIZADA": registro[3],
                 "INTENSIDAD": registro[4]
                 } for registro in bd.ejecutar_sql(leer_tabla_sql)]

    elif nombre_tabla == 'roles':
        leer_tabla_sql = f"""
            SELECT ID_ROLES, ROL FROM ROLES
            WHERE ID_ROLES = {id_registro}
        """
        return [{"ID_ROLES": registro[0],
                 "ROL": registro[1]
                 } for registro in bd.ejecutar_sql(leer_tabla_sql)]

    elif nombre_tabla == 'tarjetas_de_humor':
        leer_tabla_sql = f"""
            SELECT ID_TARJETAS_DE_HUMOR, FECHA_ACTUAL, VALOR, PROMEDIO FROM TARJETAS_DE_HUMOR
            WHERE ID_TARJETAS_DE_HUMOR = {id_registro}
        """
        return [{"ID_TARJETAS_DE_HUMOR": registro[0],
                 "FECHA_ACTUAL": registro[1],
                 "VALOR": registro[2],
                 "PROMEDIO": registro[3]
                 } for registro in bd.ejecutar_sql(leer_tabla_sql)]



#ACTUALIZAR REGISTRO
def modificar_registro(nombre_tabla, id_registro, datos_registro):
    bd = BaseDeDatos()
    modificar_registro_sql=None

    if nombre_tabla == 'usuarios':
        if 'nombre' not in datos_registro or datos_registro['nombre'] == '':
            return 'El nombre de usuario es requerido', 412
        if 'clave' not in datos_registro:
            return 'La clave es requerida', 412

        modificar_registro_sql = f"""
            UPDATE USUARIOS
            SET NOMBRE='{datos_registro["nombre"]}', 
                CLAVE='{datos_registro["clave"]}', 
                FECHA_NACIMIENTO='{datos_registro["fecha_nacimiento"]}', 
                GENERO='{datos_registro["genero"]}', 
                ROL='{datos_registro["rol"]}'
            WHERE ID_USUARIO='{id_registro}'
        """
    elif nombre_tabla == 'actividades':
        if 'tipo' not in datos_registro or datos_registro['tipo'] == '':
            return 'El tipo de actividad es requerida', 412
        if 'valor' not in datos_registro:
            return 'El valor dado para la actividad es requerida', 412

        modificar_registro_sql = f"""
            UPDATE ACTIVIDADES
            SET TIPO='{datos_registro["tipo"]}', 
                VALOR='{datos_registro["valor"]}', 
                REALIZADA='{datos_registro["realizada"]}', 
                INTENSIDAD='{datos_registro["intensidad"]}' 
            WHERE ID_ACTIVIDADES='{id_registro}'
        """
    elif nombre_tabla == 'roles':
        if 'rol' not in datos_registro or datos_registro['rol'] == '':
            return 'El rol es requerido', 412

        modificar_registro_sql = f"""
            UPDATE ROLES
            SET ROL='{datos_registro["rol"]}' 
            WHERE ID_ROLES='{id_registro}'
        """

    elif nombre_tabla == 'tarjetas_de_humor':
        if 'promedio' not in datos_registro or datos_registro['promedio'] == '':
            return 'El promedio es requerido', 412
        if 'valor' not in datos_registro:
            return 'El valor es requerido', 412

        modificar_registro_sql = f"""
            UPDATE TARJETAS_DE_HUMOR
            SET FECHA_ACTUAL='{datos_registro["fecha_actual"]}', 
            VALOR='{datos_registro["valor"]}', 
            PROMEDIO='{datos_registro["promedio"]}' 
            WHERE ID_TARJETAS_DE_HUMOR='{id_registro}'
        """
    bd.ejecutar_sql(modificar_registro_sql)


#BORRAR TABLA
def borrar_tabla(nombre_tabla):
    bd = BaseDeDatos()
    borrar_tabla_sql = f"""
        DELETE FROM {nombre_tabla} 
    """
    bd.ejecutar_sql(borrar_tabla_sql)


#BORRAR REGISTRO
def borrar_registro(nombre_tabla, id_registro):
    bd = BaseDeDatos()
    borrar_registro_sql=None

    if nombre_tabla == 'usuarios':
        borrar_registro_sql = f"""
            DELETE
            FROM USUARIOS 
            WHERE ID_USUARIO = {id_registro}
        """
    elif nombre_tabla == 'actividades':
        borrar_registro_sql = f"""
            DELETE
            FROM ACTIVIDADES 
            WHERE ID_ACTIVIDADES = {id_registro}
        """
    elif nombre_tabla == 'roles':
        borrar_registro_sql = f"""
            DELETE
            FROM ROLES 
            WHERE ID_ROLES = {id_registro}
        """
    elif nombre_tabla == 'tarjetas_de_humor':
        borrar_registro_sql = f"""
            DELETE
            FROM TARJETAS_DE_HUMOR 
            WHERE ID_TARJETAS_DE_HUMOR = {id_registro}
        """
    bd.ejecutar_sql(borrar_registro_sql)


#CONTAR REGISTROS
def contar_registros(nombre_tabla):
    bd = BaseDeDatos()
    obtener_cantidad_de_registros_sql = f"""
        SELECT COUNT(*) FROM {nombre_tabla}
    """
    return [{"CANTIDAD_DE_REGISTROS:": registro[0],
             } for registro in bd.ejecutar_sql(obtener_cantidad_de_registros_sql)]



#CONTAR REGISTROS FILTRADOS
def contar_registros_filtrados(nombre_tabla, condicion):
    bd = BaseDeDatos()
    obtener_cantidad_de_registros_filtrados_sql = f"""
        SELECT COUNT(*) FROM {nombre_tabla} WHERE {condicion}
    """
    return [{"CANTIDAD_DE_REGISTROS:": registro[0],
             } for registro in bd.ejecutar_sql(obtener_cantidad_de_registros_filtrados_sql)]



#ORDENAR REGISTROS
def ordenar_registros(nombre_tabla, campo_de_ordenacion, tipo):
    bd = BaseDeDatos()
    if nombre_tabla == 'usuarios':
        ordenar_registros_sql = f"""
            SELECT ID_USUARIO, NOMBRE, CLAVE, FECHA_NACIMIENTO, GENERO, ROL FROM USUARIOS
            ORDER BY {campo_de_ordenacion} {tipo}
        """
        return [{"ID_USUARIO": registro[0],
             "NOMBRE": registro[1],
             "CLAVE": registro[2],
             "FECHA_NACIMIENTO": registro[3],
             "GENERO": registro[4],
             "ROL": registro[5]
             } for registro in bd.ejecutar_sql(ordenar_registros_sql)]

    elif nombre_tabla == 'actividades':
        ordenar_registros_sql = f"""
            SELECT ID_ACTIVIDADES, TIPO, VALOR, REALIZADA, INTENSIDAD FROM ACTIVIDADES
            ORDER BY {campo_de_ordenacion} {tipo}
        """

        return [{"ID_ACTIVIDADES": registro[0],
             "TIPO": registro[1],
             "VALOR": registro[2],
             "REALIZADA": registro[3],
             "INTENSIDAD": registro[4]
            } for registro in bd.ejecutar_sql(ordenar_registros_sql)]

    elif nombre_tabla == 'roles':
        ordenar_registros_sql = f"""
            SELECT ID_ROLES, ROL FROM ROLES ORDER BY {campo_de_ordenacion} {tipo}
        """
        return [{"ID_ROLES": registro[0],
               "ROL": registro[1]
               }for registro in bd.ejecutar_sql(ordenar_registros_sql)]

    elif nombre_tabla == 'tarjetas_de_humor':
        ordenar_registros_sql = f"""
            SELECT ID_TARJETAS_DE_HUMOR, FECHA_ACTUAL, VALOR, PROMEDIO FROM TARJETAS_DE_HUMOR
            ORDER BY {campo_de_ordenacion} {tipo}
        """

        return [{"ID_TARJETAS_DE_HUMOR": registro[0],
                 "FECHA_ACTUAL": registro[1],
                 "VALOR": registro[2],
                 "PROMEDIO": registro[3]
                 } for registro in bd.ejecutar_sql(ordenar_registros_sql)]



#ORDENAR REGISTROS FILTRADOS
def ordenar_registros_filtrados(nombre_tabla, campo_de_ordenacion, tipo, condicion):
    bd = BaseDeDatos()
    if nombre_tabla == 'usuarios':
        ordenar_registros_filtrados_sql = f"""
            SELECT ID_USUARIO, NOMBRE, CLAVE, FECHA_NACIMIENTO, GENERO, ROL FROM USUARIOS
            WHERE {condicion} ORDER BY {campo_de_ordenacion} {tipo} 
        """
        return [{"ID_USUARIO": registro[0],
             "NOMBRE": registro[1],
             "CLAVE": registro[2],
             "FECHA_NACIMIENTO": registro[3],
             "GENERO": registro[4],
             "ROL": registro[5]
             } for registro in bd.ejecutar_sql(ordenar_registros_filtrados_sql)]

    elif nombre_tabla == 'actividades':
        ordenar_registros_filtrados_sql = f"""
            SELECT ID_ACTIVIDADES, TIPO, VALOR, REALIZADA, INTENSIDAD FROM ACTIVIDADES
            WHERE {condicion} ORDER BY {campo_de_ordenacion} {tipo} 
        """

        return [{"ID_ACTIVIDADES": registro[0],
             "TIPO": registro[1],
             "VALOR": registro[2],
             "REALIZADA": registro[3],
             "INTENSIDAD": registro[4]
            } for registro in bd.ejecutar_sql(ordenar_registros_filtrados_sql)]

    elif nombre_tabla == 'roles':
        ordenar_registros_filtrados_sql = f"""
            SELECT ID_ROLES, ROL FROM ROLES 
            WHERE {condicion} ORDER BY {campo_de_ordenacion} {tipo} 
        """
        return [{"ID_ROLES": registro[0],
               "ROL": registro[1]
               }for registro in bd.ejecutar_sql(ordenar_registros_filtrados_sql)]

    elif nombre_tabla == 'tarjetas_de_humor':
        ordenar_registros_filtrados_sql = f"""
            SELECT ID_TARJETAS_DE_HUMOR, FECHA_ACTUAL, VALOR, PROMEDIO FROM TARJETAS_DE_HUMOR
            WHERE {condicion} ORDER BY {campo_de_ordenacion} {tipo} 
        """

        return [{"ID_TARJETAS_DE_HUMOR": registro[0],
                 "FECHA_ACTUAL": registro[1],
                 "VALOR": registro[2],
                 "PROMEDIO": registro[3]
                 } for registro in bd.ejecutar_sql(ordenar_registros_filtrados_sql)]


