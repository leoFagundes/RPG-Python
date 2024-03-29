#Obs: nesse código existem alguns caractéres no meio das string como: \033m[... Esses códigos servem para mudar a cor da string no terminal.
import random
#pickle serve para salvar o aventureiro criado pelo jogador
import pickle
import os

#classe aventureiro -> seu personagem principal vai ser uma instância dessa classe
class Aventureiro:
 

 def __init__(self, nome):
     self.nome = nome
     self.forca = 1
     self.vida = 100
     self.ouro = 0
     self.velAtaque = 10
     self.key = 0
     self.key_dungeon = 0
     self.slot1 = [0, 0, 0, 'empty']
     self.slot2 = [0, 0, 0, 'empty']
     self.slot3 = [0, 0, 0, 'empty']
     self.slot4 = [0, 0, 0, 'empty']
     self.slot5 = [0, 0, 0, 'empty']
     self.slotEspadaEcantada = [0, 0, 0, 'empty']
     self.bool_slot4 = False
     self.bool_slot5 = False


 #método para  visualizar status do aventureiro
 def statusAventureiro(self):
     print("\033[36m__\033[m"*15)
     print("")
     print(f"\033[1mAventureiro: {aventureiro.nome}\033[m")
     print(f"\033[1mForça:\033[m \033[31m{self.forca:^2}\033[m")
     print(f"\033[1mVida:\033[m \033[32m{self.vida:^2}/{100+self.slot1[1]+self.slot2[1]+self.slot3[1]+self.slot4[1]+self.slot5[1]:^2}\033[m")
     print(f"\033[1mOuro:\033[m \033[33m{self.ouro:^2}\033[m")
     print(f"\033[1mVelocidade de Ataque:\033[m \033[35m{self.velAtaque:^2}\033[m")
     print("\033[36m__\033[m"*15)
     #essas condições servem para mostrar os slots caso o nome delas não esteja 'empty'
     if self.slot1[3] != 'empty':
         print(f"""\033[1;37mSlot 1\033[m - {self.slot1[3]}:
                 \033[31;1m+{self.slot1[0]}\033[m \033[1;37mde força\033[m
                 \033[32;1m+{self.slot1[1]}\033[m \033[1;37mde vida\033[m
                 \033[35;1m+{self.slot1[2]}\033[m \033[1;37mde velocidade de ataque\033[m""")
         print("\033[36m__\033[m"*15)
     if self.slot2[3] != 'empty':
         print(f"""\033[1;37mSlot 2\033[m - {self.slot2[3]}:
                 \033[31;1m+{self.slot2[0]}\033[m \033[1;37mde força\033[m
                 \033[32;1m+{self.slot2[1]}\033[m \033[1;37mde vida\033[m
                 \033[35;1m+{self.slot2[2]}\033[m \033[1;37mde velocidade de ataque\033[m""")
         print("\033[36m__\033[m"*15)
     if self.slot3[3] != 'empty':
         print(f"""\033[1;37mSlot 3\033[m - {self.slot3[3]}:
                 \033[31;1m+{self.slot3[0]}\033[m \033[1;37mde força\033[m
                 \033[32;1m+{self.slot3[1]}\033[m \033[1;37mde vida\033[m
                 \033[35;1m+{self.slot3[2]}\033[m \033[1;37mde velocidade de ataque\033[m""")
         print("\033[36m__\033[m"*15)
     if self.slot4[3] != 'empty':
         print(f"""\033[1;37mSlot 4\033[m - {self.slot4[3]}:
                 \033[31;1m+{self.slot4[0]}\033[m \033[1;37mde força\033[m
                 \033[32;1m+{self.slot4[1]}\033[m \033[1;37mde vida\033[m
                 \033[35;1m+{self.slot4[2]}\033[m \033[1;37mde velocidade de ataque\033[m""")
         print("\033[36m__\033[m"*15)
     if self.slot5[3] != 'empty':
         print(f"""\033[1;37mSlot 5\033[m - {self.slot5[3]}:
                 \033[31;1m+{self.slot5[0]}\033[m \033[1;37mde força\033[m
                 \033[32;1m+{self.slot5[1]}\033[m \033[1;37mde vida\033[m
                 \033[35;1m+{self.slot5[2]}\033[m \033[1;37mde velocidade de ataque\033[m""")
         print("\033[36m__\033[m"*15)
     if self.slotEspadaEcantada[3] != 'empty':
         print(f"""\033[1;37mSlot Especial\033[m - {self.slotEspadaEcantada[3]}:
                 \033[31;1m+{self.slotEspadaEcantada[0]}\033[m \033[1;37mde força\033[m
                 \033[32;1m+{self.slotEspadaEcantada[1]}\033[m \033[1;37mde vida\033[m
                 \033[35;1m+{self.slotEspadaEcantada[2]}\033[m \033[1;37mde velocidade de ataque\033[m""")
         print("\033[36m__\033[m"*15)
     
#classe para a loja do jogo
class Loja():
 

 def __init__(self):
     self.preco_pocao_pequena = 210
     self.preco_pocao_media = 400
     self.preco_pocao_grande = 750
     self.preco_slot4 = 1700
     self.preco_slot5 = 3200
     self.preco_espadaEncantada = 5500
     self.preco_armaduraEncantada = 5000


 def mostrarLoja(self, ouro, vida, slot1, slot2, slot3, slot4, slot5):
     print(f"""
     \033[1mOuro Atual:\033[m \033[33m{ouro:^2}\033[m | \033[1mVida atual:\033[m \033[1;32m{vida:^2}/{100 + slot1[1] + slot2[1] + slot3[1] + slot4[1] + slot5[1]:^2}\033[m\n
     \033[1;36m{"LOJA":^25}\033[m
     \033[1;36m{"Esse é o nosso catálogo:":^25}\033[m
     \033[36m{"1 - Poção Pequena (+20 de vida):"}\033[m \033[33m{self.preco_pocao_pequena} p.o\033[m
     \033[36m{"2 - Poção Média (+60 de vida) (dungeon lvl 3 necessária):"}\033[m \033[33m{self.preco_pocao_media} p.o\033[m
     \033[36m{"3 - Poção Grande (+150 de vida) (dungeon lvl 4 necessária):"}\033[m \033[33m{self.preco_pocao_grande} p.o\033[m
     \033[36m{"4 - Slot 4 (dungeon lvl 2 necessária):"}\033[m \033[33m{self.preco_slot4} p.o\033[m
     \033[36m{"5 - Slot 5 (dungeon lvl 4 necessária):"}\033[m \033[33m{self.preco_slot5} p.o\033[m
     \033[36m{"6 - Espada Encantada com os 5 Elementos (dungeon lvl 5 necessária):"}\033[m \033[33m{self.preco_espadaEncantada} p.o\033[m
     \033[36m{"7 - Armadura Encantada com os 5 Elementos (dungeon lvl 5 necessária):"}\033[m \033[33m{self.preco_armaduraEncantada} p.o\033[m
     \033[36m{"0 - sair da loja":<25}\033[m\n""")

#classe para os monstros do jogo
class Monstros:


 def __init__(self, nome, forca, vida, velAtaque, ouroDropado, chanceFuga):
     self. nome = nome
     self.forca = forca
     self.vida = vida
     self.velAtaque = velAtaque
     self.ouroDropado = ouroDropado
     self.chanceFuga = chanceFuga


 #método para visualizar os status dos monstros
 def statusMonstro(self):
     print("\033[36m__\033[m"*15)
     print("")
     print(f"\033[1mMonstro:\033[m \033[36m{self.nome}\033[m")
     print(f"\033[1mForça:\033[m \033[31m{self.forca:^2}\033[m")
     print(f"\033[1mVida:\033[m \033[32m{self.vida:^2}\033[m")
     print(f"\033[1mVelocidade de Ataque:\033[m \033[35m{self.velAtaque:^2}\033[m")
     print(f"\033[1mRecompensa:\033[m \033[33m{self.ouroDropado:^2}\033[m moedas de ouro")
     print(f"\033[1mChance de fuga:\033[m \033[33m{self.chanceFuga:^2}%\033[m")
     print("\033[36m__\033[m"*15)

#classe para os bosses do jogo
class Boss:
 

 def __init__(self, nome, forca, vida, velAtaque, ouroDropado, loot):
     self. nome = nome
     self.forca = forca
     self.vida = vida
     self.velAtaque = velAtaque
     self.ouroDropado = ouroDropado
     self.loot = loot


 #visualizar os status do Boss
 def statusBoss(self):
     print("\033[36m__\033[m"*15)
     print("")
     print(f"\033[1mBoss:\033[m \033[36m{self.nome}\033[m")
     print(f"\033[1mForça:\033[m \033[31m{self.forca:^2}\033[m")
     print(f"\033[1mVida:\033[m \033[32m{self.vida:^2}\033[m")
     print(f"\033[1mVelocidade de Ataque:\033[m \033[35m{self.velAtaque:^2}\033[m")
     print(f"\033[1mRecompensa:\033[m \033[33m{self.ouroDropado:^2}\033[m moedas de ouro")
     print("\033[36m__\033[m"*15)

