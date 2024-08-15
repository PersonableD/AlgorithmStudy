import sys
import heapq
input=sys.stdin.readline
N=int(input())
lines =[]
for _ in range(N):
    h,o = map(int,input().split())
    lines.append((min(h,o),max(h,o)))
D = int(input())
lines.sort(key=lambda x: x[1])
heap=[]
count=0
max_count=0
for end in lines:
    if end[1]-end[0]>D:
        continue
    while heap and heap[0] < end[1]-D:
        heapq.heappop(heap)
        count-=1
    heapq.heappush(heap,end[0])
    count+=1
    max_count = max(max_count,count)
print(max_count)