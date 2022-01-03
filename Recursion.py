'''
1. Anything which can be solved iteratively, usually can be done recursively
2. Recursion can help reduce repetition of code
3. If memory is expensive to the system, avoid making too many recursive calls
-iterative approaches tend to be more efficient as they dont make additional 
function calls that take up stack space. (con- readablity)
-recursion is useful when you dont know how many loops to go through
- tale call optimisation can solve recursion's memory issue
'''

#Factorial of a number
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

print(fact(3))

#Fibonacci of nth number
def fibo(n): #O(2^n), very inefficient
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(7))

#Fibonacci of nth, optimised by DP
def fib(n):
    cache={} #stores already calculated values

    if n in cache: #checks for existing results
        return cache[n]
    
    elif n<2: #base case
        cache[n]=n #adding unexisting computed results
        return cache[n]
    else:
        cache[n]=fib(n-1)+fib(n-2)
        return cache[n]

x=fib(7)
print(x)