#função para iniciar uma batalha que iremos chamar no construtor
def batalha(listaInstancia):
 '''
 Essa função recebe uma lista de 4 instancias de monstros, 
 logo em seguida vai ser sorteado na proporcionalidade 90 90 75 10
 '''
 global contadorFuga

 sorteio = [0, 1, 2, 3]
 monstroSorteado = random.choices(sorteio, weights=[90, 90, 75, 10])
 currentMonster = listaInstancia[monstroSorteado[0]]

 currentMonster.statusMonstro()

 #inicio da luta contra o monstro escolhido aleatoriamente
 while True:
     print("""\033[36;1mDeseja:\033[m
             \033[1m1-atacar
             2-tentar fugir\033[m
             """)
     escolha = input()
     
     '''
     esse if serve para pegar o valor em string e depois transformar em inteiro
     fiz isso para a pessoa poder dar enter ou digitar qualquer outro valor sem dar um erro de Type
     quando ela digitar um valor errado ou dar enter a mensagem vai aparecer novamente sem ter problemas de erro
     '''
     if escolha == '1' or escolha == '2':
         escolha = int(escolha)
     else:
         print("Escolha um valor válido.\n")
         continue

     if escolha != 1 and escolha != 2:
         print("Escolha um valor válido.\n")
         continue

     #condição para a fuga do aventureiro com base no atributo 'chanceFuga' do monstro escolhido
     if escolha == 2:
         chances = ['fugiu', 'naofugiu']
         chance = random.choices(chances, weights = [currentMonster.chanceFuga, 100-currentMonster.chanceFuga])
         if chance[0] == 'fugiu':
             print(f"Com {currentMonster.chanceFuga}% de chance de escapar, você conseguiu fugir com sucesso")
             contadorFuga = 1
             break
         elif chance[0] == 'naofugiu':
             dano = currentMonster.forca/1.25
             print(f"Você tentou fugir, porém o {currentMonster.nome} foi mais rápido e te atacou.")
             print(f"Consequência: levou {dano} de dano")
             print(f"Vida atual = {aventureiro.vida - dano}\n")
             aventureiro.vida -= dano
             if aventureiro.vida <= 0:
                 print(f"{currentMonster.nome} matou você, boa sorte na próxima vida.")
                 os.remove("aventureiro.pickle")
                 exit()
             continue
             
     #escolha que inicia a batalha com o monstro
     elif escolha == 1:
         input("\n\033[31;1mComeçar a batalha\033[m\n\n")
         while currentMonster.vida > 0:
             '''
             aqui existem duas condições
             uma caso a sua velocidade de ataque seja mais rápida que a do monstro, nesse caso você ataca primeiro
             caso contrário o monstro ataca primeiro
             '''
             if currentMonster.velAtaque > aventureiro.velAtaque:
                 print(f"""
                 \033[37;1mO monstro foi mais rápido que você, aventureiro.\033[m
                 \033[31mAtaque do monstro: {currentMonster.forca}\033[m
                 """)
                 aventureiro.vida -= currentMonster.forca
                 if aventureiro.vida <= 0:
                     print("Você morreu, tente novamente em uma próxima vida.")
                     os.remove("aventureiro.pickle")
                     exit()
                 print(f"\033[1mSua vida atual: \033[32m{aventureiro.vida}\033[m\n")

                 input("\033[1mPróximo turno\033[m\n")

                 print(f"""
                 \033[37;1mSua vez de atacar:\033[m
                 \033[31mAtaque: {aventureiro.forca}\033[m
                 """)
                 currentMonster.vida -= aventureiro.forca
                 print(f"\033[1mVida do monstro: \033[32m{currentMonster.vida}\033[m\n")
                 if currentMonster.vida <= 0:
                     break

                 input("\033[1mPróximo turno\033[m\n")
             else:
                 print(f"""
                 Você foi mais rápido que o monstro, sua vez de atacar.
                 \033[31mAtaque: {aventureiro.forca}\033[m
                 """)
                 currentMonster.vida -= aventureiro.forca
                 print(f"\033[1mVida do monstro: \033[32m{currentMonster.vida}\033[m\n")
                 if currentMonster.vida <= 0:
                     break

                 input("\033[1mPróximo turno\033[m\n")

                 print(f"""
                 Turno do monstro.
                 \033[31mAtaque do monstro: {currentMonster.forca}\033[m
                 """)
                 aventureiro.vida -= currentMonster.forca
                 if aventureiro.vida <= 0:
                     print("Você morreu, tente novamente em uma próxima vida.")
                     os.remove("aventureiro.pickle")
                     exit()
                 print(f"\033[1mSua vida atual: \033[32m{aventureiro.vida}\033[m\n")

                 input("\033[1mPróximo turno\033[m\n")
         print(f"\033[31mVocê matou o monstro {currentMonster.nome}\033[m, \033[1mvamos continuar a jornada.\033[m")
         print(f"\033[1mOuro dropado:\033[m \033[1;33m{currentMonster.ouroDropado}\033[m")
         aventureiro.ouro += currentMonster.ouroDropado
         return print(f"\033[1mSua vida atual é\033[m \033[32;1m{aventureiro.vida}\033[m")

