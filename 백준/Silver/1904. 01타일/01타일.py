import sys
input=sys.stdin.readline
N=int(input())
def f(n):
    sums={0:0,1:1,2:2,3:3}
    for i in range(4,n+1):
        sums[i]=(sums[i-1]+sums[i-2])%15746
    return sums[n]
print(f(N))