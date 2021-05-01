import os
import csv

def exit():
    print("\t\t\t\t\t\t....................Thank You For Accessing the App .....................")

#To Delete the Record of a Student

def delete():
    lines = list()
    members = input("Please Enter Your Name or Student_Id")
    with open('university_records.csv', 'r') as read_file:
        reader = csv.reader(read_file)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == members:
                    lines.remove(row)
    with open('university_records.csv', 'w') as write_file:
        writer = csv.writer(write_file)
        writer.writerows(lines)

 #To Search the Student Record
def search():
    lines = list()
    members = input("Please Enter Your Name or Student_Id : ")
    print("\n")
    with open('university_records.csv', 'r') as read_file:
        reader = csv.reader(read_file)
        for row in reader:

            lines.append(row)

            for field in row:

                if field == members:
                     print(lines)

#To add new Stiudent Records
def add_student():
    print("\t\t\t\t\t\t\t\t\t\t\t********************* Add Student Record *********************\n")
    filename = "university_records.csv"
    select = int(input("How Many Record you want to Add : "))
    for i in range(0,select):
        student_id = int(input("Enter Your Id : "))
        student_name = input("Enter Your Name : ")
        student_class = input("Enter Your Class : ")
        student_address = input("Enter Address : ")
        student_fname = input("Enter Father Name : ")
        mydict = [[student_id,student_name, student_class, student_address, student_fname]]
        with open("university_records.csv", 'a+') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in mydict:
                csv_writer.writerow(row)
            # csv_file.close()
    if len(filename)!=0:
        print("done !")
        select = input("Press M to Main Menu : ")
        if select =="M" or select =="m":
            home("Vikram","Singh")
    else:
        print("Not Stored")
        set1 = input("\t\t Press R to Refresh : ")
        if set1=='R' or set1=='r':
            add_student()
#For Login as a Admin to Access it.
def login():
    print("\n\n")
    print("\t\t\t\t\t\t\t\t\t\t\t*****************************************************************")
    print("\t\t\t\t\t\t\t\t\t\t\t*******                        Login                      *******")
    print("\t\t\t\t\t\t\t\t\t\t\t*****************************************************************")
    print("\n")
    email = input("\t\tEnter your Email :")  #id=vikramattri@gmail.com and password="adminlogin123"
    password = input("\t\tEnter Password : ")
    if email == "vikramattri123@gmail.com" and password == "adminlogin123":
        first_name = "Vikram"
        last_name = "Singh"
        home(first_name,last_name)
    elif email!="vikramattri123@gmail.com":
        print(("\n\n"))
        print("\t\t Email is Invalid !Press R to Refresh ")
        select = input()
        if select == "R" or select =="r":
            login()
        else:
            login()
    elif password != "adminlogin123":
        print(("\n\n"))
        print("\t\t Email is Invalid !Press R to Refresh ")
        select = input()
        if select == "R" or select == "r":
            login()
        else:
            login()
#Home Page or Menu Page
def home(first_name,last_name):
    print("\n\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t*************************************************************")
    print("\t\t\t\t\t\t\t\t\t\t\t*********** Welcome " + first_name+" " + last_name + " ********")
    print("\t\t\t\t\t\t\t\t\t\t\t\t*************************************************************")
    print("\n\n\n\n")
    print("\t\t\t\t\t\t\t\t\t\t\t*********************** Select the option *******************")
    print("\t\t\t\t\t\t\t\t\t\t\t* 1. Add Student                                            *")
    print("\t\t\t\t\t\t\t\t\t\t\t* 2. Search student record                                  *")
    print("\t\t\t\t\t\t\t\t\t\t\t* 3. Delete student record                                  *")
    print("\t\t\t\t\t\t\t\t\t\t\t* 4. Exit                                                   *")
    print("\t\t\t\t\t\t\t\t\t\t\t*************************************************************")
    print("\n")
    print("\t\t Select a option ")
    select = input()
    if select == "1":
        add_student()
    elif select =="2":
        search()
    elif select =="3":
        delete()
    elif select == "4":
        exit()
#Start function to start the Program
def start():
    print("\n\n\n")
    print('\t\t\t\t\t\t\t\t\t\t\t****************************************************************')
    print("\t\t\t\t\t\t\t\t\t\t\t*******************                            *****************")
    print("\t\t\t\t\t\t\t\t\t\t\t******************* Student Management System ******************")
    print("\t\t\t\t\t\t\t\t\t\t\t*******************                           ******************")
    print('\t\t\t\t\t\t\t\t\t\t\t************************************************************\n\n')
    select = input("\t\t Press any Key (y/n) :  ")
    if select=="y" or select=="Y":
        # os.system('cls')
        login()

    elif select=="n" or select=="N":
        os.system('cls')
        print("Not done")
    else:
        start()

start()