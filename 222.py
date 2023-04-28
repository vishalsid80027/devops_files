upper_limit=int(input("Enter the upper limits:"))
for i in range(0,upper_limit):
   if(i%2==0 or i%3==0):
    continue
print(i,end=" ")

