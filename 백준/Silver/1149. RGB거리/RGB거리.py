import sys
input = sys.stdin.readline


N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

# 초기값 설정
prev = cost[0][:]  # 첫 번째 집의 비용 초기화

# DP 계산
for i in range(1, N):
    curr = [0] * 3  # 현재 집의 비용을 저장
    curr[0] = cost[i][0] + min(prev[1], prev[2])  # 빨강으로 칠할 때 최소 비용
    curr[1] = cost[i][1] + min(prev[0], prev[2])  # 초록으로 칠할 때 최소 비용
    curr[2] = cost[i][2] + min(prev[0], prev[1])  # 파랑으로 칠할 때 최소 비용
    prev = curr  # 현재 값을 이전 값으로 업데이트

# 최종 최소 비용
result = min(prev)
print(result)