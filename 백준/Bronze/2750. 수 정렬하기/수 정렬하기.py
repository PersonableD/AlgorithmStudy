#a는 리스트 배열 두 그룹으로 나누기
def qsort(a,left,right):
    pl=left
    pr=right
    #피벗x는 배열의 가운데 인덱스
    x=a[(left+right)//2]
    #왼쪽커서가 오른쪽커서 위치와 같거나 왼쪽에 있을때까지
    while pl <=pr:
        #피봇값보다 큰값까지 왼쪽 커서이동
        while a[pl] < x:
            pl+=1
        #피봇값보다 작은값까지 오른쪽 커서이동
        while a[pr] > x:
            pr-=1
         # 왼쪽 커서가 오른쪽 커서보다 왼쪽에 있거나 같은 경우 요소 교환
        if pl <=pr:
            a[pl],a[pr]=a[pr],a[pl]
            pl+=1
            pr-=1
    # 왼쪽 부분 재귀 호출,처음지정한 left 부터 pr까지
    if left < pr:
        qsort(a,left,pr)
    # 오른쪽 부분 재귀 호출 pl,부터 처음 지정한 right 까지
    if pl < right:
        qsort(a,pl,right)    

n=int(input())
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)

#퀵정렬
qsort(arr,0,len(arr)-1)
#출력
for element in arr:
    print(element)