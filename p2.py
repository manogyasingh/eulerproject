su=0
darthvader=[1,2]
while darthvader[1]<4000000:
    if darthvader[1]%2==0:
        su+=darthvader[1]
    darthvader[0],darthvader[1]=darthvader[1],darthvader[0]+darthvader[1]

print(su)

#expected answer: 4613732
