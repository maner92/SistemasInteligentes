import random


class neuron:
    def __init__(self):
        self.w1 = random.uniform(-1, 1)
        self.w2 = random.uniform(-1, 1)
        self.theta = random.uniform(-1, 1)

    # Funcion de activación
    def activation(self, x_1, x_2):
        u = self.w1 * x_1 + self.w2 * x_2 - self.theta
        if u >= 0:
            return 1
        else:
            return 0

# Creación tabla de verdad


def create_table():
    print("Tabla de verdad:")
    print("\tX_1\t\t X_2\t\tExit")
    for x_1 in [0, 1]:
        for x_2 in [0, 1]:
            y = x_1 or x_2
            print("\t{}\t\t{}\t\t{}".format(x_1, x_2, y))

# Función para entrenar la celular OR


def train_OR_neuron(neuron):
    # Valores de entrada y salida esperados para la compuerta OR
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    targets = [0, 1, 1, 1]

    # Entrenamiento de la célula de McCulloch-Pitts para la compuerta OR
    epoch = 0
    error = 1
    while error != 0 and epoch < 100:
        error = 0
        for i, input_pair in enumerate(inputs):
            x1, x2 = input_pair
            target = targets[i]
            output = neuron.activation(x1, x2)
            if output != target:
                error += 1
                neuron.w1 += 0.1 * (target - output) * x1
                neuron.w2 += 0.1 * (target - output) * x2
                neuron.theta -= 0.1 * (target - output)
        epoch += 1

    # Imprimir los valores de los pesos y umbral encontrados
    print("Pesos encontrados: w1={}, w2={}".format(neuron.w1, neuron.w2))
    print("Umbral encontrado: theta={}".format(neuron.theta))

# Función para comprobar valores de peso y umbral


def check_OR(neuron):
    print("Revisando la celula para la compuerta OR:")
    for x_1 in [0, 1]:
        for x_2 in [0, 1]:
            y = x_1 or x_2
            output = neuron.activation(x_1, x_2)
            if output != y:
                print(
                    "Error: La célula de McCulloch-Pitts no funciona correctamente para la compuerta OR.")
                return
    print("La célula de McCulloch-Pitts funciona correctamente para la compuerta OR.")


create_table()
neuron = neuron()
train_OR_neuron(neuron)
check_OR(neuron)
