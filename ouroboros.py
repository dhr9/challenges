M = 5

def getReverse(n):
	return int(str(n)[-1] + str(n)[:-1])

def checkIfTrue(n):
	n_ = getReverse(n)
	if n*M == n_:
		print("We have a winner")
		print(n)
		import sys
		sys.exit(0)
	return (n_/n)

def getL():
	s = ""
	for key in list(l.keys()):
		s += str(l[key]) + " "
	return(s)

def inc(n):
	global l
	k = str(n)
	if(n in l):
		l[n] += 1
	else:
		l[n] = 1

def nextBreak(n):
	return(10**(len(str(n)))+10)

reset = 0
l = {}
lastLength = 0

START = 10**4
END = 10**6


i = START
while (i < END):
	k = int(checkIfTrue(i))
	if(k==reset):
		# print(i)
		p = getL()
		length = int(len(p)/2)
		if(length > lastLength):
			print(str(length) + " => " + str(i))
		if(length < M):
			i = nextBreak(i)
		lastLength = length
		print(p)
		l = {}
		reset = M
	if(k == 1):
		reset = 0
	# print(k)
	inc(k)
	i+=1