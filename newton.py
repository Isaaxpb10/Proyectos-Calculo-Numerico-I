# MÉTODO DE NEWTON RAPHSON EN PYTHON 
# Realizado por: Isaac Carreño CI: 31.841.776

import math

# Función evaluable segura
def f(x, expr):
    return eval(expr, {"x": x, "sin": math.sin, "cos": math.cos,
                       "tan": math.tan, "exp": math.exp, "log": math.log, "atan": math.atan})

# Derivada numérica
def derivada_automatica(x, expr):
    h = 1e-6
    return (f(x + h, expr) - f(x - h, expr)) / (2 * h)

print("\n=== MÉTODO DE NEWTON–RAPHSON ===")

# Ingreso de función
f_str = input("Ingrese f(x): ")

# Derivada opcional
op = input("¿Desea ingresar f'(x)? (s/n): ").lower()
if op == "s":
    fprime_str = input("Ingrese f'(x): ")
    usar_derivada_usuario = True
else:
    print("→ Se usará derivada automática.")
    usar_derivada_usuario = False

# Datos iniciales
x0 = float(input("Ingrese x0: "))
Es = float(input("Ingrese el error permitido (%): "))

Ea = 100
iteracion = 0

# TABLA SIMPLIFICADA
print("\nIter |       Xi       |      Xi+1      |   Error (%)")
print("--------------------------------------------------------")

while Ea > Es:
    fx = f(x0, f_str)

    # Derivada
    if usar_derivada_usuario:
        fpx = eval(fprime_str, {"x": x0, "sin": math.sin, "cos": math.cos,
                                "tan": math.tan, "exp": math.exp, "log": math.log, "atan": math.atan})
    else:
        fpx = derivada_automatica(x0, f_str)

    if fpx == 0:
        print("La derivada vale 0. No se puede continuar.")
        break

    x1 = x0 - fx/fpx

    if iteracion > 0:
        Ea = abs((x1 - x0) / x1) * 100

    print(f"{iteracion:4} | {x0:12.8f} | {x1:12.8f} | {Ea:10.6f}")

    x0 = x1
    iteracion += 1

print("\nRAÍZ APROXIMADA:", x0)
print("ERROR FINAL:", Ea)
print("ITERACIONES:", iteracion)
