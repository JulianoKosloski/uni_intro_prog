"""Aluno: Juliano Kosloski
   Curso: Tecnologia em Análise e Desenvolvimento de Sistemas"""

from random import Random, randint


print("Zombie Dice – Prototipo") #mensagem de boas-vindas para o usuário
print("Boas-vindas! Esse eh o Zombie Dice, siga as instrucoes para jogar: ")

num_players = 0

while num_players < 2: #recebe o número de jogadores e testa se é maior ou igual que dois

    print("Por favor, insira o numero de jogadores: ")
    temp = int(input())
    num_players = temp
    if num_players < 2:
        print("Voce precisa de pelo menos 2 jogadores para jogar Zombie Dice")

names_players = []
name = " "

for i in range(0, num_players): #recebe os nomes dos jogadores e armazena em uma lista

    print("Insira o nome do jogador " + str(i+1) + " :")
    name = input()
    names_players.append(name)

green_dice = "CPCTPC"
yellow_dice = "TPCTPC" #define os tipos de dados e os coloca em uma lista
red_dice = "TPTCPT"
tube_dice = [green_dice, green_dice, green_dice, green_dice, green_dice, green_dice, yellow_dice, yellow_dice, yellow_dice, yellow_dice, red_dice, red_dice, red_dice, red_dice,]

print("Que comece o banquete de cerebros!") #anuncia o início do turno

current_player = 0
hand_dice = []
shots = 0
brains = 0 #inicializa variáveis para guardar a pontuação
steps = 0

while True:

	nome_jogador = names_players[current_player] #armazena o nome do jogador atual em uma variável
	print("Turno do jogador: " + nome_jogador) #e mostra o nome na tela
    
	for i in range (0, 3): #retira três dados do tubo

		random_number = randint(0,12) #gera um número aleatório que é utilizado como índice para retirar um dado do tubo
		pulled_dice = tube_dice[random_number]

		if pulled_dice == "CPCTPC": #checa a cor do dado sorteado

			color_dice = "VERDE"

		elif pulled_dice == "TPCTPC":

			color_dice = "AMARELO"

		else:

			color_dice = "VERMELHO"
       
		print("Voce sorteou um dado: ",color_dice) #mostra a cor do dado sorteado para o jogador
		hand_dice.append(pulled_dice) #armazena os dados sorteados em uma lista ("dados na mão")
	
	print("O resultado dos seus dados foi: ") #anuncia o resultado dos dados

	for pulled_dice in hand_dice: #rola cada um dos três dados sorteados e mostra o resultado, usando contadores para marcar a pontuação

		roll_dice = randint(0,5) #gera um número aleatório para ser usado como índice da string ("faces do dado")
		if pulled_dice[roll_dice] == "C":

			print("Cerebro – Voce comeu um cerebro, nham nham!")
			brains = brains + 1 #contador de cérebros +1

		elif pulled_dice[roll_dice] == "T":

			print("TIRO – Voce levou um tiro, ouch!")
			shots = shots + 1 #contador de tiros +1

		else:
			print("PASSOS – A vitima escapou...por enquanto.")
			steps = steps + 1 #contador de passos +1

	
	print("PONTUAÇAO ATUAL: ") #mostra a pontuação atual utilizando os três contadores
	print("CEREBROS – ", brains)
	print("TIROS – ", shots)
	print("PASSOS – ", steps)

	print("Voce deseja continuar jogando dados? Digite S para sim e N para nao: ")
    
	continue_turn = input() #recebe um input positivo ou negativo do jogador para continuar o turno

	if continue_turn == "N": #se o input for negativo, passa para o turno do próximo jogador e zera os contadores
		current_player = current_player + 1
		hand_dice = []
		shots = 0
		brains = 0
		steps = 0

		if current_player == len(names_players): #se todos os jogadores já tiverem jogado, encerra o jogo

			print("Finalizando o prototipo do jogo.")
			print("Obrigado por jogar!")
		
	else: #repete o game loop se o jogador quiser jogar mais uma rodada, zerando os dados sorteados

		print("Iniciando mais uma rodada do turno atual: ")
		hand_dice = []
	


