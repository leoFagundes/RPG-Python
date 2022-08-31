import random

#(dano, vida, velAtaque, ouroDropado, chanceFuga)
monstrosDG1 = {"Aranha": [4, 1, 20, 0, 55], 
               "Cobra": [4, 2, 40, 0, 55],
               "Lobo": [6, 3, 8, 0, 40],
               "Urso": [12, 5, 8, 0, 60]}

bossDG1 = {"Bad Wolf": [5, 8, 500, 0]}

#()
itensBossDG1 = {"Armadura Bad Wolfão (lendário)": [],
                "Espada Bad Wolfiado (lendário)": [],
                "Adaga de presa de lobo (raro)": [],
                "Espada quebrada (comum)": [],
                "Armadura furada (comum)": []}

forca = 1
vida = 100
ouro = 0
velAtaque = 10

contadorFuga = 0

#status monstros
def statusMonstros(monstro, forca, vida, velAtaque, fuga):
    print("\033[36m__\033[m"*15)
    print("")
    print(f"\033[1mMonstro:\033[m \033[36m{monstro}\033[m")
    print(f"\033[1mForça:\033[m \033[31m{forca:^2}\033[m")
    print(f"\033[1mVida:\033[m \033[32m{vida:^2}\033[m")
    print(f"\033[1mVelocidade de Ataque:\033[m \033[35m{velAtaque:^2}\033[m")
    print(f"\033[1mChance de fuga:\033[m \033[33m{fuga:^2}%\033[m")
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
def batalha(vidas, monstrosDG):
    global ouro
    global vida
    global contadorFuga

    monstroAtual = random.choices(list(monstrosDG1), weights = [100, 100, 90, 4])
    print(f"\n\n\033[1mVocê encontrou um(a) \033[36m{monstroAtual[0]}\033[m:")
    statusMonstros(monstroAtual[0], monstrosDG1[monstroAtual[0]][0], monstrosDG1[monstroAtual[0]][1], monstrosDG1[monstroAtual[0]][2], monstrosDG1[monstroAtual[0]][4])
    while True:
        print("""Deseja 
                1-atacar 
                2-tentar fugir?
                """)
        escolha = int(input())
        if escolha != 1 and escolha != 2:
            print("Escolha um valor válido.\n")
            continue

        if escolha == 2:
            chances = ['fugiu', 'naofugiu']
            chance = random.choices(chances, weights = [monstrosDG1[monstroAtual[0]][4], 100-monstrosDG1[monstroAtual[0]][4]])
            if chance[0] == 'fugiu':
                print(f"Com {monstrosDG1[monstroAtual[0]][4]}% de chance de escapar, você conseguiu fugir com sucesso")
                contadorFuga = 1
                break
            elif chance[0] == 'naofugiu':
                print("Você tentou fugir, porém o monstro foi mais rápido e te atacou.")
                print("Consequência: levou 10 de dano")
                print(f"Vida atual = {vidas - 10}\n")
                vidas -= 10
                continue
        elif escolha == 1:
            input("\033[1mComeçar a batalha\033[m\n")
            vidaAtualMonstro = monstrosDG[monstroAtual[0]][1]
            while vidaAtualMonstro > 0:
                if monstrosDG[monstroAtual[0]][2] > velAtaque:
                    print(f"""
                    O monstro foi mais rápido que você, aventureiro.

                    \033[31mAtaque do monstro: {monstrosDG[monstroAtual[0]][0]}\033[m
                    """)
                    vidas -= monstrosDG1[monstroAtual[0]][0]
                    if vidas <= 0:
                        print("Você morreu, tente novamente em uma próxima vida.")
                        break
                    print(f"\033[mSua vida atual: \033[32m{vidas}\033[m\n")

                    input("\033[1mPróximo turno\033[m\n")

                    print(f"""
                    Sua vez de atacar:

                    \033[31mAtaque: {forca}\033[m
                    """)
                    vidaAtualMonstro -= forca
                    print(f"\033[1mVida do monstro: \033[32m{vidaAtualMonstro}\033[m\n")
                    if vidaAtualMonstro <= 0:
                        break

                    input("\033[1mPróximo turno\033[m\n")
                else:
                    print(f"""
                    Você foi mais rápido que o monstro, sua vez de atacar.
                    \033[31mAtaque: {forca}\033[m
                    """)
                    vidaAtualMonstro -= forca
                    print(f"\033[1mVida do monstro: \033[32m{vidaAtualMonstro}\033[m\n")
                    if vidaAtualMonstro <= 0:
                        break

                    input("\033[1mPróximo turno\033[m\n")

                    print(f"""
                    Turno do monstro.
                    \033[31mAtaque do monstro: {monstrosDG1[monstroAtual[0]][0]}\033[m
                    """)
                    vidas -= monstrosDG1[monstroAtual[0]][0]
                    if vidas <= 0:
                        print("Você morreu, tente novamente em uma próxima vida.")
                        break
                    print(f"\033[1mSua vida atual: \033[32m{vidas}\033[m\n")

                    input("\033[1mPróximo turno\033[m\n")
            print("\033[31mVocê matou o monstro\033[m, \033[1mvamos continuar a jornada.\033[m")
            print(f"Ouro dropado: {monstrosDG1[monstroAtual[0]][3]}")
            ouro += monstrosDG1[monstroAtual[0]][3]
            vida = vidas
            return print(f"Sua vida atual é {vidas}")

