basedados = []

with open("manipulacao_arquivos/iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        basedados.append(registro.split(","))

print(float(basedados[0][0]) + float(basedados[1][0]))
