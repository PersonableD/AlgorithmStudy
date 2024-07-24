import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    aplicants=[list(map(int,input().split())) for _ in range(N)]
    aplicants.sort(key=lambda x: x[0])
    test=[]
    a,b=aplicants[0]
    for i in range(N):
        c,d=aplicants[i]
        if b>d:
            b=d
            test.append(aplicants[i])
    print(len(test)+1)