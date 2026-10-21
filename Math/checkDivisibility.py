n=23
def checkDivisibility(n):
    org=n
    digit=[]
    while n!=0:
        digit.append(n%10)
        n=n//10
    s=sum(digit)
    p=1
    for i in range(len(digit)):
        p*=digit[i]
    if org%(s+p)==0:
        return True
    else:
        return False
print(checkDivisibility(n))