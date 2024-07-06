n=input()
lists=input().split()

def is_prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

count=0
for list in lists:

    if is_prime(int(list))==True:
        count+=1

print(count)