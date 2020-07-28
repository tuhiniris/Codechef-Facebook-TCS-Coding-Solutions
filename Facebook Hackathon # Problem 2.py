# CASE 9, 10, 11, 12

import copy,itertools

# Functions for Greedy Checking

 



def reduction(list2d):
	merged = list(itertools.chain(*list2d))
	return merged	

def find(x):
	import collections	 
	return(collections.Counter(x).most_common(1)[0][0])

def breaker(x,breaking=3):
	q = [x[i:i + breaking] for i in range(0, len(x), breaking)]
	return q

def mernred(list2d):
	import itertools
	merged = list(itertools.chain(*list2d))
	return breaker(merged)

def checkmax(list):
	q = (find(list))
	return q

def checkifsame(lst): 
	return len(set(lst)) == 1
			
# Uber Case

def mf(p):
	for counts in range(len(p)):
		if checkifsame(p[counts])==True:
			if len(p)==1:
				#print("Case Begin#{}: N".format(counts+1))
				break
			else:			
				continue
		else:			
			p[counts]=checkmax(p[counts])
			break
	q = mernred(p)
	return(q)	

# Backtracking Case

from itertools import chain 
from collections import Counter 

def countList(lst, x): 	
	return Counter(chain.from_iterable(set(i) for i in lst))[x] 

longint = 99999
def countOccurrences(arr, n, x): 
	res = 0
	for i in range(n): 
		if x == arr[i]: 
			res += 1
	return res 



for counx in range(int(input())):
	number = int(input())	
	QX = 'A'
	QY = 'B'
	#


	x = list(str(input()))
	if checkifsame(x)==True and len(x)>3:
		print("Case #{}: N".format(counx+1))
		#print("Same")
		continue	
	if countOccurrences(x,len(x),'B')-countOccurrences(x,len(x),'A')==1:
		print("Case #{}: N".format(counx+1))
		continue
		
			
	'''
	if len(x)==3:
		if x == ['B','A','B'] or x == ['A','B','B'] or x == ['B','B','A'] or x == ['A','A','B'] or x == ['B','A','A'] or x == ['A','B','A']:
			print("Case #{}: Y".format(0+1))
			#break
			
		elif x == ['B','B','B'] or x == ['A','A','A']:
			print("Case #{}: N".format(0+1))
			#break		
	'''
	# Greedy Case

	cx = copy.deepcopy(x)   # List to Operate

	#print(cx)
	mcx = mernred(cx)
	#print(mcx)
	count = number
	i = 0

	#for i in range(count):
	while i<count:
		#print(i)
		if (i>=1 and mcx[-1]==['A'] and len(mcx)>1) or (i>=1 and mcx[-1]==['B'] and len(mcx)>1):
			if ((countList(mcx,QX)-1)==countList(mcx,QY)):
				print("Case #{}: Y".format(counx+1))
				break
			#	
			elif ((countList(mcx,QY)-1)==countList(mcx,QX)):
				print("Case #{}: Y".format(counx+1))
				break
			
			elif len(mcx)>1 and len(mcx)!=3:
				if mcx[-1]==['A']:
					print("Case #{}: N".format(counx+1))
					break
				else:
					if number>longint-1 and mcx[-1]==['B'] and checkmax(cx)=='B':
						print("Case #{}: Y".format(counx+1))
						break
					if number>longint-1 and mcx[-1]==['B'] and checkmax(cx)=='A':
						print("Case #{}: N".format(counx+1))
						break						
							
					print("Case #{}: Y".format(counx+1))
					break	
			#	 	
			else:
				print("Case #{}: N".format(counx+1))
				break
			#print(mcx)
			#print("Not Greedy")
			break
		
		
		
			
		if (i>=0 and mcx==[['A']]) or (i>=0 and mcx==[['B']]):
			print("Case #{}: Y".format(counx+1))
			break
		if len(mcx)==1 and checkifsame(mcx[i])==1:
			print("Case #{}: N".format(counx+1))
			break			
		if len(mcx[i])>1 and checkifsame(mcx[i])==1:		
			i=i+1
			continue	
		else:
			#print(mcx[i])
			y = checkmax(mcx[i])		
			mcx[i]=y
			mcx = mernred(mcx)	
			#print(mcx)
			if len(mcx)==1 and checkifsame(mcx[0])==False:
				print("Case #{}: Y".format(counx+1))
				break
			if len(mcx)==1 and mcx == [['A']]:
				print("Case #{}: Y".format(counx+1))
				break
			if len(mcx)==1 and mcx == [['B']]:
				print("Case #{}: Y".format(counx+1))
				break		