#função para a batalha do boss que iremos chamar no construtor
def batalhaBoss(boss):
  '''
  essa função pede apenas a instancia de um boss
  '''
  contadorVasculhar = 0
  while True:
      print("""Deseja
                  1-atacar
                  2-vasculhar sala
          """)
      escolha = input()
      '''
      esse if serve para pegar o valor em string e depois transformar em inteiro
      fiz isso para a pessoa poder dar enter ou digitar qualquer outro valor sem dar um erro de Type
      quando ela digitar um valor errado ou dar enter a mensagem vai aparecer novamente sem ter problemas de erro
      '''
      if escolha == '1' or escolha == '2':
          escolha = int(escolha)
      else:
          continue
      if escolha == 2 and contadorVasculhar == 0:
          salaBoss = ["ouro", "vida", "armadilha"]
          #a recompensa tem uma chance igual de ser ouro, vida ou armadilha
          recompensa = random.choices(salaBoss, weights=[1, 1, 1])
          
          if recompensa[0] == "ouro":
              ouroMinimo = 0
              ouroMaximo = 0
              if aventureiro.key_dungeon == 0:
                  ouroMinimo = 20
                  ouroMaximo = 80
              elif aventureiro.key_dungeon == 1:
                  ouroMinimo = 20
                  ouroMaximo = 110
              elif aventureiro.key_dungeon == 2:
                  ouroMinimo = 40
                  ouroMaximo = 120
              elif aventureiro.key_dungeon == 3:
                  ouroMinimo = 50
                  ouroMaximo = 200
              elif aventureiro.key_dungeon == 4:
                  ouroMinimo = 50
                  ouroMaximo = 250
              else:
                  ouroMinimo = 100
                  ouroMaximo = 350
              ouroVasculhado = random.randint(ouroMinimo, ouroMaximo)
              print(f"\033[1mVocê encontrou\033[m \033[1;33m{ouroVasculhado}\033[m \033[1mmoedas de ouro.\033[m")
              aventureiro.ouro += ouroVasculhado
              print(f"\033[1mOuro atual:\033[m \033[1;33m{aventureiro.ouro}\033[m")
              contadorVasculhar += 1
              continue
              
          elif recompensa[0] == "vida":
              if aventureiro.key_dungeon == 1:
                  potion = random.randint(12, 18)
                  textoPotion = 'pequena'
              elif aventureiro.key_dungeon == 2 or aventureiro.key_dungeon == 3:
                  potion = random.randint(25, 45)
                  textoPotion = 'média'
              else:
                  potion = random.randint(80, 200)
                  textoPotion = 'grande'
              print(f"\033[1mVocê encontou uma poção de vida {textoPotion}.\033[m")
              print(f"\033[1mVida recuperada:\033[m \033[1;32m{potion}\033[m")
              aventureiro.vida += potion
              if aventureiro.vida > (100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]):
                  aventureiro.vida = 100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]
              print(f"\033[1mVida atual:\033[m \033[1;32m{aventureiro.vida}\033[m")
              contadorVasculhar += 1
              continue
              
          elif recompensa[0] == "armadilha":
              if aventureiro.key_dungeon == 1:
                  armadilha = random.randint(12, 18)
              elif aventureiro.key_dungeon == 2 or aventureiro.key_dungeon == 3:
                  armadilha = random.randint(18, 50)
              else:
                  armadilha = random.randint(80, 270)
              print(f"Você pisou em falso, uma armadilha explodiu e você tomou \033[1;31m{armadilha}\033[m de dano.")
              aventureiro.vida -= armadilha
              print(f"\033[1mVida atual:\033[m \033[1;32m{aventureiro.vida}\033[m")
              contadorVasculhar += 1
              if aventureiro.vida <= 0:
                      print("Você morreu, tente novamente em uma próxima vida.")
                      os.remove("aventureiro.pickle")
                      exit()
              continue
              
      elif escolha == 2 and contadorVasculhar == 1:
          print("\n\033[1mVocê já vasculhou toda a sala do Boss\033[m\n")
          continue
      #aqui começa a batalha conta o boss
      elif escolha == 1:
          boss.statusBoss()
          input("\033[1mComeçar a batalha\033[m\n")
          while boss.vida > 0:
              
              #caso a velocidade do boss for maior do que a sua ele ataca primeiro, caso contráro você ataca
              if boss.velAtaque > aventureiro.velAtaque:
                  print(f"""
                  A velocidade do Boss te superou.
                  \033[31mAtaque do {boss.nome}: {boss.forca}\033[m
                  """)
                  aventureiro.vida -= boss.forca
               
                  if aventureiro.vida <= 0:
                      print("Você morreu, tente novamente em uma próxima vida.")
                      os.remove("aventureiro.pickle")
                      exit()
                  print(f"\033[1mSua vida atual:\033[m \033[32m{aventureiro.vida}\033[m\n")

                  input("\033[1mPróximo turno\033[m\n")

                  print(f"""
                  Sua vez de atacar:
                  \033[31mAtaque: {aventureiro.forca}\033[m
                  """)
                  boss.vida -= aventureiro.forca
                  print(f"\033[1mVida do {boss.nome}: \033[32m{boss.vida}\033[m\n")
                  if boss.vida <= 0:
                      break

                  input("\033[1mPróximo turno\033[m\n")
              else:
                  print(f"""
                  Você foi mais rápido que o boss, sua vez de atacar.
                  \033[31mAtaque: {aventureiro.forca}\033[m
                  """)
                  boss.vida -= aventureiro.forca
                  print(f"\033[1mVida do {boss.nome}: \033[32m{boss.vida}\033[m\n")
                  
                  if boss.vida <= 0:
                      break

                  input("\033[1mPróximo turno\033[m\n")

                  print(f"""
                  Turno do boss.
                  \033[31mAtaque do {boss.nome}: {boss.forca}\033[m
                  """)
                  aventureiro.vida -= boss.forca
                  
                  if aventureiro.vida <= 0:
                      print("Você morreu, tente novamente em uma próxima vida.")
                      os.remove("aventureiro.pickle")
                      exit()
                  print(f"\033[1mSua vida atual: \033[32m{aventureiro.vida}\033[m\n")

                  input("\033[1mPróximo turno\033[m\n")
          print(f"\033[31mVocê matou o temido {boss.nome}\033[m, \033[1mvamos continuar a jornada.\033[m")
          
          #nessa parte o item é sorteado aleatoriamente com as chances 5, 5, 20, 20, 35, 35
          item = list(boss.loot)
          itemGanho = random.choices(item, weights=[5, 5, 20, 20, 35, 35])
          print("Você tem chance de ganhar um dos seguintes itens: \n")
          print("\n".join(item))
          print(f"""\n\033[37;1mO item dropado foi:\033[m
                  {itemGanho[0]}
                  \033[31mForça: +{boss.loot[itemGanho[0]][0]}\033[m
                  \033[32mVida: +{boss.loot[itemGanho[0]][1]}\033[m
                  \033[33mVelocidade de Ataque: +{boss.loot[itemGanho[0]][2]}\033[m
                  """)
          while True:
              print("\033[1;37mVocê deseja equipa-lo?\033[m")
              escolha = input("\033[37m1-sim\n2-não\n\033[m")
              '''
              esse if serve para pegar o valor em string e depois transformar em inteiro
              fiz isso para a pessoa poder dar enter ou digitar qualquer outro valor sem dar um erro de Type
              quando ela digitar um valor errado ou dar enter a mensagem vai aparecer novamente sem ter problemas de erro
              '''
              if escolha == '1' or escolha == '2':
                  escolha = int(escolha)
              else:
                  continue
              if escolha == 1:
               
                  #aqui o código vai verificar se você já comprou o slot 4 ou o slot 5 e gerar um texto com base nisso
                  while True:
                      if aventureiro.bool_slot4 == True and aventureiro.bool_slot5 == True:
                          texto = f"""
                          \033[1;37mVocê deseja equipar em qual slot?
                              1 - slot 1 (\033[m{aventureiro.slot1[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot1[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot1[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot1[2]}\033[m)
                              \033[1;37m2 - slot 2 (\033[m{aventureiro.slot2[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot2[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot2[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot2[2]}\033[m)
                              \033[1;37m3 - slot 3 (\033[m{aventureiro.slot3[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot3[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot3[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot3[2]}\033[m)
                              \033[1;37m4 - slot 4 (\033[m{aventureiro.slot4[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot4[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot4[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot4[2]}\033[m)
                              \033[1;37m5 - slot 5 (\033[m{aventureiro.slot5[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot5[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot5[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot5[2]}\033[m)
                              \033[1;37m0 - Não equipar\033[m
                          """
                      elif aventureiro.bool_slot4 == False and aventureiro.bool_slot5 == True:
                          texto = f"""
                          \033[1;37mVocê deseja equipar em qual slot?
                              \033[1;37m1 - slot 1 (\033[m{aventureiro.slot1[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot1[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot1[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot1[2]}\033[m)
                              \033[1;37m2 - slot 2 (\033[m{aventureiro.slot2[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot2[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot2[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot2[2]}\033[m)
                              \033[1;37m3 - slot 3 (\033[m{aventureiro.slot3[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot3[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot3[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot3[2]}\033[m)
                              \033[1;37m5 - slot 5 (\033[m{aventureiro.slot5[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot5[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot5[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot5[2]}\033[m)
                              \033[1;37m0 - Não equipar\033[m
                          """
                      elif aventureiro.bool_slot4 == True and aventureiro.bool_slot5 == False:
                          texto = f"""
                          \033[1;37mVocê deseja equipar em qual slot?
                              1 - slot 1 (\033[m{aventureiro.slot1[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot1[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot1[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot1[2]}\033[m)
                              \033[1;37m2 - slot 2 (\033[m{aventureiro.slot2[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot2[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot2[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot2[2]}\033[m)
                              \033[1;37m3 - slot 3 (\033[m{aventureiro.slot3[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot3[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot3[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot3[2]}\033[m)
                              \033[1;37m4 - slot 4 (\033[m{aventureiro.slot4[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot4[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot4[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot4[2]}\033[m)
                              \033[1;37m0 - Não equipar\033[m
                          """
                      elif aventureiro.bool_slot4 == False and aventureiro.bool_slot5 == False:
                          texto = f"""
                          \033[1;37mVocê deseja equipar em qual slot?
                              1 - slot 1 (\033[m{aventureiro.slot1[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot1[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot1[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot1[2]}\033[m)
                              \033[1;37m2 - slot 2 (\033[m{aventureiro.slot2[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot2[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot2[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot2[2]}\033[m)
                              \033[1;37m3 - slot 3 (\033[m{aventureiro.slot3[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot3[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot3[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot3[2]}\033[m)
                              \033[1;37m0 - Não equipar\033[m
                          """
                      print(texto)
                      escolha = input()
                      '''
                      esse if serve para pegar o valor em string e depois transformar em inteiro
                      fiz isso para a pessoa poder dar enter ou digitar qualquer outro valor sem dar um erro de Type
                      quando ela digitar um valor errado ou dar enter a mensagem vai aparecer novamente sem ter problemas de erro
                      '''
                      if escolha == '0' or escolha == '1' or escolha == '2' or escolha == '3' or escolha == '4' or escolha == '5':
                          escolha = int(escolha)
                      else:
                          continue
                      #aqui o aventureiro vai escolher em qual slot ele vai querer equipar o item
                      if escolha == 1:
                          print(f"Você equipou {itemGanho[0]}")
                          aventureiro.forca -= aventureiro.slot1[0]
                          #aventureiro.vida -= aventureiro.slot1[1]
                          aventureiro.velAtaque -= aventureiro.slot1[2]

                          aventureiro.slot1 = []
                          aventureiro.slot1.append(boss.loot[itemGanho[0]][0])
                          aventureiro.slot1.append(boss.loot[itemGanho[0]][1])
                          aventureiro.slot1.append(boss.loot[itemGanho[0]][2])
                          aventureiro.slot1.append(itemGanho[0])

                          aventureiro.forca += aventureiro.slot1[0]
                          aventureiro.vida += aventureiro.slot1[1]
                          aventureiro.velAtaque += aventureiro.slot1[2]
                          if aventureiro.vida > (100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]):
                              aventureiro.vida = 100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]
                          break
                      elif escolha == 2:
                          print(f"Você equipou {itemGanho[0]}")
                          aventureiro.forca -= aventureiro.slot2[0]
                          #aventureiro.vida -= aventureiro.slot2[1]
                          aventureiro.velAtaque -= aventureiro.slot2[2]

                          aventureiro.slot2 = []
                          aventureiro.slot2.append(boss.loot[itemGanho[0]][0])
                          aventureiro.slot2.append(boss.loot[itemGanho[0]][1])
                          aventureiro.slot2.append(boss.loot[itemGanho[0]][2])
                          aventureiro.slot2.append(itemGanho[0])

                          aventureiro.forca += aventureiro.slot2[0]
                          aventureiro.vida += aventureiro.slot2[1]
                          aventureiro.velAtaque += aventureiro.slot2[2]
                          if aventureiro.vida > (100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]):
                              aventureiro.vida = 100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]
                          break
                      elif escolha == 3:
                          print(f"Você equipou {itemGanho[0]}")
                          aventureiro.forca -= aventureiro.slot3[0]
                          #aventureiro.vida -= aventureiro.slot3[1]
                          aventureiro.velAtaque -= aventureiro.slot3[2]

                          aventureiro.slot3 = []
                          aventureiro.slot3.append(boss.loot[itemGanho[0]][0])
                          aventureiro.slot3.append(boss.loot[itemGanho[0]][1])
                          aventureiro.slot3.append(boss.loot[itemGanho[0]][2])
                          aventureiro.slot3.append(itemGanho[0])

                          aventureiro.forca += aventureiro.slot3[0]
                          aventureiro.vida += aventureiro.slot3[1]
                          aventureiro.velAtaque += aventureiro.slot3[2]
                          if aventureiro.vida > (100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]):
                              aventureiro.vida = 100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]
                          break
                      elif escolha == 4 and aventureiro.bool_slot4 == True:
                          print(f"Você equipou {itemGanho[0]}")
                          aventureiro.forca -= aventureiro.slot4[0]
                          #aventureiro.vida -= aventureiro.slot4[1]
                          aventureiro.velAtaque -= aventureiro.slot4[2]

                          aventureiro.slot4 = []
                          aventureiro.slot4.append(boss.loot[itemGanho[0]][0])
                          aventureiro.slot4.append(boss.loot[itemGanho[0]][1])
                          aventureiro.slot4.append(boss.loot[itemGanho[0]][2])
                          aventureiro.slot4.append(itemGanho[0])

                          aventureiro.forca += aventureiro.slot4[0]
                          aventureiro.vida += aventureiro.slot4[1]
                          aventureiro.velAtaque += aventureiro.slot4[2]
                          if aventureiro.vida > (100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]):
                              aventureiro.vida = 100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]
                          break
                      elif escolha == 5 and aventureiro.bool_slot5 == True:
                          print(f"Você equipou {itemGanho[0]}")
                          aventureiro.forca -= aventureiro.slot5[0]
                          #aventureiro.vida -= aventureiro.slot5[1]
                          aventureiro.velAtaque -= aventureiro.slot5[2]

                          aventureiro.slot5 = []
                          aventureiro.slot5.append(boss.loot[itemGanho[0]][0])
                          aventureiro.slot5.append(boss.loot[itemGanho[0]][1])
                          aventureiro.slot5.append(boss.loot[itemGanho[0]][2])
                          aventureiro.slot5.append(itemGanho[0])

                          aventureiro.forca += aventureiro.slot5[0]
                          aventureiro.vida += aventureiro.slot5[1]
                          aventureiro.velAtaque += aventureiro.slot5[2]
                          if aventureiro.vida > (100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]):
                              aventureiro.vida = 100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]
                          break
                      elif escolha == 0:
                          print(f"Você decidiu não equipar o item {itemGanho[0]}")
                          break
                      else:
                          print("Valor inválido, escolha novamente.")
                          continue
              else:
                  print(f"Você decidiu não equipar o item {itemGanho[0]}")
              print(f"\n\033[1mOuro dropado:\033[m \033[1;33m{boss.ouroDropado}\033[m")
              aventureiro.ouro += boss.ouroDropado
              return print(f"\033[1mSua vida atual é\033[m \033[1;32m{aventureiro.vida}\033[m")
       
      else:
          print("\033[1mDigite um valor válido, não sabe ler?\033[m\n")
          continue

