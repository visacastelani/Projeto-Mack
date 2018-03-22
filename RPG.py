from random import randint 
#RPG
hp = 10
enemyHP = 10

comecar = str(input("Digite 'START' para começar o jogo "))
comecar = comecar.upper()


while comecar != "START":
    print("\n\nPor favor, digite '5START'")
    comecar = str(input('\n\nDigite "START" para começar o jogo '))
    comecar = comecar.upper()
if comecar == "START":
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
                   "\n(1) -Mago: Os Oráculos de Hmacadura  "
                   "\n(2) -Guerreiro: Os Guerreiros de Lepercia"
                   "\n(3) -Arqueiro: Os Discípulos de Vicasa  \n"))

   
##########################################

#MAGO
if sexo == 1 and classe == 1:
    print("\n",nome, ",o Oráculo de Hmacadura")
    mentor = " Hmacadura"


    
elif sexo == 2 and classe == 1:
    print("\n",nome ,",a Oráculo de Hmacadura")
    mentor = " Hmacadura"

          
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
print("\n\n\nHá muito tempo atrás, uma maldição fora lançada sobre o Reino de Gammelt Rike"
      "por uma Bruxa muito poderosa."
      "\nSabendo da maldição, o rei e a rainha chamaram as três lendas mais"
      " poderoas do Reino: \n\n-Hmacadura, o sábio Mago"
      "\n-Vicasa, o ágil Arqueiro"
      "\n-Lepercia, o grande Guerreiro."
      "\n\nDeram aos três então, a tarefa de levar seu bebê"
      " para um lugar fora do alcance da maldição"
      ",até que um dia seja seguro retornar.")
      
if sexo == 1 and classe == 1:
    print("\n\nAs três lendas cumpriram a ordem do rei."
          "\nMas o herdeiro criou um vínculo com o Mago,"
          "e já sendo propício às artes místicas, resolveu treiná-lo e moldá-lo a sua imagem."
          "\n\n\n\n\n25 anos depois...\n\n")

elif sexo == 2 and classe == 1:
    print("\n\nAs três lendas cumpriram a ordem do rei.\nMas a herdeira criou um vínculo com o Mago,"
          "e já sendo propícia às artes místicas, resolveu treiná-la e moldá-la a sua imagem."
          "\n\n\n\n\n25 anos depois...\n\n")

elif sexo == 1 and classe == 2:
    print("\n\nAs três lendas cumpriram a ordem do rei.\nMas o herdeiro criou um vínculo com o Guerreiro,"
          "e já que era forte fisicamente e determinada, resolveu treiná-lo e moldá-lo a sua imagem. "
          "\n\n\n\n\n25 anos depois...\n\n")
    
elif sexo == 2 and classe == 2:
    print("\n\nAs três lendas cumpriram a ordem do rei.\nMas a herdeira criou um vínculo com o Guerreiro,"
          "e já que era forte fisicamente e determinada, resolveu treiná-la e moldá-la a sua imagem. "
          "\n\n\n\n\n25 anos depois...\n\n")
    
elif sexo == 1 and classe == 3:
    print("\n\nAs três lendas cumpriram a ordem do rei.\nMas o herdeiro criou um vínculo com o Arqueiro,"
          "e já que possuía certa agilidade e uma boa mira, resolveu treiná-lo e moldá-lo a sua imagem. "
          "\n\n\n\n\n25 anos depois...\n\n")

elif sexo == 2 and classe == 3:
    print("\n\nAs três lendas cumpriram a ordem do rei.\nMas a herdeira criou um vínculo com o Arqueiro,"
          "e já que possuía certa agilidade e uma boa mira, resolveu treiná-la e moldá-la a sua imagem.  "
          "\n\n\n\n\n25 anos depois...\n\n")
#########MAGO
if classe == 1:
    print(nome,"estava lendo na antiga biblioteca, quando então um servo veio trazer uma mensagem:",
          "\n\n'",mentor," lhe chama '."
          "\nSem demora",nome,",reune suas coisas e vai em direção ao seu Mentor, curioso"
          " com o que ele poderia querer lhe contar.\n\n")