def batalhaBoss():
    global ouro
    global vida
    contadorVasculhar = 0
    while True:
        print("""Deseja 
                    1-atacar 
                    2-vasculhar sala
            """)
        escolha = int(input())
        if escolha == 1:
            pass
        elif escolha == 2 and contadorVasculhar == 0:
            salaBoss = ["ouro", "vida", "armadilha"]
            recompensa = random.choices(salaBoss, weights=[1, 1, 1])
            if recompensa[0] == "ouro":
                ouroVasculhado = random.randint(20, 110)
                print(f"Você encontou {ouroVasculhado} moedas de ouro.")
                ouro += ouroVasculhado
                print(f"Ouro atual: {ouro}")
                contadorVasculhar += 1
                continue
            elif recompensa[0] == "vida":
                print("Você encontou uma poção de vida média.")
                print("Vida recuperada: 20")
                vida += 20
                print(f"Vida atual: {vida}")
                contadorVasculhar += 1
                continue
            elif recompensa[0] == "armadilha":
                vidaVasculhada = random.randint(5, 20)
                print(f"Você pisou em falso em uma armadilha e tomou {vidaVasculhada} de dano.")
                vida -= vidaVasculhada
                print(f"Vida atual: {vida}")
                contadorVasculhar += 1
                continue
        elif escolha == 2 and contadorVasculhar == 1:
            print("Você já vasculhou toda a sala do Boss")
            continue
        else:
            print("Digite um valor válido, não sabe ler?")
            continue


def loja():
    print(f"""\033[1;30m\n
    {"LOJA":^25}
    {"Esse é o nosso catálogo:":^25}
    {"-":<25}
    {"-":<25}
    {"-":<25}
    {"-":<25}
    {"-":<25}
    {"0 - sair da loja":<25}\n
    \033[m""")
    
############################################################################################################################################
print("""\033[1m
Bem-vindos a rede dungeon, iremos dar as instruções:

Seu objetivo é conquistar as 10 dungeons espalhadas pelo mundo, para conquistar cada uma você deve matar o BOSS que nela reside.
Além disso você tem os seus STATUS, que começam da seguinte forma:\033[m
(Obs: quando o código parar dê um enter para continuar)
""")

status()

#main
while vida > 0:
    contadorFuga = 0
    print("\033[1m-\033[m"*30)
    print("\033[1mVocê está no saguão, para onde deseja ir?\033[m")
    print("""\033[1;30m
           -1 - Visualizar Status
            0 - Loja de itens
            1 - Dark Forest (Dungeon lvl 1) \033[m
        """)
    escolha = int(input())

    if escolha == -1:
        status()
        input()

    elif escolha == 0:
        loja()
        escolha = int(input())
        if escolha == 0:
            continue

    elif escolha == 1:
        print("""
        Você entrou na Dark Forest (dungeon de nível 1)...

        Muitos monstros vagam por essas terras sombrias e amaldiçoadas, 
        você como um bom e confiante aventureiro seguiu em frente na busca da cabeça do temido BAD WOLF.
        """)
        print("Monstro à vista, hora de lutar.")

        batalha(vida, monstrosDG1)
        if contadorFuga == 1:
            continue

        print("óh não, outro monstro à vista.")
        input()
        batalha(vida, monstrosDG1)
        if contadorFuga == 1:
            continue

        print("""\n
        Após derrotar os braços direitos do grande e temido BAD WOLF você se preparar para o pior,
        pois irritou o boss da dungeon.
        Depois de 2 horas de caminhada pela Dark Forest você escuta um uivo assustador 60º a oeste, 
        nesse momento você se depara com o BAD WOLF.\n
        """)

        batalhaBoss()