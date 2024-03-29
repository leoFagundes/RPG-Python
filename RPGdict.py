import random

#----------------------------------------------------
#(forca, vida, velAtaque, ouroDropado, chanceFuga)
monstrosDG1 = {"Aranha (lvl 1)": [4, 1, 20, 20, 55], 
               "Cobra (lvl 1)": [4, 2, 40, 20, 55],
               "Lobo (lvl 1)": [6, 3, 8, 25, 40],
               "Urso (lvl 3)": [12, 5, 8, 50, 60]}

#(forca, vida=5, velAtaque, ouroDropado)
bossDG1 = {"Bad Wolf": [5, 5, 80, 200]}

#(forca, vida, velAtaque)
itensBossDG1 = {"\033[33;1mArmadura Bad Wolfão - lvl 1 (lendário)\033[m": [0, 50, 0],
                "\033[33;1mEspada Bad Wolfiado - lvl 1 (lendário)\033[m": [5, 0, 11],
                "\033[35;1mAdaga de presa de lobo - lvl 1 (épico)\033[m": [2, 0, 20],
                "\033[35;1mArmadura de pele de lobo - lvl 1 (épico)\033[m": [0, 25, 5],
                "\033[34;1mEspada quebrada - lvl 1 (raro)\033[m": [1, 0, 5],
                "\033[34;1mArmadura furada - lvl 1 (raro)\033[m": [0, 15, 0]}


#----------------------------------------------------
#(forca, vida, velAtaque, ouroDropado, chanceFuga)
monstrosDG2 = {"Goblin de Gelo (lvl 2)": [7, 3, 40, 40, 55], 
               "Espírito Congelado (lvl 2)": [8, 3, 5, 15, 55],
               "Druida de Gelo (lvl 3)": [15, 4, 10, 30, 40],
               "Golem de Gelo (lvl 4)": [20, 10, 5, 80, 65]}

#(forca, vida=10, velAtaque, ouroDropado)
bossDG2 = {"Frozen Dragon": [15, 10, 80, 350]}

#(forca, vida, velAtaque)
itensBossDG2 = {"\033[33;1mPeitoral Dragônico - lvl 2 (lendário)\033[m": [0, 100, 0],
                "\033[33;1mLança Zero Absoluto - lvl 2 (lendário)\033[m": [12, 0, 20],
                "\033[35;1mGarra de dragão - lvl 2 (épico)\033[m": [8, 0, 25],
                "\033[35;1mArmadura Congelada - lvl 2 (épico)\033[m": [0, 60, -10],
                "\033[34;1mEstaca de Gelo - lvl 2 (raro)\033[m": [3, 0, 10],
                "\033[34;1mBota Quebradiça - lvl 2 (raro)\033[m": [0, 20, 0]}

#----------------------------------------------------
#(forca, vida, velAtaque, ouroDropado, chanceFuga)
monstrosDG3 = {"Espectro (lvl 3)": [15, 12, 20, 40, 30], 
               "Poltergeist (lvl 3)": [12, 15, 20, 40, 30],
               "Banshee (lvl 3)": [25, 3, 36, 25, 31],
               "Holandês Voador (lvl 5)": [22, 15, 20, 150, 50]}

#(forca, vida=10, velAtaque, ouroDropado)
bossDG3 = {"Astaroth, O Demônio Infernal": [25, 18, 80, 600]}

#(forca, vida, velAtaque)
itensBossDG3 = {"\033[33;1mArmadura de Sangue de Demônio - lvl 3 (lendário)\033[m": [0, 320, 3],
                "\033[33;1mLivro Amaldiçoado - lvl 3 (lendário)\033[m": [70, 0, 5],
                "\033[35;1mFoice Espectral - lvl 3 (épico)\033[m": [40, 0, 15],
                "\033[35;1mCapa de Almas Perdidas - lvl 3 (épico)\033[m": [0, 240, 10],
                "\033[34;1mEspada Fantasma - lvl 3 (raro)\033[m": [25, 0, 10],
                "\033[34;1mAnel Espectral - lvl 3 (raro)\033[m": [0, 150, 5]}

#----------------------------------------------------
#(forca, vida, velAtaque, ouroDropado, chanceFuga)
monstrosDG4 = {"Marujo (lvl 4)": [45, 150, 20, 70, 30], 
               "Marinheiro (lvl 4)": [35, 220, 20, 72, 30],
               "Bucaneiro (lvl 5)": [60, 140, 1, 75, 34],
               "Barba Negra (lvl 7)": [95, 220, 70, 350, 50]}

#(forca, vida=10, velAtaque, ouroDropado)
bossDG4 = {"Kraken": [70, 270, 80, 1000]}

