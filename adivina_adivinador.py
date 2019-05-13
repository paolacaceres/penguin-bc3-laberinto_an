#juego de adivina el numero,todos juntos
#adivinar un numero generado aleartorio
#ir introdunccion por el teclado el dato adivinar 

from random import randint
generado=randint(0,10)  #generando el numero aleartorio 
print(generado)#trampa
condicion=True
intento=10
while condicion:
    if intento>0:
        numero=input("dame un numero del o al 10")
        intento=intento-1
        if generado==int(numero):
            print("ganaste una hambuergueza que paga lore")
            condicion=False
        else:
            print("el perdedor compra una pizza a lore")
            print("te quedan",intento,"intentos")
        else:
            condicion=False
            print("perdiste")