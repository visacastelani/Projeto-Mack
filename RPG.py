#STATUS
forca = 0
vitalidade = 0
inteligencia = 0
agilidade = 0
carisma = 0

#RPG
comecar = str(input('Aperte "ENTER" para começar o jogo '))


if comecar == "":
    print("\n\nVocê está prestes a vivenciar uma experiência única!"
          "\n\nMas antes, um pequeno tutorial:"
          "\nO <jogo> é narrado, e opções de diálogo são dadas ao protagonista."
          " Para escolhe-las, digite apenas o número que"
          " corresponda a opção desejada."
          "\nAs mensagens que precisarão da escolha do usuário"
          " virão acompanhadas de números. \n\nEX:"
          "\n\n     (1) A"
          "\n\n     (2) B"
          "\n\n     (3) C"
          "\n\nDito isto, vamos ao seu personagem...")

nome= str(input("\nDigite seu nome: "))


sexo= int(input("\nDigite (1) para sexo masculino ou (2) para feminino: "))
          
classe = int(input("\nBem vindo ao menu de seleção de classes."
                   "\nPara selecionar apenas digite o número referente à classe:"
                   "\n(1) Mago: Os Oráculos de Hmacadura  "
                   "\n(2) Guerreiro: Os Guerreiros de Lepercia"
                   "\n(3) Arqueiro: Os Discipulos de Vicasa  \n"))

    
##########################################

#MAGO
if sexo == 1 and classe == 1:
    print("\n",nome, ",o Oráculo de Hmacadura")
    mentor = " Hmacadema"


    
elif sexo == 2 and classe == 1:
    print("\n",nome ,",a Oráculo de Hmacadura")
    mentor = " Hmacadema"

          
#MAGO

##########################################

#GUERREIRO
elif sexo == 1 and classe == 2:
    print("\n",nome, ",A Força de Lepercia")
    mentor = " Lepercia"


elif sexo == 2 and classe == 2:
    print("\n",nome ,",A Força de Lepercia")
    mentor = " Lepercia"

#GUERREIRO

##########################################

#ARQUEIRO
elif sexo == 1 and classe == 3:
    print(nome, ",o Discípulo de Vicasa")
    mentor = " Vicasa"




elif sexo == 2 and classe == 3:
    print("\n",nome ,",a Discípula de Vicasa")
    mentor = " Vicasa"

#ARQUEIRO

##########################################
    

print("\nSeu personagem está pronto!\n")

##########################################
#MAGO

if sexo == 1 and classe == 1:
    classe1= ",o Mago"
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
          ".\nEsteja ciente que suas escolhas irão formar seu futuro, então as faça com sabedoria.")

#ARQUEIRO
#########################################


#########INÍCIO
print("\n\n\nHá muito tempo atrás, uma maldição fora lançada para o Reino(nome)"
      "por uma Bruxa muito poderosa."
      "\nSabendo da maldição, o rei e a rainha chamaram as três lendas mais"
      " poderoas do Reino: \n\n-Hmacadura, o sábio Mago"
      "\n-Vicasa, o ágil Arqueiro"
      "\n-Lepercia, o grande Guerreiro."
      "\n\nDeram aos três então, a tarefa de levar seu bebê"
      " para um lugar fora do alcance da maldição"
      ",até que um dia seja seguro retornar.")
      
if sexo == 1 and classe == 1:
    print("As três lendas cumpriram a ordem do rei.\nMas o herdeiro criou um vínculo com o Mago, e já sendo propício às artes místicas, resolveu treina-lo e molda-lo a sua imagem."
          "\n\n\n\n\n25 anos depois...\n\n")

elif sexo == 2 and classe == 1:
    print("As três lendas cumpriram a ordem do rei.\nMas a herdeira criou um vínculo com o Mago, e já sendo propícia às artes místicas, resolveu treina-la e molda-la a sua imagem."
          "\n\n\n\n\n25 anos depois...\n\n")

