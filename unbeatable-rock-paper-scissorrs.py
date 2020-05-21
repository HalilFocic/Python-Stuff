from random import randint
play = True
print("-=-=-=-UNBEATABLE ROCK PAPER SCISSORS GAME ")
print("-=-=-=-BY HALILCODES---------")
print("-=-=-=-FOLLOW FOR MORE @halilcodes")
print("-=-=-=-LINK TO CODE ON MY PAGE")
print("-=-=-=-ENJOY YOUR DAY!\n")
while play:
	player = input("PLAYER, MAKE YOUR MOVE: ").lower()
	rand_num = randint(0,2)
	if player == "end":
		play=False
		break
	if player =="scissors":
		computer = "rock"
	elif player =="rock":
		computer = "paper"
	else:
		computer ="scissors"
	# Now we check if player entered a valid move
	if player != "rock" and player !="paper" and player!="scissors":
		print("You did not enter a valid move,COMPUTER WINS! :)\n")
	else:
		print(f"You played {player}, computer play {computer}. COMPUTER WINS!")


	