#########MAGO

#########GUERREIRO
elif classe == 2:
    print(nome,"estava treinando na academia, quando então um servo veio trazer uma mensagem:",
          "\n\n'",mentor," lhe chama '."
          "\nSem demora",nome,",reune suas coisas e vai em direção ao seu Mentor, curioso"
          " com o que ele poderia querer lhe contar.\n\n")
#########GUERREIRO

#########ARQUEIRO
else:
    print(nome,"estava treinando com seus alvos, quando então um servo veio trazer uma mensagem:",
          "\n\n'",mentor," lhe chama '."
          "\nSem demora",nome,",reune suas coisas e vai em direção ao seu Mentor, curioso"
          " com o que ele poderia querer lhe contar.\n\n")
#########ARQUEIRO

    print("\n\nAo chegar,",nome,"pede licença:",
          "\n\n-Olá",mentor,"! Queria me ver?"
          "\n\n-Entre",nome,",há algo que preciso contar.\n\n")

print("################## ESCOLHA ##################")
dialogo = int(input("\n-Ora, o que é dessa vez? Lembre-se que não tenho tempo para rumores bobos!(1)\n"
                    "\n\n-O que me conta? Notícias do Reino?(2)\n"))
########MAGO

if dialogo == 1 and classe == 1:
    print("\n-Não seja arrogante",nome,". Talvez passar muito tempo com os livros tenha"
          " te feito esquecer como ter modos.\n")
elif dialogo == 2 and classe ==1:
    print("\n-Acabo de ter uma visão, está na hora de retomar o que é seu!\n")
########MAGO

########GUERREIRO
if dialogo == 1 and classe == 2:
    print("\n-Um guerreiro nao tem apenas força bruta, mas sabe o que é ter respeito, e isto lhe falta.\n")
elif dialogo == 2 and classe ==2:
    print("\n-O Mago teve uma visão. A hora de combater as forças malignas chegou.\n")
########GUERREIRO


#########ARQUEIRO
elif dialogo == 1 and classe == 3:
              print("################## ESCOLHA ##################") 
              print("\n\n-Está esquecendo uma das maiores virtudes",nome,"? A pressa é a maior inimiga da precisão!\n")
elif dialogo == 2 and classe == 3:
              print("\n\n-Você já é grande,",nome,"! Está na hora de retomar o que é seu!\n")
#########ARQUEIRO  

#########PRÓLOGO

print("\n-Enfim chegara a hora."
      "\n\nDisse",mentor,
      "\n\n-Você deve retornar ao Reino e livrá-lo do mal que o assola.\n"
      ,nome," sentiu seu estômago esfriar enquanto",mentor," terminava suas palavras"
      "\n\n-Como posso combater algo que mal conheço?"
      "\nPerguntou ",nome,
      "\n\n-Os antigos já contavam histórias sobre bruxas",nome,"."
      "\n Se quiser saber sobre a fonte do mal, consulte os documentos"
      " que encontrar ao longo da sua jornada."
      "\n\n Mas lembre-se. a batalha nem sempre é a melhor opção!")
#########PRÓLOGO

print(nome," então partiu para o Reino. O caminho"
      " seria longo, passaria por montanhas e florestas."
      " e não sabia, por fim, o que poderia enfrentar durante"
      " a sua jornada.")

print("################## ESCOLHA ##################")
print(nome,",")
caminho = int(input("chegara ao pé do que parecia ser uma infinita montanha."
                  "\nPercebeu em seu mapa então, que haviam dois caminhos para se tomar:"
                  "\n\n(1)-O primeiro, mais longo, por fora da montanha, demoraria dias para cruzá-la"
                  "\n\n(2)-O segundo, por uma antiga mina de carvão, usada por mineradores antes mesmo dele nascer.\n"))

