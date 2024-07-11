count=0
def cycle(a,b,f,s):
    global count
    if b>=10:
        b=b-10
    if b>=20:
        b=b-20
        print(f"{a} {b}")
    if f==a and s==b and count>0:
        return count
    count+=1
    return cycle(b,a+b,f,s)
   
    

N=input()
if int(N)<10:
    N="0"+ N

c=int(N[0])
d=int(N[1])
print(cycle(c,d,c,d))