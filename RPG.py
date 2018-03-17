#STATUS
forca = 0
vitalidade = 0
inteligencia = 0
agilidade = 0
carisma = 0

#RPG
comecar = str(input('Aperte "ENTER" para começar o jogo '))
comecar.upper()

if comecar == "":
    print("Você está prestes a vivenciar uma experiência única!"
          "\n\nMas antes vamos ao seu personagem...")

nome= str(input("\nDigite seu nome: "))

sexo= int(input("\nDigite '1' para sexo masculino ou '2' para feminino: "))
          
classe = int(input("\nBem vindo ao menu de seleção de classes."
                   "\nPara selecionar apenas digite o número referente à classe:"
                   "\n \n[1] Mago: Os oráculos de Macadura  "
                   "\n[2] Guerreiro: Os mlk que não faz nada HUE  "
                   "\n[3] Arqueiro: Os Discipulos de Vicasa  "))

    
##########################################

#MAGO
if sexo == 1 and classe == 1:
    print("\n",nome, ", o Oraculo de Macadura")
    forca = 2
    vitalidade = 3
    inteligencia = 8
    agilidade = 3
    carisma = 7
    print("\nStatus: ",
          "\nForça: ",forca,
          "\nVitalidade: ",vitalidade,
          "\nInteligência: ",inteligencia,
          "\nAgilidade: ",agilidade,
          "\nCarisma: ",carisma)

    
elif sexo == 2 and classe == 1:
    print("\n",nome ,", o Oraculo de Macadura")
    forca = 2
    vitalidade = 3
    inteligencia = 8
    agilidade = 3
    carisma = 7
    print("\nStatus: ",
          "\nForça: ",forca,
          "\nVitalidade: ",vitalidade,
          "\nInteligência: ",inteligencia,
          "\nAgilidade: ",agilidade,
          "\nCarisma: ",carisma)
          
#MAGO

##########################################

#GUERREIRO
elif sexo == 1 and classe == 2:
    print("\n",nome, ", A Força de Leo")
    forca = 8
    vitalidade = 5
    inteligencia = 1
    agilidade = 3
    carisma = 4
    print("\nStatus: ",
          "\nForça: ",forca,
          "\nVitalidade: ",vitalidade,
          "\nInteligência: ",inteligencia,
          "\nAgilidade: ",agilidade,
          "\nCarisma: ",carisma)

elif sexo == 2 and classe == 2:
    print("\n",nome ,", A Força de Leo")
    forca = 8
    vitalidade = 5
    inteligencia = 1
    agilidade = 3
    carisma = 4
    print("\nStatus: ",
          "\nForça: ",forca,
          "\nVitalidade: ",vitalidade,
          "\nInteligência: ",inteligencia,
          "\nAgilidade: ",agilidade,
          "\nCarisma: ",carisma)
#GUERREIRO

##########################################

#ARQUEIRO
elif sexo == 1 and classe == 3:
    print("\n",nome, ", o Discípulo de Vicasa")
    forca = 4
    vitalidade = 5
    inteligencia = 1
    agilidade = 7
    carisma = 4
    print("\nStatus: ",
          "\nForça: ",forca,
          "\nVitalidade: ",vitalidade,
          "\nInteligência: ",inteligencia,
          "\nAgilidade: ",agilidade,
          "\nCarisma: ",carisma)



elif sexo == 2 and classe == 3:
    print("\n",nome ,", a Discípula de Vicasa")
    forca = 4
    vitalidade = 5
    inteligencia = 1
    agilidade = 7
    carisma = 4
    print("\nStatus: ",
          "\nForça: ",forca,
          "\nVitalidade: ",vitalidade,
          "\nInteligência: ",inteligencia,
          "\nAgilidade: ",agilidade,
          "\nCarisma: ",carisma)
#ARQUEIRO

##########################################
    

print("Seu personagem está pronto!\n")

##########################################
#MAGO

if sexo == 1 and classe == 1:
    classe1= ",o Mago"
    print(nome,classe1)
    print("\nBem-vindo ao mundo medieval de (Nome a decidir)", nome, classe1,
          ".\nEsteja ciente que suas escolhas irão formar seu futuro, então escolha com sabedoria.")

    
elif sexo == 2 and classe == 1:
    classe1=", a Maga"
    print("\nBem-vindo ao mundo medieval de (Nome a decidir)", nome,classe1,
          ".\nEsteja ciente que suas escolhas irão formar seu futuro, então escolha com sabedoria.")

#MAGO
##########################################
#GUERREIRO
    
elif sexo == 1 and classe == 2:
    classe1=", o Guerreiro"
    print("\nBem-vindo ao mundo medieval de (Nome a decidir)", nome,classe1,
          ".\nEsteja ciente que suas escolhas irão formar seu futuro, então escolha com sabedoria.")

elif sexo == 2 and classe == 2:
    classe1=", a Guerreira"
    print("\nBem-vindo ao mundo medieval de (Nome a decidir)", nome,classe1,
          ".\nEsteja ciente que suas escolhas irão formar seu futuro, então escolha com sabedoria.")

#GUERREIRO
#########################################
#ARQUEIRO
    
elif sexo == 1 and classe == 3:
    classe1=", o Arqueiro"
    print("\nBem-vindo ao mundo medieval de (Nome a decidir)", nome,classe1,
          ".\nEsteja ciente que suas escolhas irão formar seu futuro, então escolha com sabedoria.")

elif sexo == 2 and classe == 3:
    classe1=", a Arqueira"
    print("\nBem-vindo ao mundo medieval de (Nome a decidir)", nome,classe1,
          ".\nEsteja ciente que suas escolhas irão formar seu futuro, então escolha com sabedoria.")

#ARQUEIRO
#########################################



print("\n\n\nATO I : ")

input()










