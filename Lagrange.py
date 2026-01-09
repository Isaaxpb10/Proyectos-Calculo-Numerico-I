# Proyecto de Cálculo Numérico
# Interpolación Polinómica - Polinomio de Lagrange con ordenamiento y trazabilidad
# Realizado por: Isaac Carreño CI: 31.841.776

import sympy as sp

# ==============================
# Utilidades de formato
# ==============================
def mostrar_numero(valor):
    # Si es entero, muestra como entero
    if float(valor).is_integer():
        return str(int(valor))
    else:
        return str(valor)

def formato_factor(xj):
    # Devuelve (x - a) si xj > 0, (x + a) si xj < 0, y (x) si xj == 0
    # Usando números "naturales" (sin .0)
    if float(xj) == 0.0:
        return "(x)"
    elif xj > 0:
        return f"(x - {mostrar_numero(xj)})"
    else:
        return f"(x + {mostrar_numero(abs(xj))})"

# ==============================
# Utilidades de impresión (tablas)
# ==============================
def imprimir_tabla(titulo, puntos):
    print(f"\n{titulo}")
    print("-" * len(titulo))
    print(f"{'i':>3} | {'xi':>12} | {'yi':>12}")
    print("-" * 36)
    for i, (xi, yi) in enumerate(puntos):
        print(f"{i:>3} | {mostrar_numero(xi):>12} | {mostrar_numero(yi):>12}")
    print("-" * 36)

# ==============================
# Construcción de L_i(x) paso a paso (texto)
# ==============================
def construir_Li_texto(i, puntos):
    """
    Devuelve:
    - factores del numerador: lista de strings "(x - xj)" o "(x + a)" si xj < 0
    - denominador: producto (xi - xj) para j != i
    - representación textual de Li(x)
    """
    xi, _ = puntos[i]
    denominador = 1
    factores = []
    for j, (xj, _) in enumerate(puntos):
        if j != i:
            factores.append(formato_factor(xj))
            denominador *= (xi - xj)
    Li_texto = "(" + " * ".join(factores) + f") / {mostrar_numero(denominador)}"
    return factores, denominador, Li_texto

# ==============================
# Polinomio de Lagrange (simbólico con SymPy)
# ==============================
def polinomio_lagrange_sympy(puntos):
    """
    Construye el polinomio de Lagrange:
    - Retorna P(x) expandido (SymPy) y la variable simbólica x
    - También retorna la versión en productos (sin expandir)
    """
    x = sp.Symbol('x')
    n = len(puntos)
    P_prod = 0  # forma en productos (sin expandir)
    for i in range(n):
        xi, yi = puntos[i]
        Li = 1
        for j in range(n):
            if j != i:
                xj, _ = puntos[j]
                Li *= (x - xj) / (xi - xj)
        P_prod += yi * Li
    P_exp = sp.expand(P_prod)
    return P_prod, P_exp, x

def polinomio_lagrange_productos(puntos):
    """
    Construye la expresión del polinomio de Lagrange en forma de productos (sin expandir),
    mostrando coeficientes como fracciones exactas y factores con signos limpios.
    """
    partes = []
    for i in range(len(puntos)):
        xi, yi = puntos[i]
        denominador = 1
        factores = []
        for j in range(len(puntos)):
            if j != i:
                xj, _ = puntos[j]
                factores.append(formato_factor(xj))
                denominador *= (xi - xj)
        coef = sp.Rational(yi, denominador)
        termino = f"{coef} " + "".join(factores)  # sin espacios entre factores: (x-1)(x-2)
        partes.append(termino)
    return "P(x) = " + " + ".join(partes)

# ==============================
# Impresión de la fórmula Pn y de los Li(x)
# ==============================
def mostrar_formula_Pn(puntos):
    terminos = [f"y{i}·L{i}(x)" for i in range(len(puntos))]
    print("\nFórmula general del polinomio de Lagrange:")
    print("Pn(x) = " + " + ".join(terminos))

