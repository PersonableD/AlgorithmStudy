brackets = input()

stack = []
stack_num = [0]
valid = True  # 입력이 유효한지 확인하는 플래그

for bracket in brackets:
    if bracket in "([":
        stack.append(bracket)
        stack_num.append(0)
    elif bracket == ")":
        if not stack or stack[-1] != "(":
            valid = False
            break
        stack.pop()
        temp = stack_num.pop()
        if temp == 0:
            stack_num[-1] += 2
        else:
            stack_num[-1] += temp * 2
    elif bracket == "]":
        if not stack or stack[-1] != "[":
            valid = False
            break
        stack.pop()
        temp = stack_num.pop()
        if temp == 0:
            stack_num[-1] += 3
        else:
            stack_num[-1] += temp * 3

if valid and len(stack) == 0:
    print(stack_num[0])
else:
    print(0)