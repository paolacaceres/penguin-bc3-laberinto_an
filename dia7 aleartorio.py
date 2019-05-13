#creamos un archivo 
#guardamos en la carpeta de repositorio
#con la extencion 
#uso de los numeros aleartorios
from random import randint
aleartorio=randint(0,20)   #creamos una variable y generamos un numero generado
print(aleartorio)          #imprimimos el numero generado

#creamos un archivo 
#guardamos en la carpeta de repositorio
#con la extencion 
#uso de los numeros aleartorios

#ejercicios:
"""
escribir una funcion sorteo() que recibo
una lista de participantes,y elegir a uno
de los partipantes aleartoriamente y 
retornar esa persona elegida 
"""
#desafio:
"""
no volver a retornar una persona
ya sorteada
"""


"""
lista_parII=["lau","silvi","chuba","david"]
lista=[]
def sorteo_compu (lista_par):
    ganador=lista_par[randint(0,4)]
    lista.append(ganador)
    return lista 
part=sorteo_compu(lista_parII)
print(part)
"""
from random import randint
def sorteo_compu(lista): #definimos una funcion 
    #utilizamos len() para saber la cantidad de la persona
    #para que no salga del rango
    cant=len(lista) -1
    indice=randint(0,cant) #generamos un indice aleartorio
    #seleccionamos un elemento de la lista 
    #y guardamos en la variable ganador
    ganador=lista[indice] 
    return ganador #esto se ejecuta
    print(ganador)
    #creamos una lista de los participantes
participantes=["lau","chua","david","silvani"]
    #llamamos a la funcion y guardamos en una variable
    #el resultado retornamos por la funecion 
ganar=sorteo_compu(participantes)
print(ganar)  #imprimimos el gandor





