from flask import Flask, request, redirect, url_for
from flask import render_template
from web.servicios import autenticacion_web, crud_web

app = Flask("servidorWeb")


@app.route('/')
def inicio():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/espacioPersonal')
def espacioPersonal():
    return render_template('espacioPersonal.html')


@app.route('/actividades')
def actividades():
    return render_template('actividades.html')


@app.route('/actividadesMentales')
def actividadesMentales():
    return render_template('actividadesMentales.html')


@app.route('/yoga')
def yoga():
    return render_template('yoga.html')

@app.route('/meditacion')
def meditacion():
    return render_template('meditacion.html')

@app.route('/respiracion')
def respiracion():
    return render_template('respiracion.html')

@app.route('/sudokus')
def sudokus():
    return render_template('sudokus.html')

@app.route('/puzzles')
def puzzles():
    return render_template('puzzles.html')

@app.route('/lectura')
def lectura():
    return render_template('lectura.html')


@app.route('/actividadesFisicas')
def actividadesFisicas():
    return render_template('actividadesFisicas.html')

@app.route('/correr')
def correr():
    return render_template('correr.html')

@app.route('/gimnasio')
def gimnasio():
    return render_template('gimnasio.html')

@app.route('/natacion')
def natacion():
    return render_template('natacion.html')

@app.route('/escalada')
def escalada():
    return render_template('escalada.html')

@app.route('/ciclismo')
def ciclismo():
    return render_template('ciclismo.html')

@app.route('/futbol')
def futbol():
    return render_template('futbol.html')


@app.route('/actividadesRecreativas')
def actividadesRecreativas():
    return render_template('actividadesRecreativas.html')

@app.route('/bailar')
def bailar():
    return render_template('bailar.html')

@app.route('/asado')
def asado():
    return render_template('asado.html')

@app.route('/rambla')
def rambla():
    return render_template('rambla.html')

@app.route('/shopping')
def shopping():
    return render_template('shopping.html')

@app.route('/cine')
def cine():
    return render_template('cine.html')

@app.route('/picnic')
def picnic():
    return render_template('picnic.html')


@app.route('/enfermedades')
def enfermedades():
    return render_template('enfermedades.html')

@app.route('/trastornoNeurodesarrollo')
def trastornoNeurodesarrollo():
    return render_template('trastornoNeurodesarrollo.html')

@app.route('/esquizofreniaYpsicoticos')
def esquizofreniaYpsicoticos():
    return render_template('esquizofreniaYpsicoticos.html')

@app.route('/bipolar')
def bipolar():
    return render_template('bipolar.html')

@app.route('/depresion')
def depresion():
    return render_template('depresion.html')

@app.route('/ansiedad')
def ansiedad():
    return render_template('ansiedad.html')

@app.route('/obsesivoCompulsivo')
def obsesivoCompulsivo():
    return render_template('obsesivoCompulsivo.html')


