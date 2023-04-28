
print("""
            ================================
               Welcome To CityHospital
            ================================
    """)
print("""
==========================================
     if you want to sign up choice 1
========================================== 

======================================================
    if you want to register Yourself!! choice 2
=======================================================
""")
r = int(input("enter your choice:"))
if r == 2:
    print("""

                =======================================
                !!!!!!!!!!Register Yourself!!!!!!!!
                =======================================
                                                    """)
    u = input("Input your username!!:")
    p = input("Input the password (Password must be strong!!!:")
    print("""
                ============================================
                !!Well Done!!Registration Done Successfully!!
                ============================================
                                                    """)
    x = input("enter any key to continue")
elif r == 1:
    print("""
                    ==================================
                    !!!!!!!!  {{Sign In}}  !!!!!!!!!!
                    ==================================
                                                        """)
un = input("Enter Username!!:")
ps = input("Enter Password!!:")
row = 2000
for i in row:
                a = list(i)
                if a[0] == str(ps):
                    while (True):
                        print("""
                                1.Administration
                                2.Patient(Details)
                                3.Sign Out

                                                            """)

                        a = int(input("ENTER YOUR CHOICE:"))
                        if a == 1:
                            print("""
                                    1. Display the details
                                    2. Add a new member
                                    3. Delete a member
                                    4. Make an exit
                                                             """)
                            b=int(input("Enter your choice:"))
                                            #details 
                            if b == 1:
                                print("""
                                        1. Doctors Details
                                        2. Nurse Details
                                        3. Others
                                                         """)
                        c = int(input("Enter your Choice:"))
                        if c == 1:
                             for i in row:
                                        b = 0
                                        v = list(i)
                                        k = ["NAME", "SPECIALISATION", "AGE", "ADDRESS", "CONTACT", "FEES",
                                             "MONTHLY_SALARY"]
                                        d = dict(zip(k, v))
                                        print(d)
                        elif c == 2: 
                            for i in row:
                                        v = list(i)
                                        k = ["NAME", "SPECIALISATION", "AGE", "ADDRESS", "CONTACT", "MONTHLY_SALARY"]
                                        d = dict(zip(k, v))
                                        print(d)
                            # IF USER WANTS TO ENTER DETAILS              
                        elif b == 2:
                                print("""

                                        1. Doctor Details
                                        2. Nurse Details
                                        3. Others
                                                                                    """)
                                c = int(input("ENTER YOUR CHOICE:"))
                                # enter doctor details
                                if c == 1:
                                    # ASKING THE DETAILS
                                    name = input("Enter the doctor's name")
                                    spe = input("Enter the specilization:")
                                    age = input("Enter the age:")
                                    add = input("Enter the address:")
                                    cont = input("Enter Contact Details:")
                                    fees = input("Enter the fees:")
                                    ms = input("Enter Monthly Salary:")
                                    # Inserting values in doctors details
                                   
                                    print("SUCCESSFULLY ADDED")
                                # for nurs detail
                                elif c == 2:
                                    # ASKING THE DETAILS
                                    name = input("Enter Nurse name:")
                                    age = input("Enter age:")
                                    add = input("Enter address:")
                                    cont = input("Enter Contact No:")
                                    ms = int(input("Enter Monthly Salary"))
                                    # INSERTING VALUES ENTERED TO THE TABLE
                                    print("SUCCESSFULLY ADDED")
                                     # for entering workers details
                                elif c == 3:
                                    # ASKING THE DETAILS
                                    name = input("Enter worker name:")
                                    age = input("Enter age:")
                                    add = input("Enter address:")
                                    cont = input("Enter Contact No.:")
                                    ms = input("Enter Monthly Salary:")
                                    # INSERTING VALUES ENTERED TO THE TABLE
                                    print("SUCCESSFULLY ADDED")

                                elif b == 3:
                                 print("""
                                        1. Doctor Details
                                        2. Nurse Details
                                        3. Others
                                                                                    """)
                                c = int(input("Enter your Choice:"))
                                # deleting doctor's details
                                if c == 1:
                                    name = input("Enter Doctor's Name:")
                                    print(row)
                                    p = input("you really wanna delete this data? (y/n):")
                                    if p == "y":
                                        print("SUCCESSFULLY DELETED!!")
                                    else:
                                        print("NOT DELETED")
                                         # deleting nurse details
                                elif c == 2:
                                    name = input("Enter Nurse Name:")
                                    
                                    print(row)
                                    p = input("you really wanna delete this data? (y/n):")
                                    if p == "y":
                                        
                                        print("SUCCESSFULLY DELETED!!")
                                    else:
                                        print("NOT DELETED")
                                # deleting other_workers details
                                elif c == 3:
                                    name = input("Enter the worker Name")
                                   
                                    print(row)
                                    p = input("you really wanna delete this data? (y/n):")
                                    if p == "y":
                                        
                                        print("SUCCESSFULLY DELETED!!")
                                    else:
                                        print("NOT DELETED")
                                elif b == 4:
                                 break

                        # entering the pateint detials

                                elif a == 2:

                                 print("""
                                        1. Show Patients Info
                                        2. Add New Patient
                                        3. Discharge Summary
                                        4. Exit
                                                               """)
                        b=int(input("Enter your Choice:"))
                            # showing the existing details

                            # if user wants to see the details of PATIENT
                        if b == 1:
                            
                                for i in row:
                                    b = 0
                                    v = list(i)
                                    k = ["NAME", "SEX", "AGE", "ADDRESS", "CONTACT"]
                                    d = dict(zip(k, v))
                                    print(d)

                            # adding new patient

                        elif b == 2:
                                name = input("Enter your name ")
                                sex = input("Enter the gender: ")
                                age = input("Enter age: ")
                                address = input("Enter address: ")
                                contact = input("Contact Details: ")
                               
                                for i in row:
                                    v = list(i)
                                    k = ['NAME', 'SEX', 'AGE', 'ADDRESS', 'CONTACT']
                                    print(dict(zip(k, v)))
                                    print("""
                                        ====================================
                                        !!!!!!!Registered Successfully!!!!!!
                                        ====================================
                                  """)

                                                                               
                            # dischare process
                        elif b == 3:
                                name = input("Enter the Patient Name:")
                               
                                print(row)
                                bill = input("Has he paid all the bills? (y/n):")
                                if bill == "y":
                                    break
                                    
                            # if user wants to exit
                        #elif b == 4:
                                #break
                        ###SIGN OUT


                # IF THE USERNAME AND PASSWORD IS NOT IN THE DATABASE
                #else:
                    #break

