#Programa de Ejercicios Practico 7 por Javier Chiappa
import math
import random

# Asignamos un valor a name para entrar al bucle
name = 'a'
# Bucle principal sale con cero
while name != '0':
    print("Ejercicios Practico Programacion Numero 7: Recursivas")
    name = input('Que Ejercicio desea ver? (1 al 13), 0 para salir \n')
    print('Opcion Seleccionada, %s!' % name)

    # Ejercicio 1
    if name == '1' :
        print("Consigna: Realizar la funcion de fibonacci en forma recursiva")

        def fib(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fib(n - 1) + fib(n - 2)

        numero = 0
        numero = input("Ingrese valor de fibonacci: ")
        numero = int (numero)
        print("Valor Fibonacci de : ",fib(numero))


    # # Ejercicio 2
    # if name == '2' :
    #     print("Consigna: Escribir una función recursiva que devuelva la suma de los primeros N enteros")
    #
    #     def sum(n)



    # Ejercicio 3
##    if name == '3' :
##        print("Consigna: un método recursivo que calcule el producto de un arreglo de números enteros")
##        vector = [23, 21, 19, 14, 38]
##
##        print("Largo del vector", len(vector))
##        def prod(n,ans):
##            print("largo del vector: ",len(vector) )
##
##                ans = prod(m,(vector[m-2] * vector[m-1]))
##                #ans = ans * prod((n+1),ans)
##                print(ans)
##                print("vuelta numero ",n)
##            return n,ans
##
##
##        print(prod(5,0))


    # Salida si selecciona 0 en primera opcion
    elif name == '0':
        break
    # Preguntar Nuevamente por entrada no valida

print('Gracias! Vuelva prontos!')
