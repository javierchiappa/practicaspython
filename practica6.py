

#Programa de Ejercicios Practico 6 por Javier Chiappa
import math
import random

# Asignamos un valor a name para entrar al bucle
name = 'a'
# Bucle principal sale con cero
while name != '0': 
    print("Ejercicios Practico Programacion Numero 6")
    name = input('Que Ejercicio desea ver? (1 al 13), 0 para salir \n')
    print('Opcion Seleccionada, %s!' % name)

    # Ejercicio 1
    if name == '1' :
        print("Consigna: Realizar un procedimiento que permita intercambiar el valor de dos variables")

        def intercambia(listaentrada):
     
            print("El valor de a es: ",listaentrada[2])
            print("El valor de b es: ",listaentrada[1])

        lista = [i for i in range(3)]
        lista[1] = input("Ingrese el valor de a ")
        lista[2] = input("ingrese el valor de b ")
        
        print("Se lo pasamos a la variable intercambia")
        print(intercambia(lista))
        print("Fin de Ejercicio 1")
        
    # Ejercicio 2
    if name == '2' :
        print("Consigna: función no recursiva que permita obtener el término n de la serie de fibonacci.")        
        n = 0
        def fibo(n):
            
            sumatoria = 0
            a = 1
            b = 1
            c = a + b
            count = 0
            for x in range (n-1):
                a = b
                b = c
                c = a + b
            if (n == 1):
                return 1
            if (n == 2):
                return 1
            else:
                return a   

        n = input("Ingrese el valor de n: ")
        n = int(n)
        
        print(fibo(n))


    # Ejercicio 3
    if name == '3' :
        print("Consigna: funcion que permite obtener un numero entre 2 limites")      
        def numero(n,m):
            c = random.randint(n,m)
            return c
            

        n = 0
        m = 0

        n = input("Ingrese el primero valor: ")
        m = input("Ingrese el segundo valor: ")
        n = int (n)
        m = int (m)
        print("El numero entre ellos es: ",numero(n,m))


    # Ejercicio 4
    if name == '4' :
        print("Consigna: obtener el valor absoluto de un número.")      
        def absnumero(n):
            if (n<0):
                n = n*-1

            return n   

        n = 0
        n = input("Ingrese el primero valor: ")
        n = float (n)
        print ("El valor absoluto es: ",absnumero(n))


    # Ejercicio 5
    if name == '5' :
        def division(dividendo,divisor):
            print("dividendo ",dividendo)
            print("divisor: ",divisor)
            #dividendo = dividendo - divisor
            vuelta = 0
            resto = 0
            while (dividendo >= 0):
                    vuelta = vuelta + 1
                    dividendo = dividendo - divisor
                    print("dividendo: ",dividendo)
                    print("vuelta: ",vuelta)
            resto = dividendo + divisor
            vuelta =  vuelta - 1
            return vuelta,resto

        print("Consigna: Division entera y el resto de la misma utilizando resta.")
                
        n = 0
        n = input("Ingrese el dividendo: ")
        n = float (n)
        m = input("Ingrese el divisor: ")
        m = float (m)
        print(division(n,m))

    # Ejercicio 6
    if name == '6' :

        def rad2deg(radians):
            degrees = 180 * radians / math.pi
            return degrees
        
        def deg2rad(degrees):
            radians = math.pi * degrees / 180
            return radians

        def convertir(radio,angulo):
            x = radio * math.cos(angulo)
            y = radio * math.sin(angulo)
            return x,y
    
        print("Consigna: Conversion coordenadas polares")
                
        n = 0
        n = input("Ingrese el radio: ")
        n = float (n)
        m = input("Ingrese el angulo: ")
        m = float (m)
        m = deg2rad(m)
        print(convertir(n,m))

    # Ejercicio 7
    if name == '7' :

        def mcd(num1,num2):
            resto = 0
            while(num2 > 0):
                resto = num2
                num2 = num1 % num2
                num1 = resto
            return num1

        print("Consigna: obtener el máximo común divisor de dos números medianteel algoritmo de Euclides.")  
        n = 0
        n = input("Ingrese primer numero: ")
        n = float (n)
        m = input("Ingrese segundo numero: ")
        m = float (m)
        print("El máximo común divisor de ", n," y ", m," es ", mcd(n, m))


    #Ejercicio 8
    if name == '8' :

        def divisores(number):
            n = 1
            suma = 0
            while(n<number):
                if(number%n==0):
                    print(n)
                    suma = suma + n
                else:
                    pass
                n = n + 1 
            print(number)
            print("Suma :",suma)

        print("Consigna: Suma los divisores de un numero.")  
        n = 0
        n = input("Ingrese numero: ")
        n = int (n)
        divisores(n)

        
    #Ejercicio 9
    if name == '9' :

        def divisores(number):
            n = 1
            suma = 0
            while(n<number):
                if(number%n==0):
                    suma = suma + n
                else:
                    pass
                n = n + 1 
            return suma

        def amigos(n):
            for y in range(n,0,-1):
                valorsuma = divisores(y)
                for x in range(n,0,-1):
                    if ((valorsuma == x) and (divisores(x)==y) and (x!=y)):
                        print("El numero: ",x,"Es amigo de ",y)


        print("Consigna: un algoritmo que muestre todas las parejas de número amigos menores o iguales a m,.")  
        n = 0
        n = input("Ingrese numero: ")
        n = int (n)
        amigos(n)
            
    # Ejercicio 10
    if name == '10' :

        def factorial(a):
            res=1
            x=1
            for x in range(a,0,-1):
                res=x*res           
            return res

        def combinatorio(m,n):

            respuesta=0
            
            respuesta=(factorial(m) /  (factorial(n)*factorial(m-n)))
                                      
            return respuesta
            

        print("Consigna: obtener el numero combinatorio de m sobre n.")  
        n = 0
        m = 0
        m = input("Ingrese primer numero: ")
        m = int (m)
        n = input("Ingrese segundo numero: ")
        n = int (n)
        print("El combinatorio de ", m," y ", n," es ", combinatorio(m, n))
        
    # Ejercicio 11
    if name == '11' :

        def calculasueldos(canthoras,festivo,turno):
            total = 0
            
            if (festivo == 1 or dia != "domingo"): #dia comun
                if(turno==1):
                    total = canthoras * 90
                elif(turno==2):
                    total = canthoras * 125
                
            elif (festivo == 2 or dia == "domingo"): #dia Festivo
                if(turno==1):
                    total = (canthoras * 90) * 1,10
                elif(turno==2):
                    total = (canthoras * 125) * 1,15
                
            else: #otra cosa
                print("Error")
            
            return total
        
        print("Consigna: obtener sueldos empleados")
        nombre = input("Ingrese el nombre del empleado ")
        canthoras = input("Ingrese la cantidad de horas trabajadas")
        canthoras = float(canthoras)
        dia =  input("ingrese el dia de la semana ")
        festivo = input("ingrese 1 para dia común 2 para día festivo ")
        festivo = int (festivo)
        turno = input("Ingrese 1 para Turno Diurno 2 Para Turno Nocturno")
        turno = int (turno)

        

        print("El Sueldo de: ",nombre,"Es de $ ",calculasueldos(canthoras,festivo,turno))


    # Ejercicio 12
    if name == '12' :

        def bisiesto(anio):
            
            if ((anio % 4) == 0 and (anio % 100) != 0):
                return True

            if ( (anio % 100) == 0 and (anio % 400) == 0):
                return True
            else:
                return False
        
        def diaanterior(d,m,a):
            dia = int(d)
            mes = int(m)
            anio = int(a)
        #chequeamos bisiesto
            if (bisiesto(anio)):
                print("Anio Bisiesto")
                
            if (m==1 and d==1): #ultimo dia del anio
                mes = 12
                dia = 31
                anio = anio - 1
                
            elif ((m==2 or m==4 or m==6 or m==8 or m==9 or m==11) and d==1):
                mes = mes - 1
                dia = 31
                
            elif (m==3 and d==1): #caso especial año bisiesto
                mes = 2
                if(bisiesto(anio)):
                    dia = 29
                else:
                    dia = 28
            
            elif ((m==7 or m==10 or m==12) and d==1):
                mes = mes - 1
                dia = 30

            else:
                dia = dia - 1

            return dia,mes,anio
            
        
        print("Consigna: solicite al usuario una fecha y muestre la fecha anterior")  
        d = 0
        m = 0
        a = 0
        d = input("Ingrese numero de Dia: ")
        d = int (d)
        m = input("Ingrese Mes: ")
        m = int (m)
        a = input("Ingrese Año: ")
        a = int (a)
        
        
        print("El dia anterior fue ", diaanterior(d, m, a))

    # Ejercicio 13
    if name == '13' :

        def calculapintura(arrayentrada):
            print("entrada: ",arrayentrada)
            metrospared = 0
            litros = 0
            lata1 = 0
            lata4 = 0
            lata10 = 0
            lata20 = 0
            resto = 0
            for x in range(len(habitacion[1])):
                #sumamos metros cuadrados de paredes
                metrospared = metrospared + (habitacion[0][x]*habitacion[2][x]*2)+(habitacion[1][x]*habitacion[2][x]*2)
                #restamos las puertas
                metrospared = metrospared - (habitacion[3][x] * 1.5)
                #restamos las ventanas
                metrospared = metrospared - (habitacion[4][x] * 1.8)
                metrospared = float(metrospared)

            litros = metrospared/14
            
            print("Cant de Litros a usar: ",litros)
            if (litros>=20):
                lata20 = litros / 20
                lata20 = int (lata20)
                litros=litros - (lata20*20)
                print("Latas de 20: ",lata20)

            if(litros>=10 or resto>=10):
                lata10 = litros / 10
                lata10 = int (lata10)
                print("Latas de 10: ",lata10)
                litros=litros - (lata10*10)
        
            if(litros>=4 or resto>=4):
                lata4 = litros / 4
                lata4 = int (lata4)               
                print("Latas de 4: ",lata4)
                litros=litros - (lata4*4)
                
                
            
            
            lata1 = litros 
            lata1 = int(lata1)
            litros = litros - lata1
            if (litros>0):
                    lata1 = lata1 + 1
            print("Latas de 1: ",lata1)
                
            return metrospared




        print("Consigna: Calcula pintura para una casa")  
        canthab = 0
        m = 0
        a = 0
        canthab = input("Ingrese Cantidad de Habitaciones: ")
        canthab = int(canthab)
        habitacion = [[]]
        habitacion = [[i for i in range(canthab)] for i in range(5)]

        print("Largo vector: ",len(habitacion[1]))     
        
        for x in range(len(habitacion[1])):
            print("Habitacion Numero: ",(x+1))
            ancho = input("Ingrese Ancho: ")
            ancho = float (ancho)
            habitacion[0][x] = ancho
            largo = input("Ingrese Largo: ")
            largo = float(largo)
            habitacion[1][x] = largo
            alto = input ("Ingrese Alto: ")
            alto= float (alto)
            habitacion[2][x] = alto
            puertas = input ("Ingrese Cantidad de Puertas: ")
            puertas= int (puertas)
            habitacion[3][x] = puertas
            ventanas = input("Ingrese Cantidad de Ventanas: ")        
            ventanas= int (ventanas)
            habitacion[4][x] = ventanas
        
        #print(habitacion)
        print(calculapintura(habitacion))
        

    
    # Salida si selecciona 0 en primera opcion
    elif name == '0' :
        break
    # Preguntar Nuevamente por entrada no valida
          
print('Gracias! Vuelva prontos!')         
