import sys
sys.setrecursionlimit(10**4)
input=sys.stdin.readline
N=int(input())
sums={}
def f(n):
    if n in sums:
        return sums[n]
    if n==0:
        return 0
    if n==1:
        return 1
    sums[n]= f(n-1)+f(n-2)
    return sums[n]
print(f(N))