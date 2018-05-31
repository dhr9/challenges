M = 6

def getReverse(n):
	return int(str(n)[-1] + str(n)[:-1])

def checkIfTrue(n):
	n_ = getReverse(n)
	if n*M == n_:
		print("We have a winner")
		print(str(M) + " => " + str(n))
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

def try1():
	global l
	reset = 0
	l = {}
	lastLength = 0

	START = 10
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

142857

def getNextNum(num, i, start):
	# print(num, i, start)
	temp = num*M
	return (temp%(10**i))*10 + start

def try2():
	num_arr = list(range(1,10))

	i = 1
	while(True):
		# print(num_arr)
		for j in range(len(num_arr)):
			num_arr[j] = getNextNum(num_arr[j], i, j+1)
			checkIfTrue(num_arr[j])
		i+=1

try2()


'''
1 => 11
2 => 105263157894736842
3 => 1034482758620689655172413793
4 => 102564
5 => 142857
6 => 1016949152542372881355932203389830508474576271186440677966
7 => 1014492753623188405797
8 => 1012658227848
9 => 10112359550561797752808988764044943820224719
'''