import platform
import getpass
from datetime import datetime

print("Nome maquina: ............", platform.node())
print("Arquitetura: .............", platform.architecture())
print("Sistema Operacional: .....", platform.system())
print("Versao do SO: ............", platform.release())
print("Processador: .............", platform.processor())
print("Versao do Python: ........", platform.python_version())

print(datetime.now())