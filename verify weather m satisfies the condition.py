import time
import math
import sympy

def coprime_squares(n):
    import math
    coprime_squares_number=[]
    for a in range(1,int(n**(1/2))+1):
        if math.gcd(a,n)==1:
            coprime_squares_number.append(a)
    return len(coprime_squares_number)

inicio=time.time()
#目的：nまでの自然数の中で、補題１を満たす数の個数を求めること。
#example of number of cases to test
n=1000

for m in range(2,n):    

    totien=sympy.totient(m) #euler totient function
    copri=coprime_squares(m)*2**len(sympy.factorint(m)) #number of roots of the congruence equation (without the 1/2, 2)
    ratio=copri/totien #ratio between them (if ratio=1, then n satisfies the condition)
            
    if  m%8==0 and ratio*2==1: #weather the equality holds for when 8 divides m
        print(m) 
        
    elif m%2==0 and m%4!=0 and ratio/2==1: #weather the equality holds for when 2 divides and 4 does not divide m
        print(m)

    elif ratio==1: #when m is odd or 4 divides and 8 does not divide m 
        print(m)           
            

final=time.time()

print(f"time : {final-inicio}")

print()
print("End")

#result:
"""
2
3
4
5
6
8
10
12
15
16
20
21
24
26
28
30
40
48
56
60
72
78
88
120
168
210
240
840
time : 0.4545407295227051

End
"""
