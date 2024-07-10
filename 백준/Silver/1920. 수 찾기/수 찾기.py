N = int(input())
yourNums = list(map(int, input().split()))
yourNums_set = set(yourNums)  # 리스트를 해시셋으로 변환

M = int(input())
myNums = list(map(int, input().split()))

results = []

# 해시셋을 사용한 검색
for num in myNums:
    if num in yourNums_set:
        results.append(1)
    else:
        results.append(0)

# 결과 출력
for result in results:
    print(result)
