# Attribution : https://www.geeksforgeeks.org/remove-even-frequency-characters-from-the-string/
# Template from https://www.youtube.com/watch?v=3llnfHGN9HM

import sys

def inp():  # Single Input
	return(int(sys.stdin.readline()))
def sinp():  # Single Input
	return(str(sys.stdin.readline()))    
	
def invr():  # Multi Input Integers
	return(map(int,sys.stdin.readline().split()))
	
def mapper():  # Multi Input Strings
	return(map(str,sys.stdin.readline().split()))
	
def fprint(x):  # Fast Print
	sys.stdout.write(str(x))

def solve(s): 

	yp = dict() 
	for i in range(len(s)): 
		if s[i] in yp: 
			yp[s[i]] = yp[s[i]]+1
		else: 
			yp[s[i]] = 1

	new_string = "" 

	for i in range(len(s)):
		if yp[s[i]]%2 == 0: 
			continue

		new_string = new_string+s[i]
	return(new_string) 
	
for i in range(inp()):
	if __name__=='__main__': 
		qu = inp()
		s = str(input())
		mx = []
		qiy = (solve(s))
		if qiy=="":
		    print("YES")
		else:
		    print("NO")