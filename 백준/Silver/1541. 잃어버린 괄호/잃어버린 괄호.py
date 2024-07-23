operation=input().split("-")
for i in range(len(operation)):
    if "+" in operation[i]:
        parts=list(map(int,operation[i].split("+")))
        operation[i]=sum(parts)
    else:
        operation[i] = int(operation[i])
result=operation[0]
for i in range(1,len(operation)):
    result-=operation[i]
print(result)