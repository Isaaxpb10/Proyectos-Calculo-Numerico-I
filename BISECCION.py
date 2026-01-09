# MÉTODO DE BISECCIÓN EN PYTHON 
# Realizado por: Isaac Carreño CI: 31.841.776

import math

# Función evaluable segura
f = lambda x: eval(funcion_input, {
    "x": x,
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "exp": math.exp, "log": math.log, "sqrt": math.sqrt,
    "atan": math.atan, "pi": math.pi, "e": math.e
})

def biseccion(f, a, b, Es, NI):
    """
    f  : función evaluable F(x)
    a, b : intervalo [a, b]
    Es : error máximo permitido (%)
    NI : número máximo de iteraciones 
    """

    Ea = 100        # Error aproximado relativo (%)
    i = 1           # Contador de iteraciones
    M_Actual = 0    # Punto medio actual
    M_Previa = 0    # Punto medio previo

    print("\n--- PROCESO ITERATIVO ---")
    while (i <= NI) and (Ea > Es):
        M_Previa = M_Actual
        M_Actual = (a + b) / 2
        
        if f(M_Actual) * f(b) < 0:
            a = M_Actual
        else:
            b = M_Actual

        if i > 1:
            Ea = abs((M_Actual - M_Previa) / M_Actual) * 100

        print(f"Iteración {i:2d}: a={a:.6f}, b={b:.6f}, M={M_Actual:.6f}, Ea={Ea:.6f}%")
        
        i += 1

    print("\n--- RESULTADO FINAL ---")
    print(f"Raíz aproximada: {M_Actual:.6f}")
    print(f"Error aproximado: {Ea:.6f}%")
    print(f"Iteraciones realizadas: {i-1}")
    return M_Actual

# ----------------------------------------------------------
# PROGRAMA PRINCIPAL
# ----------------------------------------------------------

print("Método de Bisección - Interactivo")
print("---------------------------------")
print("Puedes usar funciones con operaciones de 'math', por ejemplo:")
print("x**3 - x - 2   |   math.sin(x) - x/2   |   math.exp(-x) - x\n")

# Ingreso de datos
funcion_input = input("Ingresa la función f(x): ")
a = float(input("Ingresa el límite inferior (a): "))
b = float(input("Ingresa el límite superior (b): "))
Es = float(input("Ingresa el error permitido (%): "))
NI = int(input("Ingresa el número máximo de iteraciones: "))


# Validar signo en los extremos
if f(a) * f(b) > 0:
    print("\n Error: f(a) y f(b) deben tener signos opuestos.")
    print("No se cumple el teorema de Bolzano. Intenta con otro intervalo.")
else:
    biseccion(f, a, b, Es, NI)