#(forca, vida, velAtaque)
itensBossDG4 = {"\033[33;1mArmadura de Escama - lvl 4 (lendário)\033[m": [20, 500, 2],
                "\033[33;1mMosquete - lvl 4 (lendário)\033[m": [150, 0, 5],
                "\033[35;1mRevólver de Pólvora - lvl 4 (épico)\033[m": [80, 0, 8],
                "\033[35;1mFarda Pirata - lvl 4 (épico)\033[m": [0, 340, 0],
                "\033[34;1mCimitarra Pirata - lvl 4 (raro)\033[m": [65, 0, 35],
                "\033[34;1mChapéu Pirata - lvl 4 (raro)\033[m": [0, 250, 5]}

#----------------------------------------------------
#(forca, vida, velAtaque, ouroDropado, chanceFuga)
monstrosDG5 = {"Shadow Dragon (lvl 6)": [15, 12, 20, 40, 30], 
               "Dracolich (lvl 6)": [12, 15, 20, 40, 30],
               "Beholder (lvl 7)": [25, 3, 36, 25, 31],
               "Lich King (lvl 9)": [22, 15, 20, 150, 50]}

#(forca, vida=10, velAtaque, ouroDropado)
bossDG5 = {"Rei Destruído": [25, 18, 80, 600]}

#(forca, vida, velAtaque)
itensBossDG5 = {"\033[33;1mCoroa do Rei Destruído - lvl 5 (lendário)\033[m": [0, 300, 0],
                "\033[33;1mEspada do Rei Destruído - lvl 5 (lendário)\033[m": [40, 0, 5],
                "\033[35;1mMachado dos Condenados - lvl 5 (épico)\033[m": [25, 0, 15],
                "\033[35;1mPeitoral de Escamas Sombrias - lvl 5 (épico)\033[m": [0, 130, 10],
                "\033[34;1mKatana Sombria - lvl 5 (raro)\033[m": [14, 0, 10],
                "\033[34;1mManto das Trevas - lvl 5 (raro)\033[m": [0, 80, 5]}

#----------------------------------------------------
#(forca, vida, velAtaque)
slot1 = [0, 0, 0, 'empty']      #mudar a cor
slot2 = [0, 0, 0, 'empty']
slot3 = [0, 0, 0, 'empty']
slot4 = [0, 0, 0, 'empty']
slot5 = [0, 0, 0, 'empty']

forca = 1
vida = 100
ouro = 0
velAtaque = 10

contadorFuga = 0
bool_slot4 = False
bool_slot5 = False

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
    print(f"\033[1mVida:\033[m \033[32m{vida:^2}/{100+slot1[1]+slot2[1]+slot3[1]+slot4[1]+slot5[1]:^2}\033[m")
    print(f"\033[1mOuro:\033[m \033[33m{ouro:^2}\033[m")
    print(f"\033[1mVelocidade de Ataque:\033[m \033[35m{velAtaque:^2}\033[m")
    print("\033[36m__\033[m"*15)
    if slot1[3] != 'empty':
        print(f"""\033[1;37mSlot 1\033[m - {slot1[3]}: 
                \033[31;1m+{slot1[0]}\033[m \033[1;37mde força\033[m
                \033[32;1m+{slot1[1]}\033[m \033[1;37mde vida\033[m
                \033[35;1m+{slot1[2]}\033[m \033[1;37mde velocidade de ataque\033[m""")
        print("\033[36m__\033[m"*15)
    if slot2[3] != 'empty':
        print(f"""\033[1;37mSlot 2\033[m - {slot2[3]}: 
                \033[31;1m+{slot2[0]}\033[m \033[1;37mde força\033[m
                \033[32;1m+{slot2[1]}\033[m \033[1;37mde vida\033[m
                \033[35;1m+{slot2[2]}\033[m \033[1;37mde velocidade de ataque\033[m""")
        print("\033[36m__\033[m"*15)
    if slot3[3] != 'empty':
        print(f"""\033[1;37mSlot 3\033[m - {slot3[3]}: 
                \033[31;1m+{slot3[0]}\033[m \033[1;37mde força\033[m
                \033[32;1m+{slot3[1]}\033[m \033[1;37mde vida\033[m
                \033[35;1m+{slot3[2]}\033[m \033[1;37mde velocidade de ataque\033[m""")
        print("\033[36m__\033[m"*15)
    if slot4[3] != 'empty':
        print(f"""\033[1;37mSlot 4\033[m - {slot4[3]}: 
                \033[31;1m+{slot4[0]}\033[m \033[1;37mde força\033[m
                \033[32;1m+{slot4[1]}\033[m \033[1;37mde vida\033[m
                \033[35;1m+{slot4[2]}\033[m \033[1;37mde velocidade de ataque\033[m""")
        print("\033[36m__\033[m"*15)
    if slot5[3] != 'empty':
        print(f"""\033[1;37mSlot 5\033[m - {slot5[3]}: 
                \033[31;1m+{slot5[0]}\033[m \033[1;37mde força\033[m
                \033[32;1m+{slot5[1]}\033[m \033[1;37mde vida\033[m
                \033[35;1m+{slot5[2]}\033[m \033[1;37mde velocidade de ataque\033[m""")
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

