import sys
input= sys.stdin.readline
N=int(input())
arr=list(map(int,input().split()))
i=0
visited = [False]*len(arr)
pickednum=[]
result=0
def permutation(cnt,depth):
    global result
    if cnt ==depth:
        temp=0
        for i in range(len(pickednum)-1):
            temp += abs(pickednum[i]-pickednum[i+1])
        temp = max(temp,result)
        result =temp
        return
    for index in range(len(arr)):
        if visited[index]==False:
            visited[index]=True
            pickednum.append(arr[index])
            permutation(cnt+1,depth)
            pickednum.pop()
            visited[index]=False
permutation(0,len(arr))
print(result)