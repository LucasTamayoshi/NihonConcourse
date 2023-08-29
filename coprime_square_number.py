import math
def coprime_squares(n):
    import math
    coprime_squares_number=[]
    for a in range(1,int(n**(1/2))+1):
        if math.gcd(a,n)==1:
            coprime_squares_number.append(a)
    return len(coprime_squares_number)

#example: coprime_squares(840)=6
