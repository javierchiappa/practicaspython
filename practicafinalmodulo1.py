#Practica integradora modulo1
#por Javier Chiappa

import math
import random

matrizdef = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

matrizatac = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

reactoratac = 40
sincarga = 0
sinescudos = 0

print("-----------------------------------")
print("Bienvenidos a Batalla Naval Espacial")
print("-----------------------------------")

def muestratablero():


    print("    1 2 3 4")
    print("    -------")
    n = 0
    for row in matrizdef:
        n = n+1
        print(n,"|",' '.join(map(str, row)))



def muestratableroatac():


    print("    1 2 3 4")
    print("    -------")
    n = 0
    for row in matrizatac:
        n = n+1
        print(n,"|",' '.join(map(str, row)))


def posicionanave():
    print("Para empezar, posicionemos tu nave nodriza")
    x = input("Indica donde vas a poner modulo delantero en X: ")
    x = int(x) #transformamos a entero
    x = x - 1 #corregimos que pyton empieza matrices en 0
    y = input("Indica donde vas a poner modulo delantero en Y: ")
    y = int(y)
    y = y - 1
    power = input("indica la potencia del escudo (1 al 9): ")
    power = int(power)
    matrizdef[y][x] = power
    muestratablero()
    valido = 0
    while(valido==0):
        print("Ahora vamos a posicionar el modulo central")
        print("Indica donde vas a poner modulo central: ")
        ubicacion = input("1) Arriba 2) Abajo 3) Izquierda 4)Derecha ")
        ubicacion = int(ubicacion)
        if (ubicacion==1):
           if(y>=3):
               y = y - 1
               valido=1
           else:
               print("no va entrar toda tu nave aqui, prueba nuevamente")
               valido = 0

        elif (ubicacion==2):
            if(y<=2):
                y = y + 1
                valido=1
            else:
                print("no va entrar toda tu nave aqui, prueba nuevamente")
                valido = 0

        elif (ubicacion==3):
            if (x >= 3):
                x = x - 1
                valido = 1
            else:
                print("no va entrar toda tu nave aqui, prueba nuevamente")
                valido = 0

        elif (ubicacion==4):

            if (x <= 1):#antes era 2 bug?
                x = x + 1
                valido = 1
            else:
                print("no va entrar toda tu nave aqui, prueba nuevamente")
                valido = 0

        else:
            print("Solo numeros del 1 al 4")

    power = input("indica la potencia del escudo (1 al 9): ")
    power = int(power)
    matrizdef[y][x] = power
    muestratablero()

    print("Ahora vamos a posicionar el modulo final")
    power = input("indica la potencia del escudo (1 al 9): ")
    power = int(power)
    if (ubicacion==1):
        y = y - 1
    elif (ubicacion==2):
        y = y + 1
    elif (ubicacion==3):
        x = x - 1
    elif (ubicacion==4):
        x = x + 1

    matrizdef[y][x] = power
    print("-----------------------------------")
    print("Tu nave ya esta posicionada correctamente!")
    print("-----------------------------------")
    muestratablero()




def posicionaatacante():
    print("-----------------------------------")
    print("Ahora vamos a posicionar la nave del atacante!")
    print("-----------------------------------")
    x = 0 #limpiamos todas las variables
    y = 0
    power = 0
    direccion = 0
    ubicacion = 0
    valido = 0
    seedmia = input("Dame un valor al azar! : ")
    seedmia = float(seedmia)
    random.seed(seedmia)


    x = random.randint(1, 4)
    x = int(x)
    print("Valor de x: ",x)
    seedmia = seedmia+3 #sacado con un dado magico, sin hacer trampa
    random.seed(seedmia) #ahora el seed es distinto debe dar otro valor el random
    y = random.randint(1, 4)
    y = int(y)
    print("Valor de y: ", y)
    power = random.randint(1, 9)
    power = int(power)
    print("Valor de power: ", power)
    matrizatac[y][x] = power
    muestratableroatac()
    seedmia = seedmia + 2.34  # sacado con un dado magico, sin hacer trampa
    random.seed(seedmia)  # ahora el seed es distinto debe dar otro valor el random
    ubicacion = random.randint(1, 4)

    while(valido==0):
        print("Ahora vamos a posicionar el modulo central")
        print("1) Arriba 2) Abajo 3) Izquierda 4)Derecha ")
        print(ubicacion)

        if (ubicacion==1):
           if(y>=3):
               y = y - 1
               valido=1
           else:
               print("no va entrar toda tu nave aqui, prueba nuevamente")
               if (ubicacion<4):
                   ubicacion = ubicacion + 1
               else:
                   ubicacion = 1
               valido = 0

        elif (ubicacion==2):
            if(y<=2):
                y = y + 1
                valido=1
            else:
                print("no va entrar toda tu nave aqui, prueba nuevamente")
                if (ubicacion < 4):
                    ubicacion = ubicacion + 1
                else:
                    ubicacion = 1
                valido = 0

        elif (ubicacion==3):
            if (x >= 3):
                x = x - 1
                valido = 1
            else:
                print("no va entrar toda tu nave aqui, prueba nuevamente")
                if (ubicacion < 4):
                    ubicacion = ubicacion + 1
                else:
                    ubicacion = 1
                valido = 0

        elif (ubicacion==4):
            if (x <= 1):
                x = x + 1
                valido = 1
            else:
                print("no va entrar toda tu nave aqui, prueba nuevamente")
                if (ubicacion < 4):
                    ubicacion = ubicacion + 1
                else:
                    ubicacion = 1
                valido = 0

    print("valor de x:",x)
    print("valor de y:",y)

    power = power = random.randint(1, 9)
    matrizatac[y][x] = power
    muestratableroatac()

    print("Ahora vamos a posicionar el modulo final")

    power = power = random.randint(1, 9)
    print("power: ",power)

    if (ubicacion==1):
        y = y - 1
    elif (ubicacion==2):
        y = y + 1
    elif (ubicacion==3):
        x = x - 1
    elif (ubicacion==4):
        x = x + 1

    matrizatac[y][x] = power
    muestratableroatac()


