## Naive recursive Fibonacci
# Time Complexity: O(2^n)
def fib (n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

n=int(input("please enter your number:"))
print(fib(n))
