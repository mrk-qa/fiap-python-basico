usuarios = {}
usuarios = {
    "chaves":["Chaves Silva","17/06/2017","Recep_01"],
    "quico":["Enrico Flores","03/06/2017","Raiox_02"]
}

print(usuarios)

#add florinda
usuarios["florinda"]=["Florinda Flores", "26/11/2017", "Recep_01"]

print(usuarios)

print("####---------####")

#get em quico
print(usuarios.get("quico"))