def iniciaataque():
    print("-----------------------------------")
    print("Todo listo, comienza el ataque!")
    print("-----------------------------------")
    valido = 0
    destruido = 0
    while(valido==0 or sincarga==0 or sinescudos==0):
        x = input("Indica donde vas a disparar en X: ")
        x = int(x)  # transformamos a entero
        x = x - 1  # corregimos que pyton empieza matrices en 0
        y = input("Indica donde vas a disparar en Y: ")
        y = int(y)
        y = y - 1
        power = input("indica la carga de protones (1 al 9): ")
        power = int(power)

        print("Haciendo disparo en x: ",x,"y: ",y,"potencia: ",power)
        print("El valor del escudo en esta posicion es de:",matrizatac[y][x])
        escudo = matrizatac[y][x]
        escudo = int (escudo)
        if ((escudo>=power) and (escudo!=0)):
            matrizatac[y][x] = matrizatac[y][x] - power
            print ("El disparo fue efectivo")
            mostrarescudoatac()
            if ((matrizatac[y][x]) == 0):
                print("El modulo fue Destruido!")
                destruido = destruido + 1
                if (destruido==3):
                    print("Felicitaciones, nave enemiga destruida")
                    break
        elif ((matrizatac[y][x])==0):
            print("No hay nada aqui!")
        else:
            print("El escudo es muy alto para esta carga")
            mostrarescudoatac()

        atacaelenemigo() #turno terminado, ahora le toca al otro


def atacaelenemigo():
    global reactoratac
    global sincarga
    print("-------------------------------------")
    print("Capitan, Recibimos un ataque enemigo!")
    print("-------------------------------------")
    x = 0
    y = 0
    power = 0
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    power = random.randint(1, 9)


    if (reactoratac>power):
        reactoratac = reactoratac - power
    else:
        print("Sin carga en Reactor de Protones del Atacante, Ganaste!")
        sincarga = 1


    print("Recibimos un ataque en X: ",(x+1)," Y: ",(y+1),"con una potencia de: ",power)
    print("El reactor del atacante es de: ",reactoratac)
    if (matrizdef[y][x] != 0):
        print("El valor de nuestro escudo en esta posicion es de:", matrizdef[y][x])
        if (power<=matrizdef[y][x]):
            print("El disparo es efectivo")
            matrizdef[y][x] = matrizdef[y][x] - power

            if (matrizdef[y][x]<=0):
                print("Nuestro Modulo fue destruido!")
                print(mostrarescudodef())
            else:
                print("Ahora el escudo tiene un valor de: ",matrizdef[y][x])
                print(mostrarescudodef())
            if (matrizdef[y][x]==0):
                print ("El modulo fue destruido!")
                print(mostrarescudodef())
        else:
            print("El disparo no es efectivo")
            print(mostrarescudodef())
    else:
        print("Por suerte no habia nada alli")



def mostrarescudodef():

    sumatoria = 0
    for y in range(len(matrizdef)):
        for x in range(len(matrizdef[y])):
            sumatoria = sumatoria + matrizdef[y][x]
    if (sumatoria<=0):
        print("Perdiste, la nave no tiene mas escudos!")
        #sinescudos=1

    print("Escudos Restantes de la Nave: ",sumatoria)


def mostrarescudoatac():

    sumatoria = 0
    for y in range(len(matrizatac)):
        for x in range(len(matrizatac[y])):
            sumatoria = sumatoria + matrizatac[y][x]
    print("Escudos Restantes de la Nave: ",sumatoria)


muestratablero()
posicionanave()
posicionaatacante()
iniciaataque()

if (sincarga==1):
    print("Ganaste porque el enemigo se quedo sin carga de protones!")
if (sinescudos==1):
    print("Perdiste porque te quedaste sin escudos!")


