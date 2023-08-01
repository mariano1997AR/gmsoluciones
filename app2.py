from flask import Flask, render_template
import conectar
host = "localhost"
user="root"
password = "marianokpo22"
database = "prueba"

mydb = conectar.conectar(host,user,password,database)
mycursor = mydb.cursor()
#mycursor.execute("SHOW DATABASES")
#conectar.crearDB(mycursor)
conectar.verTablas(mycursor)
conectar.modificarTabla(mycursor)

app = Flask(__name__)
#programacion funcional
@app.route('/')
def index():
    mensaje = "Bienvenidos a trainningWebApp"
    lista = "Lista de elementos"
    titulo = "trainningWebApp"
    cursor =  ["mariano","andres","manuel"]
    return render_template('index.html',mensaje = mensaje,titulo=titulo,lista=lista,cursor = cursor)

@app.route('/ListaDB')
def noticias(): 
    listaPersonas =  ["mariano","andres","manuel"]
    listaDB = mycursor
    return render_template('noticias.html',listaPersonas = listaPersonas,listaDB = listaDB)

'''

input -> ingrese n de tarjeta
fecha -> xxx                
n seguridad -> 

api -> datos = datosingresas 
           ok -> datos.cuenta - pagar 
           retornar el total de lo que tiene 
           -> api informar

--> mensaje ghdfvsg

'''



if __name__ == '__main__':
    app.run(debug=True)