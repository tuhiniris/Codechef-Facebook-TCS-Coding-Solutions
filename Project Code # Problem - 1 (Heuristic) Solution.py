import sys

fastio = sys.stdin.readline

def inp():
    return(int(fastio()))
def invr():
    return(map(int,fastio().split()))

for i in range(inp()):
    n,q = invr()
    sandy = []
    me = []
    for i in range(n):
    	#sandy.append(sys.stdin.readline().strip())
    	sandy.append(str(input()))
    for i in range(q):
    	#me.append(sys.stdin.readline().strip())
    	me.append(str(input()))
    
    def testing(a=tuple((sandy)),b=tuple(me)):
        from difflib import get_close_matches as gestalt
        lines = 0
        ui=0
        while lines<=(q-1):
            lines = lines+1
            p = gestalt(b[ui],a,1,0.9)
            print(*p)
            ui = ui+1
    testing()