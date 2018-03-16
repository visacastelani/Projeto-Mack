from random import randint

contador = 0
contador1= 0

hp = 10
enemyHP = 10


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
        print("Você esta morto!")
        break

    elif enemyHP == 0 or enemyHP < 0:
        print("Você derrotou o inimigo!")
        break
    
