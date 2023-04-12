import json

with open("manipulacao_arquivos/primeiro_arquivo.json", "w") as arquivo:

    obj = {
        "json": {
            "teste": "teste",
            "teste1": "teste1",
            "teste2": "teste2",
            "teste3": "teste3"
        }
    }
    
    jsonString = json.dumps(obj)
    
    arquivo.write(jsonString)