#função para a batalha do boss final que iremos chamar no construtor
def bossFInal(boss):
    chance_de_fuga = 15
    vida_total = boss.vida
    acertar_arremesso = 40
    contra_atacar = 50
    defender = 50

    print(f'''
    {aventureiro.nome} olha com atenção para a poderosa entidade em sua frente e, sem querer acreditar, percebe que há apenas uma forma de derrota-lo...
    \nPara derrotar o poderoso Abyssal Overlord, há duas condições imprescindíveis. 
    Primeiramente, é necessário possuir uma espada encantada com os 5 elementos, cuja lâmina reluzente corta com precisão até mesmo os materiais mais resistentes. 
    Mas isso não é suficiente. 
    \nÉ preciso também ter coragem e habilidade para enfrentá-lo em sua forma mais vulnerável, quando sua vida está abaixo de 20%. Nesse momento, cada golpe é crucial, pois somente um acerto certeiro em seu coração pode selar a queda desse monstro descomunal.
    Caso mate-o sem perfurar seu coração, ele irá se auto-destruir, evaporando tudo e todos em sua volta.\n
    ''')

    boss.statusBoss()

    if aventureiro.slotEspadaEcantada[3] != 'empty':
        pass
    else:
        print("\nO aventureiro se aproxima da entrada da dungeon, mas é impedido por uma barreira mágica que o impede de entrar. Ele percebe que a barreira é alimentada pela energia da Espada Encantada, e entende que não pode prosseguir sem ela. Ele reflete sobre a importância de estar preparado para enfrentar os perigos que o aguardam dentro da dungeon, e decide procurar a lendária arma antes de tentar novamente entrar.")
        contadorFuga = 1
        return None
    
    while True:
        dano_reduzido = 0
        print(f"""
        Novo Turno
        ---------------------------------------------------
        |Vida ({aventureiro.nome}): {aventureiro.vida}
        |Vida ({boss.nome}): {boss.vida}\n
        """)
        print(f"""Deseja
                  1-Ataque normal (Dano: {aventureiro.forca})
                  2-Arremessar arma (Dano: {aventureiro.forca*1.3} | Chance de acertar: {acertar_arremesso}%)
                  3-Se defender (Dano reduzido: {defender}% | Chance de contra-atacar: {contra_atacar}%)
                  4-Perfurar coração
                  5-Fugir (Chance de fuga: {chance_de_fuga}%)
          """)
        escolha = input()
        '''
        esse if serve para pegar o valor em string e depois transformar em inteiro
        fiz isso para a pessoa poder dar enter ou digitar qualquer outro valor sem dar um erro de Type
        quando ela digitar um valor errado ou dar enter a mensagem vai aparecer novamente sem ter problemas de erro
        '''
        if escolha == '1' or escolha == '2' or escolha == '3' or escolha == '4' or escolha == '5':
            escolha = int(escolha)
        else:
            print("Opção inválida")
            continue

        if escolha == 1:
            print("Com muita determinação o aventureiro desfere uma ataque poderoso no Boss")
            print(f"\033[31mAtaque: {aventureiro.forca}\033[m")
            boss.vida -= aventureiro.forca
            print(f"\033[1mVida do {boss.nome}: \033[32m{boss.vida}\033[m\n")
            if boss.vida <= 0:
                print("Uma explosão devastadora irrompeu do corpo do Abyssal Overlord, varrendo tudo e todos ao seu redor em uma onda de destruição impiedosa.")
                print("Você morreu, falhou em perfurar o coração do Boss.")
                os.remove("aventureiro.pickle")
                exit()
                
        elif escolha == 2:
            chances = ['acertou', 'errou']
            chance = random.choices(chances, weights = [acertar_arremesso, 100-acertar_arremesso])
            if chance[0] == 'acertou':
                print("A arma arremessada pelo aventureiro atinge o corpo do boss com precisão, causando dano significativo e enfraquecendo-o ainda mais para o próximo ataque.")
                print(f"\033[31mAtaque: {aventureiro.forca*1.3}\033[m")
                boss.vida -= aventureiro.forca*1.3
                print(f"\033[1mVida do {boss.nome}: \033[32m{boss.vida}\033[m\n")
                if boss.vida <= 0:
                    print("Uma explosão devastadora irrompeu do corpo do Abyssal Overlord, varrendo tudo e todos ao seu redor em uma onda de destruição impiedosa.")
                    print("Você morreu, falhou em perfurar o coração do Boss.")
                    os.remove("aventureiro.pickle")
                    exit()
            elif chance[0] == 'errou':
                print("""
                A arma arremessada pelo aventureiro passa raspando pelo corpo do boss, errando o alvo e causando nenhum dano. 
                O guerreiro se prepara para o próximo ataque, consciente de que precisa ser mais preciso em seus movimentos para vencer essa batalha épica.
                Consequência: Perdeu a vez
                """)
                pass

        elif escolha == 3:
            dano_reduzido = 1
            print("Você se defende e espera o ataque do boss.")
            pass

        elif escolha == 4:
            if boss.vida <= vida_total * 0.2:
                print("""
                Com um movimento ágil e preciso, o aventureiro crava sua espada encantada no coração do Abyssal Overlord, selando assim sua vitória e o fim da batalha épica. 
                O ar treme com a explosão de energia do monstro derrotado, enquanto o guerreiro se mantém firme e impávido diante da magnitude da sua conquista. 
                Ainda que ferido e exausto, ele sabe que superou seu maior desafio e que seu nome será lembrado por muitas gerações como o herói que enfrentou e venceu o temível Abyssal Overlord.
                """)
                #fazer ações de fim da batalha
                break

            else:
                print(f"""
                Você tenta enfiar a espada encantada no coração do {boss.nome}, porém o coração ainda não está exposto.
                Consequência: Perdeu a vez
                """)
                pass

        elif escolha == 5:
            chances = ['fugiu', 'naofugiu']
            chance = random.choices(chances, weights = [15, 85])
            if chance[0] == 'fugiu':
                print(f"Com {chance_de_fuga}% de chance de escapar, você conseguiu fugir com sucesso")
                contadorFuga = 1
                break
            elif chance[0] == 'naofugiu':
                print(f"Você tentou fugir, porém o {boss.nome} não teve piedade.")
                print(f"Consequência: Perdeu a vez")
                print(f"Vida atual = {aventureiro.vida}\n")
                pass

        #Ataques possíveis do boss
        ataques = ['Fúria do Abismo', 'Colapso Dimensional', 'Cetro da Morte', 'Drenar Vida']
        if boss.vida >= vida_total * 0.45:
            ataque = random.choices(ataques, weights = [40, 5, 35, 7])
        elif boss.vida < vida_total * 0.45:
            ataque = random.choices(ataques, weights = [10, 15, 10, 15])

        if ataque[0] == 'Fúria do Abismo':
            dano = 0
            print("\033[1m\nO Abyssal Overlord ergue seu braço para o alto, e a energia sombria começa a se acumular em torno dele. Com um grito ensurdecedor, o boss libera uma onda de choque que sacode o chão e causa danos a todos ao seu redor. As sombras parecem ganhar vida própria, envolvendo o boss em um manto sombrio e ameaçador.\033[m")
            if dano_reduzido == 300:
                print(f"\033[1mDano recebido:\033[m \033[31m{dano}\033[m")
                aventureiro.vida -= dano
                if aventureiro.vida <= 0:
                    print("O aventureiro é lançado para trás com a força da onda de choque, seu corpo se contorcendo em agonia enquanto as sombras o envolvem e o arrastam para o abismo.")
                    os.remove("aventureiro.pickle")
                    exit()
            elif dano_reduzido == 1:
                dano = dano/2
                print("Você consegue se defender do ataque, reduzindo drasticamente o dano do Boss.")
                print(f"\033[1mDano recebido:\033[m \033[31m{dano}\033[m")
                aventureiro.vida -= dano
                if aventureiro.vida <= 0:
                    print("O aventureiro é lançado para trás com a força da onda de choque, seu corpo se contorcendo em agonia enquanto as sombras o envolvem e o arrastam para o abismo.")
                    os.remove("aventureiro.pickle")
                    exit()
                chances = ['contraAtacou', 'naoContraAtacou']
                chance = random.choices(chances, weights = [contra_atacar, 100-contra_atacar])
                if chance == 'contraAtacou':
                    print(f"Após receber o ataque {ataque[0]}, você consegue pular para cima do Boss dando um contra-ataque poderoso.")
                    print(f"\033[31mAtaque: {aventureiro.forca*1.25}\033[m")
                    boss.vida -= aventureiro.forca*1.25
                    if boss.vida <= 0:
                        print("Uma explosão devastadora irrompeu do corpo do Abyssal Overlord, varrendo tudo e todos ao seu redor em uma onda de destruição impiedosa.")
                        print("Você morreu, falhou em perfurar o coração do Boss.")
                        os.remove("aventureiro.pickle")
                        exit()
                    pass
                elif chance == 'naoContraAtacou':
                    print(f"Você tentou contra-atacar, porém {boss.nome} reagiu mais rápdo do que o esperado.")
                    pass
            print(f"\033[1mVida atual:\033[m \033[32m{aventureiro.vida}\033[m")

        elif ataque[0] == 'Colapso Dimensional':
            dano = 500
            print("\033[1m\nO Abyssal Overlord ergue ambas as mãos para o alto, e uma fenda no espaço-tempo começa a se abrir à sua frente. O vazio sombrio começa a puxar tudo ao seu redor, sugando os aventureiros em direção ao abismo sem fim. A voz rouca do boss ressoa pelo ar, desafiando aqueles que ousam enfrentá-lo.\033[m")
            if dano_reduzido == 0:
                print(f"\033[1mDano recebido:\033[m \033[31m{dano}\033[m")
                aventureiro.vida -= dano
                if aventureiro.vida <= 0:
                    print("O Abyssal Overlord se vira para o aventureiro, suas pupilas vermelhas brilhando intensamente. Ele ergue seu braço em um gesto ameaçador, e a energia sombria começa a se acumular ao seu redor. O aventureiro pode sentir o chão tremer sob seus pés enquanto o boss grita em um tom aterrorizante. Com um movimento rápido, o boss libera uma onda de choque que arremessa o aventureiro para longe, causando danos fatais e espalhando o sangue do aventureiro pelo chão da dungeon.")
                    os.remove("aventureiro.pickle")
                    exit()
            elif dano_reduzido == 1:
                dano = dano/2
                print("Você consegue se defender do ataque, reduzindo drasticamente o dano do Boss.")
                print(f"\033[1mDano recebido:\033[m \033[31m{dano}\033[m")
                aventureiro.vida -= dano
                if aventureiro.vida <= 0:
                    print("O aventureiro é lançado para trás com a força da onda de choque, seu corpo se contorcendo em agonia enquanto as sombras o envolvem e o arrastam para o abismo.")
                    os.remove("aventureiro.pickle")
                    exit()
                chances = ['contraAtacou', 'naoContraAtacou']
                chance = random.choices(chances, weights = [contra_atacar, 100-contra_atacar])
                if chance == 'contraAtacou':
                    print(f"Após receber o ataque {ataque[0]}, você consegue pular para cima do Boss dando um contra-ataque poderoso.")
                    print(f"\033[31mAtaque: {aventureiro.forca*1.25}\033[m")
                    boss.vida -= aventureiro.forca*1.25
                    if boss.vida <= 0:
                        print("Uma explosão devastadora irrompeu do corpo do Abyssal Overlord, varrendo tudo e todos ao seu redor em uma onda de destruição impiedosa.")
                        print("Você morreu, falhou em perfurar o coração do Boss.")
                        os.remove("aventureiro.pickle")
                        exit()
                    pass
                elif chance == 'naoContraAtacou':
                    print(f"Você tentou contra-atacar, porém {boss.nome} reagiu mais rápdo do que o esperado.")
                    pass
            print(f"\033[1mVida atual:\033[m \033[32m{aventureiro.vida}\033[m")

        elif ataque[0] == 'Cetro da Morte':
            dano = 350
            print("\033[1m\nO Abyssal Overlord levanta seu cetro de energia sombria, apontando-o em direção ao aventureiro. Raios negros começam a disparar do cetro, acertando seus alvos com precisão letal. O boss parece se regozijar com o sofrimento de seu oponente, rindo com desdém enquanto a energia sombria percorre seus dedos.\033[m")
            if dano_reduzido == 0:
                print(f"\033[1mDano recebido:\033[m \033[31m{dano}\033[m")
                aventureiro.vida -= dano
                if aventureiro.vida <= 0:
                    print("O aventureiro cai no chão, com o corpo coberto de marcas negras e sangrentas. Sua vida é extinta pela energia sombria, enquanto o Abyssal Overlord ri com satisfação, triunfante em sua vitória.")
                    os.remove("aventureiro.pickle")
                    exit()
            elif dano_reduzido == 1:
                dano = dano/2
                print("Você consegue se defender do ataque, reduzindo drasticamente o dano do Boss.")
                print(f"\033[1mDano recebido:\033[m \033[31m{dano}\033[m")
                aventureiro.vida -= dano
                if aventureiro.vida <= 0:
                    print("O aventureiro é lançado para trás com a força da onda de choque, seu corpo se contorcendo em agonia enquanto as sombras o envolvem e o arrastam para o abismo.")
                    os.remove("aventureiro.pickle")
                    exit()
                chances = ['contraAtacou', 'naoContraAtacou']
                chance = random.choices(chances, weights = [contra_atacar, 100-contra_atacar])
                if chance == 'contraAtacou':
                    print(f"Após receber o ataque {ataque[0]}, você consegue pular para cima do Boss dando um contra-ataque poderoso.")
                    print(f"\033[31mAtaque: {aventureiro.forca*1.25}\033[m")
                    boss.vida -= aventureiro.forca*1.25
                    if boss.vida <= 0:
                        print("Uma explosão devastadora irrompeu do corpo do Abyssal Overlord, varrendo tudo e todos ao seu redor em uma onda de destruição impiedosa.")
                        print("Você morreu, falhou em perfurar o coração do Boss.")
                        os.remove("aventureiro.pickle")
                        exit()
                    pass
                elif chance == 'naoContraAtacou':
                    print(f"Você tentou contra-atacar, porém {boss.nome} reagiu mais rápdo do que o esperado.")
                    pass
            print(f"\033[1mVida atual:\033[m \033[32m{aventureiro.vida}\033[m")

        elif ataque[0] == 'Drenar Vida':
            dano = 470
            print("\033[1m\nO Abyssal Overlord ergue seu cetro em direção ao aventureiro, e a energia sombria começa a envolvê-lo. Ele fecha os olhos, concentrando-se em drenar a vida de seu oponente para curar suas próprias feridas. O aventureiro pode sentir sua própria energia vital sendo sugada, enquanto o boss é cercado por um brilho sombrio que denota sua cura.\033[m")
            if dano_reduzido == 0:
                print(f"\033[1mDano recebido:\033[m \033[31m{dano}\033[m")
                aventureiro.vida -= dano
                if aventureiro.vida <= 0:
                    print("O aventureiro é lançado para trás com a força da onda de choque, seu corpo se contorcendo em agonia enquanto as sombras o envolvem e o arrastam para o abismo.")
                    os.remove("aventureiro.pickle")
                    exit()
                print(f"\033[1mO boss se curou:\033[m \033[32m{dano}\033[m")
                boss.vida += dano
            elif dano_reduzido == 1:
                dano = dano/2
                print("Você consegue se defender do ataque, reduzindo drasticamente o dano do Boss.")
                print(f"\033[1mDano recebido:\033[m \033[31m{dano}\033[m")
                aventureiro.vida -= dano
                if aventureiro.vida <= 0:
                    print("O aventureiro é lançado para trás com a força da onda de choque, seu corpo se contorcendo em agonia enquanto as sombras o envolvem e o arrastam para o abismo.")
                    os.remove("aventureiro.pickle")
                    exit()
                chances = ['contraAtacou', 'naoContraAtacou']
                chance = random.choices(chances, weights = [contra_atacar, 100-contra_atacar])
                if chance == 'contraAtacou':
                    print(f"Após receber o ataque {ataque[0]}, você consegue pular para cima do Boss dando um contra-ataque poderoso.")
                    print(f"\033[31mAtaque: {aventureiro.forca*1.25}\033[m")
                    boss.vida -= aventureiro.forca*1.25
                    if boss.vida <= 0:
                        print("Uma explosão devastadora irrompeu do corpo do Abyssal Overlord, varrendo tudo e todos ao seu redor em uma onda de destruição impiedosa.")
                        print("Você morreu, falhou em perfurar o coração do Boss.")
                        os.remove("aventureiro.pickle")
                        exit()
                    pass
                elif chance == 'naoContraAtacou':
                    print(f"Você tentou contra-atacar, porém {boss.nome} reagiu mais rápdo do que o esperado.")
                    pass
            print(f"\033[1mVida atual:\033[m \033[32m{aventureiro.vida}\033[m")

