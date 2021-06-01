

def printBoard(board):
	print("     1   2   3 ")
	print("    ___________")
	for i in range(3):
		print(" ",end="")
		first =1
		for j in range(3):
			if(first):
				print(str(i+1)+" | ",end="")
				first=0
			print(board[i][j],end="")
			if(j!=2):
				print(" | ",end="")
		print(" |\n",end="")
		print("   |---+---+---|",end="")
		print("\n",end="")

def someoneWon(board,turn):
	second_brake=0
	if((board[0][0]==board[1][1]) & (board[1][1]==board[2][2]) & (board[0][0]==turn)): #diagonal
		return 1
	elif((board[0][2]==board[1][1]) & (board[1][1]==board[2][0]) & (board[1][1]==turn)): #diagonal
		return 1
	else:
		for i in range(3):
			if((board[i][0]==board[i][1]) & (board[i][1]==board[i][2]) & (board[i][0]==turn)):   #horizontal
				return 1
			elif((board[0][i]==board[1][i]) & (board[1][i]==board[2][i]) & (board[1][i]==turn)): #verticle
				return 1
		for i in range(3): # check if the board is full
			for j in range(3):
				if(second_brake):
					break
				if(board[i][j]==0):
					second_brake=1
					break
				elif(i==2&j==2):
					return -1
	return 0

def movementIsInvalid(board,move):
	if( move[0]<0 | move[0]>2):
		return 1
	elif(move[1]<0 | move[1]>2):
		return 1
	elif( board[( move[0] )][( move[1] )]!=0 ):
		return 1
	else:
		return 0


user_input=1
while(user_input==1):
	current_player = int(input("Which player is going to play first? : "))
	playboard = []
	playboard.append([0,0,0])
	playboard.append([0,0,0])
	playboard.append([0,0,0])
	while(1):
		printBoard(playboard)


		move=input("Player "+str(current_player)+" give a move: ");
		move=move.split(" ")
		move[0]= int(move[0])-1
		move[1] = int(move[1])-1
		invalid = movementIsInvalid(playboard,move);
		if(invalid==0):
			playboard[move[0]][move[1]] = current_player

		result = someoneWon(playboard,current_player) 
		if(result==1):
			print("GameOver! The player "+str(current_player)+" has won the Game!")
			printBoard(playboard)
			break
		elif(result==-1):
			print("GameOver! The game ended with Tie!")
			printBoard(playboard)
			break

		if(invalid==0):
			if(current_player==1):
				current_player=2
			else:
				current_player=1
		else:
			print("The movement was invalid. Please player "+str(current_player)+" play again")




	anwser = input("Do you want to play again? (Y/y or N/n): ");
	if(anwser=='Y' or anwser=='y'):
		user_input=1
	else:
		user_input=2




