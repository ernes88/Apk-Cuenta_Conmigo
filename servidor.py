from flask import Flask, request, jsonify
from servicios.autenticacion import autenticacion_servicio
from servicios.crud import crud_servicio
from flask import render_template

app = Flask("servidor")


#################################################CRUD ENDPOINTS#########################################
#CREAR REGISTRO
@app.route('/crear_registro/<nombre_tabla>', methods=['POST'])
def crear_registro(nombre_tabla):
    datos_registro = request.get_json()
    if nombre_tabla == "usuarios":
        if 'nombre' not in datos_registro or datos_registro['nombre'] == '':
            return 'El nombre de usuario es requerido', 412
        if 'clave' not in datos_registro:
            return 'La clave es requerida', 412
        try:
            crud_servicio.crear_usuario(datos_registro['nombre'], datos_registro['clave'],
                                        datos_registro['fecha_nacimiento'], datos_registro['genero'],
                                        datos_registro['rol'])
        except Exception:
            return 'El usuario ya existe', 412
        return 'Usuario creado correctamente', 200

    elif nombre_tabla == "actividades":
        if 'tipo' not in datos_registro or datos_registro['tipo'] == '':
            return 'El tipo de actividad es requerida', 412
        if 'valor' not in datos_registro:
            return 'El valor dado para la actividad es requerida', 412
        try:
            crud_servicio.crear_actividad(datos_registro['tipo'], datos_registro['valor'],
                                          datos_registro['realizada'], datos_registro['intensidad'])
        except Exception:
            return 'La actividad ya existe', 412
        return 'Actividad creada correctamente', 200

    elif nombre_tabla == "roles":
        if 'rol' not in datos_registro or datos_registro['rol'] == '':
            return 'El rol es requerido', 412
        try:
            crud_servicio.crear_rol(datos_registro['rol'])
        except Exception:
            return 'El rol ya existe', 412
        return 'Rol creado correctamente', 200

    elif nombre_tabla == "tarjetas_de_humor":
        if 'promedio' not in datos_registro or datos_registro['promedio'] == '':
            return 'El promedio es requerido', 412
        if 'valor' not in datos_registro:
            return 'El valor es requerido', 412
        try:
            crud_servicio.crear_tarjeta_de_humor(datos_registro['fecha_actual'], datos_registro['valor'],
                                                 datos_registro['promedio'])
        except Exception:
            return 'La tarjeta de humor ya existe', 412
        return 'Tarjeta de humor creada correctamente', 200


#LEER DE CUALQUIER TABLA TODOS LOS REGISTROS
@app.route('/leer_tabla/<nombre_tabla>', methods=['GET'])
def leer_tabla(nombre_tabla):
    try:
        return jsonify(crud_servicio.leer_tabla(nombre_tabla))
    except Exception:
        return 'Datos no encontrados', 404


#LEER DE UNA TABLA UN NÚMERO DETERMINADO DE REGISTROS
@app.route('/leer_tabla/<nombre_tabla>/<limite>', methods=['GET'])
def leer_tabla_con_limite(nombre_tabla, limite):
    try:
        return jsonify(crud_servicio.leer_tabla_con_limite(nombre_tabla, limite))
    except Exception:
        return 'Datos no encontrados', 404


#LEER TODOS LOS REGISTROS DE UNA TABLA QUE CUMPLAN UNA CONDICION
@app.route('/leer_tabla_filtrada/<nombre_tabla>/<condicion>', methods=['GET'])
def leer_tabla_filtrada(nombre_tabla, condicion):
    try:
        return jsonify(crud_servicio.leer_tabla_filtrada(nombre_tabla, condicion))
    except Exception:
        return 'Datos no encontrados', 404

#LEER DE CUALQUIER TABLA UN REGISTRO EN PARTICULAR
@app.route('/leer_registro/<nombre_tabla>/<id_registro>', methods=['GET'])
def leer_registro(nombre_tabla, id_registro):
    try:
        return jsonify(crud_servicio.leer_registro(nombre_tabla, id_registro))
    except Exception:
        return 'Registro no encontrado', 404