#função para salvar o aventureiro
def salvarAventureiro(aventureiro):
    with open("aventureiro.pickle", "wb") as f:
        pickle.dump(aventureiro, f)
    print("Dados do aventureiro salvos com sucesso.")

#função para carregar o aventureiro já salvo
def carregarAventureiro():
    with open("aventureiro.pickle", "rb") as f:
        aventureiro = pickle.load(f)
    print(f"Dados do {aventureiro.nome} carregados com sucesso.")
    return aventureiro

############################################################################################################################################
#construtor
while True:
    escolha = input("\nDeseja:\n 1 - Carregar aventureiro salvo\n 2 - Criar um novo aventureiro\n")
    if escolha == '1' or escolha == '2':
        escolha = int(escolha)
    
        if escolha == 2:
            print("""\033[1m
            Bem-vindo a rede\033[m \033[31;1md\033[m\033[32;1mu\033[m\033[33;1mn\033[m\033[34;1mg\033[m\033[35;1me\033[m\033[36;1mo\033[m\033[32;1mn\033[m\033[1m, iremos dar as instruções:
            Seu objetivo é conquistar as 5 dungeons espalhadas pelo mundo, para conquistar cada uma você deve matar o BOSS que nela reside.
            """)

            #criando a instância do jogador
            nome = input("Para começar, qual o seu nome aventureiro? ") 
            aventureiro = Aventureiro(nome)
            salvarAventureiro(aventureiro)

            print(f"Bem-vindo, {aventureiro.nome}")
            print("""
            \033[1mVocê também tem os seus STATUS, que começam da seguinte forma:\033[m
            \033[4m(Obs: quando o código parar dê um enter para continuar)\033[m
            """)

            #chamando o método para mostrar os status
            aventureiro.statusAventureiro()
            break

        elif escolha == 1:
            try:
                aventureiro = carregarAventureiro()
                break
            except FileNotFoundError:
                print("\nNão existe um aventureiro salvo")
                continue
    else:
        print("Escolha inválida")
        continue

#criando a instância da loja
loja = Loja()

