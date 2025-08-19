def suma(a, b):
    """Realiza la suma de dos números"""
    return a + b

def resta(a, b):
    """Realiza la resta de dos números"""
    return a - b

def multiplicacion(a, b):
    """Realiza la multiplicación de dos números"""
    return a * b

def division(a, b):
    """Realiza la división de dos números con manejo de división por cero"""
    if b == 0:
        raise ValueError("Error: No se puede dividir por cero")
    return a / b

def obtener_numero(mensaje):
    """Obtiene un número válido del usuario"""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Por favor ingresa un número válido")

def main():
    """Función principal del programa"""
    print("=== CALCULADORA PYTHON ===")
    print("Operaciones disponibles: suma, resta, multiplicación, división")
    print("Escribe 'salir' para terminar el programa")
    print("-" * 40)
    
    # Diccionario de operaciones para una estructura más limpia
    operaciones = {
        'suma': suma,
        'resta': resta,
        'multiplicación': multiplicacion,
        'multiplicacion': multiplicacion,  # Versión sin acento
        'división': division,
        'division': division  # Versión sin acento
    }
    
    while True:
        # Obtener la operación del usuario
        operacion = input("\nIngresa la operación: ").lower().strip()
        
        # Verificar si el usuario quiere salir
        if operacion == 'salir':
            print("¡Gracias por usar la calculadora!")
            break
        
        # Verificar si la operación es válida
        if operacion not in operaciones:
            print(f"Error: Operación '{operacion}' no válida")
            print("Operaciones válidas:", ", ".join(operaciones.keys()))
            continue
        
        # Obtener los números
        try:
            num1 = obtener_numero("Ingresa el primer número: ")
            num2 = obtener_numero("Ingresa el segundo número: ")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break
        
        # Realizar la operación
        try:
            resultado = operaciones[operacion](num1, num2)
            print(f"\nResultado: {num1} {operacion} {num2} = {resultado}")
        except ValueError as e:
            print(f"\n{e}")
        except Exception as e:
            print(f"\nError inesperado: {e}")

if __name__ == "__main__":
    main()
