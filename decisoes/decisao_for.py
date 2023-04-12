tabuada = int(input('Digite um número para exibir a tabuada: '))
print('Tabuada do número ', tabuada)

for valor in range(0, 11):
    print(str(tabuada) + ' x ' + str(valor) + ' = ' + str((tabuada * valor)))
