# Template from https://www.youtube.com/watch?v=3llnfHGN9HM

import sys

def inp():  # Single Input
	return(int(sys.stdin.readline()))
	
def invr():  # Multi Input Integers
	return(map(int,sys.stdin.readline().split()))
	
def mapper():  # Multi Input Strings
	return(map(str,sys.stdin.readline().split()))
	
def fprint(x):  # Fast Print
	sys.stdout.write(str(x))

# Template Over	

yes = "Y"
no = "N"
	
for count in range(inp()):
	
	val = inp()
	flight = []
	flight.append(list(str(input())))
	flight.append(list(str(input())))
	__grid = [[val for i in range(val)] for j in range(val)]
	
	#print(__grid) # Super Private Variable
	for i in range(val):
		for j in range(val):
			
			if(i==j):
				__grid[i][j]=yes
				
			elif((i-j==1) or (i-j==-1) or (j-i==1) or (j-i==-1)):
				if(flight[1][i]==yes and flight[0][j]==yes):
					__grid[i][j]=yes
				else:
					__grid[i][j]=no
			
			elif(flight[1][i]==yes and flight[0][j]==yes):
				if(i<j):
					k = i+1
					x=0
					while(k<j):
						if(flight[1][k]==no or flight[0][k]==no):
							x=1
							break
						k+=1
					if(x==1):
						__grid[i][j]=no
					else:
						__grid[i][j]=yes
				else:
					k = j+1
					x=0
					while(k<i):
						if(flight[1][k]==no or flight[0][k]==no):
							x=1
							break
						k+=1
					if(x==1):
						__grid[i][j]=no
					else:
						__grid[i][j]=yes
			
			else:
				__grid[i][j]=no
	
	q = count+1
	print("Case #{}:".format(q))
	for i in range(val):
		for j in range(val):
			print(__grid[i][j],end="",sep='\n')
		print("")
	sys.stdout.flush()
