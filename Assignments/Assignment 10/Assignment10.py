def rowCheck(game):
	for x in range(3):
		if game[x][0] == 1 & game[x][1] == 1 & game[x][2] == 1:
			return True
		elif game[x][0] == 2 & game[x][1] == 2 & game[x][2] == 2:
			return True

	return False

def colCheck(game):
	for x in range(3):
		if game[0][x] == 1 & game[1][x] == 1 & game[2][x] == 1:
			return True
		elif game[0][x] == 2 & game[1][x] == 2 & game[2][x] == 2:
			return True

	return False	

def diaCheck(game):
	if game[0][0] == 1 & game[1][1] == 1 & game[2][2] == 1:
		return True
	elif game[2][0] == 1 & game[1][1] == 1 & game[0][2] == 1:
		return True
	elif game[0][0] == 2 & game[1][1] == 2 & game[2][2] == 2:
		return True
	elif game[2][0] == 2 & game[1][1] == 2 & game[0][2] == 2:
		return True

	return False

def check(game, row, col, player):
	if game[row][col] == 0:
		if player == 2:
			game[row][col] = 1
		elif player == 1:
			game[row][col] = 2
	else:
		newRow = int(input("Enter another row: "))
		newCol = int(input("Enter another column: "))
		return check(game, newRow, newCol, player)

	print(game[0])
	print(game[1])
	print(game[2])

	if rowCheck(game) | colCheck(game) | diaCheck(game):
		return True
	else:
		return False

game = [[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]]
won = False;
player = 1

print(game[0])
print(game[1])
print(game[2])

while won == False:
	if player == 1:
		print("It's your turn Player 1 (X)")
		player = 2
	elif player == 2:
		print("It's you turn Player 2 (O)")
		player = 1

	row = int(input("Enter row: "))
	col = int(input("Enter column: "))

	if (check(game, row, col, player)):
		if player == 2:
			print("Player 1 (X) wins")
		elif player == 1:
			print("Player 2 (O) wins")

		won = True
