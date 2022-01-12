def hcf(x,y):
    if x>y:
        small = y
    else:
        small = x
    for i in range(1,small+1):
        if(x%i==0)and (y%i==0):
            hcf =i
    return hcf
num1 = 12
num2 = 4
print("the hcf of",num1,"and",num2,"is",hcf(num1,num2))
