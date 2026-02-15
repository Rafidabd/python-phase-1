"""
Concept	             Recursion     	     Iteration
Stop rule	          Base case	         Loop condition
Control flow	Function calls itself	Loop counter
Risk	          Stack overflow	      Minimal



"""

def iter_fib(n):
    a=0
    b=1
    for i in range (n):
        a,b=b,a+b
        
    return a

print(iter_fib(5))