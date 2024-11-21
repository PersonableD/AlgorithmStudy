import sys
input = sys.stdin.readline

X = input().strip()  # 개행문자 제거

def answer():
    ans = 0
    global X
    
    if X[0] == "0":  # 0으로 시작하면
        if X[1] == "x":  # 16진수
            X = X.replace("0x","")
            num_list = list(X)
            num_list.reverse()
            for i in range(len(num_list)):
                if num_list[i] == "a":
                    num_list[i] = "10"
                elif num_list[i] == "b":
                    num_list[i] = "11"
                elif num_list[i] == "c":
                    num_list[i] = "12"
                elif num_list[i] == "d":
                    num_list[i] = "13"
                elif num_list[i] == "e":
                    num_list[i] = "14"
                elif num_list[i] == "f":
                    num_list[i] = "15"
                ans += (16**i) * int(num_list[i])
        else:  # 8진수
            X = X[1:]  # 앞의 0 제거
            num_list = list(X)
            num_list.reverse()
            for i in range(len(num_list)):
                ans += (8**i) * int(num_list[i])
    else:  # 10진수
        ans = int(X)
    
    return ans

print(answer())