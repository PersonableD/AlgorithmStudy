num=int(input())


def move(n,source,target,auxiliary):
    if n==1:
        print(f"{source} {target}")
    else:   
            move(n-1,source,auxiliary,target)
            print(f"{source} {target}")
            move(n-1,auxiliary,target,source)



print(2**num-1)
if num<=20:
    move(num,1,3,2)