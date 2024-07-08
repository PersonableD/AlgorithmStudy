t=int(input())
def is_prime(k):
    if k==1:
        return False
    for i in range(2,k):
        if k%i==0:
            return False
    return True

for i in range(t):
    n=int(input())
    for a in range(n//2,1,-1):
        b=n-a
        if is_prime(a) and is_prime(b):
            print(f"{a} {b}")
            break