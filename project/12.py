# # class GeekforGeeks:
 
# #     # default constructor
# #     def __init__(self):
# #         self.geek = "GeekforGeeks"
 
# #     # a method for printing data members
# #     def print_Geek(self):
# #         print(self.geek)
 
 
# # # creating object of the class
# # obj = GeekforGeeks()
 
# # # calling the instance method using the object obj
# # obj.print_Geek()






# class addition:
#     first=0
#     second=0
#     result=0
#     def __init__(self,f,s):
#         self.first=f
#         self.second=s

#     def display(self):
#         print("first number="+str(self.first))
#         print("second number="+str(self.second))
#         print("adddition of two number="+str(self.result))
#     def calculate(self):
#         self.result=self.first+self.second

# obj=addition(200,300)
# obj.calculate()
# obj.display()


# annualincome=int(input("Enter your annual income="))
# if annualincome<=20000:
#     taxamount=0
# elif annualincome<=50000:
#     taxamount=(annualincome-20000)*0.05
# elif annualincome<=100000:
#     taxamount=(annualincome-50000)*0.10+1200
# print("The claculated income tax on",annualincome,"=",taxamount)



import random
import tkinter
from tkinter import *
from tkinter import messagebox
window = tkinter.Tk()
window.geometry('600x500')
window.title("Burger ordering app")

name_label=Label(window,text='Your Name:')
name_label.grid(column=0,row=0)

name_entry=Entry(window,width=25)
name_entry.grid(row=0,column=1)


name_label=Label(window,text='Select Your Burger')
name_label.grid(column=0,row=1)


my_burgerList= ["veg Burger","Aloo tikki Burger","Chicken Burger","Cheese Burger","Paneer Burger"]

burger_list= Listbox(window ,selectmode=MULTIPLE,bg="black",fg="red")
burger_list.grid(row=2,column=1)

for item in my_burgerList:
    burger_list.insert(0,item)


def add_burger():
    result=''
    for item in burger_list.curselection():
        result=result+str(burger_list.get(item))+'\n'
        Label(window ,text="Your selections are "+"\n"+result).grid(row=4 ,column=1)   
    

def checkout():
     order_id= random.randint(0,1000000)
     messagebox.showinfo('submitted','successfuly placed\n'+ 'name:' + name_entry.get()+'\norder id:'+str(order_id))
    
  


def exit_me():
    answer=messagebox.askyesno("Hii","Do you want to exit?") 
    if(answer==1):
        window.destroy()
      
    

b1=Button(window,text="Add Burger",command=add_burger)
b1.grid(column=0,row=3)

    

check= Button(window,text="Checkout",command=checkout)
check.grid(row=6,column=0)

exit_btn=Button(window,text="Exit",command=exit_me)
exit_btn.grid(row=10,column=0)
window.mainloop()