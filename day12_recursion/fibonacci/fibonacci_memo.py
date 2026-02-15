#Memoization = store results so we don’t recompute
# now we will turn recursion into a pro algorithm
memo={}
def fib(n):
    if n in memo:
        return memo[n] #returning stored result
    if n<=1:
        return n #this is the base case
    memo[n]=fib(n-1)+fib(n-2)  #where the computation happens
    return memo[n]  #returning the computed result 
print(fib(5)) 
"""
fib(5)
 → fib(4)
   → fib(3)
     → fib(2)
       → fib(1) return 1
       → fib(0) return 0
     → compute 1 + 0 = 1
   → fib(2) FOUND in memo, skip recursion
   → compute 1 + 1 = 2
 → fib(3) FOUND in memo
 → compute 3 + 2 = 5


 
 """