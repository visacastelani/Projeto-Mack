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

sexo= int(input("Digite '1' para sexo masculino ou '2' para feminino "))
          
classe = int(input("\nBem vindo ao menu de seleção de classes."
                   "\nPara selecionar apenas digite o número referente à classe:\n \nMago 1 \nGuerreiro 2 \nArqueiro 3 "))
                  

##########################################

#MAGO
if sexo == 1 and classe == 1:
    print("\n",nome, ", o Mago")
    forca = 2
    vitalidade = 3
    inteligencia = 8
    agilidade = 3
    carisma = 4
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
    carisma = 4
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
