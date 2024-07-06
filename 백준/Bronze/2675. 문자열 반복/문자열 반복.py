t=int(input())
for i in range(t):
    mult, string = map(str,input().split())
    mult = int(mult)
    result=[]
    for i in range(len(string)):
        multStr= string[i]*mult
        result.append(multStr)

    print("".join(result))