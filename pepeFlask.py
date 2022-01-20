from flask import Flask,request,render_template,session
import pymongo#pip install pymongo
#tambien instalar dnspython (pip install dnspython)
import certifi #pip install certifi
ca = certifi.where()
conexion = pymongo.MongoClient("mongodb+srv://RafaSamSilv:th3mong0eldeB@cluster0.np198.mongodb.net"+
"/prueba?retryWrites=true&w=majority",tlsCAFile=ca)
baseDatos=conexion.prueba
coleccion=baseDatos.coleccion1
aplicacion=Flask(__name__)

aplicacion.secret_key = 'claveSecreta'
@aplicacion.route('/generaSesion')
def Generasesion():
    session['prueba']='hola'
    return 'se genero sesion'

@aplicacion.route('/verSesion')
def vervarsesion():
    return session['prueba']


@aplicacion.route('/')
def bienvenida():
    return 'Bienvenido a la pagina'

@aplicacion.route('/insertaDatos')
def muestraFormInserta():
    return render_template('inserta.html')

@aplicacion.route('/recibeDatosInserta',methods=['POST'])
def recibeDatosaInsertar():
    usuario=request.form.get('elusuario')
    clave=request.form.get('elpass')
    coleccion.insert_one({'usuario':usuario,
    'laClave':clave})
    return f'{usuario}-{clave} registro agregado correctamente'

@aplicacion.route('/login')
def muestraFormLogin():
    return render_template('el_login.html')

@aplicacion.route('/verificaUser',methods=['POST'])
def recibeDatosVerificaUser():
    usuario=request.form.get('elusuario')
    clave=request.form.get('elpass')
    resultados=coleccion.find({'nombre2':usuario,'apellido':clave})
    total=0
    for resultado in resultados:
        total+=1
    if total>0:
        return 'datos validos'
    else:
        return 'datos erroneos'

@aplicacion.route('/miercoles')
def elMiercoles():
    return 'tercer dia habil de la semana'

@aplicacion.route('/python')
def muestraPython():
    return 'es un lenguaje de programacion'

@aplicacion.route('/palabra')
def muestraPalabra():
    definicion=request.args.get('concepto')
    respuesta=''
    if definicion=='byte':
        respuesta='equivale a 8 bits'
    elif definicion=='bit':
        respuesta='''unidad minima de
        informacion equivale a 0 o 1'''
    elif definicion=='perro':
        respuesta='un buen amigo del hombre'
    else:
        respuesta='palabra no hallada'
    return respuesta


if __name__ == '__main__':
    aplicacion.run(host='0.0.0.0',port='8010',
    debug=True )
