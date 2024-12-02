import itertools
N=int(input())
arr=list(map(int,input().split()))
i=0
result=0
for perm in itertools.permutations(arr):
    temp=0
    perm_list = list(perm)
    for i in range(len(perm_list)-1):
        temp += abs(perm_list[i]-perm_list[i+1])
    temp = max(temp,result)
    result=temp
print(result)