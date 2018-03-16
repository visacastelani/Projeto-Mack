from random import randint

hp = 10
enemyHP = 10

print("Você encontra um inimigo pelo caminho. Ele parece estar distraído."
      "Deseja tentar passar despercebido? (Chance = 3 em 5 de sucesso)")

opcao = str(input("Digite 'Stealth' para passar sorrateiramente ou Lutar para lutar"))
opcao = opcao.upper()

if opcao == "STEALTH":
    
    chance = randint(0,3)

    if chance == 0 or chance == 1 or chance == 2:
        print("\nVocê conseguiu passar sorrateiramente!")

    elif chance == 3 :
        print("\nO inimigo te notou, prepare-se!")
        while hp >0 or enemyHP >0:
    
            if hp >0 or enemyHP >0:

                #DANO RECEBIDO
                dmg = randint(0,2)
                hp = hp - dmg
                
                #DANO CAUSADO
                dmg1 = randint(0,3)
                enemyHP = enemyHP - dmg1

                print("\nO inimigo irá atacar, defenda-se!")
                print("\nDMG: ",dmg,
                    "\nHP: " ,hp)
                
                print("\nSua vez de atacar!")
                print("\nDMG no Monstro: ", dmg1,
                      "\nHP do Monstro:", enemyHP,)


            if  hp == 0 or hp < 0:
                print("\n\n\n\nVocê esta morto!")
                break

            elif enemyHP == 0 or enemyHP < 0:
                print("\n\n\n\nVocê derrotou o inimigo!")
                break


elif opcao =="LUTAR":
    print("\n\nVocê decidiu Lutar!")
    while hp >0 or enemyHP >0:
    
        if hp >0 or enemyHP >0:

            #DANO RECEBIDO
            dmg = randint(0,2)
            hp = hp - dmg
            #DANO CAUSADO
            dmg1 = randint(0,3)
            enemyHP = enemyHP - dmg1
            print("\nO inimigo irá atacar, defenda-se!")
            print("\nDMG: ",dmg,
                  "\nHP: " ,hp)

            print("\nSua vez de atacar!")
            print("\nDMG no Monstro: ", dmg1,
                  "\nHP do Monstro:", enemyHP,)

        if  hp == 0 or hp < 0:
            print("\n\n\n\nVocê esta morto!")
            break

        elif enemyHP == 0 or enemyHP < 0:
            print("\n\n\n\nVocê derrotou o inimigo!")
            break
    

                





    
