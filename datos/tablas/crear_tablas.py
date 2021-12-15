import sqlite3

sql_tabla_usuarios = '''
CREATE TABLE USUARIOS(
 ID_USUARIO INTEGER PRIMARY KEY,
 NOMBRE TEXT,
 CLAVE TEXT,
 FECHA_NACIMIENTO DATE,
 GENERO TEXT,
 ROL TEXT
)
'''

sql_tabla_roles = '''
CREATE TABLE ROLES(
 ID_ROLES INTEGER PRIMARY KEY,
 ROL TEXT
)
'''

sql_tarjetas_de_humor = '''
CREATE TABLE TARJETAS_DE_HUMOR(
 ID_TARJETAS_DE_HUMOR INTEGER PRIMARY KEY, 
 FECHA_ACTUAL DATE, 
 VALOR INTEGER, 
 PROMEDIO FLOAT
)
'''

sql_tabla_actividades = ''' 
 CREATE TABLE ACTIVIDADES(
 ID_ACTIVIDADES INTEGER PRIMARY KEY, 
 TIPO TEXT, 
 VALOR INTEGER, 
 REALIZADA TEXT, 
 INTENSIDAD TEXT
)
'''

sql_tabla_sesiones = '''
CREATE TABLE SESIONES(
 ID_SESIONES INTEGER PRIMARY KEY,
 ID_USUARIO TEXT,
 FECHA_HORA TEXT,
 FOREIGN KEY(ID_USUARIO) REFERENCES USUARIOS(ID_USUARIO) 
)
'''

sql_tabla_usuarios_tarjetas_de_humor= '''
CREATE TABLE USUARIOS_TARJETAS_DE_HUMOR(
NUMERO_USUARIO INTEGER PRIMARY KEY, 
NUMERO_TARJETA_DE_HUMOR INTEGER, 
FOREIGN KEY(NUMERO_USUARIO) REFERENCES USUARIOS(ID_USUARIO), 
FOREIGN KEY(NUMERO_TARJETA_DE_HUMOR) REFERENCES TARJETAS_DE_HUMOR(ID_TARJETAS_DE_HUMOR)
)
'''

sql_tabla_usuarios_actividades = ''' 
CREATE TABLE USUARIOS_ACTIVIDADES(
NUMERO_USUARIO INTEGER PRIMARY KEY, 
NUMERO_ACTIVIDAD INTEGER, 
FOREIGN KEY(NUMERO_USUARIO) REFERENCES USUARIOS(ID_USUARIO), 
FOREIGN KEY(NUMERO_ACTIVIDAD) REFERENCES ACTIVIDADES(ID_ACTIVIDADES)
)
'''

if __name__ == '__main__':
    try:
        print('Creando Base de datos..')
        conexion = sqlite3.connect('../../Cuenta_Conmigo.v5.db')

        print('Creando Tablas..')
        conexion.execute(sql_tabla_usuarios)
        conexion.execute(sql_tabla_roles)
        conexion.execute(sql_tarjetas_de_humor)
        conexion.execute(sql_tabla_actividades)
        conexion.execute(sql_tabla_sesiones)
        conexion.execute(sql_tabla_usuarios_tarjetas_de_humor)
        conexion.execute(sql_tabla_usuarios_actividades)

        conexion.close()
        print('Creacion Finalizada.')
    except Exception as e:
        print(f'Error creando base de datos: {e}', e)
