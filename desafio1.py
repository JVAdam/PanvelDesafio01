## Funções
def verificaPositivo(num):
    if(num<0):
        return 0
    else:
        return 1
    
def mostraLinha(rex, oli, bob):
    for x in range(3):
        print(str(x+1)+".  ", end="")
        for i in range(21):
            print("-", end="")
            if(i == rex):
                print("R", end="")
            elif(i == oli):
                print("O", end="")
            elif(i == bob):
                print("B", end="")
        if(rex > oli):
            rex -= 1
        else:
            rex += 1
        if(bob > oli):
            bob -= 1
        else:
            bob += 1
        print("\n")


def mais_proximo(rex, oli, bob):
    distanciaRex = abs(oli - rex)
    distanciaBob = abs(oli - bob)

    if(distanciaRex>distanciaBob):
        vencedor = "Bob"
    elif(distanciaBob>distanciaRex):
        vencedor = "Rex"
    else:
        vencedor = "Oli"

    return vencedor

## ---------------------------------------------------------
## Main
rex = int(input("Informe a posição que Rex está: [0-20]\n"))
while verificaPositivo(rex)==0 or rex>20:
    print("Valor inválido, tente novamente!")
    print("Informe a posição de Rex: ")
    rex = int(input())

oli = int(input("Informe a posição que Oli está: [0-20]\n"))
while verificaPositivo(oli)==0 or oli>20:
    print("Valor inválido, tente novamente!")
    print("Informe a posição de Oli: ")
    rex = int(input())

bob = int(input("Informe a posição que Bob está: [0-20]\n"))
while verificaPositivo(bob)==0 or bob>20:
    print("Valor inválido, tente novamente!")
    print("Informe a posição de Bob: ")
    rex = int(input())

mostraLinha(rex, oli, bob)

if(mais_proximo(rex, oli, bob)=="Oli"):
    print("Oli fugiu!")
elif(mais_proximo(rex, oli, bob)=="Bob"):
    print("Bob chegou primeiro!")
else:
    print("Rex chegou primeiro!")