def mostrar_Li_detallados(puntos, etiquetas_originales):
    """
    Muestra, para cada i:
    - Numerador (factores)
    - Denominador
    - Li(x) textual
    - y_i * Li(x) textual
    Conservar las etiquetas originales y0, y1, ... según el orden ingresado.
    """
    print("\nConstrucción detallada de cada Li(x):")
    for i in range(len(puntos)):
        xi, yi = puntos[i]
        factores, denom, Li_txt = construir_Li_texto(i, puntos)
        print(f"\n- L{i}(x):")
        print(f"  • xi = {mostrar_numero(xi)}")
        print(f"  • Numerador: " + (" * ".join(factores) if factores else "1"))
        print(
            "  • Denominador: "
            + " * ".join([f"({mostrar_numero(xi)} - {mostrar_numero(xj)})"
                          for j, (xj, _) in enumerate(puntos) if j != i])
        )
        print(f"    = {mostrar_numero(denom)}")
        print(f"  • Forma final: L{i}(x) = {Li_txt}")
        print(f"  • y{i}·L{i}(x) = {etiquetas_originales[i]} * {Li_txt} = {mostrar_numero(yi)} * {Li_txt}")

# ==============================
# Trazabilidad de la comprobación P(xk) = yk
# ==============================
def comprobar_en_puntos_simple(puntos, P, x):
    """
    Comprueba que P(xi) = yi para cada punto ingresado.
    """
    print("\nComprobación de interpolación:")
    for i, (xi, yi) in enumerate(puntos):
        valor = float(P.subs(x, xi))
        print(f"P(x{i}) = P({mostrar_numero(xi)}) = {mostrar_numero(valor)}  →  esperado: y{i} = {mostrar_numero(yi)}")

# ==============================
# Programa principal (interactivo)
# ==============================
def main():
    print("=== Proyecto de Cálculo Numérico ===")
    print("Interpolación Polinómica de Lagrange con ordenamiento y trazabilidad\n")

    # Captura de puntos por teclado
    while True:
        try:
            n = int(input("Ingrese el número de puntos: "))
            if n < 2:
                print("Se requieren al menos 2 puntos. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Ingrese un entero.")
    puntos_ingresados = []
    print("\nIngrese los puntos (xi, yi) en el orden que desee:")
    for i in range(n):
        while True:
            try:
                xi = float(input(f"  x{i}: "))
                yi = float(input(f"  y{i}: "))
                puntos_ingresados.append((xi, yi))
                break
            except ValueError:
                print("  Entrada inválida. Use números reales. Intente de nuevo.")

    # Etiquetas originales (y0, y1, ..., yn) según orden de ingreso
    etiquetas_originales = [f"y{i}" for i in range(n)]

    # Mostrar tabla en el orden ingresado
    imprimir_tabla("Tabla de datos (orden ingresado)", puntos_ingresados)

    # Ordenar por xi ascendente y mostrar
    puntos_ordenados = sorted(puntos_ingresados, key=lambda p: p[0])
    imprimir_tabla("Tabla de datos (ordenada ascendentemente por xi)", puntos_ordenados)

    # Fórmula general y construcción de Li sobre la tabla ordenada
    mostrar_formula_Pn(puntos_ordenados)
    mostrar_Li_detallados(puntos_ordenados, etiquetas_originales)

    # Construir P(x): forma en productos y expandida (usando la tabla ordenada)
    P_prod, P_exp, x = polinomio_lagrange_sympy(puntos_ordenados)

    print("\nPolinomio armado (forma de productos):")
    print(polinomio_lagrange_productos(puntos_ordenados))

    # Comprobación paso a paso en cada xi ordenado
    comprobar_en_puntos_simple(puntos_ordenados, P_prod, x)

    # Evaluaciones adicionales opcionales
    while True:
        opcion = input("\n¿Desea evaluar el polinomio en otro valor de x? (s/n): ").strip().lower()
        if opcion == "s":
            try:
                val = float(input("Ingrese el valor de x: "))
                val_num = float(sp.N(P_prod.subs(x, val)))
                print(f"P({mostrar_numero(val)}) = {mostrar_numero(val_num)}")
            except ValueError:
                print("Entrada inválida. Intente de nuevo.")
        elif opcion == "n":
            print("\nPrograma finalizado. ¡Excelente trabajo!")
            break
        else:
            print("Opción inválida. Responda 's' o 'n'.")

if __name__ == "__main__":
    main()