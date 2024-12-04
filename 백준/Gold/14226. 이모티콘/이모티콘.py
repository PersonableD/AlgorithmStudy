from collections import deque
import sys
input=sys.stdin.readline
S=int(input())
def bfs(s):
    queue=deque([(1,0,0)])
    visited=[[False]*(s+1) for _ in range(s+1)]
    visited[1][0]=True
    while queue:
        screen,clipboard,time=queue.popleft()
        if screen ==s:
            return time
        if not visited[screen][screen]:
            visited[screen][screen]=True
            queue.append((screen,screen,time+1))
        if clipboard > 0 and screen + clipboard <= s and not visited[screen+clipboard][clipboard]:
            visited[screen+clipboard][clipboard]=True
            queue.append((screen+clipboard,clipboard,time+1))
        if screen-1>0 and not visited[screen-1][clipboard]:
            visited[screen-1][clipboard]=True
            queue.append((screen-1,clipboard,time+1))
print(bfs(S))