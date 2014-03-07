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
3. Corners - 4, 2, 6, 8
4. Edges - 9, 7, 1, 3
5. Center - 5
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

def findmove(sig):
	winmove = []
	token = False
	for i in combinations(range(1, 10), 2):
		diff = 15 - sum(i)
		if 1 <= diff <= 9:
			if diff not in i:
				if board[diff] == " ":
					if board[i[0]] == sig and board[i[1]] == sig:
						winmove.append(diff)
						token = True
						break
	if token:
		obj = {"place": winmove[0], "token": token}
	if not token:
		obj = {"token": token}
	return obj

def findplace(place):
	move = []
	token = False
	if place == "corner":
		selected = [4, 2, 6, 8]
	elif place == "edge":
		selected = [9, 7, 1, 3]
	for i in selected:
		if board[i] == " ":
			token = True
			move.append(i)
			break
	if token:
		obj = {"place": move[0], "token": token}
	if not token:
		obj = {"token": token}
	return obj


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
unneed = []
gamewin = False

while True:
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
			place = int(raw_input("Turn: %s, %s-%s: " % (turn, count, sign)))
			lst.append(inputs[place])
			board[inputs[place]] = sign
		

	elif turn == "Computer":
		called_1 = findmove("O")
		called_2 = findmove("X")
		if called_1["token"] or called_2["token"]:
			if called_1["token"]:
				chosen = called_1
			elif called_2["token"]:
				chosen = called_2
			place = chosen["place"]
			lst.append(place)
			board[place] = sign
		else:
			move_1 = findplace("corner")
			move_2 = findplace("edge")
			if move_1["token"] or move_2["token"]:
				if move_1["token"]:
					chosen = move_1
				elif move_2["token"]:
					chosen = move_2
				place = chosen["place"]
				
			elif board[5] == " ":
				place = 5
				
			lst.append(place)
			board[place] = sign
		system('clear')
		pboard()
		raw_input("Press Anything to Continue")

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