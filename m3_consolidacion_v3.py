from random import shuffle

def hacer_grandioso(mago):
    mago = (f"El gran {mago}")
    return(mago)

def imprimir_nombres(nombre):
    print(nombre)
    return()

listaFamosos = [
                "Harry Houdini",
                "Isaac Newton",
                "David Blaine",
                "Steven Hawking",
                "Lionel Messi",
                "Raymond Teller",
                "Albert Einstein",
                "O Rey Pele",
                "Juanes"
                ]

#for x in range(len(listaFamosos)):
#    imprimir_nombres(listaFamosos[x])

shuffle(listaFamosos)
shuffle(listaFamosos)

for x in range(len(listaFamosos)):
    imprimir_nombres(listaFamosos[x])

print()
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("::::::::::::::Magos Grandiosos::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print()

for x in range(len(listaFamosos)):
    if (listaFamosos[x]=="Harry Houdini") or (listaFamosos[x]=="David Blaine") or (listaFamosos[x]=="Raymond Teller"):
        imprimir_nombres(hacer_grandioso(listaFamosos[x]))
print()
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print(":::::::::::::Cientificos Famosos::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print()

for x in range(len(listaFamosos)):
    if (listaFamosos[x]=="Isaac Newton") or (listaFamosos[x]=="Steven Hawking") or (listaFamosos[x]=="Albert Einstein"):
        imprimir_nombres(listaFamosos[x])

print()
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print(":::::::::::::::::Otros Famosos::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print()

for x in range(len(listaFamosos)):
    if (listaFamosos[x]=="Lionel Messi") or (listaFamosos[x]=="O Rey Pele") or (listaFamosos[x]=="Juanes"):
        imprimir_nombres(listaFamosos[x])
