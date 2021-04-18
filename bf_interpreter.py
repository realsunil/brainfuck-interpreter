import sys

cells = [0]
ptr_loc = 0

if(len(sys.argv) < 2):
	print("Give file name as command line argument")
	exit(0)

file_handle = open(sys.argv[1], "r")

code = file_handle.read()
i=0
a=[]
while i<len(code):

	if code[i] == '<':
		ptr_loc -= 1
		if(ptr_loc < 0):
			print("RANGE ERROR")
			exit(1)

	elif code[i] == '>':
		ptr_loc += 1
		# print(len(cells))
		# print(ptr_loc)
		if(len(cells) < ptr_loc+1):
			cells.extend([0])
		if(ptr_loc > 30000):
			print("RANGE ERROR")
			exit(1)

	elif code[i] == '.':
		try:
			print(chr(cells[ptr_loc]), end="")
		except ValueError:
			print("Not in ASCII range")

	elif code[i] == ',':
		try:
			if not len(a)>0:
				a=list(input())
			x=a.pop(0)
			if x=='0':
				break;
			else:
				cells[ptr_loc]=ord(x)
			
		except TypeError:
			print("TypeError")

	elif code[i] == '+':
		cells[ptr_loc] += 1

	elif code[i] == '-':
		cells[ptr_loc] -= 1

	elif code[i] == '[':
		if cells[ptr_loc] == 0:
			open_braces = 1
			while open_braces > 0:
				i += 1
				if code[i] == '[':
					open_braces += 1
				elif code[i] == ']':
					open_braces -= 1

	elif code[i] == ']':
		open_braces = 1
		while open_braces > 0:
			i -= 1
			if code[i] == '[':
				open_braces -= 1
			elif code[i] == ']':
				open_braces += 1
		# i still gets incremented in your main while loop
		i -= 1
	i += 1
