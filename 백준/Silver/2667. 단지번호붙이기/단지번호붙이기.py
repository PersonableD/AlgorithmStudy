from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
apt =[list(input().strip())for _ in range(N)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
queue=deque()
visited=[[False]*N for _ in range(N+1)]
house=[]
for i in range(N):
    for j in range(N):
        cnt=0
        if visited[i][j]==False and apt[i][j]=="1":
            queue.append((i,j))
            while queue:
                x,y=queue.popleft()
                visited[x][y]=True
                for k in range(4):
                    nx,ny= dx[k]+x,dy[k]+y
                    if 0<=nx<N and 0<= ny<N and apt[nx][ny]=="1" and visited[nx][ny]==False:
                        queue.append((nx,ny))
                        visited[nx][ny]=True
                cnt+=1
            house.append(cnt)
house.sort()
print(len(house))
for i in house:
    print(i)