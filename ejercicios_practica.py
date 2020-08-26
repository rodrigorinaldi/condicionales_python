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

    print("ingrese la operacion a realizar: +, -, *, /, **")
    operador = str(input())
    print("operador ingresado", operador)

    if operador == "+":
    
        suma = numero_1 + numero_2
        print('La suma entre {} y {} es {}'.format(numero_1, numero_2, suma))
    if operador == "-":

        resta = numero_1 - numero_2
        print('La resta entre {} y {} es {}'.format(numero_1, numero_2, resta))
    if operador == "*":

        multiplicacion = numero_1 * numero_2
        print('La multiplicacion entre {} y {} es {}'.format(numero_1, numero_2, multiplicacion))
    if operador == "/":

        division = numero_1 / numero_2
        print('La division entre {} y {} es {}'.format(numero_1, numero_2, division))
    if operador == "**":

        exponente = numero_1 ** numero_2
        print('El exponente entre {} y {} es {}'.format(numero_1, numero_2, exponente))


    #suma = (numero_1 + numero_2)
    #resta = (numero_1 - numero_2)
    #multiplicacion = (numero_1 * numero_2)
    #division = (numero_1 / numero_2)
    #potencia = (numero_1 ** numero_2)

    #if operador == (suma):
        #print("realizar operacion")
        #suma = str(input())
        #print("el resultado es", suma)
    
    #elif operador == (resta):
         #print("realizar operacion")
         #resta = str(input())
         #print("el resultado es", resta)

    #elif operador == (multiplicacion):
         #print("realizar operacion")
         #resta = str(input())
         #print("el resultado es", multiplicacion)

    #elif operador == (division):
         #print("realizar operacion")
         #resta = str(input())
         #print("el resultado es", division)

    #elif operador == (potencia):
         #print("realizar operacion")
         #resta = str(input())
         #print("el resultado es", potencia)        

    #else:
        #print("es incorrecto")
    
    

    
    
    
    

    


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
    #myStr = " Hello "
    #print(dir(myStr))

    

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

    
    print("elegir operacion a realizar tipeando 1 o 2" )
    operacion = str(input())
    print("operacion elegida", operacion)

    texto = [palabra_1, palabra_2, palabra_3]

    # texto.sort()
    #     print(texto)

    if operacion == "1":
        if palabra_1 > palabra_2 and palabra_3:
            print("{} es mayor que {} y que {}".format(palabra_1, palabra_2, palabra_3))
        if palabra_1 > palabra_2 < palabra_3:
            print("{} es mayor que {} y menor que {}".format(palabra_1, palabra_2, palabra_3))
        if palabra_1 < palabra_2 > palabra_3:
            print("{} es menor que {} y mayor que {}".format(palabra_1, palabra_2, palabra_3))

    if operacion == "2":
        if len(palabra_1) > len(palabra_2) > len(palabra_3):
            print("palabra_1 es mayor que palabra_2 y que palabra_3")
        if len(palabra_2) > len(palabra_3) > len(palabra_1):
            print("palabra_2 es mayor que palabra_1 y palabra_3")

        else:
            print("palabra_3 es mayor que 1 y 2")
        
        
        

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
    print("ingresar 3 valores diferentes")

    print("ingresar primer valor")
    valor_1 = str(input())
    print("valor ingresado", valor_1)

    print("ingresar segundo valor")
    valor_2 = str(input())
    print("valor ingresado", valor_2)

    print("ingresar tercer valor")
    valor_3 = str(input())
    print("valor ingresado", valor_3)

    valor_1 = 37
    valor_2 = 39
    valor_3 = 35

    if valor_1 > valor_2 and valor_3:
        print("el mayor es valor_1", valor_1)
    elif valor_2 > valor_1 and valor_3:
        print("el mayor es valor_2", valor_2)
    else:
        print("el 3 es el mayor", valor_3)

    
    
    if valor_1 < valor_2 < valor_3:
        print("el menor es valor_1", valor_1)
    elif valor_2 < valor_3 < valor_1:
        print("el menor es valor_2", valor_2)   
    else:
        print("el tercer valor es el menor", valor_3)



    promedio = (valor_1 + valor_2 + valor_3) / 3
    print("promedio", promedio)



             




    
if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
