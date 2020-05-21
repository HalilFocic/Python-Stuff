from random import randint
play = True
print("Rock, Paper & Scissors game ! ")
print("-------BY HALILCODES---------")
print("FOLLOW FOR MORE PROJECTS,MEMES AND QUIZES!")
print("ENJOY YOUR DAY!\n")
while play:
	player = input("PLAYER, MAKE YOUR MOVE: ").lower()
	rand_num = randint(0,2)
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"

	print(f"Computer plays {computer}" )

	if player == computer:
		print("It's a tie!")
	elif player == "rock":
		if computer == "scissors":
			print("Player wins!")
		else:
			print("Computer wins!")
	elif player == "paper":
		if computer == "rock":
			print("Player wins!")
		else:
			print("Computer wins!")
	elif player == "scissors":
		if computer == "paper":
			print("Player wins!")
		else:
			print("Computer wins!")	
	else:
		print("Please enter a valid move!")

	smt = input("Do you want to play another game(yes/no):").lower()
	if smt =="no":
		play=False


print("Thank you for playing,leave a like!")