#função para a luta do monstro
def batalha(vidas, monstrosDG):
    global ouro
    global vida
    global contadorFuga

    monstroAtual = random.choices(list(monstrosDG), weights = [90, 90, 80, 10])
    print(f"\n\n\033[1mVocê encontrou um(a) \033[36m{monstroAtual[0]}\033[m:")
    statusMonstros(monstroAtual[0], monstrosDG[monstroAtual[0]][0], monstrosDG[monstroAtual[0]][1], monstrosDG[monstroAtual[0]][2], monstrosDG[monstroAtual[0]][4])
    while True:
        print("""\033[36;1mDeseja:\033[m 
                \033[1m1-atacar 
                2-tentar fugir\033[m
                """)
        escolha = input()
        if escolha == '1' or escolha == '2':
            escolha = int(escolha)
        else:
            continue
        if escolha != 1 and escolha != 2:
            print("Escolha um valor válido.\n")
            continue

        if escolha == 2:
            chances = ['fugiu', 'naofugiu']
            chance = random.choices(chances, weights = [monstrosDG[monstroAtual[0]][4], 100-monstrosDG[monstroAtual[0]][4]])
            if chance[0] == 'fugiu':
                print(f"Com {monstrosDG[monstroAtual[0]][4]}% de chance de escapar, você conseguiu fugir com sucesso")
                contadorFuga = 1
                break
            elif chance[0] == 'naofugiu':
                print("Você tentou fugir, porém o monstro foi mais rápido e te atacou.")
                print("Consequência: levou 10 de dano")
                print(f"Vida atual = {vidas - 10}\n")
                vidas -= 10
                vida = vidas
                continue
        elif escolha == 1:
            input("\n\033[31;1mComeçar a batalha\033[m\n\n")
            vidaAtualMonstro = monstrosDG[monstroAtual[0]][1]
            while vidaAtualMonstro > 0:
                if monstrosDG[monstroAtual[0]][2] > velAtaque:
                    print(f"""
                    \033[37;1mO monstro foi mais rápido que você, aventureiro.\033[m
                    \033[31mAtaque do monstro: {monstrosDG[monstroAtual[0]][0]}\033[m
                    """)
                    vidas -= monstrosDG[monstroAtual[0]][0]
                    if vidas <= 0:
                        print("Você morreu, tente novamente em uma próxima vida.")
                        exit()
                    print(f"\033[1mSua vida atual: \033[32m{vidas}\033[m\n")

                    input("\033[1mPróximo turno\033[m\n")

                    print(f"""
                     \033[37;1mSua vez de atacar:\033[m
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
                    \033[31mAtaque do monstro: {monstrosDG[monstroAtual[0]][0]}\033[m
                    """)
                    vidas -= monstrosDG[monstroAtual[0]][0]
                    if vidas <= 0:
                        print("Você morreu, tente novamente em uma próxima vida.")
                        exit()
                    print(f"\033[1mSua vida atual: \033[32m{vidas}\033[m\n")

                    input("\033[1mPróximo turno\033[m\n")
            print("\033[31mVocê matou o monstro\033[m, \033[1mvamos continuar a jornada.\033[m")
            print(f"\033[1mOuro dropado:\033[m \033[1;33m{monstrosDG[monstroAtual[0]][3]}\033[m")
            ouro += monstrosDG[monstroAtual[0]][3]
            vida = vidas
            return print(f"\033[1mSua vida atual é\033[m \033[32;1m{vidas}\033[m")

