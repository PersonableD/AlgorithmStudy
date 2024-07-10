dwarfs=[]
exist=False

for i in range(9):
    n=int(input())
    dwarfs.append(n)

tota_sum=sum(dwarfs)
for i in range(8):
    for j in range(i+1,9):
        if tota_sum-dwarfs[i]-dwarfs[j]==100:
            exist=True
            #난쟁이 두명 제거
            dwarfs.pop(i)
            dwarfs.pop(j-1)
            #난쟁이 두명 제외한 난쟁이 오름차순 정렬
            dwarfs.sort()
            break
    if exist==True:
        break

for dwarf in dwarfs:
    print(dwarf)