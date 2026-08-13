import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='DylanBaptist162008',database='STUDENT_MANAGEMENT')
mycursor=mydb.cursor()

def add_student():
    while True:
        inp=input("Do you want to enter data(y/n):").lower()
        if inp=='n':
            break
        elif inp=='y':
            name=input("Enter the name:")
            age=int(input("Enter the age:"))
            gender=input("Enter the gender:")
            department=input("Enter the department:")
            year=int(input("Enter the year:"))
            email=input("Enter the email:")
            phone=input("Enter the phone number:")

            query="INSERT INTO STUDENTS(NAME,AGE,GENDER,DEPARTMENT,YEAR,EMAIL,PHONE) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            values=(name,age,gender,department,year,email,phone)
            mycursor.execute(query,values)
            mydb.commit()
            print("Data added successfully")
        else:
            print("Invalid input")

def view_students():
    mycursor.execute("SELECT * FROM STUDENTS")
    rows=mycursor.fetchall()
    if not rows:
        print("No student records are available")
    else:
        for data in rows:
            print('=' * 40)
            print("STUDENT_ID:",data[0])
            print("NAME:",data[1])
            print("AGE:",data[2])
            print("GENDER:",data[3])
            print("DEPARTMENT:",data[4])
            print("YEAR:",data[5])
            print("EMAIL:",data[6])
            print("PHONE:",data[7])
            print('=' * 40)


def search_student():
    student_id=int(input("Enter the ID of the Student:"))
    query="SELECT * FROM STUDENTS WHERE STUDENT_ID=%s"
    values=(student_id,)
    mycursor.execute(query,values)
    row = mycursor.fetchone()

    if row is None:
        print("ID doesn't exist")
    else:
        print("-" * 40)
        print("Student ID :", row[0])
        print("Name       :", row[1])
        print("Age        :", row[2])
        print("Gender     :", row[3])
        print("Department :", row[4])
        print("Year       :", row[5])
        print("Email      :", row[6])
        print("Phone      :", row[7])
        print("-" * 40)
    

def update_student():
    student_id=int(input("Enter the ID of the Student:"))
    print("What do you want to update?")
    print("1.Name")
    print("2.Age")
    print("3.Gender")
    print("4.Department")
    print("5.Year")
    print("6.Email")
    print("7.Phone")

    update_choice=int(input("Enter your choice:"))
    if update_choice==1:
        column='NAME'
        new_value=input("Enter the new name:")
    elif update_choice==2:
        column='AGE'
        new_value=int(input("Enter the new age:"))
    elif update_choice==3:
        column='GENDER'
        new_value=input("Enter the new gender:")
    elif update_choice==4:
        column='DEPARTMENT'
        new_value=input("Enter the new department:")
    elif update_choice==5:
        column='YEAR'
        new_value=int(input("Enter the new year:"))
    elif update_choice==6:
        column='EMAIL'
        new_value=input("Enter the new Email:")
    elif update_choice==7:
        column='PHONE'
        new_value=input("Enter the new phone number:")
    else:
        print("Invalid choice")
        return
    query=f"UPDATE STUDENTS SET {column}=%s WHERE STUDENT_ID=%s"
    values=(new_value,student_id)
    mycursor.execute(query,values)
    mydb.commit()
    if mycursor.rowcount==0:
        print("ID doesn't exist")
    else:
        print("Data updated successfully")

def delete_student():
    student_id=int(input("Enter the ID of Student:"))
    query="DELETE FROM STUDENTS WHERE STUDENT_ID=%s"
    values=(student_id,)
    mycursor.execute(query,values)
    mydb.commit()
    if mycursor.rowcount==0:
        print("ID doesn't exist")
    else:
        print("Data deleted successfully")        
        


while True:
    print('=' * 40)
    print("        STUDENT MANAGEMENT SYSTEM")
    print('=' * 40)

    print("1. Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Exit")
    
    print('=' * 40)
    try:
        choice = int(input("Enter your choice:"))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if choice==1:
        add_student()
    elif choice==2:
        view_students()
    elif choice==3:
        search_student()
    elif choice==4:
        update_student()
    elif choice==5:
        delete_student()
    elif choice==6:
        mycursor.close()
        mydb.close()
        print("Thank You")
        break