#main
while aventureiro.vida > 0:
 menu = '''
 s - Save
 -1 - Visualizar Status
 0 - Loja de itens
 1 - Dark Forest (Dungeon lvl 1)
 '''
 if aventureiro.key > 0:
     menu += '2 - Frozen Tomb (Dungeon lvl 2)\n'
 if aventureiro.key > 1:
     menu += ' 3 - Ghost Village (Dungeon lvl 3)\n'
 if aventureiro.key > 2:
     menu += ' 4 - Pirates Bay (Dungeon lvl 4)\n'
 if aventureiro.key > 3:
     menu += ' 5 - World Destroyed (Dungeon lvl 5)\n'
 if aventureiro.key > 4:
     menu += ' 6 - Abyssal Overlord (Governante das Profundezas)\n'
 contadorFuga = 0
 print("\033[36;1m\nVocê está no saguão, para onde deseja ir?\033[m")
 print(f"""\033[1;36m{menu}\033[m""")
 escolha = input()

 #sequência de escolha principal
 if escolha == 's' or escolha == "S":
     salvarAventureiro(aventureiro)
     print(f"\nCASO {aventureiro.nome.upper()} MORRA, O SAVE SERÁ APAGADO!")
     print("""
     Deseja sair? 
        1 - Sim
        2 - Não
     """)
     escolha = input()
     if escolha == '1':
        exit()
     else:
        pass

 #sequência de escolha principal
 elif escolha == '-1':
     aventureiro.statusAventureiro()
     input()
     continue
 
 #sequência de escolha principal
 elif escolha == '0':
     while True:
       loja.mostrarLoja(aventureiro.ouro,aventureiro.vida, aventureiro.slot1, aventureiro.slot2, aventureiro.slot3, aventureiro.slot4, aventureiro.slot5)
       escolha = input()
       if escolha == '0':
           break
 
       elif escolha == '1':
           if aventureiro.ouro < loja.preco_pocao_pequena:
               print("\033[1mVocê não tem\033[m \033[33mouro\033[m \033[1msuficiente\033[m")
               print(f"\033[1mFaltam\033[m \033[33m{loja.preco_pocao_pequena-aventureiro.ouro} p.o\033[m \033[1mpara comprar a poção\033[m ")
               continue
           else:
               aventureiro.vida += 20
               if aventureiro.vida > (100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]):
                       aventureiro.vida = 100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]
               print("\033[1mVida recuperada:\033[m \033[1;32m+20\033[m")
               print(f"\033[1mVida atual:\033[m \033[1;32m{aventureiro.vida}/{100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]:^2}\033[m")
               aventureiro.ouro -= loja.preco_pocao_pequena

       elif escolha == '2' and aventureiro.key >= 3:
           if aventureiro.ouro < loja.preco_pocao_media:
               print("\033[1mVocê não tem\033[m \033[33mouro\033[m \033[1msuficiente\033[m")
               print(f"\033[1mFaltam\033[m \033[33m{loja.preco_pocao_media-aventureiro.ouro} p.o\033[m \033[1mpara comprar a poção\033[m ")
               continue
           else:
               aventureiro.vida += 60
               if aventureiro.vida > (100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]):
                       aventureiro.vida = 100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]
               print("\033[1mVida recuperada:\033[m \033[1;32m+60\033[m")
               print(f"\033[1mVida atual:\033[m \033[1;32m{aventureiro.vida}/{100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]:^2}\033[m")
               aventureiro.ouro -= loja.preco_pocao_media
               
       elif escolha == '3' and aventureiro.key >= 4:
           if aventureiro.ouro < loja.preco_pocao_grande:
               print("\033[1mVocê não tem\033[m \033[33mouro\033[m \033[1msuficiente\033[m")
               print(f"\033[1mFaltam\033[m \033[33m{loja.preco_pocao_grande-aventureiro.ouro} p.o\033[m \033[1mpara comprar a poção\033[m ")
               continue
           else:
               aventureiro.vida += 150
               if aventureiro.vida > (100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]):
                       aventureiro.vida = 100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]
               print("\033[1mVida recuperada:\033[m \033[1;32m+150\033[m")
               print(f"\033[1mVida atual:\033[m \033[1;32m{aventureiro.vida}/{100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]:^2}\033[m")
               aventureiro.ouro -= loja.preco_pocao_grande

       elif escolha == '4' and aventureiro.key >= 2:
           if aventureiro.bool_slot4 == True:
               print("\033[1mVocê já comprou esse item, mas pela burrice vou tirar 150 de ouro do seu bolso.\033[m")
               print(f"\033[1mOuro:\033[m \033[33m-150 p.o\033[m")
               aventureiro.ouro -= 150
               continue
           if aventureiro.ouro < loja.preco_slot4:
               print("\033[1mVocê não tem\033[m \033[33mouro\033[m \033[1msuficiente\033[m")
               print(f"\033[1mFaltam\033[m \033[33m{loja.preco_slot4-aventureiro.ouro} p.o\033[m \033[1mpara comprar esse slot\033[m ")
               continue
           else:
               print("\033[1mSlot 4 comprado com sucesso, você já pode utilizá-lo\033[m")
               print(f"\033[1mOuro: \033[m \033[33m-{loja.preco_slot4} p.o\033[m \033[1m=\033[m \033[33m {aventureiro.ouro-loja.preco_slot4} p.o\033[m ")
               aventureiro.ouro -= loja.preco_slot4
               aventureiro.bool_slot4 = True

       elif escolha == '5' and aventureiro.key >= 4:
           if aventureiro.bool_slot5 == True:
               print("\033[1mVocê já comprou esse item, mas pela burrice vou tirar 300 de ouro do seu bolso.\033[m")
               print(f"\033[1mOuro:\033[m \033[33m-300 p.o\033[m")
               aventureiro.ouro -= 300
               continue
           if aventureiro.ouro < loja.preco_slot5:
               print("\033[1mVocê não tem\033[m \033[33mouro\033[m \033[1msuficiente\033[m")
               print(f"\033[1mFaltam\033[m \033[33m{loja.preco_slot5-aventureiro.ouro} p.o\033[m \033[1mpara comprar esse slot\033[m ")
               continue
           else:
               print("\033[1mSlot 5 comprado com sucesso, você já pode utilizá-lo\033[m")
               print(f"\033[1mOuro: \033[m \033[33m-{loja.preco_slot5} p.o\033[m \033[1m=\033[m \033[33m{aventureiro.ouro-loja.preco_slot5} p.o\033[m ")
               aventureiro.ouro -= loja.preco_slot5
               aventureiro.bool_slot5 = True

       elif escolha == '6' and aventureiro.key >= 5:
            if aventureiro.ouro < loja.preco_espadaEncantada:
               print("\033[1mVocê não tem\033[m \033[33mouro\033[m \033[1msuficiente\033[m")
               print(f"\033[1mFaltam\033[m \033[33m{loja.preco_espadaEncantada-aventureiro.ouro} p.o\033[m \033[1mpara comprar esse item\033[m ")
               continue
            else:
               espadaEncantada = [500, 0, 99999, 'Espada Encantada']
               print(f"""\n\033[37;1mSTATUS\033[m
                  {espadaEncantada[3]}
                  \033[31mForça: +{espadaEncantada[0]}\033[m
                  \033[32mVida: +{espadaEncantada[1]}\033[m
                  \033[33mVelocidade de Ataque: +{espadaEncantada[2]}\033[m
                  """)
               print("\033[1m\nEspada Encantada comprada com sucesso.\033[m")
               print(f"Você equipou {espadaEncantada[0]}")
               aventureiro.slotEspadaEcantada = espadaEncantada
               aventureiro.forca += aventureiro.slotEspadaEcantada[0]
               aventureiro.vida += aventureiro.slotEspadaEcantada[1]
               aventureiro.velAtaque += aventureiro.slotEspadaEcantada[2]

       elif escolha == '7' and aventureiro.key >= 5:
            if aventureiro.ouro < loja.preco_armaduraEncantada:
               print("\033[1mVocê não tem\033[m \033[33mouro\033[m \033[1msuficiente\033[m")
               print(f"\033[1mFaltam\033[m \033[33m{loja.preco_armaduraEncantada-aventureiro.ouro} p.o\033[m \033[1mpara comprar esse item\033[m ")
               continue
            else:
               print("\033[1mArmadura Encantada comprada com sucesso.\n\033[m")
               #aqui o código vai verificar se você já comprou o slot 4 ou o slot 5 e gerar um texto com base nisso
               while True:
                    armaduraEncantada = {'Armadura Encantada': [50, 1500, 0]}
                    if aventureiro.bool_slot4 == True and aventureiro.bool_slot5 == True:
                        texto = f"""
                        \033[1;37mVocê deseja equipar em qual slot?
                            1 - slot 1 (\033[m{aventureiro.slot1[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot1[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot1[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot1[2]}\033[m)
                            \033[1;37m2 - slot 2 (\033[m{aventureiro.slot2[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot2[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot2[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot2[2]}\033[m)
                            \033[1;37m3 - slot 3 (\033[m{aventureiro.slot3[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot3[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot3[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot3[2]}\033[m)
                            \033[1;37m4 - slot 4 (\033[m{aventureiro.slot4[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot4[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot4[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot4[2]}\033[m)
                            \033[1;37m5 - slot 5 (\033[m{aventureiro.slot5[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot5[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot5[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot5[2]}\033[m)
                            \033[1;37m0 - Não equipar\033[m
                        """
                    elif aventureiro.bool_slot4 == False and aventureiro.bool_slot5 == True:
                        texto = f"""
                        \033[1;37mVocê deseja equipar em qual slot?
                            \033[1;37m1 - slot 1 (\033[m{aventureiro.slot1[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot1[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot1[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot1[2]}\033[m)
                            \033[1;37m2 - slot 2 (\033[m{aventureiro.slot2[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot2[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot2[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot2[2]}\033[m)
                            \033[1;37m3 - slot 3 (\033[m{aventureiro.slot3[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot3[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot3[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot3[2]}\033[m)
                            \033[1;37m5 - slot 5 (\033[m{aventureiro.slot5[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot5[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot5[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot5[2]}\033[m)
                            \033[1;37m0 - Não equipar\033[m
                        """
                    elif aventureiro.bool_slot4 == True and aventureiro.bool_slot5 == False:
                        texto = f"""
                        \033[1;37mVocê deseja equipar em qual slot?
                            1 - slot 1 (\033[m{aventureiro.slot1[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot1[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot1[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot1[2]}\033[m)
                            \033[1;37m2 - slot 2 (\033[m{aventureiro.slot2[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot2[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot2[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot2[2]}\033[m)
                            \033[1;37m3 - slot 3 (\033[m{aventureiro.slot3[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot3[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot3[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot3[2]}\033[m)
                            \033[1;37m4 - slot 4 (\033[m{aventureiro.slot4[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot4[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot4[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot4[2]}\033[m)
                            \033[1;37m0 - Não equipar\033[m
                        """
                    elif aventureiro.bool_slot4 == False and aventureiro.bool_slot5 == False:
                        texto = f"""
                        \033[1;37mVocê deseja equipar em qual slot?
                            1 - slot 1 (\033[m{aventureiro.slot1[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot1[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot1[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot1[2]}\033[m)
                            \033[1;37m2 - slot 2 (\033[m{aventureiro.slot2[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot2[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot2[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot2[2]}\033[m)
                            \033[1;37m3 - slot 3 (\033[m{aventureiro.slot3[3]}\033[1;37m) (Atributos atuais: Força:\033[m \033[31m{aventureiro.slot3[0]}\033[m | \033[1;37mVida:\033[m \033[32m{aventureiro.slot3[1]}\033[m | \033[1;37mVelocidade de Ataque:\033[m \033[35m{aventureiro.slot3[2]}\033[m)
                            \033[1;37m0 - Não equipar\033[m
                        """
                    print(texto)
                    escolha = input()
                    '''
                    esse if serve para pegar o valor em string e depois transformar em inteiro
                    fiz isso para a pessoa poder dar enter ou digitar qualquer outro valor sem dar um erro de Type
                    quando ela digitar um valor errado ou dar enter a mensagem vai aparecer novamente sem ter problemas de erro
                    '''
                    if escolha == '0' or escolha == '1' or escolha == '2' or escolha == '3' or escolha == '4' or escolha == '5':
                        escolha = int(escolha)
                    else:
                        continue
                    #aqui o aventureiro vai escolher em qual slot ele vai querer equipar o item
                    if escolha == 1:
                        print(f"Você equipou {'Armadura Encantada'}")
                        aventureiro.forca -= aventureiro.slot1[0]
                        #aventureiro.vida -= aventureiro.slot1[1]
                        aventureiro.velAtaque -= aventureiro.slot1[2]

                        aventureiro.slot1 = []
                        aventureiro.slot1.append(armaduraEncantada['Armadura Encantada'][0])
                        aventureiro.slot1.append(armaduraEncantada['Armadura Encantada'][1])
                        aventureiro.slot1.append(armaduraEncantada['Armadura Encantada'][2])
                        aventureiro.slot1.append('Armadura Encantada')

                        aventureiro.forca += aventureiro.slot1[0]
                        aventureiro.vida += aventureiro.slot1[1]
                        aventureiro.velAtaque += aventureiro.slot1[2]
                        if aventureiro.vida > (100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]):
                            aventureiro.vida = 100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]
                        break
                    elif escolha == 2:
                        print(f"Você equipou {'Armadura Encantada'}")
                        aventureiro.forca -= aventureiro.slot2[0]
                        #aventureiro.vida -= aventureiro.slot2[1]
                        aventureiro.velAtaque -= aventureiro.slot2[2]

                        aventureiro.slot2 = []
                        aventureiro.slot2.append(armaduraEncantada['Armadura Encantada'][0])
                        aventureiro.slot2.append(armaduraEncantada['Armadura Encantada'][1])
                        aventureiro.slot2.append(armaduraEncantada['Armadura Encantada'][2])
                        aventureiro.slot2.append('Armadura Encantada')

                        aventureiro.forca += aventureiro.slot2[0]
                        aventureiro.vida += aventureiro.slot2[1]
                        aventureiro.velAtaque += aventureiro.slot2[2]
                        if aventureiro.vida > (100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]):
                            aventureiro.vida = 100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]
                        break
                    elif escolha == 3:
                        print(f"Você equipou {'Armadura Encantada'}")
                        aventureiro.forca -= aventureiro.slot3[0]
                        #aventureiro.vida -= aventureiro.slot3[1]
                        aventureiro.velAtaque -= aventureiro.slot3[2]

                        aventureiro.slot3 = []
                        aventureiro.slot3.append(armaduraEncantada['Armadura Encantada'][0])
                        aventureiro.slot3.append(armaduraEncantada['Armadura Encantada'][1])
                        aventureiro.slot3.append(armaduraEncantada['Armadura Encantada'][2])
                        aventureiro.slot3.append('Armadura Encantada')

                        aventureiro.forca += aventureiro.slot3[0]
                        aventureiro.vida += aventureiro.slot3[1]
                        aventureiro.velAtaque += aventureiro.slot3[2]
                        if aventureiro.vida > (100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]):
                            aventureiro.vida = 100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]
                        break
                    elif escolha == 4 and aventureiro.bool_slot4 == True:
                        print(f"Você equipou {'Armadura Encantada'}")
                        aventureiro.forca -= aventureiro.slot4[0]
                        #aventureiro.vida -= aventureiro.slot4[1]
                        aventureiro.velAtaque -= aventureiro.slot4[2]

                        aventureiro.slot4 = []
                        aventureiro.slot4.append(armaduraEncantada['Armadura Encantada'][0])
                        aventureiro.slot4.append(armaduraEncantada['Armadura Encantada'][1])
                        aventureiro.slot4.append(armaduraEncantada['Armadura Encantada'][2])
                        aventureiro.slot4.append('Armadura Encantada')

                        aventureiro.forca += aventureiro.slot4[0]
                        aventureiro.vida += aventureiro.slot4[1]
                        aventureiro.velAtaque += aventureiro.slot4[2]
                        if aventureiro.vida > (100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]):
                            aventureiro.vida = 100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]
                        break
                    elif escolha == 5 and aventureiro.bool_slot5 == True:
                        print(f"Você equipou {'Armadura Encantada'}")
                        aventureiro.forca -= aventureiro.slot5[0]
                        #aventureiro.vida -= aventureiro.slot5[1]
                        aventureiro.velAtaque -= aventureiro.slot5[2]

                        aventureiro.slot5 = []
                        aventureiro.slot5.append(armaduraEncantada['Armadura Encantada'][0])
                        aventureiro.slot5.append(armaduraEncantada['Armadura Encantada'][1])
                        aventureiro.slot5.append(armaduraEncantada['Armadura Encantada'][2])
                        aventureiro.slot5.append('Armadura Encantada')

                        aventureiro.forca += aventureiro.slot5[0]
                        aventureiro.vida += aventureiro.slot5[1]
                        aventureiro.velAtaque += aventureiro.slot5[2]
                        if aventureiro.vida > (100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]):
                            aventureiro.vida = 100 + aventureiro.slot1[1] + aventureiro.slot2[1] + aventureiro.slot3[1] + aventureiro.slot4[1] + aventureiro.slot5[1]
                        break
                    else:
                        print("Valor inválido, escolha novamente.")
                        continue
       else:
           print("\033[1mConclua os requisitos para comprar esse slot\033[m")

 #sequência de escolha principal
 elif escolha == '1':
     aventureiro.key_dungeon = 1
     #(nome, forca, vida, velAtaque, ouroDropado, chanceFuga)
     aranha = Monstros("Aranha (lvl 1)", 4, 1, 20, 20, 55)
     cobra = Monstros("Cobra (lvl 1)", 4, 2, 40, 20, 55)
     lobo = Monstros("Lobo (lvl 1)", 6, 3, 8, 25, 40)
     urso = Monstros("Urso (lvl 3)", 12, 5, 8, 50, 60)

     #(forca, vida, velAtaque)
     loot1 = {"\033[33;1mArmadura Bad Wolfão - lvl 1 (lendário)\033[m": [0, 50, 0],
             "\033[33;1mEspada Bad Wolfiado - lvl 1 (lendário)\033[m": [5, 0, 11],
             "\033[35;1mAdaga de presa de lobo - lvl 1 (épico)\033[m": [2, 0, 20],
             "\033[35;1mArmadura de pele de lobo - lvl 1 (épico)\033[m": [0, 25, 5],
             "\033[34;1mEspada quebrada - lvl 1 (raro)\033[m": [1, 0, 5],
             "\033[34;1mArmadura furada - lvl 1 (raro)\033[m": [0, 15, 0]}
     #(forca, vida=5, velAtaque, ouroDropado, loot)
     boss1 = Boss("Bad Wolf", 5, 5, 80, 180, loot1)

     listaInstancia1 = [aranha, cobra, lobo, urso]

     #main
     print("""\033[1m
     Você adentrou a Dark Forest (dungeon de nível 1), onde muitos monstros perambulam por essas terras sombrias e amaldiçoadas. 
     Como um aventureiro corajoso e determinado em busca da cabeça do temido BAD WOLF, você segue em frente, pronto para enfrentar os perigos que encontrar pelo caminho."\033[m
     """)
     print("\033[34;1mMonstro à vista, hora de lutar.\033[m")
     batalha(listaInstancia1)
     if contadorFuga == 1:
         continue
     aranha.vida = 1
     cobra.vida = 2
     lobo.vida = 3
     urso.vida = 5
     print("\033[34;1m\nóh não, outro monstro à vista.\033[m")
     input()
     batalha(listaInstancia1)
     if contadorFuga == 1:
         continue
     print("""\n\033[1m
     Após vencer os braços direitos do temido BAD WOLF, você se prepara para a batalha final contra o chefe da dungeon. 
     Com o coração acelerado, você caminha por duas longas horas pela Dark Forest até que, de repente, um uivo assustador ecoa a 60 graus a oeste. Sabendo que é o BAD WOLF, você se prepara para o confronto mais desafiador da sua jornada.\033[m\n
     """)
     batalhaBoss(boss1)
     print("""\n\033[1m
      Você derrotou a primeira\033[m \033[31;1md\033[m\033[32;1mu\033[m\033[33;1mn\033[m\033[34;1mg\033[m\033[35;1me\033[m\033[36;1mo\033[m\033[32;1mn\033[m!! \033[1mMeus parabéns.
      Dungeon liberada: Frozen Tomb
      \033[m\n""")
     if aventureiro.key == 0:
          aventureiro.key = 1

 #sequência de escolha principal
 elif escolha == '2' and aventureiro.key >= 1:
     aventureiro.key_dungeon = 2
     #(nome, forca, vida, velAtaque, ouroDropado, chanceFuga)
     goblin = Monstros("Goblin de Gelo (lvl 2)", 7, 3, 40, 20, 55)
     espirito = Monstros("Espírito Congelado (lvl 2)", 8, 3, 5, 25, 55)
     druida = Monstros("Druida de Gelo (lvl 3)", 15, 4, 10, 30, 40)
     golem = Monstros("Golem de Gelo (lvl 4)", 20, 10, 5, 70, 65)

     #(forca, vida, velAtaque)
     loot2 = {"\033[33;1mPeitoral Dragônico - lvl 2 (lendário)\033[m": [0, 100, 0],
             "\033[33;1mLança Zero Absoluto - lvl 2 (lendário)\033[m": [12, 0, 20],
             "\033[35;1mGarra de dragão - lvl 2 (épico)\033[m": [8, 0, 25],
             "\033[35;1mArmadura Congelada - lvl 2 (épico)\033[m": [0, 60, -10],
             "\033[34;1mEstaca de Gelo - lvl 2 (raro)\033[m": [3, 0, 10],
             "\033[34;1mBota Quebradiça - lvl 2 (raro)\033[m": [0, 20, 0]}
     #(forca, vida=5, velAtaque, ouroDropado, loot)
     boss2 = Boss("Frozen Dragon", 15, 10, 80, 200, loot2)

     listaInstancia2 = [goblin, espirito, druida, golem]

     #main
     print("""\033[34;1m
      Você entrou na Frozen Tomb (dungeon de lvl 2)...
      Milhares de anos atrás um mago poderoso condenou essas terras congelando tudo que via pela frente,
      muitos monstros de gelo surgiram com os resquícios de poder que sobraram do grande mago, tome cuidado... um erro e será congelado para sempre.\033[m
      """)
     print("\033[34;1mVocê sente um calafrio, monstro à vista.\033[m")
     batalha(listaInstancia2)
     if contadorFuga == 1:
          continue
     goblin.vida = 3
     espirito.vida = 3
     druida.vida = 4
     golem.vida = 10
     print("\033[34;1m\nMais um monstro à vista.\033[m")
     input()
     batalha(listaInstancia2)
     if contadorFuga == 1:
          continue
     print("""\n\033[1m
      Um enorme dragão surge das colinas e nota sua presença, ele está furioso com o intruso que invadiu sua dungeon\033[m\n
      """)
     batalhaBoss(boss2)
     print("""\n\033[1m
      Você derrotou a segunda\033[m \033[31;1md\033[m\033[32;1mu\033[m\033[33;1mn\033[m\033[34;1mg\033[m\033[35;1me\033[m\033[36;1mo\033[m\033[32;1mn\033[m!! \033[1mMeus parabéns.
      Dungeon liberada: Ghost Village
      \033[m\n""")
     if aventureiro.key == 1:
          aventureiro.key = 2

 #sequência de escolha principal
 elif escolha == '3' and aventureiro.key >= 2:
     aventureiro.key_dungeon = 3
     #(nome, forca, vida, velAtaque, ouroDropado, chanceFuga)
     espectro = Monstros("Espectro (lvl 3)", 15, 12, 20, 40, 30)
     poltergeist = Monstros("Poltergeist (lvl 3)", 12, 15, 20, 40, 30)
     banshee = Monstros("Banshee (lvl 3)", 25, 3, 36, 30, 31)
     holandes = Monstros("Holandês Voador (lvl 5)", 22, 15, 20, 110, 50)

     #(forca, vida, velAtaque)
     loot3 = {"\033[33;1mArmadura de Sangue de Demônio - lvl 3 (lendário)\033[m": [0, 320, 0],
             "\033[33;1mLivro Amaldiçoado - lvl 3 (lendário)\033[m": [70, 0, 5],
             "\033[35;1mFoice Espectral - lvl 3 (épico)\033[m": [40, 0, 15],
             "\033[35;1mCapa de Almas Perdidas - lvl 3 (épico)\033[m": [0, 240, 10],
             "\033[34;1mEspada Fantasma - lvl 3 (raro)\033[m": [25, 0, 10],
             "\033[34;1mAnel Espectral - lvl 3 (raro)\033[m": [0, 150, 5]}
     #(forca, vida=5, velAtaque, ouroDropado, loot)
     boss3 = Boss("Astaroth, O Demônio Infernal", 25, 18, 80, 300, loot3)

     listaInstancia3 = [espectro, poltergeist, banshee, holandes]

     #main
     print("""\033[34;1m
      Ao adentrar as profundezas, seus olhos fitam um vilarejo abandonado, que emana uma aura de magia obscura e te envolve, deixando-o preso dentro dele. Bem-vindo à Dungeon Ghost Village  (Dungeon lvl 3)\033[m
      """)
     print("\033[34;1mDemônios te cercam, hora de lutar.\033[m")
     batalha(listaInstancia3)
     if contadorFuga == 1:
          continue
     espectro.vida = 12
     poltergeist.vida = 15
     banshee.vida = 3
     holandes.vida = 15
     print("\033[34;1m\nOutro fantasma à vista.\033[m")
     input()
     batalha(listaInstancia3)
     if contadorFuga == 1:
         continue
     print("""\n\033[1m
     Após derrotar todos os fantasmas da vila, Astaroth fica enfurecido e busca vingaça.\033[m\n
     """)
     batalhaBoss(boss3)
     print("""\n\033[1m
      Você derrotou a terceira\033[m \033[31;1md\033[m\033[32;1mu\033[m\033[33;1mn\033[m\033[34;1mg\033[m\033[35;1me\033[m\033[36;1mo\033[m\033[32;1mn\033[m!! \033[1mMeus parabéns.
      Dungeon liberada: Pirates Bay
      \033[m\n""")
     if aventureiro.key == 2:
          aventureiro.key = 3

 #sequência de escolha principal
 elif escolha == '4' and aventureiro.key >= 3:
     aventureiro.key_dungeon = 4
     marujo = Monstros("Marujo (lvl 4)", 45, 150, 20, 70, 30)
     marinheiro = Monstros("Marinheiro (lvl 4)", 35, 220, 200, 72, 30)
     bucaneiro = Monstros("Bucaneiro (lvl 5)", 60, 180, 1, 75, 34)
     barbaNegra = Monstros("Barba Negra (lvl 7)", 95, 220, 70, 250, 50)

     #(forca, vida, velAtaque)
     loot4 = {"\033[33;1mArmadura de Escama - lvl 4 (lendário)\033[m": [20, 500, 2],
             "\033[33;1mMosquete - lvl 4 (lendário)\033[m": [150, 0, 5],
             "\033[35;1mRevólver de Pólvora - lvl 4 (épico)\033[m": [80, 0, 8],
             "\033[35;1mFarda Pirata - lvl 4 (épico)\033[m": [0, 340, 0],
             "\033[34;1mCimitarra Pirata - lvl 4 (raro)\033[m": [65, 0, 35],
             "\033[34;1mChapéu Pirata - lvl 4 (raro)\033[m": [0, 250, 5]}
     #(forca, vida=5, velAtaque, ouroDropado, loot)
     boss4 = Boss("Kraken", 90, 350, 80, 450, loot4)

     listaInstancia4 = [marujo, marinheiro, bucaneiro, barbaNegra]

     #main
     print("""\033[34;1m
      O mar... muitas vezes pode ser traiçoeiro, sombrio e perverso. Em busca da quarta dungeon você entra no território aquático mais perigoso conehcido pelos aventureiros.
      Em busca da cabeça do Kraken você entra na Dungeon conhecida como Pirates Bay (Dungeon lvl 4)\033[m
      """)
     print("\033[34;1mSeu navio foi invadido, prepare-se.\033[m")
     batalha(listaInstancia4)
     if contadorFuga == 1:
         continue
     marujo.vida = 150
     marinheiro.vida = 220
     bucaneiro.vida = 140
     barbaNegra = 220
     print("\033[34;1m\nInimigo à vista, atirar!!\033[m")
     input()
     batalha(listaInstancia4)
     if contadorFuga == 1:
         continue
     print("""\n\033[1m
     As ondas do oceano se agitam violentamente e um som ensurdecedor é ouvido quando o temido Kraken emerge das profundezas, dominando o campo de batalha com sua presença colossal.\033[m\n
     """)
     batalhaBoss(boss4)
     print("""\n\033[1m
     Você derrotou a quarta\033[m \033[31;1md\033[m\033[32;1mu\033[m\033[33;1mn\033[m\033[34;1mg\033[m\033[35;1me\033[m\033[36;1mo\033[m\033[32;1mn\033[m!! \033[1mMeus parabéns.
     Dungeon liberada: Destroyed World
     \033[m\n""")
     if aventureiro.key == 3:
         aventureiro.key = 4

 #sequência de escolha principal
 elif escolha == '5' and aventureiro.key >= 4:
     aventureiro.key_dungeon = 5
     shadowDragon = Monstros("Shadow Dragon (lvl 6)", 150, 370, 35, 150, 35)
     dracoLich = Monstros("Dracolich (lvl 6)", 150, 350, 52, 150, 40)
     beholder = Monstros("Beholder (lvl 7)", 200, 430, 10, 180, 45)
     lichKing = Monstros("Lich King (lvl 9)", 300, 350, 50, 300, 60)

     #(forca, vida, velAtaque)
     loot5 = {"\033[33;1mCoroa do Rei Destruído - lvl 5 (lendário)\033[m": [0, 1000, 10],
             "\033[33;1mEspada do Rei Destruído - lvl 5 (lendário)\033[m": [320, 0, 20],
             "\033[35;1mMachado dos Condenados - lvl 5 (épico)\033[m": [250, 0, 10],
             "\033[35;1mPeitoral de Escamas Sombrias - lvl 5 (épico)\033[m": [0, 750, 0],
             "\033[34;1mKatana Sombria - lvl 5 (raro)\033[m": [150, 0, 35],
             "\033[34;1mManto das Trevas - lvl 5 (raro)\033[m": [20, 450, 0]}
     #(forca, vida, velAtaque, ouroDropado, loot)
     boss5 = Boss("Rei Destruído", 250, 750, 50, 750, loot5)

     listaInstancia5 = [shadowDragon, dracoLich, beholder, lichKing]

     #main
     print("""\033[34;1m
     O aventureiro caminhou com cautela até a entrada da Dungeon Destruida, sua mochila pesada nas costas. Ele sabia dos perigos que a esperavam dentro daquele lugar abandonado há tanto tempo. Com uma respiração profunda, ele deu um passo adiante e desceu as escadas íngremes, decidido a enfrentar qualquer desafio que surgisse em seu caminho. 
     A escuridão engoliu o aventureiro enquanto ele avançava cada vez mais fundo na dungeon, determinado a desvendar seus mistérios e sair vitorioso.
     Bem-vindo a Dungeon World Destroyed (Dungeon lvl 5)\033[m
     """)
     print("\033[34;1mO som de arranhar de garras ecoa pelas paredes, anunciando que criaturas selvagens estão próximas.\033[m")
     batalha(listaInstancia5)
     if contadorFuga == 1:
         continue
     shadowDragon.vida = 370
     dracoLich.vida = 350
     beholder.vida = 430
     lichKing.vida = 350
     print("\033[34;1m\nUm novo monstro surge da escuridão!\033[m")
     input()
     batalha(listaInstancia5)
     if contadorFuga == 1:
         continue
     print("""\n\033[1m
     Com passos pesados e olhar fixo em seu objetivo, o Rei Destruído adentra a câmara final, pronto para enfrentar os heróis que ousaram desafiá-lo.\033[m\n
     """)
     batalhaBoss(boss5)
     print("""\n\033[1m
     Você derrotou a quinta\033[m \033[31;1md\033[m\033[32;1mu\033[m\033[33;1mn\033[m\033[34;1mg\033[m\033[35;1me\033[m\033[36;1mo\033[m\033[32;1mn\033[m!! \033[1mMeus parabéns.
     Abyssal Overlord acordou, cuidado!
     \033[m\n""")
     if aventureiro.key == 4:
         aventureiro.key = 5
 
 #sequência de escolha principal
 elif escolha == '6' and aventureiro.key >= 5:
     aventureiro.key_dungeon = 5

     #(forca, vida, velAtaque)
     loot6 = {}

     #(forca, vida, velAtaque, ouroDropado, loot)
     boss6 = Boss("Abyssal Overlord", 400, 4000, 9999999999999, 10000, loot6)
     #main
     print(f"""\033[34;1m
     \nEnquanto você adentra a câmara final, a atmosfera se torna densa e opressiva. Seus sentidos são atingidos por um cheiro pútrido, e você ouve o som de garras afiadas raspando contra pedra. No centro da sala, em um trono macabro, está o Abyssal Overlord, um ser colossal de aparência monstruosa. Sua presença irradia um mal insondável, e seus olhos brilham com uma chama sinistra. 
     Com uma voz grave e gutural, ele fala: '{aventureiro.nome.capitalize()} ousa me desafiar? Preparem-se para enfrentar a fúria do Abyssal Overlord, criatura das trevas que governa este reino com punho de ferro!'\033[m
     """)
     bossFInal(boss6)
     if contadorFuga == 1:
         continue
    
 else:
     continue
