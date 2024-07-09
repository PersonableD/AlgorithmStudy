def hanoi(n,start,via,end):
    if n==1:
    #원판이 하나일때는 바로 end로 옮김
        print(f'{start} {end}')
        return
    #원판이 2개 이상일때는 n-1개의 원반을 중간기둥으로 옮긴뒤
    hanoi(n-1,start,end,via)
    #n 원반을 end로 옮기고
    print(f'{start} {end}')
    #중간기둥에 있는 n-1의 원반을 end로 옮긴다
    hanoi(n-1,via,start,end)

num=int(input())
#n=1일때 1번, n=2일때 1+2번, n=3일때 1+2+2^2번... n번일때 1+2+2^2+2^3+...2^n-1 의 일반항
print(2**num-1)
if num<=20:
    hanoi(num,1,2,3)