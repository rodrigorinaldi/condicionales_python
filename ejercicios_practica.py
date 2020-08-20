#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''
    print("ingresar primer numero")
    numero_1 = int(input())
    print("numero ingresado", numero_1)

    print("ingresar segundo numero")
    numero_2 = int(input())
    print("numero ingresado", numero_2)

    if numero_1 < numero_2:
        print("numero 2 es mayor")

    else:
        print("numero 2 es menor")    
    
    if numero_1 and numero_2 >= 0:
        print("positivo")

    else:
        print("negativo")    




def ej2():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''
    print("ingresar primer numero")
    numero_1 = int(input())
    print("numero ingresado", numero_1)

    print("ingresar segundo numero")
    numero_2 = int(input())
    print("numero ingresado", numero_2)

    print("ingresar tercer numero")
    numero_3 = int(input())
    print("numero ingresado", numero_3)

    if (numero_1 % 2) == 0:
        print(numero_1, "es par")
    else:
        print(numero_1, "es impar")  

    if (numero_2 % 2) == 0:
        print(numero_2, "es par")
    else:
        print(numero_2, "es impar") 

    if(numero_3 % 2) == 0:
        print(numero_3, "es par")
    else:
        print(numero_3, "es impar")      




def ej3():
    print('Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
    print(" ingresar dos numeros para luego sumarlos")

    print ("primer numero")
    numero_1 = int(input())
    print("numero ingresado", numero_1)

    print("segundo numero")
    numero_2 = int(input())
    print("numero ingresado", numero_2)

    print("sumar ambos numeros")
    suma = numero_1 + numero_2
    print("el resultado de la suma es", suma) 




def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''
    print("ingresar 3 palabras a elección")

    print("igresar primer palabra")
    palabra_1 = str(input())
    print("palabra ingresada", palabra_1)

    print("ingresar segunda palabra")
    palabra_2 = str(input())
    print("palabra ingresada", palabra_2)

    print("ingresar tercer palabra")
    palabra_3 = str(input())
    print("palabra ingresada", palabra_3)
    
    ordenar_1 =  "ordenar_por_alfabeto"
    ordenar_2 =  "ordenar_por_tamaño"

        




   
   
        

    











def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
    #ej5()
