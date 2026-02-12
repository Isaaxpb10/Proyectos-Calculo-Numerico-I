📘 Métodos Numéricos en Python – Colección de Algoritmos
Este repositorio reúne una serie de algoritmos fundamentales de Cálculo Numérico, implementados en Python y documentados para uso académico.
Incluye métodos de búsqueda de raíces, interpolación e integración numérica, todos diseñados para comparar resultados aproximados con soluciones exactas mediante el error relativo.

Métodos Implementados:

🔹 1. Método de Bisección
Encuentra raíces encerradas en un intervalo 
[
𝑎
,
𝑏
]
.

Garantiza convergencia si la función cambia de signo.

Ideal para funciones continuas y problemas donde se requiere estabilidad.

🔹 2. Método de Newton–Raphson
Método iterativo basado en derivadas.

Convergencia rápida cuando se inicia cerca de la raíz.

Implementado usando funciones simbólicas para derivación automática.

🔹 3. Polinomio de Lagrange
Construye el polinomio interpolante a partir de puntos dados.

Permite evaluar la función aproximada en cualquier valor.

Útil para aproximación de datos experimentales.

🔹 4. Método de Riemann (Rectángulos)
Aproxima integrales definidas mediante sumas de rectángulos.

Implementado exactamente como se enseña en Cálculo Numérico:

Cálculo de 
ℎ

Generación de puntos 
𝑋
0
,
𝑋
1
,
.
.
.
,
𝑋
𝑛
−
1

Suma 
ℎ
[
𝑓
(
𝑋
0
)
+
𝑓
(
𝑋
1
)
+
.
.
.
]

Comparación con la integral exacta usando SymPy.

🛠️ Características Principales

Entrada dinámica de funciones
Los programas permiten ingresar funciones directamente desde consola, por ejemplo:

Código
3*x*sqrt(x**2 + 19)
x**2 * exp(x**3 + 1)
sin(x) + x**2

✔ Cálculo de la solución exacta
Se utiliza SymPy para:

Integración simbólica (método de Riemann)

Derivación automática (Newton–Raphson)

Evaluación precisa de expresiones

✔ Cálculo del error relativo
Cada método compara:

Valor aproximado

Valor exacto (cuando aplica)

Usando:

error
=
∣
𝐼
real
−
𝐼
aprox
∣
∣
𝐼
real
∣

✔ Código limpio y documentado
Cada archivo incluye:

Explicación del método

Comentarios detallados

Estructura modular

Buenas prácticas de programación

📂 Estructura del Repositorio
Código

📁 Métodos-Numericos

│── 📄 biseccion.py

│── 📄 newton_raphson.py

│── 📄 lagrange.py

│── 📄 riemann.py

│── 📄 README.md

▶️ Requisitos
Instalar SymPy:

Código
pip install sympy
Opcionalmente, NumPy:

Código
pip install numpy

📌 Ejemplo de uso (Método de Riemann)
Código
Ingresa la función f(x): 3*x*sqrt(x**2 + 19)
Límite inferior a: 0
Límite superior b: 2
Número de subintervalos n: 10
El programa mostrará:

h

Lista de Xi

Área aproximada

Integral exacta

Error relativo

👨‍💻 Autor
Isaac Carreño 31.841.776
Cálculo Numérico
Universidad UDO

⭐ Si este repositorio te fue útil, considera dejar una estrella en GitHub
