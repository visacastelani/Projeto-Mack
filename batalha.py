from random import randint

contador = 0
contador1= 0

hp = 10
enemyHP = 10

lutar = str(input("\n\nDigite 'LUTAR' para comaçar o duelo!"))
lutar = lutar.upper()

while lutar != "LUTAR":
        lutar = str(input("\n\nDigite 'LUTAR' para comaçar o duelo!"))
        lutar = lutar.upper()

if lutar == "LUTAR":

        while hp > 0 or enemyHP > 0:
                
                print("\nO inimigo irá atacar, defenda-se!")
                #DANO RECEBIDO
                dmg = randint(0,2)
                hp = hp - dmg
                print("\n####   DANO RECEBIDO: ",dmg,
                "\n####   HP ATUAL:      " ,hp)
                if  hp == 0 or hp < 0:
                        print("\n\nVocê esta morto!")
                        break
                
                           
                                            
                print("\nSua vez de atacar!")
                #DANO CAUSADO
                dmg1 = randint(0,3)
                enemyHP = enemyHP - dmg1
                print("\n####   DANO CAUSADO: ", dmg1,
                "\n####   HP DO MONSTRO:", enemyHP)

                input("\n\nAperte 'ENTER' para ir para a"
                                   " próxima rodada!")

                

                if enemyHP == 0 or enemyHP < 0:
                        print("\n\nVocê derrotou o inimigo!")
                        break
                


input()