#########CAMINHO PELA MONTANHA
if caminho == 1:
    print(nome,"decidiu então ir pelo primeiro caminho."
          "\nNão sabia quais perigos poderiam o aguardar pelas minas,"
          "\ncom certeza, a primeira opção lhe parecia mais segura"
          "\nComeçou então a escalada, antigos caminhos de pedras"
          "\nusados por pastores de ovelhas pareciam ser a rota clara."
          "\nJá era tarde, e",nome," já pensava em como passaria"
          " a noite.\nAvistou então, ao topo da montanha, o que parecia ser"
          " uma velha cabana")

    print("\n\n################## ESCOLHA ##################")

    cabana = int(input("\nPelo menos de longe, parece ser um local seguro"
                           " para passa a noite. O herdeiro então decide: "
                           "\n\n(1)-Ir até a cabana e verificar o local."
                           "\n\n(2)-Fazer uma fogueira e passar a noite ao ar livre.\n"))

    if cabana == 1:
        print(nome," decidiu então por passar a noite na cabana, mas precisaria visitar"
                  " o local primeiro, para saber se era seguro."
                  "\nAo chegar próximo a cabana",nome," começou a escutar barulhos estranhos"
                  " vindos da velha casa. \nSe aproximando com cautela, abriu a porta e entrou."
                  "\nNada a vista, o lugar parecia mesmo seguro, até que...:"
                  "\n\n-RAAAWRRRRRRR!!!!")
        
        hp = 10
        enemyHP = 10

        lutar = str(input("\n\nDigite 'LUTAR' para comaçar o duelo!"))
        lutar = lutar.upper()

        while lutar != "LUTAR":
                lutar = str(input("\n\nDigite 'LUTAR' para começar o duelo!"))
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
                                print("\n\nA batalha foi árdua, você lutou"
                                      " bravamente, mas infelizmente"
                                      " as forças das trevas venceram."
                                      "\n\nVocê esta morto!")
                                vitoria = 0
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
                                vitoria = 1
                                break
        if vitoria == 1:
            print("\n\nHavia um esqueleto dentro da cabana!"
                  "\nEle te atacou de surpresa, mas seu tempo"
                  " de treino fez valer e você conseguiu derrotá-lo!"
                  "\n\n",nome," olhou em volta e percebeu uma velha bolsa"
                  " de couro, largada próximo a uma mesa."
                  "\nAo chegar perto, notara que havia uma carta, e então"
                  " decidiu lê-la.\n\nA carta dizia....."
                  "\n-----------------------------------------------------------------------------------------------------------------------------------------------"
                  "\n\nEspero que alguém leia essa carta..."
                  "\n\nMeu nome é Grace, a Arcana Branca. Ou pelo menos era antes de toda essa bagunça."
                  "\nQuando aquela Bruxa das Trevas retornou, pensávamos que não sofríamos tanto perigo,"
                  "\n mas ela conseguiu encontrar um livro de feitiços, que foi escrito pelo primeiro"
                  "\n Necromante que pisou nessas terras e acabara de lançar sua maldição. O desespero foi geral,"
                  "\n muitos ficaram paralisados esperando seu infeliz destino, outros se uniram e fugiram rapidamente."
                  "\n Mas outros escaparam sem honra, assim como eu. Não me arrependo do que eu fiz, mas também não me orgulho."
                  "\n Vou contar essa história, em memória da que morreu para que eu pudesse viver."
                  "\n Fui sempre praticante de magia Branca, ajudava sempre a família de pescadores quando o dia de pesca não fora muito boa,"
                  "\n em um piscar de olhos suas redes estavam cheias de peixes."
                  "\n Eles eram amigos de meu irmão e quando ele estava viajando em suas cruzadas, eu os ajudava."
                  "\n Mas então algo muito estranho aconteceu, era hora do almoço, quando uma mancha negra surgiu no céu."
                  "\n Eu sabia que aquilo se tratara de uma maldição, chamei a família de pescadores para alertar o que estava acontecendo."
                  "\n A nuvem se aproximava muito depressa e eles não acreditaram em mim. Estávamos distantes da fronteira do reino,"
                  "\n foi então que tive uma ideia, não era boa, pois uma Arcana Branca nunca podia pensar em usar magia das Trevas,"
                  "\n porém era questão de vida e morte. Existia um feitiço de teletransporte que podia usar para nos salvar,"
                  "\n entretanto exigia um sacrifício. A família preferiu ficar e enfrentar seu destino, eu não tive essa coragem,"
                  "\n então segurei a filha mais nova da família em meus braços e evaporei dali."
                  "\n Quando pisquei já estava fora do reino e fora do alcance da maldição. Em meus braços, estava o esqueleto da menininha."
                  "\n Fazemos o que fazemos para sobreviver, eu fiz a minha escolha, eles fizeram a deles."
                  "\n Não sou mais digna de meu título, eu mudei a partir daquele dia, meu nome agora é Grace, a Arcana das Trevas.\n\n"
                  "\n-----------------------------------------------------------------------------------------------------------------------------------------------")


        else:
            print("Não há futuro para alguém morto")

    if cabana == 2:
        print(nome," decide então acampar em uma clareira próxima."
          "\nEra melhor e mais seguro, e estava uma noite agradável..")

