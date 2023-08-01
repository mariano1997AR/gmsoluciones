from flask import Flask,render_template,request

app = Flask(__name__)
#creamos la estructura 
estructura = {"GM soluciones","Servicios","Contacto"}
lista = list(estructura)
lista1 = lista

# codigo del servidor 
@app.route('/')
def index():
    return render_template('index.html',lista1=lista1)

@app.route('/servicios')
def servicios():
    return render_template('servicios.html',lista1=lista1)

@app.route('/contacto',methods=['GET','POST'])
def contacto():
    if request.method == 'POST':
        #procesar los datos enviados por el formulario
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        respuesta_mensaje = f"Hola {nombre}, has enviado los datos"
        return render_template('respuesta.html', respuesta_mensaje = respuesta_mensaje)
    return render_template('contacto.html',lista1=lista1)

if __name__ == '__main__':
    app.run(debug=True,port=4000)