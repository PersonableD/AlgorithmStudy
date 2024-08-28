from itertools import permutations
N=int(input())
nums=list(map(int,input().split()))
oper_num=list(map(int,input().split()))
operators = []
operator_types = ['+', '-', '*', '/']
for op, count in zip(operator_types, oper_num):
    operators.extend([op] * count)
all_oper_permutations = set(permutations(operators,N-1))
def caculate(num1,num2,op):
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='*':
        return num1*num2
    else:
        if num1<0:
            return -((-num1)//num2)
        else:
            return num1//num2
max_result=float('-inf')
min_result=float('inf')
for oper_perm in all_oper_permutations:
    result=nums[0]
    for i in range(N-1):
        result=caculate(result,nums[i+1],oper_perm[i])
    max_result=max(max_result,result)
    min_result=min(min_result,result)
print(max_result)
print(min_result)