#função para a luta do boss
def batalhaBoss(vidas, bossDG, itensBossDG):
    global ouro
    global vida
    global forca
    global velAtaque
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global bool_slot4
    global bool_slot5
    contadorVasculhar = 0
    while True:
        print("""Deseja 
                    1-atacar 
                    2-vasculhar sala
            """)
        escolha = input()
        if escolha == '1' or escolha == '2':
            escolha = int(escolha)
        else:
            continue
        if escolha == 1:
            statusBoss(list(bossDG.keys())[0], bossDG[list(bossDG.keys())[0]][0], bossDG[list(bossDG.keys())[0]][1], bossDG[list(bossDG.keys())[0]][2], bossDG[list(bossDG.keys())[0]][3])
            input("\033[1mComeçar a batalha\033[m\n")
            vidaAtualBoss = bossDG[list(bossDG)[0]][1]
            while vidaAtualBoss > 0:
                if bossDG[list(bossDG)[0]][2] > velAtaque:
                    print(f"""
                    A velocidade do Boss te superou.
                    \033[31mAtaque do {list(bossDG)[0]}: {bossDG[list(bossDG)[0]][0]}\033[m
                    """)
                    vidas -= bossDG[list(bossDG)[0]][0]
                    if vidas <= 0:
                        print("Você morreu, tente novamente em uma próxima vida.")
                        exit()
                    print(f"\033[1mSua vida atual:\033[m \033[32m{vidas}\033[m\n")

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
            itemGanho = random.choices(item, weights=[5, 5, 20, 20, 35, 35])
            print("Você tem chance de ganhar um dos seguintes itens: \n")
            print("\n".join(item))
            print(f"""\n\033[37;1mO item dropado foi:\033[m 
                    {itemGanho[0]}
                    \033[31mForça: +{itensBossDG[itemGanho[0]][0]}\033[m
                    \033[32mVida: +{itensBossDG[itemGanho[0]][1]}\033[m
                    \033[33mVelocidade de Ataque: +{itensBossDG[itemGanho[0]][2]}\033[m
                    """)
            while True:
                print("\033[1;37mVocê deseja equipa-lo?\033[m")
                escolha = input("\033[37m1-sim\n2-não\n\033[m")
                if escolha == '1' or escolha == '2':
                    escolha = int(escolha)
                else:
                    continue
                if escolha == 1:
                    while True:
                        if bool_slot4 == True and bool_slot5 == True:
                            texto = f"""
                            \033[1;37mVocê deseja equipar em qual slot?
                                0 - Não Equipar
                                1 - slot 1 ({slot1[3]}) -> (Força: \033[31m{slot1[0]}\033[m | Vida: \033[32m{slot1[1]}\033[m | Velocidade de Ataque: \033[33m{slot1[2]}\033[m)
                                2 - slot 2 ({slot2[3]}) -> (Força: \033[31m{slot2[0]}\033[m | Vida: \033[32m{slot2[1]}\033[m | Velocidade de Ataque: \033[33m{slot2[2]}\033[m)
                                3 - slot 3 ({slot3[3]}) -> (Força: \033[31m{slot3[0]}\033[m | Vida: \033[32m{slot3[1]}\033[m | Velocidade de Ataque: \033[33m{slot3[2]}\033[m)
                                4 - slot 4 ({slot4[3]}) -> (Força: \033[31m{slot4[0]}\033[m | Vida: \033[32m{slot4[1]}\033[m | Velocidade de Ataque: \033[33m{slot4[2]}\033[m)
                                5 - slot 5 ({slot5[3]}) -> (Força: \033[31m{slot5[0]}\033[m | Vida: \033[32m{slot5[1]}\033[m | Velocidade de Ataque: \033[33m{slot5[2]}\033[m)
                                \033[m
                            """
                        elif bool_slot4 == False and bool_slot5 == True:
                            texto = f"""
                            \033[1;37mVocê deseja equipar em qual slot?
                                0 - Não Equipar
                                1 - slot 1 ({slot1[3]}) -> (Força: \033[31m{slot1[0]}\033[m | Vida: \033[32m{slot1[1]}\033[m | Velocidade de Ataque: \033[33m{slot1[2]}\033[m)
                                2 - slot 2 ({slot2[3]}) -> (Força: \033[31m{slot2[0]}\033[m | Vida: \033[32m{slot2[1]}\033[m | Velocidade de Ataque: \033[33m{slot2[2]}\033[m)
                                3 - slot 3 ({slot3[3]}) -> (Força: \033[31m{slot3[0]}\033[m | Vida: \033[32m{slot3[1]}\033[m | Velocidade de Ataque: \033[33m{slot3[2]}\033[m)
                                5 - slot 5 ({slot5[3]}) -> (Força: \033[31m{slot5[0]}\033[m | Vida: \033[32m{slot5[1]}\033[m | Velocidade de Ataque: \033[33m{slot5[2]}\033[m)
                                \033[m
                            """
                        elif bool_slot4 == True and bool_slot5 == False:
                            texto = f"""
                            \033[1;37mVocê deseja equipar em qual slot?
                                0 - Não Equipar
                                1 - slot 1 ({slot1[3]}) -> (Força: \033[31m{slot1[0]}\033[m | Vida: \033[32m{slot1[1]}\033[m | Velocidade de Ataque: \033[33m{slot1[2]}\033[m)
                                2 - slot 2 ({slot2[3]}) -> (Força: \033[31m{slot2[0]}\033[m | Vida: \033[32m{slot2[1]}\033[m | Velocidade de Ataque: \033[33m{slot2[2]}\033[m)
                                3 - slot 3 ({slot3[3]}) -> (Força: \033[31m{slot3[0]}\033[m | Vida: \033[32m{slot3[1]}\033[m | Velocidade de Ataque: \033[33m{slot3[2]}\033[m)
                                5 - slot 4 ({slot4[3]}) -> (Força: \033[31m{slot4[0]}\033[m | Vida: \033[32m{slot4[1]}\033[m | Velocidade de Ataque: \033[33m{slot4[2]}\033[m)
                                \033[m
                            """
                        elif bool_slot4 == False and bool_slot5 == False:
                            texto = f"""
                            \033[1;37mVocê deseja equipar em qual slot?
                                0 - Não Equipar
                                1 - slot 1 ({slot1[3]}) -> (Força: \033[31m{slot1[0]}\033[m | Vida: \033[32m{slot1[1]}\033[m | Velocidade de Ataque: \033[33m{slot1[2]}\033[m)
                                2 - slot 2 ({slot2[3]}) -> (Força: \033[31m{slot2[0]}\033[m | Vida: \033[32m{slot2[1]}\033[m | Velocidade de Ataque: \033[33m{slot2[2]}\033[m)
                                3 - slot 3 ({slot3[3]}) -> (Força: \033[31m{slot3[0]}\033[m | Vida: \033[32m{slot3[1]}\033[m | Velocidade de Ataque: \033[33m{slot3[2]}\033[m)
                                \033[m
                            """
                        print(texto)
                        escolha = input()
                        if escolha == '0' or escolha == '1' or escolha == '2' or escolha == '3' or escolha == '4' or escolha == '5':
                            escolha = int(escolha)
                        else:
                            continue
                        if escolha == 1:
                            print(f"Você equipou {itemGanho[0]}")
                            forca -= slot1[0]
                            vida -= slot1[1]
                            velAtaque -= slot1[2]

                            slot1 = []
                            slot1.append(itensBossDG[itemGanho[0]][0])
                            slot1.append(itensBossDG[itemGanho[0]][1])
                            slot1.append(itensBossDG[itemGanho[0]][2])
                            slot1.append(itemGanho[0])

                            forca += slot1[0]
                            vidas += slot1[1]
                            vida = vidas
                            vida += slot1[1]
                            velAtaque += slot1[2]
                            break
                        elif escolha == 2:
                            print(f"Você equipou {itemGanho[0]}")
                            forca -= slot2[0]
                            vida -= slot2[1]
                            velAtaque -= slot2[2]

                            slot2 = []
                            slot2.append(itensBossDG[itemGanho[0]][0])
                            slot2.append(itensBossDG[itemGanho[0]][1])
                            slot2.append(itensBossDG[itemGanho[0]][2])
                            slot2.append(itemGanho[0])

                            forca += slot2[0]
                            vidas += slot2[1]
                            vida = vidas
                            vida += slot2[1]
                            velAtaque += slot2[2]
                            break
                        elif escolha == 3:
                            print(f"Você equipou {itemGanho[0]}")
                            forca -= slot3[0]
                            vida -= slot3[1]
                            velAtaque -= slot3[2]

                            slot3 = []
                            slot3.append(itensBossDG[itemGanho[0]][0])
                            slot3.append(itensBossDG[itemGanho[0]][1])
                            slot3.append(itensBossDG[itemGanho[0]][2])
                            slot3.append(itemGanho[0])

                            forca += slot3[0]
                            vidas += slot3[1]
                            vida = vidas
                            vida += slot3[1]
                            velAtaque += slot3[2]
                            break
                        elif escolha == 4 and bool_slot4 == True:
                            print(f"Você equipou {itemGanho[0]}")
                            forca -= slot4[0]
                            vida -= slot4[1]
                            velAtaque -= slot4[2]

                            slot4 = []
                            slot4.append(itensBossDG[itemGanho[0]][0])
                            slot4.append(itensBossDG[itemGanho[0]][1])
                            slot4.append(itensBossDG[itemGanho[0]][2])
                            slot4.append(itemGanho[0])

                            forca += slot4[0]
                            vidas += slot4[1]
                            vida = vidas
                            vida += slot4[1]
                            velAtaque += slot4[2]
                            break
                        elif escolha == 5 and bool_slot5 == True:
                            print(f"Você equipou {itemGanho[0]}")
                            forca -= slot5[0]
                            vida -= slot5[1]
                            velAtaque -= slot5[2]

                            slot5 = []
                            slot5.append(itensBossDG[itemGanho[0]][0])
                            slot5.append(itensBossDG[itemGanho[0]][1])
                            slot5.append(itensBossDG[itemGanho[0]][2])
                            slot5.append(itemGanho[0])

                            forca += slot5[0]
                            vidas += slot5[1]
                            vida = vidas
                            vida += slot5[1]
                            velAtaque += slot5[2]
                            break
                        elif escolha == 0:
                            break
                        else:
                            print("Valor inválido, escolha novamente.")
                            continue
                else:
                    print("Você não equipou o item.")
                print(f"\n\033[1mOuro dropado:\033[m \033[1;33m{bossDG[list(bossDG)[0]][3]}\033[m")
                ouro += bossDG[list(bossDG)[0]][3]
                vida = vidas
                return print(f"\033[1mSua vida atual é\033[m \033[1;32m{vidas}\033[m")
        elif escolha == 2 and contadorVasculhar == 0:
            salaBoss = ["ouro", "vida", "armadilha"]
            recompensa = random.choices(salaBoss, weights=[1, 1, 1])
            if recompensa[0] == "ouro":
                ouroVasculhado = random.randint(20, 110)
                print(f"\033[1mVocê encontrou\033[m \033[1;33m{ouroVasculhado}\033[m \033[1mmoedas de ouro.\033[m")
                ouro += ouroVasculhado
                print(f"\033[1mOuro atual:\033[m \033[1;33m{ouro}\033[m")
                contadorVasculhar += 1
                continue
            elif recompensa[0] == "vida":
                vidaGanha = random.randint(14, 28)
                print("\033[1mVocê encontou uma poção de vida.\033[m")
                print(f"\033[1mVida recuperada:\033[m \033[1;32m{vidaGanha}\033[m")
                vida += vidaGanha
                if vida > (100 + slot1[1] + slot2[1] + slot3[1] + slot4[1] + slot5[1]):
                    vida = 100 + slot1[1] + slot2[1] + slot3[1] + slot4[1] + slot5[1]
                vidas = vida
                print(f"\033[1mVida atual:\033[m \033[1;32m{vida}\033[m")
                contadorVasculhar += 1
                continue
            elif recompensa[0] == "armadilha":
                vidaVasculhada = random.randint(5, 20)
                print(f"Você pisou em falso, uma armadilha explodiu e você tomou \033[1;31m{vidaVasculhada}\033[m de dano.")
                vida -= vidaVasculhada
                vidas = vida
                print(f"\033[1mVida atual:\033[m \033[1;32m{vida}\033[m")
                contadorVasculhar += 1
                continue
        elif escolha == 2 and contadorVasculhar == 1:
            print("\n\033[1mVocê já vasculhou toda a sala do Boss\033[m\n")
            continue
        else:
            print("\033[1mDigite um valor válido, não sabe ler?\033[m\n")
            continue

