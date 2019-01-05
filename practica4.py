
#Programa de Ejercicios Practico 4 por Javier Chiappa



# Asignamos un valor a name para entrar al bucle
name = 'a'
# Bucle principal sale con cero
while name != '0': 
    print("Ejercicios Practico Programacion Numero 4")
    name = input('Que Ejercicio desea ver? (1 al 13), 0 para salir \n')
    print('Opcion Seleccionada, %s!' % name)

    # Ejercicio 1
    if name == '1' :
        print("Consigna: Calcule el cuadrado de los primeros 9 numeros naturales ")
        
        for i in range(1,10):
            print ("Cuadrado de ",i," es ", i**2)
            

    # Ejercicio 2
    if name == '2' :
        numero=0
        resultado=0
        print("Consigna: Calcule la suma de  la suma de los N primeros números naturales")
        numero = input ('ingrese numero ')
        numero = int (numero)
        for i in range(1,numero+1):
            resultado = resultado + i
        print ("Resultado: ",resultado)

    # Ejercicio 3
    if name == '3' :
        numero=0
        resultado=0
        modulo=0
        print("Consigna: Calcule la suma de  la suma de los N primeros números naturales pares")
        numero = input ('ingrese numero ')
        numero = int (numero)
        numero = numero * 2
        for i in range(1,numero+1,1): #damos 5 vueltas
            if ((i % 2)==0):
                resultado = resultado + i
                print (i,resultado)
                
        print ("Resultado: ",resultado)

        
    # Ejercicio 4
    if name == '4':
        print ("Consigna: Calcule la media de numeros ingresados hasta que se ingrese -1")
        numero = 0
        Resultado = 0
        i = 0
        while (numero != -1):
               i = i+1
               Resultado = Resultado + numero
               numero = input("Ingrese numero ")
               numero = float (numero)

        i = i-1 #descontamos la última vuelta       
        print ("El promedio de", i , "numeros ingresados es de:",(Resultado/(i)))


    # Ejercicio 5
    if name == '5':
        print ("Consigna: Pide una clave 3 veces")
        clave = 0
        intento = 0
        for intento in range(1,4):
            print ("intento numero ",intento, "de 3 en total")
            clave = input ("ingrese la contrasenia: ")
            if (clave=='eureka'):
                print("Contrasenia Correcta!")
                break
            else:
                print("Contrasenia Incorrecta")
                if (intento == 3):
                    print("Usted utilizo todos sus intentos, clave Bloqueada")
                
        print("Fin de Ejercicio 5")


    # Ejercicio 6
    if name == '6':
        print ("Consigna: Lee numeros enteros hasta ingesar 0, calcula max, min y media")
        numero = 1
        numeromax = 0
        numeromin = 0
        sumatoria = 0
        vueltas = 0
        numero = input("ingrese numero entero: ")
        numero = int(numero)
        numeromin = numero
        while (numero != 0):
            vueltas = vueltas+1
            sumatoria = sumatoria + numero
            if (numero>=numeromax):
                numeromax=numero
            if (numero<=numeromin):
                numeromin=numero
            numero = input("ingrese numero entero: ")
            numero = int(numero)
        
        print("El numero maximo es: ",numeromax,"El Numero Minimo es",numeromin,"El Medio es",(sumatoria/vueltas))

    # Ejercicio 7
    if name == '7':
        print ("Consigna: Imprime numeros multiplos de 2 y 3 entre 0 y 100")
        i = 0
        sumar = 0
        sumatoria2 = 0
        sumatoria3 = 0
        imprimirnum = 0
        imprimirnum = input ("ingrese 1 para imprimir todos los numeros, 2 para ver sólo el total: ")
        imprimirnum = int(imprimirnum)
        for i in range(1,101): #recorremos el bucle 100 veces
            if ((i % 2) == 0): #probamos el modulo de 2, si es cero, es divisible por 2
                sumatoria2 = sumatoria2 + 1
                if (imprimirnum == 1):#opcion para imprimir o no esta frase
                    print ("El numero ",i,"es multiplo de 2")
                sumar = 1
            if ((i % 3) == 0):#probamos el modulo de 3
                sumatoria3 = sumatoria3 + 1
                if (imprimirnum == 1):
                    print ("El numero ",i,"es multiplo de 3")
                sumar = 1
        print ("La suma de los numeros que son multiplos de 2 es de: ",sumatoria2)
        print ("La suma de los numeros que son multiplos de 3 es de: ",sumatoria3)
        print ("El total es de : ",(sumatoria2+sumatoria3))
        print ("Fin de Ejercicio 7")

        

    # Ejercicio 8
    if name == '8':
        print ("Consigna: leer fecha, validarla y convertir mes a numero")
        dia = 0
        mes = 0
        anio = 0
        valido = 0
        bisiesto=0
        while (valido != 1): #hacemos un bucle hasta que el dia sea valido
            dia = input("ingrese el dia: ")
            dia = int(dia)
            if (dia>=1 and dia<=31):
                print("Dia valido")
                
            else:
                print("Dia no valido, intente nuevamente")
        
            mes = input("ingrese el mes: ")
            mes = int(mes)
            if (mes==2 and dia>=28):
                print("Mes no Valido Febrero tiene hasta 28 dias, a menos que sea bisiesto")
                valido=0
                excepcion=1
                
            if (mes==2 or mes==4 or mes==6 or mes==9 or mes==11 and dia>=30):
                print("Mes no Valido esos meses tienen hasta 30 dias")
                valido=0
                excepcion=1
                
            elif (mes>=1 and mes<=12 and excepcion!=0):
                print("Mes valido")
                valido=1
                excepcion=0
            else:
                print("Mes no valido, intente nuevamente")
                valido=0

            anio = input("ingrese el anio: ")
            anio = int(anio)
            #chequeamos bisiesto
            bisiesto = 0
            if ((anio % 4) == 0 and (anio % 100) != 0):
                bisiesto = 1

            if ( (anio % 100) == 0 and (anio % 400) == 0):
                bisiesto = 1

            if (bisiesto==1 and mes==2 and excepcion==1 and dia>=29):
                print("Es un Año Bisiesto y por eso es valido")
                valido =1
                
            if (bisiesto==0 and mes==2 and excepcion==1 and dia>=28):
                print("NO un Año Bisiesto y por eso NO es valido")
                valido =0
            

            if (anio>=1 and anio<=2018):
                print("Anio valido")
                
            else:
                print("Anio no valido, intente nuevamente")

            if (valido==0):
                print("FECHA NO VALIDA")
            if (valido==1):
                print("FECHA VALIDA")
                
        # cambiar mes en numero por letras
        if (mes == 1):
            mes = 'Enero'
        elif(mes == 2):
            mes = 'Febrero'
        elif(mes == 3):
            mes = 'Marzo'
        elif(mes == 4):
            mes = 'Abril'
        elif(mes == 5):
            mes = 'Mayo'
        elif(mes == 6):
            mes = 'Junio'
        elif(mes == 7):
            mes = 'Julio'
        elif(mes == 8):
            mes = 'Agosto'
        elif(mes == 9):
            mes = 'Septiembre'
        elif(mes == 10):
            mes = 'Octubre'
        elif(mes == 11):
            mes = 'Noviembre'
        elif(mes == 12):
            mes = 'Diciembre'

        print("La Fecha es: ",dia," de ",mes," de ",anio)
        print ("Fin de Ejercicio 8")


    #Ejercicio 9
    elif name == '9' :
        print('Consigna: Calcular las calificaciones de un grupo de alumnos, deje el nombre vacio para salir   \n')
        Nombre = 0
        
        #Entrada de datos y conversion a Float
        while (Nombre != ' '):
            #limpiamos las variables
            Nombre = 0
            Practica = 0
            Problemas = 0
            Teoria = 0
            Total = 0
            Nombre = input('Ingrese Nombre del Alumno  ')
            if (Nombre == ''):
                break
            Practica = input('Ingrese Notas de Practicas  ')
            Practica = int (Practica)
            if (Practica<0 or Practica>10):
                print("Error, la nota debe ser entre 0 y 10")
                break
            Problemas = input('Ingrese Notas de Problemas  ')
            Problemas = int (Problemas)
            if (Problemas<0 or Problemas>10):
                print("Error, la nota debe ser entre 0 y 10")
                break
            Teoria = input('Ingrese Notas de Teorias  ')
            Teoria = int (Teoria)
            if (Teoria<0 or Teoria>10):
                print("Error, la nota debe ser entre 0 y 10")
                break
            print('Calculando...')
            Total = (Practica * 0.1) + (Problemas * 0.5) + (Teoria * 0.4)
            Total = int (Total)
            print('Resultados \n')
            print('La nota final de',Nombre,' Es de:',Total )

        
        print ('Fin de Ejercicio9 \n')
            
            
    #Ejercicio 10
    elif name == '10' :
        print('Consigna: Crea un cuadrado de Asteriscos   \n')
        Lado = 0
        i = 0
        Lado = input("Ingrese el numero de Lado: ")
        Lado = int(Lado)
        print("-------------------")
        for i in range(1,Lado+1):
            print('* ', end='', flush=True)
        print('')

        
        for i in range(1,Lado-1):
            print('* ', end='', flush=True)

            for i in range(1,(Lado-1)):
                print(' ', end='', flush=True)
    
            print(' *', end='', flush=True)
        
            print('')

            
        for i in range(1,Lado+1):
           print('* ', end='', flush=True)
            
        print('')


        
        print("-------------------")
        print("Fin de Ejercicio 10")

    #Ejercicio 11
    elif name == '11' :
        print('Consigna: Crea una cascada descendiente de Asteriscos   \n')
        Lado = 0
        i = 0
        Lado = input("Ingrese el numero de Lado: ")
        Lado = int(Lado)
        cant = Lado+1
        for i in range(1,Lado+1):
            
            for i in range(1,cant):
                print('* ', end='', flush=True)
                
            print('')
            cant = cant-1
                
        print('')
        print("Fin de Ejercicio 11")


    #Ejercicio 12
    elif name == '12' :
        print('Consigna: Dice si un Anio es bisiesto o no  \n')
        anio = 0
        bisiesto = 0
        anio = input("Ingrese el Anio: ")
        anio = int(anio)

        if ((anio % 4) == 0 and (anio % 100) != 0):
            bisiesto = 1

        if ( (anio % 100) == 0 and (anio % 400) == 0):
            bisiesto = 1
        
        if (bisiesto == 1):
            print("El Anio",anio," SI es Bisiesto")
        else:
            print("El Anio",anio," NO es Bisiesto")
        
        print("Fin de Ejercicio 12")


    #Ejercicio 13
    elif name == '13' :
        print('Consigna: Notas de un Docente de Humanistica  \n')
        investigacion = 0
        exposicion = 0
        parcial = 0
        notafinal = 0
        vuelta = 0
        notamayor = 0
        sumareprobados = 0
        mayorexposicion = 0
        cantparcial = 0
        cantreprobados = 0
        salir = 1

        while (salir != 0):
            vuelta = vuelta+1
            investigacion = 0
            exposicion = 0
            parcial = 0
            notafinal = 0

            
            print("Ingrese las notas del estudiante N: ",vuelta)
            investigacion = input("Ingrese la nota de Investigacion: ")
            exposicion = input("Ingrese la nota de Exposicion: ")
            parcial = input("Ingrese la nota del Parcial: ")
            investigacion = int(investigacion)
            exposicion = int(exposicion)
            parcial = int(parcial)
            notafinal = (investigacion * 0.25) + (exposicion * 0.35) + (parcial * 0.4)
            notafinal = float(notafinal)
            print("La nota final del estudiante es: {0:.2f}".format(notafinal))
            if (notafinal < 6.5):
                sumareprobados = sumareprobados + notafinal
                cantreprobados = cantreprobados + 1
            if (notafinal > 7.5):
                notamayor = notamayor + 1
            if (exposicion > mayorexposicion):
                mayorexposicion = exposicion
            if ( (parcial>4) and (parcial<=7.5)):
                cantparcial = cantparcial + 1
            
            salir = input("Para salir presione 0, para cargar proximo alumno presione 1 ")
            salir = int(salir)

            

        print("Resultados \n")

        print("Nota promedio de estudiantes que reprobaron el curso: {0:.2f}".format(sumareprobados/cantreprobados) )
        print("Porcentaje de estudiantes que tienen nota de investigacion mayor a 7.5: {0:.2f}".format((notamayor/vuelta)*100))
        print("Mayor nota obtenida en las exposiciones: ",mayorexposicion)
        print("Cantidad de alumnos que tuvieron parcial entre 4 y 7.5: ",cantparcial)
           



        
        print("Fin de Ejercicio 12")
        
        

    # Salida si selecciona 0 en primera opcion
    elif name == '0' :
        break
    # Preguntar Nuevamente por entrada no valida
    else :
        print ('Ingrese un numero del 1 al 13, usted ingreso %s , intente nuevamente' % name)
        
print('Gracias! Vuelva prontos!')
