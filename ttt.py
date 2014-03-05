from random import choice
from itertools import combinations
from os import system

"""
4 - 9 - 2
3 - 5 - 7
8 - 1 - 6

Strategy: 
1. Winning Move
2. Block User Win,
3. Corners
4. Edges
5. Center
"""

def pboard():
	cnt = 1
	for i in [4, 9, 2, 3, 5, 7, 8, 1, 6]:
		print ("[%s]" % board[i]),
		if cnt % 3 == 0:
			print "\n"
		cnt += 1

def check(p_lst):
	token = False
	for i in combinations(p_lst, 3):
		if sum(i) == 15:
			token = True
	return token

board = {}
for i in range(1, 10):
	board.update({i:" "})

inputs = {
	1:4, 2:9, 3:2,
	4:3, 5:5, 6:7,
	7:8, 8:1, 9:6
}

system('clear')
print "You're X, and the Computer is O."
if choice(["user", "computer"]) == "user":
	keys = ["O", "X"]
	print "You go First.\n"
else:
	keys = ["X", "O"]
	print "The Computer Goes First\n"
raw_input("Press Anything to Continue: ")

count = 1
user = []
computer = []
gamewin = False

while count < 10:
	system('clear')
	
	pboard()
	sign = keys[count % 2]
	
	if sign == "X":
		turn = "User"
		lst = user
	else:
		turn = "Computer"
		lst = computer
	
	if turn == "User":	
		# place = int(raw_input("Turn: %s, %s-%s: " % (turn, count, sign)))
		# lst.append(inputs[place])
		# board[inputs[place]] = sign
		pass
		

	elif turn == "Computer":
		go = raw_input("Go? ")
		if go == "y":
			winmove = []
			token = False
			for i in combinations(range(1, 10), 2):
				diff = 15 - sum(i)
				if 1 <= diff <= 8:
					if diff not in i:
						if board[diff] == " ":
							if board[i[0]] == "O" and board[i[1]] == "O":
								winmove.append(diff)
								token = True
								break
			if token:
				place = winmove[0]
				lst.append(place)
				board[place] = sign
		else:
			place = int(go)
			lst.append(inputs[place])
			board[inputs[place]] = sign

	count += 1
	if check(lst):
		system('clear')
		print "TIC TAC TOE"
		winner = turn
		gamewin = True
		break

pboard()
if gamewin:
	print "The %s Won!" % winner
else:
	print "It's a Draw!"