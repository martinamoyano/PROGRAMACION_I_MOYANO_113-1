'''
1. Ingresar 1er operando (A=x)
2. Ingresar 2do operando (B=y)
3. Calcular todas las operaciones
4. Informar resultados
    a) “El resultado de A+B es: r”
    b) “El resultado de A-B es: r”
    c) “El resultado de A/B es: r” o “No es posible dividir por cero”
    d) “El resultado de A*B es: r”
    e) “El factorial de A es: r1 y El factorial de B es: r2”
5. Salir
• Todas las funciones matemáticas del menú se deberán realizar en una biblioteca aparte,que contenga las funciones
para realizar las cinco operaciones.
• En el menú deberán aparecer los valores actuales cargados en los operandos A y B(donde dice “x” e “y” en el ejemplo,
se debe mostrar el número cargado)
• Deberán contemplarse los casos de error (división por cero, etc.)
• Documentar todas las funciones
'''

from funciones import *

#----------------------------------------------------

A = None
B = None

while True: 
    limpiar_pantalla()
    match menu():
        case "1": 
            A = (ingreso_operandos("primer"))
            print(f"A = {A}")
        case "2":
            B = (ingreso_operandos("segundo"))
            print(f"B = {B}")
        case "3":
            try:
                calcular_operaciones(A, B)
                print("Operaciones calculadas con éxito.")
            except ValueError as e:
                print(e)
        case "4":
            print("D")
        case "5":
            print("\n¡Hasta luego! 👋 \n" )
            break
        case _:
            print("Opción invalida. Reingrese su opción (1-5)")
    pausa()