elif caminho == 2:
        print("\n\nMesmo com receio do que iria encontrar,",nome," escolheu ir pelas minas.\n"
              "O caminho pela mina era assustador.\nTudo rangia e fazia barulhos estranhos"
              "\nAcendera uma torcha para iluminar o seu caminho e adentrou a mina."
              "\nAlém da escuridão, o ambiente o sufocava e tornavam seus passos mais pesados.\nn",
              nome," então decidiu descansar próximo ao que parecia ser um alojamento"
              " dos antigos trabalhadores.\n"
              "Ao vasculhar alguns velhos sacos largados por ali em busca de algo para comer",
              nome," encontrou um velho pedaço de papel, gasto e sujo, parecia uma carta."
              "\nComeçou a lê-la, e nela dizia...\n\n"
              "\n-----------------------------------------------------------------------------------------------------------------------------------------------"
              "\n Caro leitor, meu nome é Agar, o Ladino e tenho uma história para contar,"
              "\n a história de como fugi de Gammelt Rike. Era um dia normal no nosso reino,"
              "\n crianças brincavam nas ruas, mercenários gastavam seus ouros nas tavernas,"
              "\n cavaleiros asseguravam a segurança de todos. Até que recebi um contrato real"
              "\n para investigar uma estranha força mística que surgira na parte leste do reino,"
              "\n modéstia à parte, sempre fui o melhor ladino do reino. Chegando lá, vi uma sombra se materializando,"
              "\n foi quando surgiu ela, a mesma bruxa que liderara a Grande Guerra das Bruxas."
              "\n Ela fora seguida por seu lacaio, que entregara uma espécie de livro,"
              "\n mas um livro que emanava uma aura negra, até uma caverna. Esperei ao anoitecer para averiguar mais um pouco,"
              "\n ouvi a bruxa dizer que naquele livro existia uma maldição, mas uma maldição tão poderosa que seria necessário um sacrifício."
              "\n O lacaio disse que era muito arriscado, pois a vida de sua mestra seria perdida no processo."
              "\n Levei então as informações até o Rei Arathorn II, neto do Grande Rei Eldarion."
              "\n Ele reuniu o grande concelho, que incluía as três lendas, as deu ordens que não conheço,"
              "\n apenas sei que os três não foram mais vistos em Gammelt Rike e que os outros campeões reais foram caçar a bruxa."
              "\n Depois de dois dias de busca sem nenhum êxito, o Rei ordenou que os cidadãos deveriam se recompor,"
              "\n pois iria ser servida uma ceia ao meio dia para compensar seus esforços."
              "\n Porém isso foi um erro, quando todos as pessoas estavam prestes a cear uma nuvem negra como a noite vinha do horizonte,"
              "\n não tive nenhuma dúvida, montei em meu cavalo e fugi do castelo. Tentei ajudar o máximo de pessoas que pude,"
              "\n infelizmente não possuo poderes divinos, logo o que pude fazer foi encher uma carruagem com mulheres e crianças e seguir além das montanhas."
              "\n Foi a primeira vez que me senti realmente útil, pois minhas ações e habilidades sempre foram associadas com trapaceiros,"
              "\n e ladrões, mas nesse dia me senti como se fosse Agar, o Herói."
              "\n-----------------------------------------------------------------------------------------------------------------------------------------------")
    
