"""
PROYECTO DE CÁLCULO NUMÉRICO
Método de Riemann (Rectángulos)
Autor: Isaac Carreño

Descripción:
------------
Este programa implementa el método numérico de Riemann utilizando
rectángulos simples para aproximar el valor de una integral definida.

El procedimiento sigue exactamente la metodología vista en clase:

1. Se define el intervalo [a, b] y el número de subintervalos n.
2. Se calcula el tamaño del paso:
       h = (b - a) / n
3. Se generan los puntos:
       X0 = a
       X1 = X0 + h
       X2 = X1 + h
       ...
       X(n-1) = a + (n-1)*h
4. Se calcula el área aproximada mediante:
       A ≈ h * [ f(X0) + f(X1) + ... + f(X(n-1)) ]
5. Se calcula el valor real de la integral usando SymPy.
6. Se calcula el error relativo:
       error = |I_real - I_aprox| / |I_real|

El programa imprime:
- El valor de h
- Los puntos Xi generados
- El área aproximada
- El valor real de la integral
- El error relativo
"""

import numpy as np
from math import *
import sympy as sp


def f(x, func_str):
    """
    Evalúa la función ingresada por el usuario.

    Parámetros:
    -----------
    x : float
        Punto donde se evaluará la función.
    func_str : str
        Cadena que representa la función, por ejemplo: "sin(x) + x**2".

    Retorna:
    --------
    float : valor de f(x)
    """
    return eval(func_str)


def riemann(a, b, n, func_str):
    """
    Implementa el método de Riemann (rectángulos simples) tal como se vio en clase.

    Parámetros:
    -----------
    a : float
        Límite inferior del intervalo.
    b : float
        Límite superior del intervalo.
    n : int
        Número de subintervalos.
    func_str : str
        Función f(x) ingresada por el usuario.

    Retorna:
    --------
    area_aprox : float
        Aproximación de la integral mediante rectángulos.
    h : float
        Tamaño del paso.
    x : list
        Lista de puntos Xi generados.
    """

    a = float(a)
    b = float(b)
    n = int(n)

    # Tamaño del paso
    h = (b - a) / n

    # Generación de los puntos Xi: X0, X1, ..., X(n-1)
    x = [a + i * h for i in range(n)]

    # Cálculo del área aproximada: h * sum(f(Xi))
    area_aprox = 0
    for xi in x:
        area_aprox += h * f(xi, func_str)

    return area_aprox, h, x


def integral_real(a, b, func_str):
    """
    Calcula la integral exacta usando SymPy.

    Parámetros:
    -----------
    a, b : float
        Límites de integración.
    func_str : str
        Función f(x) ingresada por el usuario.

    Retorna:
    --------
    float : valor real de la integral
    """

    x = sp.symbols('x')

    # Convertir la función del usuario a expresión simbólica
    # Reemplazamos funciones de Python por las de SymPy
    func_sym = func_str.replace("sqrt", "sp.sqrt") \
                       .replace("sin", "sp.sin") \
                       .replace("cos", "sp.cos") \
                       .replace("tan", "sp.tan") \
                       .replace("exp", "sp.exp") \
                       .replace("log", "sp.log")

    funcion = eval(func_sym)

    integral = sp.integrate(funcion, (x, a, b))
    return float(integral)


def main():
    """
    Función principal del programa.
    Solicita los datos al usuario y muestra los resultados.
    """

    print("=== MÉTODO DE RIEMANN (RECTÁNGULOS) ===")
    print("Autor: Isaac Carreño\n")

    # Entrada de datos
    func_str = input("Ingresa la función f(x): ")
    a = float(input("Límite inferior a: "))
    b = float(input("Límite superior b: "))
    n = int(input("Número de subintervalos n: "))

    # Cálculo con el método de Riemann
    area_aprox, h, x = riemann(a, b, n, func_str)

    # Cálculo del valor real mediante SymPy
    area_real = integral_real(a, b, func_str)

    # Cálculo del error relativo
    error_rel = abs(area_real - area_aprox) / abs(area_real)

    # Resultados
    print("\n--- RESULTADOS ---")
    print(f"h = {h}")
    print(f"Puntos Xi = {x}")
    print(f"Área aproximada = {area_aprox}")
    print(f"Área real = {area_real}")
    print(f"Error relativo = {error_rel}")

    print("\nCálculo completado correctamente.")


if __name__ == "__main__":
    main()
