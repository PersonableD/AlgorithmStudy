import sys
from itertools import combinations

input = sys.stdin.readline

def count_teachable_words(learned_chars, words):
    count = 0
    for word in words:
        if word.issubset(learned_chars):
            count += 1
    return count

N, K = map(int, input().split())
words = [set(input().rstrip()) for _ in range(N)]

if K < 5:
    print(0)
    sys.exit()
elif K >= 26:
    print(N)
    sys.exit()

# 필수 문자
essential_chars = set('antic')

# 각 단어에서 필수 문자를 제외한 나머지 문자들
remaining_chars = set()
for word in words:
    remaining_chars.update(word - essential_chars)

# 배울 수 있는 추가 문자 수
additional_chars_count = K - 5

max_teachable = 0

# 추가로 배울 수 있는 문자 조합을 모두 시도
for chars in combinations(remaining_chars, min(additional_chars_count, len(remaining_chars))):
    learned_chars = essential_chars.union(chars)
    teachable = count_teachable_words(learned_chars, words)
    max_teachable = max(max_teachable, teachable)

print(max_teachable)