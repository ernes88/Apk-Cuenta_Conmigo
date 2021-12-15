from datos.base_de_datos import BaseDeDatos

#CREATE
def crear_actividad(tipo, valor, realizada, intensidad):
    crear_actvidad_sql = f"""
        INSERT INTO ACTIVIDADES(TIPO, VALOR, REALIZADA, INTENSIDAD)
        VALUES ('{tipo}','{valor}','{realizada}','{intensidad}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_actvidad_sql)

#READ
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

#READ
def obtener_actividades():
    obtener_actividades_sql = f"""
            SELECT ID_ACTIVIDADES, TIPO, VALOR, REALIZADA, INTENSIDAD FROM ACTIVIDADES
        """
    bd = BaseDeDatos()
    return [{"ID_ACTIVIDADES": registro[0],
             "TIPO": registro[1],
             "VALOR": registro[2],
             "REALIZADA": registro[3],
             "INTENSIDAD": registro[4]
             } for registro in bd.ejecutar_sql(obtener_actividades_sql)]
