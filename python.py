def calculadora():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")
    
    if operacion == "+":
        print("Resultado:", num1 + num2)
    elif operacion == "-":
        print("Resultado:", num1 - num2)
    elif operacion == "*":
        print("Resultado:", num1 * num2)
    elif operacion == "/":
        if num2 != 0:
            print("Resultado:", num1 / num2)

calculadora()
