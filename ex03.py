fila = ["Ana", "Bruno", "Carla", "Diego"]

atendido = fila.pop(0)
fila.remove("Carla")
fila.append("Eva")

print(f"Foi antendido: {atendido}, fila atual: {fila}, o próximo a ser atendido é Bruno")