#função para a loja
preco_pocao_pequena = 160
preco_pocao_media = 550
preco_pocao_grande = 1300
preco_slot4 = 1500
preco_slot5 = 3000
def loja():
    print(f"""
    \033[1mOuro Atual:\033[m \033[33m{ouro:^2}\033[m | \033[1mVida atual:\033[m \033[1;32m{vida:^2}/{100 + slot1[1] + slot2[1] + slot3[1] + slot4[1] + slot5[1]:^2}\033[m\n
    \033[1;36m{"LOJA":^25}\033[m
    \033[1;36m{"Esse é o nosso catálogo:":^25}\033[m
    \033[36m{"1 - Poção Pequena (+10 de vida):"}\033[m \033[33m{preco_pocao_pequena} p.o\033[m
    \033[36m{"2 - Poção Média (+x de vida):"}\033[m \033[33m{preco_pocao_media} p.o\033[m
    \033[36m{"3 - Poção Grande (+x de vida):"}\033[m \033[33m{preco_pocao_grande} p.o\033[m
    \033[36m{"4 - Slot 4 (dungeon lvl 2 necessária):"}\033[m \033[33m{preco_slot4} p.o\033[m
    \033[36m{"5 - Slot 5 (dungeon lvl 4 necessária):"}\033[m \033[33m{preco_slot5} p.o\033[m
    \033[36m{"0 - sair da loja":<25}\033[m\n""")
    
