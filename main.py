import random

#(forca, vida, velAtaque, ouroDropado, chanceFuga)
monstrosDG1 = {"Aranha": [4, 1, 20, 0, 55], 
               "Cobra": [4, 2, 40, 0, 55],
               "Lobo": [6, 3, 8, 0, 40],
               "Urso": [12, 5, 8, 0, 60]}

bossDG1 = {"Bad Wolf": [5, 8, 500, 0]}


#(forca, vida, velAtaque)
itensBossDG1 = {"Armadura Bad Wolfão (lendário)": [0, 0, 0],
                "Espada Bad Wolfiado (lendário)": [0, 0, 0],
                "Adaga de presa de lobo (raro)": [0, 0, 0],
                "Espada quebrada (comum)": [0, 0, 0],
                "Armadura furada (comum)": [0, 0, 0]}

#testando sistema de itens
statusItens = [0, 0, 0]

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

#satatusBoss
def statusBoss(monstro, forca, vida, velAtaque, ouro):
    print("\033[36m__\033[m"*15)
    print("")
    print(f"\033[1mBoss:\033[m \033[36m{monstro}\033[m")
    print(f"\033[1mForça:\033[m \033[31m{forca:^2}\033[m")
    print(f"\033[1mVida:\033[m \033[32m{vida:^2}\033[m")
    print(f"\033[1mVelocidade de Ataque:\033[m \033[35m{velAtaque:^2}\033[m")
    print(f"\033[1mRecompensa:\033[m \033[33m{ouro:^2}\033[m moedas de ouro")
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
                        exit()
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
                        exit()
                    print(f"\033[1mSua vida atual: \033[32m{vidas}\033[m\n")

                    input("\033[1mPróximo turno\033[m\n")
            print("\033[31mVocê matou o monstro\033[m, \033[1mvamos continuar a jornada.\033[m")
            print(f"Ouro dropado: {monstrosDG1[monstroAtual[0]][3]}")
            ouro += monstrosDG1[monstroAtual[0]][3]
            vida = vidas
            return print(f"Sua vida atual é {vidas}")

def batalhaBoss(vidas, bossDG, itensBossDG):
    global ouro
    global vida
    global forca
    global velAtaque
    global statusItens
    contadorVasculhar = 0
    while True:
        print("""Deseja 
                    1-atacar 
                    2-vasculhar sala
            """)
        escolha = int(input())
        if escolha == 1:
            statusBoss("Bad Wolf", bossDG1["Bad Wolf"][0], bossDG1["Bad Wolf"][1], bossDG1["Bad Wolf"][2], bossDG1["Bad Wolf"][3])
            input("\033[1mComeçar a batalha\033[m\n")
            vidaAtualBoss = bossDG[list(bossDG)[0]][1]
            while vidaAtualBoss > 0:
                if bossDG[list(bossDG)[0]][2] > velAtaque:
                    print(f"""
                    A velocidade do boss te superou.

                    \033[31mAtaque do {list(bossDG)[0]}: {bossDG[list(bossDG)[0]][0]}\033[m
                    """)
                    vidas -= bossDG[list(bossDG)[0]][0]
                    if vidas <= 0:
                        print("Você morreu, tente novamente em uma próxima vida.")
                        exit()
                    print(f"\033[mSua vida atual: \033[32m{vidas}\033[m\n")

                    input("\033[1mPróximo turno\033[m\n")

                    print(f"""
                    Sua vez de atacar:

                    \033[31mAtaque: {forca}\033[m
                    """)
                    vidaAtualBoss -= forca
                    print(f"\033[1mVida do {list(bossDG)[0]}: \033[32m{vidaAtualBoss}\033[m\n")
                    if vidaAtualBoss <= 0:
                        break

                    input("\033[1mPróximo turno\033[m\n")
                else:
                    print(f"""
                    Você foi mais rápido que o boss, sua vez de atacar.
                    \033[31mAtaque: {forca}\033[m
                    """)
                    vidaAtualBoss -= forca
                    print(f"\033[1mVida do {list(bossDG)[0]}: \033[32m{vidaAtualBoss}\033[m\n")
                    if vidaAtualBoss <= 0:
                        break

                    input("\033[1mPróximo turno\033[m\n")

                    print(f"""
                    Turno do boss.
                    \033[31mAtaque do boss: {bossDG[list(bossDG)[0]][0]}\033[m
                    """)
                    vidas -= bossDG[list(bossDG)[0]][0]
                    if vidas <= 0:
                        print("Você morreu, tente novamente em uma próxima vida.")
                        exit()
                    print(f"\033[1mSua vida atual: \033[32m{vidas}\033[m\n")

                    input("\033[1mPróximo turno\033[m\n")
            print(f"\033[31mVocê matou o temido {list(bossDG)[0]}\033[m, \033[1mvamos continuar a jornada.\033[m")
            item = list(itensBossDG)
            itemGanho = random.choices(item, weights=[2, 5, 15, 40, 40])
            print("Você tem chance de ganhar um dos seguintes itens: \n")
            print("\n".join(item))
            print(f"""\nO item dropado foi: 
                    {itemGanho[0]}
                    Força: +{itensBossDG[itemGanho[0]][0]}
                    Vida: +{itensBossDG[itemGanho[0]][1]}
                    Velocidade de Ataque: +{itensBossDG[itemGanho[0]][2]}
                    """)
            print("Você deseja equipa-lo?")
            escolha = int(input("1-sim\n2-não\n"))
            if escolha == 1:
                print(f"Você equipou {itemGanho[0]}")
                forca -= statusItens[0]
                vida -= statusItens[0]
                velAtaque -= statusItens[0]
                statusItens = []
                statusItens.append(itensBossDG[itemGanho[0]][0])
                statusItens.append(itensBossDG[itemGanho[0]][1])
                statusItens.append(itensBossDG[itemGanho[0]][2])
                forca += statusItens[0]
                vida += statusItens[0]
                velAtaque += statusItens[0]
                
            elif escolha == 2:
                pass
            print(f"\nOuro dropado: {bossDG[list(bossDG)[0]][3]}")
            ouro += bossDG[list(bossDG)[0]][3]
            vida = vidas
            return print(f"Sua vida atual é {vidas}")
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
                print(f"Você pisou em falso, uma armadilha explodiu e você tomou {vidaVasculhada} de dano.")
                vida -= vidaVasculhada
                print(f"Vida atual: {vida}")
                contadorVasculhar += 1
                continue
        elif escolha == 2 and contadorVasculhar == 1:
            print("Você já vasculhou toda a sala do Boss\n")
            continue
        else:
            print("Digite um valor válido, não sabe ler?\n")
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

        batalhaBoss(vida, bossDG1, itensBossDG1)