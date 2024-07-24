import sys
input=sys.stdin.readline
N=int(input())
sequence=list(map(int,input().split()))
length=[1]*(len(sequence))
def LIS(s):
    if s==len(sequence):
        return
    for i in range(s):
        if sequence[i]<sequence[s]:
            length[s]=max(length[i]+1,length[s])
    LIS(s+1)
LIS(1)
print(max(length))