print("\n\n\nEnfim, passado alguns dias",nome," já conseguia ver a grande Floresta Mork."
      "\nTodos a temiam, estava claro o por quê."
      "\nÁrvores altas como gigantes e sombras negras que espantavam qualquer viajante"
      "\nAquele não era um lugar para ficar de passagem.\n",nome," precisava logo"
      " sair dali."
      "\n\nO problema então, surgia ali.\nEm seu mapa",nome," observou uma bifurcação"
      ", ambos os caminhos levavam ao castelo, o epicentro da maldição, porém passavam por locais"
      " diferentes,\nmas igualmente ameaçadores")

print("\n\n################## ESCOLHA ##################\n\n")

caminho2 = int(input("\n\n(1) A Leste, o caminho levava para Dodsgrotte, uma antiga gruta"
                     " dita ser abandonada, mas que era lar da poderosa Bruxa em tempos antigos."
                     "\n(2) A Oeste, Landsbyen, uma vila de elfos, que outrora exalava sabedoria"
                     " antiga.\n"))



####COMEÇO CAMINHO 1 LESTE
if caminho2 == 1:
    print("\n\nO espírito de aventura queimava forte em ",nome,".\n"
          "Decidiu então partir para Dodsgrotte. Quem sabe quais mistérios"
          " ainda podiam ser revelados no lar da Bruxa."
          "\n\nAlguns dias de viagem separavam ",nome," de seu destino, era melhor se apressar,"
          "\nventos sinistros sopraram, e algo das sombras parecia lhe observar."
          "\nCom mais alguns dias de viagem ",nome," se deparou com algumas placas indicando o caminho"
          "\npara o reino, sabia que então, a Gruta estava perto\n"
          ,nome," se deparou com a entrada da caverna, tão sinistra quanto pudera imaginar."
          "\nTeve então, de escolher: ")

    print("\n\n################## ESCOLHA ##################\n\n")

    gruta = int(input("(1) -Entrar na Gruta e tentar encontrar algum documento que"
                      " contesse alguma informação útil."
                      "\n(2) -É mais sabido preservar a vida e continuar sua história,"
                      "\nprovavelmente a opção mais segura seria ignorar a Gruta e seguir para o Reino\n"))
    if gruta == 1:
        print(nome," estava mesmo determinado em descobrir mais sobre os mistérios da maldição."
              "\nNa Gruta então, ele adentrou.\nSua respiração não conseguia esconder seu medo,"
              "\nmas o olhar em seus olhos mostravam fogo e coragem.\n\n"
              "Barulhos estranhos podiam ser ouvidos ao fundo, logo sua respiração já"
              " estava mais pesada.\n"
              "Uma silhueta já podia ser vista, às sombras de uma fogueira crepitante."
              "\nQuanto mais próximo chegava,",nome," podia ver com mais clareza a criatura que guardava"
              " na caverna da Bruxa."
              "\nEra horrível, o corpo já estava morto por fora há muito tempo",nome,", não conseguia"
              " entender como ainda estava de pé."
              "\nO monstro estava próximo ao fogo, e um armário podia ser visto ao fundo."
              "\nAlgo ali prendeu a atenção de ",nome,".\nHavia o que parecia ser velhos pergaminhos"
              " próximos a uma montanha de livros velhos."
              "\n",nome," precisava se decidir ali:")

        print("\n\n################## ESCOLHA ##################\n\n")


        stealth = int(input("\n\n(1) -Tentar passar sorrateiramente e roubar os documentos."
                                "\n(2) -Voltar a entrada e seguir o caminho.\n"))
        if stealth == 1:
        
            chance = randint(0,3)

            if chance == 0 or chance == 1:
                ##########################INSERIR O LIVRO
                print("\nVocê conseguiu se esgueirar, apanhou uma bolsa com alguns pergaminhos"
                      " e correu para um lugar seguro. "
                      "\nQuando sentiu que estava em um local,"
                      "\ntirou um pergaminho da bolsa, nele estava escrito:"
                      "\n-----------------------------------------------------------------------------------------------------------------------------------------------"
                      "\nHoje completa um mês desde que a maldição chegou à Grammelt Rike."
                      "\nEu vi minha amada e meu bebê serem transformados em monstros."
                      "\nNão me transformei, pois, uso um colar à prova de maldições, foi um presente de um feiticeiro."
                      "\nEla e meu bebê tentaram me matar."
                      "\nNão tive alternativa, a não ser acabar com o sofrimento deles, mas a culpa está me consumindo por dentro."
                      "\nDo que adianta não ter me transformado em um monstro fisicamente, mas mentalmente ter me transformado no pior monstro que já existiu?"
                      "\nDeixo esse recado para qualquer alma que ainda lembra como se lê."
                      "\nMeu nome é Azaghal, e estou prestes a rever meus amados..."    
                      "\n-----------------------------------------------------------------------------------------------------------------------------------------------")
                
            elif chance == 2 or chance == 3:
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
                        if  hp == 0 or hp < 0:
                            print("\n\n\n\nVocê lembra das histórias que contavam sobre os bosques."
                                  "\nInfelizmente,todas elas eram verdadeiras."
                                  "\nVocê esta morto!")
                            break
                            

                        print("\nSua vez de atacar!")
                        print("\nDMG no Monstro: ", dmg1,
                                "\nHP do Monstro:", enemyHP,)

                        input("\n\nAperte 'ENTER' para ir para a"
                            " próxima rodada!")


                        

                        if enemyHP == 0 or enemyHP < 0:
                            print("\n\n\n\nVocê derrotou o inimigo!"
                                  "\n\nA criatura medonha solta um grito antes de cair"
                                  " no chão, parecia ter sido morta uma segunda vez"
                                  "\nPodendo agora olhar com mais calma",nome," olhou pelo local até encontrar uma bolsa cheia de pergaminhos,"
                                  "\npegou então um pergaminho da bolsa, nele estava escrito:"
                                  "\n-----------------------------------------------------------------------------------------------------------------------------------------------"
                                  "\nHoje completa um mês desde que a maldição chegou à Grammelt Rike."
                                  "\nEu vi minha amada e meu bebê serem transformados em monstros."
                                  "\nNão me transformei, pois, uso um colar à prova de maldições, foi um presente de um feiticeiro."
                                  "\nEla e meu bebê tentaram me matar."
                                  "\nNão tive alternativa, a não ser acabar com o sofrimento deles, mas a culpa está me consumindo por dentro."
                                  "\nDo que adianta não ter me transformado em um monstro fisicamente, mas mentalmente ter me transformado no pior monstro que já existiu?"
                                  "\nDeixo esse recado para qualquer alma que ainda lembra como se lê."
                                  "\nMeu nome é Azaghal, e estou prestes a rever meus amados..."    
                                  "\n-----------------------------------------------------------------------------------------------------------------------------------------------")
                                 ##############RESUMIR A VIAGEM ( USAR TERMOS GENÉRICOS, QUE SIRVAM PARA OS DOIS CAMINHOS ##################
                        break
            else:
                print("\nEnfrentar o monstro e acabar morto por um pedaço"
                      " de papel era um risco real.",
                      nome," decidiu então, voltar à entrada.")
                        





    elif gruta == 2:
        print("\nNenhum documento valeria a pena arriscar o próprio pescoço."
            "\n",nome," decidiu retornar à entrada.")

