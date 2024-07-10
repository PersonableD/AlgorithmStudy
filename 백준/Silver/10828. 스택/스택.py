N=int(input())
stack=[]
for i in range(N) :
    instruct=input()
    if "push" in instruct:
        n,element= instruct.split()
        stack.append(int(element))
    if "pop" in instruct:
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)
    if "size" in instruct:
        print(len(stack))
    if "empty"in instruct:
        if stack:
            print(0)
        else:
            print(1)
    if "top" in instruct:
        if len(stack)!=0:
            print(stack[-1])
        else:
            print(-1)