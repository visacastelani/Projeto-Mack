#STATUS
forca = 0
vitalidade = 0
inteligencia = 0
agilidade = 0
carisma = 0

#RPG
comecar = str(input('Digite "START" para começar o jogo '))
comecar.upper()

if comecar == "START":
    print("Você está prestes a vivenciar uma experiência única, mas antes vamos ao seu personagem...")

nome= str(input("Digite seu nome: "))

sexo= int(input("Digite '1' para sexo masculino ou '2' para feminino: "))
          
classe = int(input("\nBem vindo ao menu de seleção de classes."
                   "\nPara selecionar apenas digite o número referente à classe:\n \nMago 1 \nGuerreiro 2 \nArqueiro 3 \nGatuno 4 \nBardo 5 \n"))
                  

##########################################

#MAGO
if sexo == 1 and classe == 1:
    print("\n",nome, ", o Mago")
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
    print("\n",nome ,", a Maga")
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
    print("\n",nome, ", o Guerreiro")
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
    print("\n",nome ,", a Guerreira")
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
    print("\n",nome, ", o Arqueiro")
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
    print("\n",nome ,", a Arqueira")
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
    
#GATUNO
elif sexo == 1 and classe == 4:
    print("\n",nome, ", o Gatuno")
    forca = 3
    vitalidade = 5
    inteligencia = 5
    agilidade = 9
    carisma = 4
    print("\nStatus: ",
          "\nForça: ",forca,
          "\nVitalidade: ",vitalidade,
          "\nInteligência: ",inteligencia,
          "\nAgilidade: ",agilidade,
          "\nCarisma: ",carisma)



elif sexo == 2 and classe == 4:
    print("\n",nome ,", a Gatuna")
    forca = 3
    vitalidade = 5
    inteligencia = 5
    agilidade = 9
    carisma = 4
    print("\nStatus: ",
          "\nForça: ",forca,
          "\nVitalidade: ",vitalidade,
          "\nInteligência: ",inteligencia,
          "\nAgilidade: ",agilidade,
          "\nCarisma: ",carisma)
#GATUNO

##########################################
    
#BARDO
if sexo == 1 and classe == 5:
    print("\n",nome, ", o Bardo")
    forca = 2
    vitalidade = 3
    inteligencia = 5
    agilidade = 3
    carisma = 9
    print("\nStatus: ",
          "\nForça: ",forca,
          "\nVitalidade: ",vitalidade,
          "\nInteligência: ",inteligencia,
          "\nAgilidade: ",agilidade,
          "\nCarisma: ",carisma)

    
elif sexo == 2 and classe == 5:
    print("\n",nome ,", a Barda")
    forca = 2
    vitalidade = 3
    inteligencia = 5
    agilidade = 3
    carisma = 9
    print("\nStatus: ",
          "\nForça: ",forca,
          "\nVitalidade: ",vitalidade,
          "\nInteligência: ",inteligencia,
          "\nAgilidade: ",agilidade,
          "\nCarisma: ",carisma)
          
#BARDO

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
#GATUNO
    
elif sexo == 1 and classe == 4:
    classe1=", o Gatuno"
    print("\nBem-vindo ao mundo medieval de (Nome a decidir)", nome,classe1,
          ".\nEsteja ciente que suas escolhas irão formar seu futuro, então escolha com sabedoria.")
    
elif sexo == 2 and classe == 4:
    classe1=", a Gatuna"
    print("\nBem-vindo ao mundo medieval de (Nome a decidir)", nome,classe1,
          ".\nEsteja ciente que suas escolhas irão formar seu futuro, então escolha com sabedoria.")
 
#GATUNO
##########################################
#BARDO

if sexo == 1 and classe == 5:
    classe1=", o Bardo"
    print("\nBem-vindo ao mundo medieval de (Nome a decidir)", nome,classe1,
          ".\nEsteja ciente que suas escolhas irão formar seu futuro, então escolha com sabedoria.")

if sexo == 2 and classe == 5:
    classe1=", a Barda"
    print("\nBem-vindo ao mundo medieval de (Nome a decidir)", nome,classe1,
          ".\nEsteja ciente que suas escolhas irão formar seu futuro, então escolha com sabedoria.")

input()










