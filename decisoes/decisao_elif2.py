nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
doenca_infectocontagiosa = input('Suspeita de doença infecto-contagioga?').upper()

if idade >= 65 and doenca_infectocontagiosa == 'SIM':
    print('O paciente será direcionado para sala AMARELA - COM prioridade')
elif idade < 65 and doenca_infectocontagiosa == 'SIM':
    print('O paciente será direcionado para sala AMARELA - SEM prioridade')
elif idade >= 65 and doenca_infectocontagiosa == 'NAO':
    print('O paciente será direcionado para sala BRANCA - COM prioridade')
elif idade < 65 and doenca_infectocontagiosa == 'NAO':
    print('O paciente será direcionado para sala BRANCA - SEM prioridade')
else:
    print('Responda a suspeita de doença infectocontagiosa com SIM ou NAO')