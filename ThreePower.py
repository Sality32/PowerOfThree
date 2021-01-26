def powerThree(n):
    i=3
    while n>i:
        if n%i==0:
            i=i*3
        else: 
            break
    if n==i:   
        return True
    elif n==1:
        return True
    else: return False

rsl = powerThree(27)
print(rsl)