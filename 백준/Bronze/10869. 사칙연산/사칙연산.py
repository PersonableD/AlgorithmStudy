a, b=input().split()
a=int(a)
b=int(b)
if (1<=a) and (b<=10000):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)
else:
    print("a,b가 범위를 벗어났습니다")

