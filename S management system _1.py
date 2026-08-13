students = []

def add_student():
        student_id = int(input("Enter student ID :"))
        name = input("Enter Name :")
        course = input("Enter Course :")
        Marks = float(input("Enter Marks :"))
       
        while True:
            if Marks<0 or Marks>100:
                print("Invalide") 
                Marks = float(input("Enter valide Marks :"))
            else:
                break
            
            
        student = {
            "id": student_id,
            "name": name,
            "course": course,
            "marks": Marks
            }
       
        students.append(student)
        
        print("Student added Sucessfully!!")

def view_students():
        if len(students) == 0:
            print("No Student Found!")
            return

        for student in students:
            print(student)

def search_student():
    student_id = int(input("Enter Student ID: "))
    
    for student in students:
        if student["id"] == student_id:
            print("Student Found!")
            print("ID     :", student["id"])
            print("Name   :", student["name"])
            print("Course :", student["course"])
            print("Marks  :", student["marks"])
            return

    print("Student Not Found!")   

def update_student():
    search = int(input("Enter student id :"))
    for student in students:
        if student["id"] == search:
            print("student found!!")
            print("1.Update Name")
            print("2.Update Course")
            print("3.Update Marks")
            print("4.Cancel")

            choice = input("enter your choice what you wanty to update:")

            if choice == "1":
                n_name = input("enter new name:")
                student["name"] = n_name
                print("Name Updated")
            elif choice =="2":
                n_course = input("enter new course:")
                student["course"] = n_course
                print("Course updated")
            elif choice =="3":
                n_marks = float(input("enter new Marks:"))
                if n_marks < 0 or n_marks > 100:
                    print("Invalid marks!")
                    return
                student["marks"] = n_marks
                print("Marks updater")
            elif choice =="4":
                print("Update cancile!")
            else:
                print("Invalide Choice!")
            return

    print("Student Not found!")

def delete_student():
    select = int(input("enter student id :"))
    for student in students :
        if student["id"] == select:
            print("student found!")
            comfirm= input("are you sure?(yes/no):")
            if comfirm.lower()== "yes":
                students.remove(student)
                print("Deleted!")
            else:
                print("Delete cancelled!")
            return



while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
         add_student()

    elif choice == "2":
        view_students()

    elif choice =="3":
        search_student()


    elif choice =="4":
        update_student()

    elif choice =="5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        break
    else :
        print("Invalide Choice!")

    
    