####FIM CAMINHO 1


####COMEÇO CAMINHO 2 OESTE
        
    if caminho2 == 2:
        print("\nO espírito de curiosidade queimava forte em",nome,".\n"
              "\nDecidiu então partir para Landsbyen, a antiga Vila de Elfos."
              "\nQuem sabe quais segredos mais podiam ser revelados\n quando"
              " compartilhada a sabedoria dos elfos antigos?")
        print("\n",nome," já perdera a conta de quantas horas estava andando"
          " e a vila não parecia estar ficando mais perto."
          "\nFinalmente então,",nome," consegue ver distante algum sinal de civilização."
          "\nApertando o passo, logo se via de frente para a Vila dos elfos."
          "\nEstranhou o silêncio mortal, mas não estava surpreso."
          "\nNão havia um sinal de vida na vila.."
          "\nA noite já estava chegando, não havia muito tempo para nada, então",nome," tinha logo"
          " que se decidir: ")

        print("\n\n################## ESCOLHA ##################\n\n")

        vila = int(input("(1) -Se abrigar em uma das casas e procurar informações."
                     "\n(2) -Recolher materiais para preparar uma fogueira.\n"))

        if vila == 1:
            print("\nA escolha estava clara e ",nome," sabia o que procurar."
                  "\nQualquer informação sobre a maldição iria ajudar em sua jornada."
                  "\n\nUma das contruções lhe chamou a atenção,"
                  "\numa cabana grande de dois andares, parecia ser uma das"
                  " únicas construções que sobreviveu à catastrofes e o tempo,"
                  "\num bom lugar para procurar um livro que antecedia a maldição."
                  "\nFelizmente a busca teve resultado:"
                  "\n-----------------------------------------------------------------------------------------------------------------------------------------------"
                  "\nEssa é a história de Izzy, a Caçadora de Demônios"
                  "\nNasceu entre os elfos feiticeiros da floresta, que dividia Gammelt Rike e as montanhas."
                  "\nQuando era apenas uma criança, viu seus pais serem mortos por demônios que habitavam as cavernas das montanhas."
                  "\nIsso foi um marco em sua vida, após desse evento, ela jurou caçar cada um até que fossem extintos."
                  "\nE foi o que ela fez, durante a Era de Ouro do reino, aceitava contratos e caçava as criaturas da noite."
                  "\nAté que muitos boatos de magia negra foram relatados por todo reino."
                  "\nNuma noite, ela seguiu vultos até a entrada de uma caverna distante dos arredores do reino de Gammelt Rike,"
                  "\nentão conseguiu ver que existia um exército de necromantes liderado por uma Bruxa das Trevas."
                  "\nQuando alertou a realeza, o Rei Eldarion proclamou um concelho,"
                  "\nque incluía os conselheiros reais e os campeões Axxi’s, o Paladino Negro; David, o Bárbaro e Izzy, a Caçadora de Demônios."
                  "\nComo todos já sabem, o Reino de Gammelt Rike saiu vitorioso dessa guerra, mas Izzy não."
                  "\nEla e os outros dois líderes dessa batalha haviam sido mortos em batalha."
                  "\n-----------------------------------------------------------------------------------------------------------------------------------------------")  
        else:
            print("Exausto da viagem,",nome," decide fazer uma fogueira. Se aquecer e alimentar"
                  " a essa hora se tornara também uma questão de sobrevivência."
                  "\nUnindo isso a uma boa noite de sono, o dia seguinte seria produtivo,"
                  "\npouco agora restava do caminho até o Reino.")

####FIM CAMINHO 2

print("\n\nEm seu mapa agora,",nome," via que apenas alguns poucos dias de viagem o impediam de chegar ao Reino.")

input()
    










