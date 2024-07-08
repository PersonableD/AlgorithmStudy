import sys
sys.setrecursionlimit(10**5)
n=int(input())

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n* factorial(n-1)

print(factorial(n))