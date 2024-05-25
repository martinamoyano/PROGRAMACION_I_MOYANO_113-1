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
    resultado = None
    if b != 0:
        resultado = a/b 
    return resultado

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
    
def informar_operaciones(a, b: int, suma, resta, multiplicacion, division, factorial_a, factorial_b):
    print(f"El resultado de {a}+{b} es: {suma} \n"
          f"El resultado de {a}-{b} es: {resta} \n"
          f"El resultado de {a}*{b} es: {multiplicacion} \n"
          f"El factorial de {a} es: {factorial_a} y El factorial de {b} es: {factorial_b}")
    if division != None:
        print(f"El resultado de {a}/{b} es: {division}")
    else:
        print("No se puede dividir por cero")