############################################################################################################################################
print("""\033[1m
Bem-vindos a rede\033[m \033[31;1md\033[m\033[32;1mu\033[m\033[33;1mn\033[m\033[34;1mg\033[m\033[35;1me\033[m\033[36;1mo\033[m\033[32;1mn\033[m\033[1m, iremos dar as instruções:
Seu objetivo é conquistar as 10 dungeons espalhadas pelo mundo, para conquistar cada uma você deve matar o BOSS que nela reside.
Além disso você tem os seus STATUS, que começam da seguinte forma:\033[m
\033[4m(Obs: quando o código parar dê um enter para continuar)\033[m
""")

status()

#main
dungeon_key = 0
while vida > 0:
    menu = '''
    -1 - Visualizar Status
    0 - Loja de itens
    1 - Dark Forest (Dungeon lvl 1) 
    '''
    if dungeon_key > 0:
        menu += '2 - Frozen Tomb (Dungeon lvl 2)\n'
    if dungeon_key > 1:
        menu += '    3 - Ghost Village (Dungeon lvl 3)\n'
    if dungeon_key > 2:
        menu += '    4 - Pirates Bay (Dungeon lvl 4)\n'
    if dungeon_key > 3:
        menu += '    5 - Destroyed World (Dungeon lvl 5)\n'
    contadorFuga = 0
    
    print("\033[36;1m\nVocê está no saguão, para onde deseja ir?\033[m")
    print(f"""\033[1;36m{menu}\033[m""")
    escolha = input()


    if escolha == '-1':
        status()
        input()

    elif escolha == '0':
        loja()
        escolha = input()
        if escolha == '0':
            continue

        elif escolha == '1':
            if ouro < preco_pocao_pequena:
                print("\033[1mVocê não tem\033[m \033[33mouro\033[m \033[1msuficiente\033[m")
                print(f"\033[1mFaltam\033[m \033[33m{preco_pocao_pequena-ouro} p.o\033[m \033[1mpara comprar a poção\033[m ")
                continue
            else:
                vida += 10
                if vida > (100 + slot1[1] + slot2[1] + slot3[1] + slot4[1] + slot5[1]):
                        vida = 100 + slot1[1] + slot2[1] + slot3[1] + slot4[1] + slot5[1]
                print("\033[1mVida recuperada:\033[m \033[1;32m+10\033[m")
                print(f"\033[1mVida atual:\033[m \033[1;32m{vida}/{100 + slot1[1] + slot2[1] + slot3[1] + slot4[1] + slot5[1]:^2}\033[m")
                ouro -= preco_pocao_pequena

        elif escolha == '4' and dungeon_key >= 2:
            if ouro < preco_slot4:
                print("\033[1mVocê não tem\033[m \033[33mouro\033[m \033[1msuficiente\033[m")
                print(f"\033[1mFaltam\033[m \033[33m{preco_slot4-ouro} p.o\033[m \033[1mpara comprar esse slot\033[m ")
                continue
            else:
                print("\033[1mSlot 4 comprado com sucesso, você já pode utilizá-lo\033[m")
                print(f"\033[1mOuro: \033[m \033[33m-{preco_slot4} p.o\033[m \033[1m= \033[m  \033[33m-{ouro-preco_slot4} p.o\033[m ")
                ouro -= preco_slot4
                bool_slot4 = True

        elif escolha == '5' and dungeon_key >= 4:
            if ouro < preco_slot5:
                print("\033[1mVocê não tem\033[m \033[33mouro\033[m \033[1msuficiente\033[m")
                print(f"\033[1mFaltam\033[m \033[33m{preco_slot5-ouro} p.o\033[m \033[1mpara comprar esse slot\033[m ")
                continue
            else:
                print("\033[1mSlot 5 comprado com sucesso, você já pode utilizá-lo\033[m")
                print(f"\033[1mOuro: \033[m \033[33m-{preco_slot5} p.o\033[m \033[1m= \033[m  \033[33m-{ouro-preco_slot5} p.o\033[m ")
                ouro -= preco_slot5
                bool_slot5 = True
        else:
            print("\033[1mConclua os requisitos para comprar esse slot\033[m")

    elif escolha == '1':
        print("""\033[1m
        Você entrou na Dark Forest (dungeon de lvl 1)...
        Muitos monstros vagam por essas terras sombrias e amaldiçoadas, 
        você como um bom e confiante aventureiro seguiu em frente na busca da cabeça do temido BAD WOLF.\033[m
        """)
        print("\033[34;1mMonstro à vista, hora de lutar.\033[m")

        batalha(vida, monstrosDG1)
        if contadorFuga == 1:
            continue

        print("\033[34;1m\nóh não, outro monstro à vista.\033[m")
        input()
        batalha(vida, monstrosDG1)
        if contadorFuga == 1:
            continue

        print("""\n\033[1m
        Após derrotar os braços direitos do grande e temido BAD WOLF você se preparar para o pior,      
        pois irritou o boss da dungeon.
        Depois de 2 horas de caminhada pela Dark Forest você escuta um uivo assustador 60º a oeste, 
        nesse momento você se depara com o BAD WOLF.\033[m\n
        """)

        batalhaBoss(vida, bossDG1, itensBossDG1)

        print("""\n\033[1m
        Você derrotou a primeira\033[m \033[31;1md\033[m\033[32;1mu\033[m\033[33;1mn\033[m\033[34;1mg\033[m\033[35;1me\033[m\033[36;1mo\033[m\033[32;1mn\033[m!! \033[1mMeus parabéns.
        Dungeon liberada: Frozen Tomb
        \033[m\n""")
        if dungeon_key == 0:
            dungeon_key = 1

    elif escolha == '2' and dungeon_key >= 1:
        print("""\033[34;1m
        Você entrou na Frozen Tomb (dungeon de lvl 2)...
        Milhares de anos atrás um mago poderoso condenou essas terras congelando tudo que via pela frente, 
        muitos monstros de gelo surgiram com os resquícios de poder que sobraram do grande mago, tome cuidado... um erro e será congelado para sempre.\033[m
        """)
        print("\033[34;1mVocê sente um calafrio, monstro à vista.\033[m")

        batalha(vida, monstrosDG2)
        if contadorFuga == 1:
            continue

        print("\033[34;1m\nMais um monstro à vista.\033[m")
        input()
        batalha(vida, monstrosDG2)
        if contadorFuga == 1:
            continue

        print("""\n\033[1m
        Um enorme dragão surge das colinas e nota sua presença, ele está furioso com o intruso que invadiu sua dunegeon\033[m\n
        """)

        batalhaBoss(vida, bossDG2, itensBossDG2)

        print("""\n\033[1m
        Você derrotou a segunda\033[m \033[31;1md\033[m\033[32;1mu\033[m\033[33;1mn\033[m\033[34;1mg\033[m\033[35;1me\033[m\033[36;1mo\033[m\033[32;1mn\033[m!! \033[1mMeus parabéns.
        Dungeon liberada: Ghost Village
        \033[m\n""")
        if dungeon_key == 1:
            dungeon_key = 2
    
    elif escolha == '3' and dungeon_key >= 2:
        print("""\033[34;1m
        Caminhando pelas profundezas você avista um vilarejo abandonado e alguma magia obscura te mantém preso dentro dele.
        Você encontrou a dunegon Ghost Village (Dungeon lvl 3)\033[m
        """)
        print("\033[34;1mDemônios te cercam, hora de lutar.\033[m")

        batalha(vida, monstrosDG3)
        if contadorFuga == 1:
            continue

        print("\033[34;1m\nOutro fantasma à vista.\033[m")
        input()
        batalha(vida, monstrosDG3)
        if contadorFuga == 1:
            continue

        print("""\n\033[1m
        Após derrotar todos os fantasmas da vila, Astaroth fica enfurecido e busca vingaça.\033[m\n
        """)

        batalhaBoss(vida, bossDG3, itensBossDG3)

        print("""\n\033[1m
        Você derrotou a terceira\033[m \033[31;1md\033[m\033[32;1mu\033[m\033[33;1mn\033[m\033[34;1mg\033[m\033[35;1me\033[m\033[36;1mo\033[m\033[32;1mn\033[m!! \033[1mMeus parabéns.
        Dungeon liberada: Pirates Bay
        \033[m\n""")
        if dungeon_key == 2:
            dungeon_key = 3
        
    elif escolha == '4' and dungeon_key >= 3:
        print("""\033[34;1m
        O mar... muitas vezes pode ser traiçoeiro, sombrio e perverso. Em busca da quarta dungeon você entra no território aquático mais perigoso conehcido pelos aventureiros.
        Em busca da cabeça do Kraken você entra na Dungeon conhecida como Pirates Bay (Dungeon lvl 4)\033[m
        """)
        print("\033[34;1mSeu navio foi invadido, prepare-se.\033[m")

        batalha(vida, monstrosDG4)
        if contadorFuga == 1:
            continue

        print("\033[34;1m\nInimigo à vista, atirar!!\033[m")
        input()
        batalha(vida, monstrosDG4)
        if contadorFuga == 1:
            continue

        print("""\n\033[1m
        O Kraken percebe a presença de meros aventureiros em seu território, você despertou a fúria do ser aquático mais poderoso conhecido pelo homem.\033[m\n
        """)

        batalhaBoss(vida, bossDG4, itensBossDG4)

        print("""\n\033[1m
        Você derrotou a quarta\033[m \033[31;1md\033[m\033[32;1mu\033[m\033[33;1mn\033[m\033[34;1mg\033[m\033[35;1me\033[m\033[36;1mo\033[m\033[32;1mn\033[m!! \033[1mMeus parabéns.
        Dungeon liberada: Destroyed World
        \033[m\n""")
        if dungeon_key == 3:
            dungeon_key = 4
        
    elif escolha == '5' and dungeon_key >= 4:
        print("""\033[34;1m
        Após derrotar todas as dungeons você finalmente encontrou a última e mais perigosa dungeon onde encontramos os monstros mais perigosos, sombrios e temidos da humanidade.
        Você encontrou uma nova dungeon: Destroyed World (Dungeon lvl 4)\033[m
        """)
        print("\033[34;1mQue a calamidade comece.\033[m")

        batalha(vida, monstrosDG5)
        if contadorFuga == 1:
            continue

        print("\033[34;1m\nPrepare-se, um monstro logo em frente.\033[m")
        input()
        batalha(vida, monstrosDG5)
        if contadorFuga == 1:
            continue

        print("""\n\033[1m
        Após anos de inatividade o boss finalmente sentiu um poder que vale a pena, um aventureiro corajoso o bastante para desafiálo em um batalha,
        o Rei renasce das cinzas e vai em sua direção a fim de entretenimento, prepare-se aventureiro um grande desafio está a sua frente.
        Que o genocídio comece, surge o Rei Destruído\033[m\n
        """)

        batalhaBoss(vida, bossDG5, itensBossDG5)

        print("""\n\033[1m
        Você derrotou a quinta\033[m \033[31;1md\033[m\033[32;1mu\033[m\033[33;1mn\033[m\033[34;1mg\033[m\033[35;1me\033[m\033[36;1mo\033[m\033[32;1mn\033[m!! \033[1mMeus parabéns.
        boss liberado: XXXXX
        \033[m\n""")
        if dungeon_key == 4:
            dungeon_key = 5
        
    else:
        continue
