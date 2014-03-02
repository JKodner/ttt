board = {}
for i in range(1, 10):
	board.update({i:" "})

def pboard():
	for i in range(1, 10):
		print ("[%s]" % board[i]),
		if i % 3 == 0:
			print "\n"