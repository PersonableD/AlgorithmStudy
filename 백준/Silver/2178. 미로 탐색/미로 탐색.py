from collections import deque
import sys
input=sys.stdin.readline
N,M=map(int,input().strip().split())
maze=[input().strip() for _ in range(N)]
def BFS_Shortest(maze,N,M):
    queue=deque([(0,0)])
    distance=[[0]*(M) for _ in range(N)]
    distance[0][0]=1
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while queue:
        x,y=queue.popleft()
        if x==N-1 and y==M-1:
            return distance[x][y]
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<= nx <N and 0<= ny < M and maze[nx][ny]=="1" and distance[nx][ny]==0:
                queue.append((nx,ny))
                distance[nx][ny]=distance[x][y]+1
print(BFS_Shortest(maze,N,M))