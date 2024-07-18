N,M=map(int,input().split())
tiles=[list(input().strip())for _ in range(N)]
visited=[[False]*(M) for _ in range(N)]
tile_count=0
for i in range(N):
    for j in range(M):
        if tiles[i][j]=='-':
            if visited[i][j]==True:
                continue
            tile_count+=1
            for k in range(j,M):
                if tiles[i][k]=='|':
                    break
                if tiles[i][k]=='-':
                    visited[i][k]=True
        if tiles[i][j]=='|':
            if visited[i][j]==True:
                continue
            tile_count+=1
            for k in range(i,N):
                if tiles[k][j]=='-':
                    break
                if tiles[k][j]=='|':
                    visited[k][j]=True
print(tile_count)