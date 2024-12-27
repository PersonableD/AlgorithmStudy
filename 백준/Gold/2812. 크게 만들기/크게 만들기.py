import sys
N,K=map(int,input().split())
num_str=input()
stack=[]
to_remove=K
for num in num_str:
    while to_remove>0 and stack and stack[-1]<num:
        stack.pop()
        to_remove-=1
    stack.append(num)
stack=stack[:N-K]
print(*stack,sep="")