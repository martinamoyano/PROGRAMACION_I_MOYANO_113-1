from funciones import *

#----------------------------------------------------

A = None
B = None
flag_operaciones = False

while True: 
    limpiar_pantalla()
    match menu():
        case "1": 
            A = ingreso_operandos("primer")
            print(f"A = {A}")
        case "2":
            B = ingreso_operandos("segundo")
            print(f"B = {B}")
        case "3":
            flag_operaciones = True
            try:
                if not validar_existencia_operandos(A, B):
                    raise ValueError("No se ingresaron los operandos necesarios para realizar las operaciones. Por favor, reingrese los operandos.")
                suma = suma(A, B)
                resta = resta(A, B)
                division = division(A, B)
                multiplicacion = multiplicacion(A, B)
                factorial_a = factorial(A)
                factorial_b = factorial(B)
                print("Operaciones calculadas con éxito.")
            except ValueError as e:
                print(e)
                flag_operaciones = False
        case "4":
            try: 
                if not flag_operaciones:
                    raise RuntimeError("No se pueden mostrar los resultados porque primero debe realizar las operaciones.")
                informar_operaciones(A, B, suma, resta, multiplicacion, division, factorial_a, factorial_b)
            except RuntimeError as e:
                print(e)
        case "5":
            print("\n¡Hasta luego! 👋 \n" )
            break
        case _:
            print("Opción invalida. Reingrese su opción (1-5)")
    pausa()