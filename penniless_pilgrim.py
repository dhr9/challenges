import numpy as np

class Grid:

	def __init__(self):
		self.grid = np.array([[None,None,None,None,None],[None,None,None,None,None],[None,None,None,None,None],[None,None,None,None,None],[None,None,None,None,None]])
		self.hor = np.ones(5*4).reshape(5,4)
		self.ver = np.ones(4*5).reshape(4,5)

	def printGrid(self):
		spacer = 5
		# print(self.hor)
		# print(self.ver)
		for r in self.grid:
			for e in r:
				print(str(e)+" "*(spacer-len(str(e))) +"\t",end="")
			print()

	def check(self,dr,dc):
		if(self.row + dr > 4):
			return False
		if(self.row + dr < 0):
			return False
		if(self.col + dc > 4):
			return False
		if(self.col + dc < 0):
			return False

		# print(dr,dc)
		if(dr == 0):
			K = 0
			if(dc == -1):
				K = -1
			return self.hor[self.row][self.col + K] != 0
		if(dc == 0):
			K = 0
			if(dr == -1):
				K = -1
			# print(self.row + K,self.col)
			return self.ver[self.row + K][self.col] != 0

		return True

	def ended_or_true(self):
		if self.row == 4 and self.col == 4 :
			# if int(self.grid[self.row][self.col]) <= 0:
			# 	self.printGrid()
			# 	print("------------------------------------")
				# import sys
				# sys.exit(0)
			return None
		return True

	def left(self):
		if not self.check(0,-1):
			return False
		self.hor[self.row][self.col-1] = 0
		v = self.grid[self.row][self.col]
		self.col -= 1
		self.grid[self.row][self.col] = v - 2
		return self.ended_or_true()

	def right(self):
		if not self.check(0,1):
			return False
		self.hor[self.row][self.col] = 0
		v = self.grid[self.row][self.col]
		self.col += 1
		self.grid[self.row][self.col] = v + 2
		return self.ended_or_true()

	def down(self):
		if not self.check(1,0):
			return False
		self.ver[self.row][self.col] = 0
		v = self.grid[self.row][self.col]
		self.row += 1
		self.grid[self.row][self.col] = v * 2
		return self.ended_or_true()

	def up(self):
		if not self.check(-1,0):
			return False
		self.ver[self.row-1][self.col] = 0
		v = self.grid[self.row][self.col]
		self.row -= 1
		self.grid[self.row][self.col] = v / 2
		return self.ended_or_true()

	def init(self):
		self.row = 0
		self.col = 0
		self.grid[self.row][self.col] = 0 
		self.right()
		self.right()
		return self

	def copy(self):
		f = Grid()
		f.grid = np.copy(self.grid)
		f.hor = np.copy(self.hor)
		f.ver = np.copy(self.ver)
		f.row = self.row
		f.col = self.col
		return f

	def get_options(self):
		d = []
		if(self.check(0,1)):
			d.append("right")
		if(self.check(0,-1)):
			d.append("left")
		if(self.check(-1,0)):
			d.append("up")
		if(self.check(1,0)):
			d.append("down")

		return d

	def exc(self, name):
		d = {
			"right":self.right,
			"left":self.left,
			"up":self.up,
			"down":self.down
		}
		return d[name]()

def iterate(g,c=0):
	global min_val, max_c, count
	options = g.get_options()
	# print(options)
	if len(options) == 0:
		# g.printGrid()
		max_c = max(max_c,c)
		count += 1
		return
	for fn_name in options:
		k = g.copy()
		if k is None:
			print()
			continue
		ret_val = k.exc(fn_name)
		# k.printGrid()
		# print(fn_name," ==> ",ret_val)
		if ret_val is None:
			# STOP NEW ITERATIONS
			min_val = min(min_val, k.grid[4][4])
			if k.grid[4][4] <= 0:
				k.printGrid()
				print("------------------------------------",c)
			max_c = max(max_c,c)
			count += 1		
			continue
		iterate(k,c+1)

max_c = 0
count = 0
min_val = 100000
g = Grid().init()
# print("down\t",g.down())
# print("right\t",g.right())
# print("up\t\t",g.up())
# # print("left\t",g.left())
# # print("left\t",g.left())
# print("down\t",g.down())
# print("right\t",g.right())
# print("left\t",g.left())
# print("down\t",g.down())
# print("right\t",g.right())
# print("left\t",g.left())

# print(g.hor)
# print(g.ver)
# g.printGrid()

# print("====================================")
iterate(g)
print(min_val)
print(max_c)
print(count)
#  _ _ _ _ 
# |_|_|_|_|
# |_|_|_|_|
# |_|_|_|_|
# |_|_|_|_|