#ACTUALIZAR UN REGISTRO
@app.route('/modificar_registro/<nombre_tabla>/<id_registro>', methods=['PUT'])
def modificar_registro(nombre_tabla, id_registro):
    datos_registro = request.get_json()
    try:
        crud_servicio.modificar_registro(nombre_tabla, id_registro, datos_registro)
    except Exception:
        return 'El registro ya existe', 412
    return 'Registro modificado correctamente', 200


#BORRAR UNA TABLA COMPLETAMENTE
@app.route('/borrar_tabla/<nombre_tabla>', methods=['DELETE'])
def borrar_tabla(nombre_tabla):
    crud_servicio.borrar_tabla(nombre_tabla)
    return "Tabla borrada correctamente", 200


#BORRAR DE CUALQUIER TABLA UN REGISTRO EN PARTICULAR
@app.route('/borrar_registro/<nombre_tabla>/<id_registro>', methods=['DELETE'])
def borrar_registro(nombre_tabla, id_registro):
    crud_servicio.borrar_registro(nombre_tabla, id_registro)
    return "Registro borrado correctamente", 200


#OBTENER CANTIDAD DE REGISTROS
@app.route('/contar_registros/<nombre_tabla>', methods=['GET'])
def obtener_cantidad_de_registros(nombre_tabla):
    try:
        return jsonify(crud_servicio.contar_registros(nombre_tabla))
    except Exception:
        return 'Registros no contados', 404


#OBTENER CANTIDAD DE REGISTROS QUE CUMPLAN UNA DETERMINADA CONDICIÓN
@app.route('/contar_registros/<nombre_tabla>/<condicion>', methods=['GET'])
def obtener_cantidad_de_registros_filtrados(nombre_tabla, condicion):
    try:
        return jsonify(crud_servicio.contar_registros_filtrados(nombre_tabla, condicion))
    except Exception:
        return 'Registros no contados', 404



#ORDENAR REGISTROS
@app.route('/ordenar_registros/<nombre_tabla>/<campo_de_ordenacion>/<tipo>', methods=['GET'])
def ordenar_registros(nombre_tabla, campo_de_ordenacion, tipo):
    try:
        return jsonify(crud_servicio.ordenar_registros(nombre_tabla, campo_de_ordenacion, tipo))
    except Exception:
        return 'Registros no ordenados', 404


#ORDENAR REGISTROS QUE CUMPLAN UNA DETERMINADA CONDICIÓN
@app.route('/ordenar_registros/<nombre_tabla>/<campo_de_ordenacion>/<tipo>/<condicion>', methods=['GET'])
def ordenar_registros_filtrados(nombre_tabla, campo_de_ordenacion, tipo, condicion):
    try:
        return jsonify(crud_servicio.ordenar_registros_filtrados(nombre_tabla, campo_de_ordenacion, tipo, condicion))
    except Exception:
        return 'Registros no ordenados', 404


#login
@app.route('/login', methods=['POST'])
def login():
    datos_usuario = request.get_json()
    if 'nombre' not in datos_usuario:
        return 'El nombre de usuario es requerido', 412
    if 'clave' not in datos_usuario:
        return 'La clave es requerida', 412
    try:
        id_sesion = autenticacion_servicio.login(datos_usuario['nombre'], datos_usuario['clave'])
        return jsonify({"id_sesion": id_sesion})
    except Exception:
        return 'Usuario no encontrado', 404


#sesiones
@app.route('/validar_sesion_por_id/<id_sesion>', methods=['GET'])
def validar_sesion_por_id(id_sesion):
    try:
        if (autenticacion_servicio.validar_sesion_por_id(id_sesion)):
            return jsonify('Sesión activa')
        else:
            return jsonify('sesión inactiva')
    except Exception:
        return 'Datos no encontrados', 404


@app.route('/obtener_sesiones', methods=['GET'])
def obtener_sesiones():
    try:
        return jsonify(autenticacion_servicio.obtener_sesiones())
    except Exception:
        return 'Datos no encontrados', 404


#PÁGINA DE BIENVENIDA
@app.route('/')
def get_index():
    titulo_cuenta_conmigo = 'Cuenta conmigo'
    return render_template('index.html', titulo=titulo_cuenta_conmigo)


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