elif sexo == 1 and classe == 2:
    print("As três lendas cumpriram a ordem do rei.\nMas o herdeiro criou um vínculo com o Guerreiro, e já que era forte fisicamente e determinada, resolveu treina-lo e molda-lo a sua imagem. "
          "\n\n\n\n\n25 anos depois...\n\n")
    
elif sexo == 2 and classe == 2:
    print("As três lendas cumpriram a ordem do rei.\nMas a herdeira criou um vínculo com o Guerreiro, e já que era forte fisicamente e determinada, resolveu treina-la e molda-la a sua imagem. "
          "\n\n\n\n\n25 anos depois...\n\n")
    
elif sexo == 1 and classe == 3:
    print("As três lendas cumpriram a ordem do rei.\nMas o herdeiro criou um vínculo com o Arqueiro, e já que possuía certa agilidade e uma boa mira, resolveu treina-lo e molda-lo a sua imagem. "
          "\n\n\n\n\n25 anos depois...\n\n")

elif sexo == 2 and classe == 3:
    print("As três lendas cumpriram a ordem do rei.\nMas a herdeira criou um vínculo com o Arqueiro, e já que possuía certa agilidade e uma boa mira, resolveu treina-la e molda-la a sua imagem.  "
          "\n\n\n\n\n25 anos depois...\n\n")
#########MAGO
if classe == 1:
    print(nome,"estava lendo na antiga biblioteca, quando então um servo veio trazer uma mensagem:",
          "\n\n'",mentor," lhe chama '."
          "\nSem demora",nome,",reune suas coisas e vai em direção ao seu Mentor, curioso"
          " com o que ele poderia querer lhe contar")
#########MAGO

#########GUERREIRO
elif classe == 2:
    print(nome,"estava treinando na academia, quando então um servo veio trazer uma mensagem:",
          "\n\n'",mentor," lhe chama '."
          "\nSem demora",nome,",reune suas coisas e vai em direção ao seu Mentor, curioso"
          " com o que ele poderia querer lhe contar")
#########GUERREIRO

#########ARQUEIRO
else:
    print(nome,"estava treinando com seus alvos, quando então um servo veio trazer uma mensagem:",
          "\n\n'",mentor," lhe chama '."
          "\nSem demora",nome,",reune suas coisas e vai em direção ao seu Mentor, curioso"
          " com o que ele poderia querer lhe contar")
#########ARQUEIRO

    print("\n\nAo chegar,",nome,"pede licença:",
          "\n\n-Olá",mentor,"! Queria me ver?"
          "\n\n-Entre",nome,",há algo que preciso contar.")

dialogo = int(input("\n-Ora, o que é dessa vez? Lembre-se que não tenho tempo para rumores bobos!(1)\n"
                    "\n\n-O que me conta? Noticias do Reino?(2)\n"))
########MAGO
if dialogo == 1 and classe == 1:
    print("\n-Não seja arrogante",nome,". Talvez passar muito tempo com os livros tenha"
          " te feito esquecer como ter modos.\n")
elif dialogo == 2 and classe ==1:
    print("\n-Pergaminhos voaram do Reino, está na hora de retomar o que é seu!\n")
########MAGO

########GUERREIRO
if dialogo == 1 and classe == 2:
    print("\n-Um guerreiro nao tem apenas força bruta, mas sabe o que é ter respeito, e isto lhe falta.\n")
elif dialogo == 2 and classe ==2:
    print("\n-Noticias do Reino. A hora de combater as forças malignas chegou.\n")
########GUERREIRO


#########ARQUEIRO
elif dialogo == 1 and classe == 3:
              print("\n\n-Está esquecendo uma das maiores virtudes",nome,"? A pressa é a maior inimiga da precisão!\n")
elif dialogo == 2 and classe == 3:
              print("\n\n-Você já é grande,",nome,"! Está na hora de retomar o que é seu!\n")
#########ARQUEIRO  

#########INÍCIO







input()
    










