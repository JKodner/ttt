"""
4 - 9 - 2
3 - 5 - 7
8 - 1 - 6
"""

def pboard():
	cnt = 1
	for i in [4, 9, 2, 3, 5, 7, 8, 1, 6]:
		print ("[%s]" % board[i]),
		if cnt % 3 == 0:
			print "\n"
		cnt += 1

board = {}
for i in range(1, 10):
	board.update({i:" "})

inputs = {
	1:4, 2:9, 3:2,
	4:3, 5:5, 6:7,
	7:8, 8:1, 9:6
}

keys = ["X", "O"]
count = 1

user = []
computer = []

while count < 10:
	pboard()
	sign = keys[count % 2]
	place = int(raw_input("Turn %s-%s: " % (count, sign)))
	board[inputs[place]] = sign
	count += 1

pboard()