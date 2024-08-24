import sys
input = sys.stdin.readline
N,K= map(int,input().split())
number = list(input())
stack=[]
remove_count=0
for i in range(N):
    while remove_count<K and stack and stack[-1]<number[i]:
        stack.pop()
        remove_count+=1
    stack.append(number[i])
while remove_count<K:
    stack.pop()
    remove_count+=1
result = "".join(stack)
print(result)