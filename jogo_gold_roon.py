from sys import exit

# Variável global adicionada para verificar se o jogador é digno de pegar a espada
digno = True

# adicionamos .lower() em todas as decisões, para garantir que a resposta seja precisa
def gold_room(): 
    global digno  # Declara que vamos usar a variável global 'digno'
    print("Esta sala está cheia de ouro. Quanto você pega? (Máximo 100)") 
    choice = input("> ")
    if choice.isdigit() and 0 <= int(choice) <= 100: 
        how_much = int(choice) #consertamos o código, ele precisa pegar menos de 50 de ouro para progredir
        if how_much > 0:
            digno = False  # Se o jogador pegar qualquer quantidade de ouro, ele não é digno
    else: 
        dead("Cara, aprenda a digitar um número entre 0 e 100.") 
    if how_much < 50:
        print("Legal, você não é ganancioso!") 
    else: 
        dead("Seu ganancioso!")
    sword_room()  # Avança para a sala da espada sagrada após a sala de ouro

def bear_room(): #sala do urso (já existente, porém com mudanças)
    print("Há um urso aqui.")
    print("O urso tem um monte de mel.")
    print("O urso gordo está na frente de outra porta.")   
    print("Como você vai mover o urso?") 
    print("Você pode provocar ele o pegar o seu mel.") #frase adicionada para deixar mais claro as opções
    bear_moved = False
    while True: 
        choice = input("> ").lower()
        if choice == "pegar mel":
            dead("O urso olha para você e então dá um tapa na sua cara.")
        elif choice == "provocar urso" and not bear_moved: 
            print("O urso se moveu da porta.")
            print("Você pode passar por ela agora.") 
            bear_moved = True
        elif choice == "provocar urso" and bear_moved:
            dead("O urso fica irritado e mastiga sua perna.") 
        elif choice == "abrir porta" and bear_moved: 
            elpato()  # Muda para a sala do pato gigante
        else: 
            print("Não faço ideia do que isso significa.")

def cthulhu_room(): #(já existente, porém com mudanças)
    print("Aqui você vê o grande mal Cthulhu.")
    print("Ele, isso, seja lá o que for, olha para você e você enlouquece.") 
    print("Você foge para salvar sua vida, come sua cabeça ou dá um soco nele?")
    choice = input("> ").lower()
    if "fugir" in choice: 
        start()  # Volta para a sala inicial
    elif "cabeça" in choice: 
        dead("Delicioso.") #morte
    elif "soco" in choice: #terceira opção (a certa)
        print("Você, mais louco do que a própria criatura, decide dar o melhor soco da sua vida.")
        print("Porém, de nada adianta, o grande mal te empurra tão forte que você voa até a próxima sala.")
        riddle_room()  # Vai para a sala da charada
    
    else:
        cthulhu_room()  # Caso de escolha inválida, repete a sala

def elpato(): # sala do pato gigante (sala nova)
    print("Ao abrir a porta você se depara com uma fofa e gigantesca figura: um pato gigante!")
    print("O pato, com seus grandes olhos vermelhos encara você, seu enorme bico está pintado pelo sangue de alguém que passou por lá anteriormente.")
    print("Duas ideias surgem nessa sua cabeça mediocre: você pode voltar ou correr em direção ao pato.")
    print("O que você faz?")
    choice = input("> ").lower() #escolha
    if "voltar" in choice: #escolha errada = morte
        dead("O urso estava esperando pela sua volta e agora você será a janta dele.") 
    elif "correr" in choice: #escolha certa = continua
        print("Você corre o mais rápido que pode em direção ao pato, ele tenta te devorar, mas você consegue passar por baixo dele.")
        print("Uma nova e grande porta o espera mais para frente, você, sem tempo para pensar, entra dentro da próxima sala.")
        gold_room()  # Avança para a sala do ouro
    else:
        elpato()  # Caso de escolha inválida, repete a sala

def riddle_room(): # sala da charada
    print("Você entra em uma sala misteriosa, onde as paredes estão cobertas de símbolos antigos.")
    print("No centro da sala, uma voz ecoa:")
    print("'Eu estou sempre faminto, eu devoro tudo que toco. Se me deres de beber, eu morrerei. O que sou eu?'")
    print("Você deve responder corretamente para avançar. Qual é a sua resposta?")
    
    choice = input("> ").lower()

    if choice == "fogo" or choice == "chama": #escolhas corretas
        print("A voz se cala e uma porta secreta se abre, revelando uma sala cheia de ouro.")
        gold_room()  # Avança para a sala do ouro
    else:
        dead("A voz grita: 'Errado!' e o chão se abre, te engolindo para a morte.") #qualquer outra escolha leva a morte

# Nova função adicionada para verificar se o jogador é digno de pegar a espada sagrada
def sword_room():
    global digno  # Declara que vamos usar a variável global 'digno'
    print("Você entra em uma sala com uma espada sagrada enterrada em uma pedra.")
    if digno: #se você não pegou nenhum ouro na sala do ouro você ganha o jogo
        print("A espada brilha e se solta facilmente da pedra. Você é digno e a pega com sucesso!")
        print("Você ganhou o jogo! Parabéns!")
        exit(0)  # Termina o jogo com vitória
    else: 
        print("Você tenta puxar a espada, mas ela não se move. Você não é digno.")
        dead("Você falhou em obter a espada e morreu em sua tentativa.")  # O jogador morre se não for digno

def dead(why): # função de morte, não fizemos alterações
    print(why, "Bom trabalho!") 
    exit(0)
    

def start(): # função de inicio, não fizemos mudança
    print("Você está em uma sala escura.")
    print("Há uma porta à sua direita e outra à sua esquerda.") 
    print("Qual você escolhe?")
    choice = input("> ").lower()
    if choice == "esquerda": 
        bear_room()  # Vai para a sala do urso
    elif choice == "direita": 
        cthulhu_room()  # Vai para a sala do Cthulhu
    else: 
        dead("Você tropeça na sala até morrer de fome.") # morte





start() #para dar inicio ao game
