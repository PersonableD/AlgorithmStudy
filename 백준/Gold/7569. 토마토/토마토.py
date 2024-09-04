from collections import deque
import sys
input=sys.stdin.readline
M,N,H=map(int,input().split())
boxes=[list(map(int,input().split())) for _ in range(N*H)]
all_row=N*H
dx=[1,-1,0,0,N,-N]
dy=[0,0,1,-1,0,0]
ripen_tomatos=deque()
unripe = 0
for i in range(all_row):
    for j in range(M):
        if boxes[i][j] ==1:
            ripen_tomatos.append((i,j))
        if boxes[i][j] ==0:
            unripe+=1
if unripe ==0:
    print(0)
else:
    day=-1
    while ripen_tomatos:
        day+=1
        for _ in range(len(ripen_tomatos)):
            x,y = ripen_tomatos.popleft()
            for i in range(6):
                if (i == 0 and x%N == N-1) or (i == 1 and x%N == 0):
                    continue
                nx,ny = dx[i]+x,dy[i]+y
                if 0<=nx<all_row and 0<=ny<M and boxes[nx][ny]==0:
                        boxes[nx][ny]=1
                        ripen_tomatos.append((nx,ny))
                        unripe-=1
    print(day if unripe==0 else -1)