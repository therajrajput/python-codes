def raj(n):
    sm=0
    i=1
    while i<n:
        if n%i==0:
            sm=sm+i
        i=i+1
    
    if n==sm:
        print(n,"is a pefect number")
    else:
        print(n,"is not perfet number")
raj(6)  

