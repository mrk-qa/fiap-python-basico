with open("manipulacao_arquivos/primeiro_arquivo.json", "r") as arquivo:
  for linha in arquivo.readlines():
    print(linha)