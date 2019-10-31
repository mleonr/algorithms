import numpy as np
np.random.seed(2)
arr1 = np.random.randint(0,10,16)
arr2 = np.random.randint(0,10,16)
n1 = list(arr1)
n2 = list(arr2)
def NMA(x,y):
    ls= list()
    if len(x)==1 and len(y)==1:
        ls.insert(0,(x[0]*y[0])%10)
        if (x[0]*y[0])//10 != 0:
            ls.insert(0,(x[0]*y[0])//10)
        return ls
    n = len(x)
    a=x[0:n//2] 
    b=x[n//2:]
    c=y[0:n//2]
    d=y[n//2:]
     
    ls1 = NMA(a,c) 
    ls1.extend([0]*n)
    ls2 = add(NMA(a,d),NMA(b,c)) 
    ls2.extend([0]*(n//2))
    
    return add(add(ls1,ls2),NMA(b,d))	
def add(l1,l2):
    if len(l1)>len(l2):
        s = len(l2)-1
        res=0
        for i,e in reversed(list(enumerate(l1))):
            if s != -1:
                val=l1[i]+l2[s]+res
                res = val//10
                l1[i]=val%10
                s=s-1;
            else:
                val=l1[i]+res
                res = val//10
                l1[i]=val%10
        return l1
    elif len(l1)<len(l2):
        s = len(l1)-1
        res=0
        for i,e in reversed(list(enumerate(l2))):
            if s != -1:
                val=l2[i]+l1[s]+res
                res = val//10
                l2[i]=val%10
                s=s-1;
            else:
                val=l2[i]+res
                res = val//10
                l2[i]=val%10
        return l2
    else:
        s = len(l2)-1
        res=0
        for i,e in reversed(list(enumerate(l1))):
            val=l1[i]+l2[s]+res
            res = val//10
            l1[i]=val%10
            s=s-1;
        if res!=0:
            l1.insert(0,res)
        return l1
# return NMA(a,c)*(10**n)+(NMA(a,d)+NMA(b,c))*(10**(n//2))+NMA(b,d)
resultado=NMA(n1,n2)
print(resultado)