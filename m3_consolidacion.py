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

for x in range(len(listaFamosos)):
    imprimir_nombres(listaFamosos[x])

print()
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("::::::::::::::Magos Grandiosos::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print()

for x in range(len(listaFamosos)):
    if (x==0) or (x==2) or (x==5):
        imprimir_nombres(hacer_grandioso(listaFamosos[x]))
print()
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print(":::::::::::::Cientificos Famosos::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print()

for x in range(len(listaFamosos)):
    if (x==1) or (x==3) or (x==6):
        imprimir_nombres(listaFamosos[x])

print()
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print(":::::::::::::::::Otros Famosos::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print()

for x in range(len(listaFamosos)):
    if (x==4) or (x==7) or (x==8):
        imprimir_nombres(listaFamosos[x])
