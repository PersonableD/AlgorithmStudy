import sys
input=sys.stdin.readline
N,M=map(int,input().split())
visited=[False]*(N+1)
def func(num_list):
    if len(num_list)==M:
        print(*num_list)
        return
    for i in range(1,N+1):
        if not visited[i]:
            visited[i]=True
            num_list.append(i)
            func(num_list)
            visited[i]=False
            num_list.pop()
func([])