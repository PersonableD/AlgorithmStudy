from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
area = [list(map(int,input().split())) for _ in range(N)]
arr_min = min(min(row) for row in area)
arr_max = max(max(row) for row in area)
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def search_safezone(num):
    count=0
    visited=[[False]*(N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if num<area[i][j] and visited[i][j]==False:
                queue=deque([(i,j)])
                visited[i][j]=True
                while queue:
                    x,y=queue.popleft()
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if 0<= nx <N and 0<= ny < N and area[nx][ny]>num and visited[nx][ny]==False:
                            queue.append((nx,ny))
                            visited[nx][ny]=True
                count+=1
    return count
safezone_count=[]
safezone_count.append(search_safezone(0))
for i in range(arr_min,arr_max+1):
    num=search_safezone(i)
    safezone_count.append(num)
print(max(safezone_count))