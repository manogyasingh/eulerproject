primes=[None, None, True,True]
def sievecontinue(primes,till):
    till+=1
    yet=len(primes)
    primes+= ([True for i in range(yet,till)])
    for i in range (2,till):
        if primes[i]:
            uplim=till//i+1
            while uplim*i>=till-1:
                uplim-=1
            for j in range (2,uplim):
                primes[i*j]=0
    return primes

if __name__=="__main__":
    primes=sievecontinue(primes,10000)
    while(True):
        print(primes[int(input())])
