import random

#(dano, vida, velAtaque, ouroDropado)
monstrosDG1 = {"Aranha": [4, 1, 20, 0], 
               "Cobra": [4, 2, 40, 0],
               "Lobo": [6, 3, 8, 0],
               "Urso": [12, 5, 8, 0]}
bossDG1 = {"Bad Wolf": [5, 8, 500, 0]}

forca = 1
vida = 100
ouro = 0
velAtaque = 10

#status monstros
def statusMonstros(monstro, forca, vida, velAtaque):
    print("\033[36m__\033[m"*15)
    print("")
    print(f"\033[1mMonstro:\033[m \033[36m{monstro}\033[m")
    print(f"\033[1mForça:\033[m \033[31m{forca:^2}\033[m")
    print(f"\033[1mVida:\033[m \033[32m{vida:^2}\033[m")
    print(f"\033[1mVelocidade de Ataque:\033[m \033[35m{velAtaque:^2}\033[m")
    print("\033[36m__\033[m"*15)

#status personagem
def status():
    print("\033[36m__\033[m"*15)
    print("")
    print(f"\033[1mForça:\033[m \033[31m{forca:^2}\033[m")
    print(f"\033[1mVida:\033[m \033[32m{vida:^2}\033[m")
    print(f"\033[1mOuro:\033[m \033[33m{ouro:^2}\033[m")
    print(f"\033[1mVelocidade de Ataque:\033[m \033[35m{velAtaque:^2}\033[m")
    print("\033[36m__\033[m"*15)

#função para o ataque do monstro
def ataqueMonstro(vida):
    vidaAtualMonstro = monstrosDG1[monstroAtual[0]][1]
    while vidaAtualMonstro > 0:
        if monstrosDG1[monstroAtual[0]][2] > velAtaque:
            print(f"""
            O monstro é mais rápido que você, aventureiro.

            Ataque do monstro: {monstrosDG1[monstroAtual[0]][0]}
            """)
            vida -= monstrosDG1[monstroAtual[0]][0]
            if vida <= 0:
                print("Você morreu, tente novamente em uma próxima vida.")
                break
            print(f"Vida atual: {vida}")

            input()

            print(f"""
            Sua vez de atacar:

            Ataque: {forca}
            """)
            vidaAtualMonstro -= forca
            print(f"Vida do monstro: {vidaAtualMonstro}")
            if vidaAtualMonstro <= 0:
                break

            input()
        else:
            print(f"""
            Você é mais rápido que o monstro, sua vez de atacar.
            Ataque: {forca}
            """)
            vidaAtualMonstro -= forca
            print(f"Vida do monstro: {vidaAtualMonstro}\n")
            if vidaAtualMonstro <= 0:
                break

            input()

            print(f"""
            Turno do monstro.
            Ataque do monstro: {monstrosDG1[monstroAtual[0]][0]}
            """)
            vida -= monstrosDG1[monstroAtual[0]][0]
            if vida <= 0:
                print("Você morreu, tente novamente em uma próxima vida.")
                break
            print(f"Vida atual: {vida}")

            input()
    print("Você matou o monstro, vamos continuar a jornada.")            

print("""\033[1m
Bem-vindos a rede dungeon, iremos dar as instruções:

Seu objetivo é conquistar as 10 dungeons espalhadas pelo mundo, para conquistar cada uma você deve matar o BOSS que nela reside.
Além disso você tem os seus STATUS, que começam da seguinte forma:\033[m
(Obs: quando o código parar dê um enter para continuar)
""")

status()

#main
while vida > 0:
    print("-"*30)
    print("Você está no saguão, para onde deseja ir?")
    print("""
            0 - Loja de itens
            1 - Dark Forest (Dungeon lvl 1) 
        """)
    escolha = int(input())

    if escolha == 0:
        print("""
        ---------LOJA---------
        Esse é o nosso catálogo:
        -
        -
        -
        -
        - 0 sair
        """)
        escolha = int(input())
        if escolha == 0:
            continue

    elif escolha == 1:
        print("""
        Você entrou na Dark Forest (dungeon de nível 1)...

        Muitos monstros vagam por essas terras sombrias e amaldiçoadas, 
        você como um bom e confiante aventureiro seguiu em frente na busca da cabeça do temido BAD WOLF.
        """)
        print("Você encontrou um monstro, hora de lutar.")

        monstroAtual = random.choices(list(monstrosDG1), weights = [100, 100, 90, 4])
        print(f"\n\nVocê encontrou um(a) {monstroAtual[0]}:")
        statusMonstros(monstroAtual[0], monstrosDG1[monstroAtual[0]][0], monstrosDG1[monstroAtual[0]][1], monstrosDG1[monstroAtual[0]][2])

        ataqueMonstro(vida)



