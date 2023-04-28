# num=int(input("Enter your number"))
# sum=0
# for num in range(1,num+1,1):
#     sum+=num
#     print("total number is=",sum)


# import math
# p=int(input("Enter your initial value:"))
# i=int(input("Enter your intrest rate:"))
# y=int(input("Enter your time periods:"))
# for x in range(1,y+1):
#     total_amount=p+(p/100*i*y)
# print(total_amount)



# data="hello"
# for index in range(len(data)):
#     print(index,data[index]) 
# import tkinter as tk
# label = tk.Label(
#     text="Hello, Tkinter",
#     fg="white",
#     bg="black",
#     width=10,
#     height=10
# )


# def pattern(n):
#     for i in range(0,n):
#         for j in range(0,i+1):
#             print("*",end=" ")
#         print()
# n=3
# pattern(n)


def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("^",end=" ")
        print()
n=4
pattern(n)