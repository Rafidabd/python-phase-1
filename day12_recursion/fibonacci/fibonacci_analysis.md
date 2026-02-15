# Fibonacci Algorithm Analysis

# What is Fibonacci (plain explanation)

Fibonacci is a number sequence where each number is the sum of the previous two.
I first saw this in math, but coding it made the idea way clearer than theory.

``` Definition: ```

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n >= 2

# Recursive Fibonacci (Naive)

Code:

def fib_recursive(n):
if n <= 1:
return n
return fib_recursive(n - 1) + fib_recursive(n - 2)

# My thoughts:

This version directly follows the math formula.
It looks clean and elegant, but becomes insanely slow for large n.
This was my first real lesson that elegant code is not always efficient code.

Time Complexity: O(2^n)
Space Complexity: O(n)

# Iterative Fibonacci (Loop)

Code:

def fib_iterative(n):
a, b = 0, 1
for _ in range(n):
a, b = b, a + b
return a

 # My thoughts:

This one feels more mechanical but very efficient.
Only two variables change, no recursion, no stack growth.
If I had to use Fibonacci in a real project, I would use this version.

Time Complexity: O(n)
Space Complexity: O(1) 

# Fibonacci with Memoization (Caching)

Code:

def fib_memo(n, memo={}):
if n in memo:
return memo[n]
if n <= 1:
return n
memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
return memo[n]

 # My thoughts:

This felt like unlocking a cheat code.
The function remembers previous results so it doesn’t recompute them.
This was my first real exposure to dynamic programming style thinking.

Time Complexity: O(n)
Space Complexity: O(n)

# Method Comparison :

Recursive: O(2^n) time, O(n) space, elegant but very slow
Iterative: O(n) time, O(1) space, best practical solution
Memoization: O(n) time, O(n) space, good for learning DP

# Personal Observations

Recursive Fibonacci looks cool but is mostly educational.
Iterative version is boring but practical.
Memoization made recursion powerful instead of useless.
Understanding the call stack made recursion less scary.
Fibonacci itself is not that useful, but the thinking style is.

# Why I Studied This

I used Fibonacci to understand recursion execution flow, time complexity, caching, and why iterative solutions dominate in real systems.
This topic improved my problem-solving mindset more than the sequence itself.

# Final Thoughts

At first recursion felt like black magic.
After tracing Fibonacci manually, it became mechanical and logical.
Fibonacci is overused in tutorials, but I now understand why universities love it.
It forces you to think about execution flow, efficiency, and memory.

End of file. 