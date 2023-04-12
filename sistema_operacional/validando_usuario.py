import getpass

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha: ........")

if usuario == "mrk" and senha == "hello_python":
    print("Bem vindo Marco")
else:
    print("Você não tem acesso")