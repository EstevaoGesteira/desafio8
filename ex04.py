convidados = []

for i in range(4):
    convidado = input("Digite o nome do convidado: ")
    convidados.append(convidado)
convidados.sort()

print(f"Total de convidados: {len(convidados)}")
for convidados in convidados:
    print(convidados)