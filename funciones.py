from os import system

def suma(a: int, b: int)-> int:
    """Suma dos numeros enteros

    Args:
        a (int): primer numero a sumar
        b (int): segundo numero a sumar

    Returns:
        int: Resultado de la suma 
    """
    return a + b

def resta(a: int, b: int)-> int:
    """Resta dos numeros enteros

    Args:
        a (int): primer numero 
        b (int): segundo numero 

    Returns:
        int: Resultado de la resta 
    """
    return a - b

def division(a: int, b: int)-> float:
    """Divide dos números

    Args:
        a (int): primer número (dividendo)
        b (int): segundo número (divisor)

    Returns:
        float: Resultado de la división.
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError ("Error. No se puede dividir por cero")
    
def multiplicacion(a:int, b:int)-> int:
    """Multiplica dos números

    Args:
        a (int): primer numero (multiplicando)
        b (int): segundo numero (multiplicador)

    Returns:
        int: Resultado de la multiplicación
    """
    return a * b

def factorial(num:int)-> int:
    """Devuelve el factorial de un número

    Args:
        num (int): Número a factorizar

    Returns:
        int: Número factorizado
    """
    if num < 0:
        raise ValueError("Error. Solo se pueden factorizar números naturales.")

    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def limpiar_pantalla():
    """Limpia la consola
    """
    system("cls")

def pausa():
    """Detiene la ejecución del script y muestra un mensaje que pide al usuario presionar una tecla para continuar. 
    """
    system("pause")

def menu()-> int:
    """Menú de opciones al usuario

    Returns:
        int: Devuelve la opción seleccionada
    """
    print("          Menú de opciones")
    print("-------------------------------------")
    print("1 - Ingresar primer operando \n"
          "2 - Ingresar segundo operando \n"
          "3 - Calcular todas las operaciones \n"
          "4 - Informar resultados \n"
          "5 - Salir")
    print("-------------------------------------")

    return input("Ingrese opción deseada: ")

def ingreso_operandos(orden: str)-> int:
    """Permite el ingreso de operandos para realizar las cuentas

    Args:
        orden (str): Indica qué operando se está ingresando (primero, segundo, etc)

    Returns:
        int: Devuelve el numero ingresado para operar con él
    """
    while True:
        try:
            valor = int(input(f"Ingrese el {orden} operando: "))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def validar_existencia_operandos(a, b: int)-> bool:
    validacion = (a != None and b != None)
    return validacion
        
def calcular_operaciones(a, b: int)-> None:
    if not validar_existencia_operandos(a, b):
        raise ValueError("No se ingresaron los operandos necesarios para realizar las operaciones. Por favor, reingrese los operandos.")

    suma(a, b)
    resta(a, b)
    division(a, b)
    multiplicacion(a, b)
    factorial(a)
    factorial(b)
    


