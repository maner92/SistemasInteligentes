import random
import itertools

# Definir la función que representa la célula de McCulloch-Pitts


def mcculloch_pitts(x, w, theta):
    potencial = sum([x[i]*w[i] for i in range(len(x))])
    if potencial >= theta:
        return 1
    else:
        return 0


# Definir una función para generar todas las combinaciones posibles de entradas


def generate_inputs(n):
    return list(itertools.product([0, 1], repeat=n))


# Definir una función para generar una tabla de verdad para una compuerta lógica determinada


def generate_truth_table(inputs, function):
    table = []
    for x in inputs:
        output = function(x)
        table.append((x, output))
    return table


# Entrenar la célula de McCulloch-Pitts para obtener los pesos y el umbral adecuados para una compuerta lógica determinada


def train(x, y, lr=0.1, epochs=1000):
    w = [random.uniform(0, 1) for i in range(len(x[0]))]
    theta = random.uniform(0, 1)
    for epoch in range(epochs):
        for i in range(len(x)):
            output = mcculloch_pitts(x[i], w, theta)
            error = y[i] - output
            w = [w[j] + lr*error*x[i][j] for j in range(len(w))]
            theta = theta + lr*error
    return w, theta


# Definir la función que representa el Perceptrón Simple


def perceptron_simple(x, w, b):
    potencial = sum([x[i]*w[i] for i in range(len(x))]) + b
    if potencial >= 0:
        return 1
    else:
        return 0


# Escoger la compuerta lógica y las entradas
gate = input("Selecciona la compuerta lógica (AND, OR, NOT): ")
n = int(input("Selecciona el número de entradas: "))

# Definir la función que representa la compuerta lógica elegida
if gate == "AND":
    def function(x): return 0 if 0 in x else 1
elif gate == "OR":
    def function(x): return 1 if 1 in x else 0
elif gate == "NOT":
    def function(x): return 0 if x[0] == 1 else 1
else:
    print("Compuerta lógica no válida.")
    exit()

# Generar todas las combinaciones posibles de entradas
inputs = generate_inputs(n)

# Generar la tabla de verdad para la compuerta lógica elegida
truth_table = generate_truth_table(inputs, function)
print("Tabla de verdad para la compuerta lógica", gate, "con", n, "entradas:")
for row in truth_table:
    print(row)

# Entrenar el Perceptrón Simple para la compuerta lógica elegida
x = [row[0] for row in truth_table]
y = [row[1] for row in truth_table]
w, b = train(x, y)

# Imprimir los pesos y el umbral entrenados
print("Pesos entrenados:", w)
print("Umbral entrenado:", b)

# Imprimir la salida del Perce
print("Salida del Perceptrón Simple para todas las combinaciones posibles de entradas:")
for x in inputs:
    output = perceptron_simple(x, w, b)
print(x, "->", output)