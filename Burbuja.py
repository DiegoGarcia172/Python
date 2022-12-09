import random
def burbuja(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i] > nlist[i + 1]:
                tmp = nlist[i]
                nlist[i] = nlist[i + 1]
                nlist[i+1] = tmp
            
 
nlist = [random.randint(0, 100)for i in range(10)]



print(nlist)
burbuja(nlist)
print(nlist)
input()