"""
Three Laws of recursion:
1. Base Case

-Stopping condition (like loop break)

2. Recursive Case

-Function calls itself

3. Progress Rule

-Each call must move closer to base case

****Basic format:
def func(problem):
    if base_case:
        return solution
    return func(smaller_problem)

$$$$Cheat sheet:
    Recursion = function calling itself
    Base case = stop
    Recursive case = smaller problem
    Call stack = memory frames
    Linear recursion = n-1
    Binary recursion = n-1 and n-2
    Divide & conquer = split problem
    Backtracking = try & undo



"""
import sys
sys.getrecursionlimit()  #Basically near 1000
sys.setrecursionlimit(2000) #we can set it too






