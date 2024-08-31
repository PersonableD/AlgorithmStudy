from collections import deque
import sys
input=sys.stdin.readline
R,C=map(int,input().split())
forest=[list(input().strip()) for _ in range(R)]
hedgehog=deque()
water=deque()
for i in range(R):
    for j in range(C):
        if forest[i][j]=="S":
            hedgehog.append((i,j,0))
        elif forest[i][j] =="*":
            water.append((i,j))
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs():
    while hedgehog:
        for _ in range(len(water)):
            x,y=water.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0<=nx<R and 0<=ny<C and (forest[nx][ny]=="." or forest[nx][ny]=="S"):
                    forest[nx][ny]="*"
                    water.append((nx,ny))
        for _ in range(len(hedgehog)):
            x,y,time =hedgehog.popleft()
            if forest[x][y]=="D":
                return time
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0<=nx<R and 0<=ny<C:
                    if forest[nx][ny]=="." or forest[nx][ny]=="D":
                        if forest[nx][ny]!="D":
                            forest[nx][ny]="S"
                        hedgehog.append((nx,ny,time+1))
    return "KAKTUS"
print(bfs())