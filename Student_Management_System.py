import os
import csv

def exit():
    print("\t\t\t\t\t\t............................Thank You For Accessing the App ............................")

#To Delete the Record of a Student

def Delete():
    lines = list()

    members = input("Please Enter Your Name or Student_Id")

    with open('university_records.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:

            lines.append(row)

            for field in row:

                if field == members:
                    lines.remove(row)
    with open('university_records.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

 #To Search the Student Record
def Search():
    lines = list()

    members = input("Please Enter Your Name or Student_Id : ")
    print("\n")
    with open('university_records.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:

            lines.append(row)

            for field in row:

                if field == members:
                    # print("\t\t Student Id : ",lines[0])
                    # print("\t\t Student Name : ", lines[1])
                    # print("\t\t Student Class : ", lines[2])
                    # print("\t\t Address: ", lines[3])
                    # print("\t\t Father Name : ", lines[4])
                     print(lines)

#To add new Stiudent Records
def Add_Student():
    print("\t\t\t\t\t\t\t\t\t\t\t*********************** Add Student Record ************************")
    print("\n")
    filename = "university_records.csv"
    fields = ['Student_Id', 'Student_Name', 'Class', 'Address', 'Father Name']
    Select = int(input("How Many Record you want to Add : "))
    for i in range(0,Select):
        Student_Id = int(input("Enter Your Id : "))
        Student_Name = input("Enter Your Name : ")
        Student_Class = input("Enter Your Class : ")
        Student_Address = input("Enter Address : ")
        Student_Fname = input("Enter Father Name : ")
        # mydict=[{'Student_Id':Student_Id,'Student_Name':Student_Name,'Class':Student_Class,'Address':Student_Address, 'Father Name':Student_Fname }]
        mydict = [[Student_Id,Student_Name, Student_Class, Student_Address, Student_Fname]]
        with open("university_records.csv", 'a+') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in mydict:
                csv_writer.writerow(row)
            # csv_file.close()
    if len(filename)!=0:
        print("done !")
        select = input("Press M to Main Menu : ")
        if select =="M" or select =="m":
            Home("Vikram","Singh")
    else:
        print("Not Stored")
        set1 = input("\t\t Press R to Refresh : ")
        if set1=='R' or set1=='r':
            Add_Student()
#For Login as a Admin to Access it.
def Login():
    print("\n\n")
    print("\t\t\t\t\t\t\t\t\t\t\t********************************************************************")
    print("\t\t\t\t\t\t\t\t\t\t\t*******                        Login                         *******")
    print("\t\t\t\t\t\t\t\t\t\t\t********************************************************************")
    print("\n")
    email = input("\t\tEnter your Email :")  #id=vikramattri@gmail.com and password="adminlogin123"
    password = input("\t\tEnter Password : ")
    if email == "vikramattri123@gmail.com" and password == "adminlogin123":
        first_name = "Vikram"
        last_name = "Singh"
        Home(first_name,last_name)
    elif email!="vikramattri123@gmail.com":
        print(("\n\n"))
        print("\t\t Email is Invalid !Press R to Refresh ")
        Select = input()
        if Select == "R" or Select =="r":
            Login()
        else:
            Login()
    elif password != "adminlogin123":
        print(("\n\n"))
        print("\t\t Email is Invalid !Press R to Refresh ")
        Select = input()
        if Select == "R" or Select == "r":
            Login()
        else:
            Login()
#Home Page or Menu Page
def Home(first_name,last_name):
    print("\n\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t*****************************************************************")
    print("\t\t\t\t\t\t\t\t\t\t\t***************** Welcome " + first_name+" " + last_name + " *************")
    print("\t\t\t\t\t\t\t\t\t\t\t\t*****************************************************************")
    print("\n\n\n\n")
    print("\t\t\t\t\t\t\t\t\t\t\t*************************** Select the option **********************")
    print("\t\t\t\t\t\t\t\t\t\t\t* 1. Add Student                                                   *")
    print("\t\t\t\t\t\t\t\t\t\t\t* 2. Search student record                                         *")
    print("\t\t\t\t\t\t\t\t\t\t\t* 3. Delete student record                                         *")
    print("\t\t\t\t\t\t\t\t\t\t\t* 4. Exit                                                          *")
    print("\t\t\t\t\t\t\t\t\t\t\t********************************************************************")
    print("\n")
    print("\t\t Select a option ")
    select = input()
    if select == "1":
        Add_Student()
    elif select =="2":
        Search()
    elif select =="3":
        Delete()
    elif select == "4":
        exit()
#Start function to start the Program
def start():
    print('\t\t\t\t\t\t\t\t\t\t\t*********************************************************************')
    print("\t\t\t\t\t\t\t\t\t\t\t*********************                            ********************")
    print("\t\t\t\t\t\t\t\t\t\t\t********************* Student Management System ********************")
    print("\t\t\t\t\t\t\t\t\t\t\t*********************                            ********************")
    print('\t\t\t\t\t\t\t\t\t\t\t*********************************************************************')
    print("\t\t Press any Key (y/n) ")
    select = input()
    if select=="y" or select=="Y":
        # os.system('cls')
        Login()

    elif select=="n" or select=="N":
        os.system('cls')
        print("Not done")
    else:
        start()

start()