@app.route('/sobreCuentaConmigo')
def sobreCuentaConmigo():
    return render_template('sobreCuentaConmigo.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not autenticacion_web.validar_credenciales(request.form['login'], request.form['password']):
            error = 'Credenciales inválidas'
        else:
            return redirect(url_for('inicio'))
    return render_template('iniciarSesion.html', error=error)


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    error = None
    if request.method == 'POST':
        if not autenticacion_web.crear_usuario(request.form['login'], request.form['password']):
            error = 'No se pudo crear el usuario'
        else:
            return redirect(url_for('/'))
    return render_template('formulario.html', error=error)





############################################################CRUD ENDPOINTS#########################################
#CREAR REGISTRO
@app.route('/crear_usuario', methods=['GET', 'POST'])
def crear_usuario():
    error = None
    if request.method == 'POST':
        if not crud_web.crear_usuario(request.form['nombre'], request.form['clave'], request.form['fecha_nacimiento'], request.form['genero'], request.form['rol']):
            error = 'No se pudo crear el usuario'
        else:
            return redirect(url_for('index'))
    return render_template('formulario.html', error=error)


@app.route('/crear_actividad', methods=['GET', 'POST'])
def crear_actividad():
    error = None
    if request.method == 'POST':
        if not crud_web.crear_actividad(request.form['tipo'], request.form['valor'], request.form['realizada'], request.form['intensidad']):
            error = 'No se pudo crear la actividad'
        else:
            return redirect(url_for('index'))
    return render_template('crear_actividad.html', error=error)


@app.route('/crear_rol', methods=['GET', 'POST'])
def crear_rol():
    error = None
    if request.method == 'POST':
        if not crud_web.crear_rol(request.form['rol']):
            error = 'No se pudo crear el rol'
        else:
            return redirect(url_for('index'))
    return render_template('crear_rol.html', error=error)


@app.route('/crear_tarjeta_de_humor', methods=['GET', 'POST'])
def crear_tarjeta_de_humor():
    error = None
    if request.method == 'POST':
        if not crud_web.crear_tarjeta_de_humor(request.form['fecha_actual'], request.form['valor'], request.form['promedio']):
            error = 'No se pudo crear la tarjeta de humor'
        else:
            return redirect(url_for('index'))
    return render_template('crear_tarjeta_de_humor.html', error=error)


#LEER DE USUARIOS TODOS LOS REGISTROS
@app.route('/leer_usuarios', methods=['GET', 'POST'])
def leer_usuarios():
    registros = crud_web.leer_tabla("usuarios")
    return render_template('mostrar_datos_usuarios.html', registros=registros)

#LEER DE ACTIVIDADES TODOS LOS REGISTROS
@app.route('/leer_actividades', methods=['GET', 'POST'])
def leer_actividades():
    registros = crud_web.leer_tabla("actividades")
    return render_template('mostrar_datos_actividades.html', registros=registros)

#LEER DE ROLES TODOS LOS REGISTROS
@app.route('/leer_roles', methods=['GET', 'POST'])
def leer_roles():
    registros = crud_web.leer_tabla("roles")
    return render_template('mostrar_datos_roles.html', registros=registros)

#LEER DE TARJETAS DE HUMOR TODOS LOS REGISTROS
@app.route('/leer_tarjetas_de_humor', methods=['GET', 'POST'])
def leer_tarjetas_de_humor():
    registros = crud_web.leer_tabla("tarjetas_de_humor")
    return render_template('mostrar_datos_tarjetas.html', registros=registros)


#LEER DE CUALQUIER TABLA TODOS LOS REGISTROS CON LIMITE
@app.route('/leer_tabla/<nombre_tabla>/<limite>', methods=['GET'])
def leer_tabla_con_limite(nombre_tabla, limite):
    datos = crud_web.leer_tabla_con_limite(nombre_tabla, limite)
    return render_template('mostrar_datos.html', tabla=datos)


#LEER TODOS LOS REGISTROS DE UNA TABLA QUE CUMPLAN UNA CONDICION
@app.route('/leer_tabla_filtrada/<nombre_tabla>/<condicion>', methods=['GET'])
def leer_tabla_filtrada(nombre_tabla, condicion):
    datos = crud_web.leer_tabla_filtrada(nombre_tabla, condicion)
    return render_template('mostrar_datos.html', tabla=datos)


#LEER DE CUALQUIER TABLA UN REGISTRO EN PARTICULAR
@app.route('/leer_registro/<nombre_tabla>/<id_registro>', methods=['GET'])
def leer_registro(nombre_tabla, id_registro):
    datos = crud_web.leer_registro(nombre_tabla, id_registro)
    return render_template('mostrar_datos.html', tabla=datos)


#ACTUALIZAR UN REGISTRO
@app.route('/modificar_usuario', methods=['GET', 'POST'])
def modificar_usuario():
    error = None
    if request.method == 'POST':
        if not crud_web.modificar_usuario(request.form['id_registro'], request.form['nombre'], request.form['clave'], request.form['fecha_nacimiento'], request.form['genero'], request.form['rol']):
            error = 'No se pudo modificar el usuario'
        else:
            return redirect(url_for('index'))
    return render_template('modificar_usuario.html', error=error)

@app.route('/modificar_actividad', methods=['GET', 'POST'])
def modificar_actividad():
    error = None
    if request.method == 'POST':
        if not crud_web.modificar_actividad(request.form['id_registro'], request.form['tipo'], request.form['valor'], request.form['realizada'], request.form['intensidad']):
            error = 'No se pudo modificar la actividad'
        else:
            return redirect(url_for('index'))
    return render_template('modificar_actividad.html', error=error)

@app.route('/modificar_rol', methods=['GET', 'POST'])
def modificar_rol():
    error = None
    if request.method == 'POST':
        if not crud_web.modificar_rol(request.form['id_registro'], request.form['rol']):
            error = 'No se pudo modificar el rol'
        else:
            return redirect(url_for('index'))
    return render_template('modificar_rol.html', error=error)


@app.route('/modificar_tarjeta_de_humor', methods=['GET', 'POST'])
def modificar_tarjeta_de_humor():
    error = None
    if request.method == 'POST':
        if not crud_web.modificar_tarjeta_de_humor(request.form['id_registro'], request.form['fecha_actual'], request.form['valor'], request.form['promedio']):
            error = 'No se pudo modificar la tarjeta de humor'
        else:
            return redirect(url_for('index'))
    return render_template('modificar_tarjeta_de_humor.html', error=error)


#BORRAR UNA TABLA COMPLETAMENTE
@app.route('/borrar_tabla', methods=['GET', 'POST'])
def borrar_tabla():
    error = None
    if request.method == 'POST':
        if not crud_web.borrar_tabla(request.form['tablas']):
            error = 'No se pudo borrar la tabla'
        else:
            return redirect(url_for('index'))
    return render_template('borrar_tabla.html', error=error)


#BORRAR DE CUALQUIER TABLA UN REGISTRO EN PARTICULAR
@app.route('/borrar_registro', methods=['GET', 'POST'])
def borrar_registro():
    error = None
    if request.method == 'POST':
        if not crud_web.borrar_registro(request.form['tablas'], request.form['id_registro']):
            error = 'No se pudo borrar el registro'
        else:

            return redirect(url_for('index'))
    return render_template('borrar_registro.html', error=error)


#OBTENER CANTIDAD DE REGISTROS
@app.route('/contar_registros/<nombre_tabla>', methods=['GET'])
def obtener_cantidad_de_registros(nombre_tabla):
    datos = crud_web.obtener_cantidad_de_registros(nombre_tabla)
    return render_template('mostrar_datos.html', tabla=datos)


#OBTENER CANTIDAD DE REGISTROS QUE CUMPLAN UNA DETERMINADA CONDICIÓN
@app.route('/contar_registros/<nombre_tabla>/<condicion>', methods=['GET'])
def obtener_cantidad_de_registros_filtrados(nombre_tabla, condicion):
    datos = crud_web.obtener_cantidad_de_registros_filtrados(nombre_tabla, condicion)
    return render_template('mostrar_datos.html', tabla=datos)


#ORDENAR REGISTROS
@app.route('/ordenar_registros/<nombre_tabla>/<campo_de_ordenacion>/<tipo>', methods=['GET'])
def ordenar_registros(nombre_tabla, campo_de_ordenacion, tipo):
    datos = crud_web.ordenar_registros(nombre_tabla, campo_de_ordenacion, tipo)
    return render_template('mostrar_datos.html', tabla=datos)


# ORDENAR REGISTROS QUE CUMPLAN UNA DETERMINADA CONDICIÓN
@app.route('/ordenar_registros/<nombre_tabla>/<campo_de_ordenacion>/<tipo>/<condicion>', methods=['GET'])
def ordenar_registros_filtrados(nombre_tabla, campo_de_ordenacion, tipo, condicion):
    datos = crud_web.ordenar_registros_filtrados(nombre_tabla, campo_de_ordenacion, tipo, condicion)
    return render_template('mostrar_datos.html', tabla=datos)


#sesiones
@app.route('/validar_sesion_por_id/<id_sesion>', methods=['GET'])
def validar_sesion_por_id(id_sesion):
    autenticacion_web.validar_credenciales(id_sesion)
    return redirect(url_for('confirmacion'))


@app.route('/obtener_sesiones', methods=['GET'])
def obtener_sesiones():
    datos = autenticacion_web.obtener_sesiones()
    return render_template('mostrar_datos.html', tabla=datos)


if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
