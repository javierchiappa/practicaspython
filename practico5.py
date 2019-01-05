
#Programa de Ejercicios Practico 5 por Javier Chiappa

import random

# Asignamos un valor a name para entrar al bucle
name = 'a'
# Bucle principal sale con cero
while name != '0': 
    print("Ejercicios Practico Programacion Numero 5")
    name = input('Que Ejercicio desea ver? (1 al 13), 0 para salir \n')
    print('Opcion Seleccionada, %s!' % name)

    # Ejercicio 1
    if name == '1' :
         print("Consigna: calcule los cuadrados de los primeros 100 números enteros")
         i=0
         
         numerosenteros = [i for i in range(101)]
         for i in range(1,101):
            numerosenteros[i]=i*i
            
         
         for i in numerosenteros:
          print(i)
         print("Fin de Ejercicio 1")

    # Ejercicio2
    if name == '2' :
        print("Consigna: Promedio de N temperaturas almacenadas en un Vector")
        temperaturas = [23,21,19,14,38,26,31,9,12,11]
        sumatoria = 0
        promedio = 0
        for i in range(len(temperaturas)):
            print(temperaturas[i])
            sumatoria = sumatoria + temperaturas[i]
            
        print ("Cantidad de Temperaturas ",len(temperaturas))
        promedio = sumatoria/len(temperaturas)
        print ("Promedio de Temperaturas: ",promedio)
        print ("Temperaturas que son mayores a la media :")
        for i in range(len(temperaturas)):
            if (temperaturas[i]>=promedio):
                print(temperaturas[i])

        print("Fin de Ejercicio 2")        
    # Ejercicio3
    if name == '3' :
        print("Consigna: Suma de todos los elementos de un vector de tamaño 20 y su media aritmética")
        vector = [23,21,19,14,38,26,31,9,12,11,13,56,34,58,54,23,14,98,67,10]
        sumatoria = 0
        promedio = 0
        print ("Cantidad de elementos en el vector ",len(vector))
        for i in range(len(vector)):
                print(vector[i])
                sumatoria = sumatoria + vector[i]
        promedio = sumatoria/len(vector)
        print ("Promedio de elementos en el vector ",promedio)
        print("Fin de Ejercicio 3")

    # Ejercicio4
    if name == '4' :
        print("Consigna: numero de elementos negativos, cero y positivos de un vector de 100 elementos")       
        vector4 = [i for i in range(101)]
        negativos = 0
        cero = 0
        positivos = 0
        random.seed(3.1415)
        print("Cargando vector de 100 elementos con numeros aleatorios")
        for i in range(101):
                vector4[i] = random.randint(-100, 100)
         
        print("Calculando negativos, cero y positivos")
        for i in range(101):
                if (vector4[i]>0):
                    positivos = positivos + 1
                if (vector4[i]<0):
                    negativos = negativos + 1
                if (vector4[i]==0):
                    cero = cero + 1
               # print(vector4[i], end=' ', flush=True)
               # print('')
        print("Resultados: ")
        print("Numeros Positivos: ",positivos)
        print("Numeros Negativos: ",negativos)
        print("Numeros cero: ",cero)
        print("Fin de Ejercicio 4")

    # Ejercicio5
    if name == '5' :
        print("Consigna: ingresar una frase de 30 caracteres y desplazarla hacia la derecha")       
        frase = [i for i in range(30)]
        i=0
        a=0
        b=0
        for i in range (30):
            frase[i] = input(': ')[0].lower()

        for a in range(5):
            for b in range(a*2):
                    print (' ',end='', flush=True)
            for i in range (30):
                print (frase[i],end='', flush=True)
            print (' ') 
        print (' ')   
        print("Fin de Ejercicio 5")


    # Ejercicio6
    if name == '6' :
        print("Consigna: lee las notas de un alumno, calucla el maximo y el minimo")       
        notas = [i for i in range(10)]
        sumatoria = 0
        promedio = 0
        NotaMax = 0
        NotaMin = 0
        print ("Cargado de Notas ")
        for i in range(10):
            notas[i] = input ("Ingrese Nota: ")
            notas [i] = float(notas[i])
            
        print ("Procesado de Notas ")
        NotaMin = notas[1]

        for i in range(10):
            sumatoria = sumatoria + notas[i]
            if (notas[i]>NotaMax):
                NotaMax = notas[i]
            if (notas[i]<NotaMin):
                NotaMin = notas[i]

        promedio = sumatoria/10

        print("Resultados ...  ")
        print("Promedio de Notas ",promedio)
        print("Nota mas Alta: ",NotaMax)
        print("Nota mas Baja: ",NotaMin)
        

    #ejercicio 7
    if name == '7' :
        print("Consigna: Rellenar array con 100 numeros enteros, mostrarlos en orden descendente")

        enteros = [i for i in range (101)]

        for i in range(100,0,-1):
            print (enteros[i])
        print("Fin de Ejercicio 7")



        #Ejercicio 1 Matrices (ejercicio 8)
    if name == '8' :
        matriz =[   [1,0,0,0,0],
                    [0,1,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,1,0],
                    [0,0,0,0,1]     ]

        for row in matriz:
          print(' '.join(map(str,row)))
        print("Fin de Ejercicio 8")
        



    if name == '9' :
        print("Consigna:Dada una lista de n * m elementos realizar un metodo que calcule y muestre la suma de los numeros pares y la suma de los numeros impares.")
        n = 0
        m = 0
        n = input ("ingrese el valor de n: ")
        m = input ("ingrese el valor de m: ")
        n = int(n)
        m = int(m)
        lista = [[]]
        lista = [[0 for x in range(n)] for x in range(m)]
        
        
        x = 0
        y = 0
        CantPar = 0
        CantImpar = 0
        print("llenando matriz con numeros aleatorios...")
        for x in range(len(lista)):
            for y in range(len(lista[x])):
                lista[x][y] = random.randint(0, 100)
            
        print(lista)
        print("Calculando Resultados...")
        for x in range(len(lista)):
            for y in range(len(lista[x])):
                if(lista[x][y]%2):
                    CantPar = CantPar+1
                else:
                    CantImpar = CantImpar+1
                    
        print("Numeros Pares...",CantPar)
        print("Numeros Impares...",CantImpar)
        print("Fin de Ejercicio 9")

        #Ejercicio 3 Matrices (ejercicio10)
    if name == '10' :
        print("Consigna:una matriz de m * n elementos que se rellene con números aleatorios del 1 al 100 ycalcular su traspuesta..")
        n = 0
        m = 0
        n = input ("ingrese el valor de n: ")
        m = input ("ingrese el valor de m: ")
        n = int(n)
        m = int(m)
        lista = [[]]
        lista = [[0 for x in range(n)] for x in range(m)]

        listat = [[]]
        lista = [[0 for x in range(m)] for x in range(n)]
        
        x = 0
        y = 0
        CantPar = 0
        CantImpar = 0
        print("llenando matriz con numeros aleatorios...")
        for x in range(len(lista)):
            for y in range(len(lista[x])):
                lista[x][y] = random.randint(0, 100)
            
        for row in lista:
          print(' '.join(map(str,row)))
          
        print("Calculando Resultados...")

        listat = [*zip(*lista)]

        for row in listat:
          print(' '.join(map(str,row)))
        print("Fin de Ejercicio 10")
        
    if name == '11' :
        print("Consigna:Estadisticas de Venta Empresa por Correo..")

        ventas = [[]]
        ventas = [[0 for x in range(12)] for x in range(100)] 

        anuales = [i for i in range (100)] 
        totalmensual = [i for i in range (12)]
        masvendidomes = [i for i in range (12)]
        recordproductomes = [i for i in range (12)]
        recordmes = 0
        recordmensual = 0
        recordnumero = 0

        print("llenando matriz con numeros aleatorios...")
        for x in range(len(ventas)):
            for y in range(len(ventas[x])):
                ventas[x][y] = random.randint(0, 100)
            
        for row in ventas:
          print(' '.join(map(str,row)))
          
        print("Calculando Resultados...")

        for x in range(len(ventas)): #recorremos cada producto x
            for y in range(len(ventas[x])): #recorremos cada mes en y
                anuales[x] = ventas[x][y] + anuales[x]
                totalmensual[y] = ventas[x][y] + totalmensual[y]
                
                if (ventas[x][y]>recordproductomes[y]): #Marcamos los records de ventas en cada mes
                    recordproductomes[y] = ventas[x][y]
                    masvendidomes[y] = x
                    
                    

        print("Ventas Anuales de Cada Producto...")
        for x in range(len(anuales)):
            print("Ventas Anuales producto: ",x+1,"es de $ ",anuales[x])
        print("Total Ventas Mensuales...")
        for x in range(len(totalmensual)):
            print("Total de Ventas del Mes: ",x+1,"es de $ ",totalmensual[x])
        for x in range(len(masvendidomes)):
            print("Producto Mas Vendido del Mes: ",x,"es el ",masvendidomes[x],"Con una cantidad de ",recordproductomes[x])
            if (recordmensual<recordproductomes[x]): #calculamos el ganador absoluto de todos los meses
                recordmensual = recordproductomes[x]
                recordmes = x
                recordnumero = masvendidomes[x]

        print ("El Producto", recordnumero," En el Mes de ",recordmes, "vendio una cantidad de ",recordmensual)
        print("Fin de Ejercicio 11")

    if name == '12' :
        print("Consigna:Distribuidora de Conocida Marca de Café tiene 16 representantes..")



    if name == '13' :
        print("Consigna:una matriz magica..")
        n = 0
        n = input ("ingrese el valor de n: ")
        n = int(n)
        sumatoriafilas = [0 for x in range(n)]
        sumatoriacolumnas = [0 for x in range(n)]
        diagonalfacil = 0
        diagonaldificil = 0
        suma = 0
        lista = [[]]
        lista = [[0 for x in range(n)] for x in range(n)]
        prueba = [[2,7,6],[9,5,1],[4,3,8]]
        prueba2 = [[1,1,1],[2,2,2],[5,3,3]]
        for x in range(n):
            for y in range(n):
                sumatoriafilas[y] = sumatoriafilas[y] + prueba[x][y]
                if (x==y):
                    diagonalfacil = diagonalfacil + prueba[x][y]

        for x in range(n):
            for y in range(n):
                sumatoriacolumnas[x] = sumatoriacolumnas[x] + prueba[x][y]

        y = n
        for x in range(n):
            y = y - 1
            diagonaldificil = diagonaldificil + prueba[x][y]

        
        for row in prueba:
          print(' '.join(map(str,row)))
                

        suma = diagonaldificil
        for x in range(n):
            if (diagonalfacil == sumatoriafilas[x] == sumatoriacolumnas[x] == diagonaldificil):           
                valido = 1
            else:
                valido = 0
                print("La Matriz NO es Magica")
        if (valido == 1):
            print("LA MAtriz es Magica")
            print("Suma: ",suma)

    # Salida si selecciona 0 en primera opcion
    elif name == '0' :
        break
    # Preguntar Nuevamente por entrada no valida
    else :
        print ('Ingrese un numero del 1 al 13, usted ingreso %s , intente nuevamente' % name)
        
print('Gracias! Vuelva prontos!')
               
