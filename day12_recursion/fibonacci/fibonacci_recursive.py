## Naive recursive Fibonacci
# Time Complexity: O(2^n)
def fib (n):
    if n==0:
        return 0
    if n==1:      
        return 1
    return fib(n-1)+fib(n-2)   #fib(4),here fib(2) is calculated twice and fib(1) three times..now if that was fib(50),that would be horrible,time complexity.

n=int(input("please enter your number:"))
print(fib(n))
