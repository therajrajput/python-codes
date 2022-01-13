#pthone program cheak any perfet number or not:
num=int(input("enter any number"))   
sum=0
i=1
while i<num:
 if num%i==0:
    sum=sum+i
 i=i+1
if num==sum:
    print(num,"is a pefect number")
else:
   print(num,"is not perfet number")
