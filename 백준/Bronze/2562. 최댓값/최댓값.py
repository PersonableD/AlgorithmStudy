numbers=[]
i=0
j=0
k=0
#9개의 자연수 입력받아 배열에 넣기
while i <9:
    number=int(input())
    numbers.append(number)
    i+=1

maxValue=numbers[0]
maxIndex=0
#최대값구하기
#for number in numbers:
#    print(number)
for i in range(len(numbers)):
    if numbers[i]>maxValue:
        maxValue=numbers[i]
        maxIndex=i



print(maxValue)
print(maxIndex+1)