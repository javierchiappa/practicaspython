#Programa de Ejercicios Practico 3 por Javier Chiappa
#Asignamos variables globales
pi = 3.14159

# Ssignamos un valor a name para entrar al bucle
name = 'a'
# Bucle principal sale con cero
while name != '0': 

    name = input('Que Ejercicio desea ver? (1 al 13), 0 para salir \n')
    print('Opcion Seleccionada, %s!' % name)
    

    # Ejercicio 1
    if name == '1' :
        #limpiamos las variables
        A = 0
        B = 0
        C = 0
        print('Ejercicio1 \n')
        print('Consigna: Algoritmo que intercambie los valores de A y B y muestre cuánto valen al final las dos variables  \n')
        A = input('ingrese valor de A  ')
        B = input('ingrese valor de B  ')
        print('Calculando...')
        C = A
        A = B
        B = C
        print('El valor de A es %s' % A)
        print('El valor de B es %s' % B)
        print ('Fin de Ejercicio1 \n')

    # Ejercicio 2
    elif name == '2' :
        print ('Ejercicio2 \n')
        print('Consigna: Algoritmo que lea dos números, Calculando... y escribiendo el valor de su suma, resta,producto y división  \n')
        #limpiamos las variables
        A = 0
        B = 0
        C = 0
        #Entrada de datos y conversion a Float
        A = input('ingrese valor de A  ')
        B = input('ingrese valor de B  ')
        A = float (A)
        B = float (B)
        print('Calculando...')
        Suma = A + B
        Resta = A - B
        Division = A / B
        Multiplicacion = A * B
        print('Resultados \n')
        print('El valor de suma es %s' % Suma)
        print('El valor de resta es %s' % Resta)
        print('El valor de multiplicacion es %s' % Multiplicacion)
        print('El valor de Division es %s' % Division)
        print ('Fin de Ejercicio2 \n')

    # Ejercicio 3
    elif name == '3' :
        print ('Ejercicio3 \n')
        print('Consigna: Calcular Porcentaje de Niños y de Niñas  \n')
        #limpiamos las variables
        Ninios = 0
        Ninias = 0
        Total = 0
        PorcNinios = 0
        PorcNinias = 0
        #Entrada de datos y conversion a Entero
        Ninios = input('Ingrese Cantidad de Niños  ')
        Ninias = input('Ingrese Cantidad de Niñas  ')
        Ninios = int (Ninios)
        Ninias = int (Ninias)
        print('Calculando...')
        Total = Ninios + Ninias
        PorcNinios = (Ninios * 100) / Total
        PorcNinias = (Ninias * 100) / Total
        print('Resultados \n')
        print('El Total de Niños es %s' % Total)
        print('El porcentaje de Varones es %s' % PorcNinios)
        print('El porcentaje de Mujeres es %s' % PorcNinias)        
        print ('Fin de Ejercicio3 \n')

    # Ejercicio 4
    elif name == '4' :
        print ('Ejercicio4 \n')
        print('Consigna: Calcular las calificaciones de un alumno.   \n')
        #limpiamos las variables
        Nombre = 0
        Practica = 0
        Problemas = 0
        Teoria = 0
        Total = 0
        #Entrada de datos y conversion a Float
        Nombre = input('Ingrese Nombre del Alumno  ')
        Practica = input('Ingrese Notas de Practicas  ')
        Problemas = input('Ingrese Notas de Problemas  ')
        Teoria = input('Ingrese Notas de Teorias  ')
        Practica = float (Practica)
        Problemas = float (Problemas)
        Teoria = float (Teoria)
        print('Calculando...')
        Total = (Practica * 0.1) + (Problemas * 0.5) + (Teoria * 0.4)
        Total = int (Total)
        print('Resultados \n')
        print('La nota final de',Nombre,' Es de:',Total )        
        print ('Fin de Ejercicio4 \n')


    # Ejercicio 5
    elif name == '5' :
        print ('Ejercicio5 \n')
        print('Consigna: Calcular Perimetro y Area de un Circulo   \n')
        #limpiamos las variables
        Area = 0
        Perimetro = 0
        Redio = 0
        #Entrada de datos y conversion a Float
        Radio = input('Ingrese el Radio del Circulo:  ')
        Radio = float (Radio)
        print('Calculando...')
        Perimetro = pi * Radio
        Area = pi * Radio * Radio
        print('Resultados \n')
        print('El circulo tiene un Perimetro de: ',Perimetro,'y un Area de: ',Area )   
        print ('Fin de Ejercicio5 \n')


    # Ejercicio 6
    elif name == '6' :
        print ('Ejercicio6 \n')
        print('Consigna: Calcular Perimetro y Area de un Cuadrilatero   \n')
        #limpiamos las variables
        Base = 0
        Altura = 0
        Area = 0
        Perimetro = 0
        #Entrada de datos y conversion a Float
        Base = input('Ingrese medida de la base:  ')
        Altura = input('Ingrese medida de la altura:  ')
        Base = float (Base)
        Altura = float (Altura)
        print('Calculando...')
        Perimetro = (Base * 2) + (Altura * 2)
        Area = Base * Altura
        print('Resultados \n')
        print('El cuadrilatero tiene un Perimetro de: ',Perimetro,'y un Area de: ',Area )           
        print ('Fin de Ejercicio6 \n')

    # Ejercicio 7
    elif name == '7' :
        print ('Ejercicio7 \n')
        print('Consigna: Calcular Volumen de un Cilindro   \n')
        #limpiamos las variables
        Diametro = 0
        Radio = 0
        Altura = 0
        Volumen = 0
        #Entrada de datos y conversion a Float
        Diametro = input('Ingrese Diametro de la base en metros:  ')
        Altura = input('Ingrese la altura del cilindro en metros:  ')
        Diametro = float (Diametro)
        Altura = float (Altura)
        print('Calculando...')
        Radio = Diametro/2
        Volumen = pi * Radio * Radio * Altura
        print('Resultados \n')
        print('El Cilindro tiene un Volumen de: ',Volumen,'metros cubicos' )           
        print ('Fin de Ejercicio7 \n')


    # Ejercicio 8
    elif name == '8' :
        print ('Ejercicio8 \n')
        print('Consigna: Calcular Promedio de Precios en 3 Establecimientos.   \n')
        #limpiamos las variables
        Precio1 = 0
        Precio2 = 0
        Precio3 = 0
        Medio = 0
        #Entrada de datos y conversion a Float
        Precio1 = input('Ingrese Precio en Primer Establecimiento  ')
        Precio2 = input('Ingrese Precio en Segundo Establecimiento   ')
        Precio3 = input('Ingrese Precio en Tercer Establecimiento  ')
 
        Precio1 = float (Precio1)
        Precio2 = float (Precio2)
        Precio3 = float (Precio3)

        print('Calculando...')
        Medio = (Precio1 + Precio2 + Precio3) / 3
        Medio = float(Medio)
        print('Resultados \n')
        print('El precio Medio es {0:.2f}'.format(Medio))     #formateado float para 2 decimales   
        print ('Fin de Ejercicio8 \n')

    # Ejercicio 9
    elif name == '9' :
        print ('Ejercicio9 \n')
        print('Consigna: Convierte dias en Horas, Minutos y Segundos   \n')
        #limpiamos las variables
        Dias = 0
        Horas = 0
        Minutos = 0
        Segundos = 0
        #Entrada de datos y conversion a Float
        Dias = input('Ingrese Cantidad de Días:  ')
        Dias = int (Dias)
        print('Calculando...')
        Horas = Dias * 24
        Minutos = Horas * 60
        Segundos = Minutos * 60
        Horas = int (Horas)
        Minutos = int (Minutos)
        Segundos = int (Segundos)
        print('Resultados \n')
        print('La cantidad de Horas son {0}'.format(Horas))    
        print('La cantidad de Minutos son {0}'.format(Minutos))     
        print('La cantidad de Segundos son {0}'.format(Segundos))       
        print ('Fin de Ejercicio9 \n')


    # Ejercicio 10
    elif name == '10' :
        print ('Ejercicio9 \n')
        print('Consigna: Convierte Metros en cm, mm y pulgadas  \n')
        #limpiamos las variables
        Metros = 0
        Centimetros = 0
        Milimetros = 0
        Pulgadas = 0
        #Entrada de datos y conversion a Float
        Metros = input('Ingrese Cantidad de Metros:  ')
        Metros = float (Metros)
        print('Calculando...')
        Centimetros = Metros * 100
        Milimetros = Centimetros * 10
        Pulgadas = Centimetros * 2.54
        Centimetros = float (Centimetros)
        Milimetros = float (Milimetros)
        Pulgadas = float (Pulgadas)
        print('Resultados \n')
        print('La cantidad de Centimetros son {0:.2f}'.format(Centimetros))    
        print('La cantidad de Milimetros son {0:.2f}'.format(Milimetros))     
        print('La cantidad de Pulgadas son {0:.2f}'.format(Pulgadas))       
        print ('Fin de Ejercicio10 \n')


    # Ejercicio 11
    elif name == '11' :
        print ('Ejercicio11 \n')
        print('Consigna: Calcula Cantidad de Kilometros que puede recorrer un auto  \n')
        #limpiamos las variables
        Consumo = 0
        Litros = 0
        Kilometros = 0
        #Entrada de datos y conversion a Float
        Consumo = input('Ingrese el consumo promedio lt/km:  ')
        Litros = input('Ingrese la cantidad de Litros Cargados en la Estacion:  ')

        Consumo = float (Consumo)
        Litros = float (Litros)
        print('Calculando...')
        Kilometros = Litros / Consumo
        
        Kilometros = float (Kilometros)

        print('Resultados \n')
        print('La cantidad de Kilometros que puede recorrer es de {0:.2f}'.format(Kilometros))    

        print ('Fin de Ejercicio11 \n')

    # Ejercicio 12
    elif name == '12' :
        print ('Ejercicio12 \n')
        print('Consigna: Calcula Porcentaje de Aumentos de un producto en un Año  \n')
        #limpiamos las variables
        Precio1 = 0
        Precio2 = 0
        Porcentaje = 0
        #Entrada de datos y conversion a Float
        Precio1 = input('Ingrese el precio a Principio de Año:  ')
        Precio2 = input('Ingrese el precio a Final de Año:  ')
        
        Precio1 = float (Precio1)
        Precio2 = float (Precio2)
        print('Calculando...')

        Porcentaje = (Precio1 * 100) / Precio2
        
        Porcentaje = float (Porcentaje)

        print('Resultados \n')
        print('La variación de precio es del {0:.2f} %'.format(Porcentaje))    

        print ('Fin de Ejercicio12 \n')



    # Ejercicio 13
    elif name == '13' :
        print ('Ejercicio13 \n')
        print('Consigna: Leer un caracter y determinar si esta entre la I y la M  \n')
        #limpiamos las variables
        Caracter = 0

        #Entrada de datos y conversion a Mayusculas
        Caracter = input('Ingrese el caracter ')

        Caracter = Caracter.upper()
       

        print('Calculando...')
        print('Resultados \n')
        print('El Valor del caracter es',Caracter)
        if (Caracter < 'I'):
            print ('Menor que I')

        if (Caracter > 'M'):
            print ('Mayor que M')

        if (Caracter > 'I' and Caracter < 'M'):
            print('El Caracter Ingresado se encuentra entre la I y la M')
            
        print ('Fin de Ejercicio13 \n')

    # Ejercicio 14
    elif name == '14' :
        print ('Ejercicio14 \n')
        print('Consigna: Leer 2 caracteres y determinar si estan en orden alfabetico \n')
        #limpiamos las variables
        Caracter1 = 0
        Caracter2 = 0
        #Entrada de datos y conversion a Mayusculas
        Caracter1 = input('Ingrese el primer caracter ')
        Caracter2 = input('Ingrese el segundo caracter ')
        Caracter1 = Caracter1.upper()
        Caracter2 = Caracter2.upper()

        print('Calculando...')
        print('Resultados \n')
        
        if (Caracter1 < Caracter2):
            print ('Estan en Orden Alfabetico')

        if (Caracter1 > Caracter2):
            print ('No estan en Orden Alfabetico')

      
            
        print ('Fin de Ejercicio14 \n')





    # Ejercicio 15
    elif name == '15' :
        print ('Ejercicio15 \n')
        print('Consigna: Leer un caracter y determinar antes o despues de la N  \n')
        #limpiamos las variables
        Caracter = 0

        #Entrada de datos y conversion a Mayusculas
        Caracter = input('Ingrese el caracter ')

        Caracter = Caracter.upper()
       

        print('Calculando...')
        print('Resultados \n')
        print('El Valor del caracter es',Caracter)
        if (Caracter < 'N'):
            print ('Antes que la N')

        elif (Caracter > 'N'):
            print ('Despues que la N')
        elif (Caracter == 'N'):
            print ('El Caracter es la N')

        else:
            print('El Caracter no es válido')
            
        print ('Fin de Ejercicio15 \n')

    # Ejercicio 16
    elif name == '16' :
        print ('Ejercicio16 \n')
        print('Consigna: Determinar el Valor de A, B, C y D despues de las instrucciones \n')
        #limpiamos las variables
        A = 0
        B = 0
        C = 0
        D = 0
        
        print('Calculando...')
        A = 1
        B = 4
        A = int (A)
        B = int (B)
        C = A+B
        D = A-B
        A = C + (2 * B)
        B = C + B
        C = A * B
        D = B + D
        A = D + C

        if (C > D):
            C = A - D
        else:
            C = B - D

        print('Resultados \n')
        
        print ('El Valor de A es:',A)
        print ('El Valor de B es:',B)
        print ('El Valor de C es:',C)
        print ('El Valor de D es:',D)
            
        print ('Fin de Ejercicio16 \n')

        

    # Ejercicio 17
    elif name == '17' :
        print ('Ejercicio17 \n')
        print('Consigna: Calculadora de operaciones Basicas  \n')
        print('Ingrese S para Suma, R para Resta, P o M para Producto y D para Division  \n')
        #limpiamos las variables
        Operacion = 0
        Operando1 = 0
        Operando2 = 0
        Resultado = 0
        #Entrada de datos y conversion a Float

        Operacion = input('Que operacion desea realizar:  ')
        Operacion = Operacion.upper()

        Operando1 = input('Ingrese Primer Operando:  ')
        Operando2 = input('Ingrese Segundo Operando:  ')
        
        Operando1 = float (Operando1)
        Operando2 = float (Operando2)
        print('Calculando...')
        if (Operacion == 'S'):
            print('Operacion Seleccionada: Suma')
            Resultado = Operando1 + Operando2
        elif(Operacion == 'R'):
            print('Operacion Seleccionada: Resta')
            Resultado = Operando1 - Operando2           
        elif(Operacion == 'P' or Operacion == 'M'):
            print('Operacion Seleccionada: Producto')
            Resultado = Operando1 * Operando2
        elif(Operacion == 'D'):
            print('Operacion Seleccionada: Division')
            Resultado = Operando1 / Operando2
        else:
            print('No ingreso una Operacion Valida')
            
        

        print('Resultados \n')
        print('El Resultado es de',Resultado)    

        print ('Fin de Ejercicio17 \n')


    # Ejercicio 18
    elif name == '18' :
        print ('Ejercicio18 \n')
        print('Consigna: Empresa Te Llevo a Todos Lados, calculo de Importe de Alquiler de Auto  \n')
        print('Nuestros vehiculos consumen 0,08 lt/kms!  \n')
        #limpiamos y asignamos las variables
        Horas = 0
        Kilometros = 0
        Monto = 0
        Consumo = 0.08
        Litros = 0
        Minutos = 0
        #Entrada de datos y conversion a Float
        Kilometros = input('Ingrese los Kilometros Recorridos:  ')
        Horas = input('Ingrese la cantidad de Horas de Uso del Vehiculo:  ')

        Kilometros = float (Kilometros)
        Horas = float (Horas)
        
        print('Calculando...')

        if (Horas < 2):
            Monto = 400
        elif(Horas > 2):
            Minutos = Horas *60
            Litros = Kilometros * Consumo
            Monto = (Minutos * 5.20) + (Litros * 40)
            Monto = float(Monto)
        else:
            print('Cantidad de Horas Error')

        print('Resultados \n')
        if (Horas > 2):
            print('El Consumo de Combustible fue de {0:.2f} Litros'.format(Litros))
            
        print('El Monto Total es de $ {0:.2f}'.format(Monto))    

        print ('Fin de Ejercicio18 \n')




    # Ejercicio 19
    elif name == '19' :
        print ('Ejercicio19 \n')
        print('Consigna:Calcular el Descuento de una tienda dado el Mes y el Monto \n')
        #limpiamos las variables
        Mes = 0
        Monto = 0
        #Entrada de datos y conversion a Mayusculas y float
        Mes = input('Ingrese el Mes ')
        Monto = input('Ingrese el Importe ')
        Mes = Mes.upper()
        Monto = float(Monto)

        print('Calculando...')
        print('Resultados \n')
        
        if (Mes == 'OCTUBRE'):
            print ('Mes de Octubre!, tiene un descuento de 15%')
            Monto = Monto * 0.85
            print('El Importe Total es de $ {0:.2f}'.format(Monto))

        else:
            print ('Lo sentimos, no tiene descuento')
            print('El Importe Total es de $ {0:.2f}'.format(Monto))
      
        print ('Fin de Ejercicio19 \n')


        

    # Ejercicio 20
    elif name == '20' :
        print ('Ejercicio20 \n')
        print('Consigna:Calcular si un numero es par o impar\n')
        #limpiamos las variables
        Numero = 0
        Par = 0
        Impar = 0
        Resultado = 0
        #Entrada de datos y conversion a Mayusculas y float
        Numero = input('Ingrese el Numero ')
        Numero = int(Numero)
        print('Calculando...')
        Resultado = Numero % 2
        print('Resultados \n')
        
        if (Resultado == 0):
            print ('El Numero ',Numero,' Es Par')
        else:
            print ('El Numero ',Numero,' Es Impar')
        
        print ('Fin de Ejercicio20 \n')



    # Ejercicio 21
    elif name == '21' :
        print ('Ejercicio 21 \n')
        print('Consigna: Calculo de Sueldos Semanalaes de una empresa  \n')
        print('Ingrese la Condición de Contratación  \n')
        print('1 ) Salario Fijo + Comisión  \n')
        print('2 ) Salario Fijo  \n')
        print('3 ) Comision \n')
        #limpiamos y asignamos las variables
        Horas = 0
        HorasExtra = 0
        Condicion = 0
        Ventas = 0
        Salario = 0
        ValorHora = 0
        #Entrada de datos y conversion a Float
        Condicion = input('Ingrese el Codigo de la condicion:  ')
        
        Condicion = int (Condicion)
        
        print('Calculando...')

        if (Condicion == 3):
            print ('Condicion Seleccionada: Comision')
            Ventas = input('Ingrese el Monto de Venta Total:  ')
            Ventas = float(Ventas)
            Salario = Ventas * 0.4
            print('El Salario Semanal es de $ {0:.2f}'.format(Salario))


        elif(Condicion == 1):
            print ('Condicion Seleccionada: Salario Fijo+Comision')
            ValorHora = input('Ingrese el Valor de la Hora:  ')
            ValorHora = float(ValorHora)
            Horas = input('Ingrese la Cantidad de Horas Trabajadas:  ')
            Horas = float(Horas)
            Ventas = input('Ingrese el Monto de Venta Total:  ')
            Ventas = float(Ventas)
            if (Horas > 40):
                Horas = 40
            Salario = (Ventas * 0.25) + (Horas * ValorHora)
            print('El Salario Semanal es de $ {0:.2f}'.format(Salario))



        elif(Condicion == 2):

            print ('Condicion Seleccionada: Salario Fijo')
            ValorHora = input('Ingrese el Valor de la Hora:  ')
            ValorHora = float(ValorHora)
            Horas = input('Ingrese la Cantidad de Horas Trabajadas:  ')
            Horas = float(Horas)
            if (Horas > 40):
                HorasExtra = (Horas - 40)
                Horas = 40
            Salario = (Horas * ValorHora) + (HorasExtra * (ValorHora * 1.5))
            print('El Salario Semanal es de $ {0:.2f}'.format(Salario))
            
            
        else:
            print('Condicion Error, ingrese un numero del 1 al 3')


        print ('Fin de Ejercicio21 \n')



    # Ejercicio 22
    elif name == '22' :
        print ('Ejercicio 22 \n')
        print('Consigna: Pedir 2 Numeros y mostrar un Menu para elegir que operacion se quiere realizar  \n')
        print('Ingrese S para Suma, R para Resta, P o M para Producto y D para Division  \n')
        #limpiamos las variables
        Operacion = 0
        Operando1 = 0
        Operando2 = 0
        Resultado = 0
        #Entrada de datos y conversion a Float

        Operando1 = input('Ingrese Primer Operando:  ')
        Operando2 = input('Ingrese Segundo Operando:  ')

        Operacion = input('Que operacion desea realizar:  ')
        Operacion = Operacion.upper()
        
        Operando1 = float (Operando1)
        Operando2 = float (Operando2)
        print('Calculando...')
        if (Operacion == 'S'):
            print('Operacion Seleccionada: Suma')
            Resultado = Operando1 + Operando2
        elif(Operacion == 'R'):
            print('Operacion Seleccionada: Resta')
            Resultado = Operando1 - Operando2           
        elif(Operacion == 'P' or Operacion == 'M'):
            print('Operacion Seleccionada: Producto')
            Resultado = Operando1 * Operando2
        elif(Operacion == 'D'):
            print('Operacion Seleccionada: Division')
            if (Operando2 == 0):
                print('Esta tratando de realizar division por cero, error')
                Resultado = 'ERROR'
            else:
                Resultado = Operando1 / Operando2
        else:
            print('No ingreso una Operacion Valida')
            
        

        print('Resultados \n')
        print('El Resultado es de',Resultado)    

        print ('Fin de Ejercicio22 \n')





    # Salida si selecciona 0 en primera opcion
    elif name == '0' :
        break
    # Preguntar Nuevamente por entrada no valida
    else :
        print ('Ingrese un numero del 1 al 13, usted ingresó %s , intente nuevamente' % name)
        name = input('Que Ejercicio desea ver? (1 al 13), 0 para salir \n')
        

print('Gracias! Vuelva prontos!')
