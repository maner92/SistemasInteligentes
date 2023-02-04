import random

def hill_climbing(items, capacity):
    # Inicializar solución actual con una solución aleatoria
    current_solution = [random.randint(0, 1) for _ in range(len(items))]
    current_value = sum([items[i][1] for i in range(len(items)) if current_solution[i] == 1])
    current_weight = sum([items[i][0] for i in range(len(items)) if current_solution[i] == 1])

    while True:
        # Generar solución vecina
        next_solution = current_solution.copy()
        next_solution[random.randint(0, len(items) - 1)] = 1 - next_solution[random.randint(0, len(items) - 1)]
        next_value = sum([items[i][1] for i in range(len(items)) if next_solution[i] == 1])
        next_weight = sum([items[i][0] for i in range(len(items)) if next_solution[i] == 1])

        # Si la solución vecina es mejor o igual que la solución actual, actualizar la solución actual
        if next_value >= current_value and next_weight <= capacity:
            current_solution = next_solution
            current_value = next_value
            current_weight = next_weight
        else:
            # Si no se encuentra una solución mejor, detener el algoritmo
            break

    return current_solution, current_value

