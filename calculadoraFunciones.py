import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def raiz_cuadrada(a):
    return math.sqrt(a)

def potencia(a, b):
    return a ** b

while True:
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Raíz Cuadrada")
    print("6. Potencia")
    print("7. Salir")

    try:
        opcion = int(input("Seleccione una operación (1/2/3/4/5/6/7): "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 7:
        print("Saliendo de la calculadora...")
        break

    if opcion == 5 or opcion == 6:
        try:
            n1 = float(input("Ingrese el número: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
    else:
        try:
            n1 = float(input("Ingrese el primer número: "))
            n2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Por favor, ingrese números válidos.")
            continue

    if opcion == 1:
        resultado = suma(n1, n2)
    elif opcion == 2:
        resultado = resta(n1, n2)
    elif opcion == 3:
        resultado = multiplicacion(n1, n2)
    elif opcion == 4:
        resultado = division(n1, n2)
    elif opcion == 5:
        resultado = raiz_cuadrada(n1)
    elif opcion == 6:
        try:
            num2 = float(input("Ingrese el exponente: "))
            resultado = potencia(n1, n2)
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
    else:
        print("Opción inválida")
        continue

    print("Resultado:", resultado)
