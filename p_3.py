class Node:
	def __init__(self, data, level ,fval):
		self.data = data
		self.level = level
		self.fval = fval
	
	def generate_child(self):
		x,y = self.find(self.data,'_')
		val_list = [[x,y-1], [x,y+1], [x-1,y], [x+1,y]]
		children = []
		for i in val_list:
			child = self.shuffle(self.data, x, y, i[0],i[1])
			if child is not None :
				child_node = Node(child, self.level+1, 0)
				children.append(child_node)
		return children
	
	def shuffle(self, puz, x1, y1, x2, y2):
		if x2 >= 0 and x2 < len(self.data) and y2>=0 and y2<len(self.data):
			temp_puz = []
			temp_puz = self.copy(puz)
			temp = temp_puz[x2][y2]
			temp_puz[x2][y2] = temp_puz[x1][y1]
			temp_puz[x1][y1] = temp
			return temp_puz
		else:
			return None
			
			
	def copy(self,root):
		temp = []
		for i in root:
			t = []
			for j in i:
				t.append(j)
			temp.append(t)
		return temp
		
	def find(self,puz,x):
		for i in range(0, len(self.data)):
			for j in range(0,len(self.data)):
				if puz[i][j] == x:
					return i,j
					
class Puzzle:
	def __init__(self,size):
		self.n = size
		self.open = []
		self.closed = []
	
	def accept(self):
		puz = []
		for i in range(0,self.n):
			temp = input().split(" ")
			puz.append(temp)
		return puz
	
	def f(self, start, goal):
		return self.h(start.data, goal) + start.level
	
	def h(self, start, goal):
		temp = 0 
		for i in range(0, self.n):
			for j in range(0, self.n):
				if start[i][j] != goal[i][j] and start[i][j] != '_':
					temp += 1
		return temp
	
	def process(self):
		print("Enter the start state Matrix : \n")
		start = self.accept()
		print("Enter the goal state Matrix : \n")
		goal = self.accept()
		start = Node(start,0,0)
		start.fval = self.f(start,goal)
		self.open.append(start)
		print("\n\n")
		while True:
			cur = self.open[0]
			print("")
			print(" || ")
			print(" || ")
			print(" \/ \n")
			
			for i in cur.data:
				for j in i :
					print(j, end=" ")
				print("")
				
			if self.h(cur.data,goal) == 0 :
				break
				
			for i in cur.generate_child():
				i.fval = self.f(i,goal)
				self.open.append(i)
				
			self.closed.append(cur)
			del self.open[0]
			self.open.sort(key = lambda x:x.fval,reverse=False)

puz = Puzzle(3)
puz.process()


























'''
Algorithm: 8-Puzzle Problem using A* Search Algorithm
Start the program.
Define a Node class to store the puzzle state, level, and evaluation value (fval).
Define a function to find the blank space (_) in the puzzle.
Generate child nodes by moving the blank space LEFT, RIGHT, UP, or DOWN.
Check whether each movement is within the grid boundaries.
Create a new puzzle state by swapping the blank space with the adjacent tile.
Define a Puzzle class and initialize the puzzle size, OPEN list, and CLOSED list.
Accept the initial state and goal state matrices from the user.
Calculate the heuristic value by counting the number of misplaced tiles, excluding the blank space.
Calculate the evaluation function using:

f(n) = g(n) + h(n)

g(n) = Current level or path cost.
h(n) = Number of misplaced tiles.
Insert the initial state into the OPEN list.
Repeat the following steps:
Select the node with the lowest fval from the OPEN list.
Display the current puzzle state.
Check whether the current state matches the goal state.
If yes, terminate the search.
Otherwise, generate all possible child states.
Calculate the fval of each child and add it to the OPEN list.
Move the current node to the CLOSED list.
Remove the current node from the OPEN list.
Sort the OPEN list according to the lowest fval.
Continue until the goal state is reached.
Stop the program.
'''
		
	
