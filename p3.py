from math import sqrt
 
u=3000000
prime=[None,None]+[True]*(u-1)
for i in range(2,len(prime)):
    if prime[i]:
        for j in range(i,u//i+1):
            prime[i*j]=False
primes=[i for i in range(u) if prime[i]]
 
def primef(a):
    if a == 1:
        return tuple()
    if prime[a]:
        return (a,)
    for i in primes:
        if i*i>a:
            break
        else:
            if a%i==0:
                return (i,) + primef(a//i)
anst=primef(600851475143)
if anst=tuple():
    print(600851475143)
else:
    print(anst[-1])
