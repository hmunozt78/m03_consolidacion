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

magos = []
cientificos = []
otros= []

for x in range(len(listaFamosos)):
    imprimir_nombres(listaFamosos[x])

    if (listaFamosos[x]=="Harry Houdini") or (listaFamosos[x]=="David Blaine") or (listaFamosos[x]=="Raymond Teller"):
        magos.append(listaFamosos[x])

    if (listaFamosos[x]=="Isaac Newton") or (listaFamosos[x]=="Steven Hawking") or (listaFamosos[x]=="Albert Einstein"):
        cientificos.append(listaFamosos[x])
    
    if (listaFamosos[x]=="Lionel Messi") or (listaFamosos[x]=="O Rey Pele") or (listaFamosos[x]=="Juanes"):
        otros.append(listaFamosos[x])


print()
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("::::::::::::::Magos Grandiosos::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print()

for x in range(len(magos)):
    imprimir_nombres(hacer_grandioso(magos[x]))
print()
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print(":::::::::::::Cientificos Famosos::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print()

for x in range(len(cientificos)):
    imprimir_nombres(cientificos[x])

print()
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print(":::::::::::::::::Otros Famosos::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print()

for x in range(len(otros)):
    imprimir_nombres(otros[x])
