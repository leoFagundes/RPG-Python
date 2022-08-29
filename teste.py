import random

#(dano, vida, velAtaque, ouroDropado)
monstrosDG1 = {"Aranha": [4, 1, 20, 0], 
               "Cobra": [4, 2, 40, 0],
               "Lobo": [6, 3, 8, 0],
               "Urso": [12, 5, 8, 0]}
               
bossDG1 = {"Bad Wolf": [5, 8, 500, 0]}


def statusMonstros(monstro, forca, vida, velAtaque):
    print("\033[36m__\033[m"*15)
    print("")
    print(f"STATUS {monstro}")
    print(f"\033[1mForça:\033[m \033[31m{forca:^2}\033[m")
    print(f"\033[1mVida:\033[m \033[32m{vida:^2}\033[m")
    print(f"\033[1mVelocidade de Ataque:\033[m \033[35m{velAtaque:^2}\033[m")
    print("\033[36m__\033[m"*15)

monstroAtual = random.choices(list(monstrosDG1), weights = [100, 100, 90, 5])

print(monstroAtual[0])




'''print(f"\nVocê encontrou um {monstroAtual}: \nSTATUS:")
statusMonstros(monstroAtual, danoMonstro, vidaMonstro, velAtaqueMonstro)'''
