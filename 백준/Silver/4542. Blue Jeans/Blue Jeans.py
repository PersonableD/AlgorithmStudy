n = int(input())
def find_common_substring(strings):
    first_string = strings[0]
    max_common = ""
    for length in range(3, len(first_string) + 1):
        for start in range(len(first_string) - length + 1):
            substring = first_string[start:start + length]
            if all(substring in s for s in strings[1:]):
                if len(substring) > len(max_common) or (len(substring) == len(max_common) and substring < max_common):
                    max_common = substring
    return max_common if max_common else "no significant commonalities"
for _ in range(n):
    m = int(input())
    strings = [input() for _ in range(m)]
    result = find_common_substring(strings)
    print(result)