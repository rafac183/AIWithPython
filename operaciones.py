def sumar(a: float, b: float) -> float:
    """
    Suma dos números y retorna el resultado.

    Args:
        a (float): Primer número a sumar
        b (float): Segundo número a sumar

    Returns:
        float: El resultado de la suma de a y b

    Raises:
        TypeError: Si alguno de los argumentos no es un número
    """
    # Validación de tipos
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los argumentos deben ser números")
    
    return a + b