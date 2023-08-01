'''
fdfs
fsdfsd
fdsf

'''
x = 10 #espacio en memoria 
x = 3.434
x = "fdfsdfsnsdjfsd"
#listas
#estructura de datos -> lista pila etc diccionarios conjuntos tuplas

lista = ["fdfs",1,2,[1,2,3]]
lista.append("mariano")
tupla = (243,43,5)
suma = 3 +5
#0 1 2
print(lista[3][2])
print(3+5)
print(suma)
print(tupla)

#estructura de datos
#listas conjunto 
#funciones
def saludo():
    print("hola")
    
saludo()

def saludo(arg = "Luis"):
    print("hola me llamo " + arg)
    
def listas(lista):
    print(lista)


def sumar(a,b):
    return a + b    


def sumamos():
     suma = sumar(3,4)
     print(suma)
     
lista = [12443,434,343,434]    


saludo()
listas(lista)

#suma = sumar(4,3)
#print(suma)

sumamos()
sumamos()

#estructuras de control





#print(x)
#manejar datos 
f = open("datos.csv","r")
#print(f.readline())

for x in f:
    print(x)