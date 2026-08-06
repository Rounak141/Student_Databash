students = []

def add_student():
        student_id = int(input("Enter student ID :"))
        name = input("Enter Name :")
        course = input("Enter Course :")
        Marks = float(input("Enter Marks :"))
        if Marks<0 or Marks>100:
            print("Invalide") 
            return None
        
        student = {
            "id": student_id,
            "name": name,
            "course": course,
            "marks": Marks
            }
        return student

def view_students():
        if len(students) == 0:
            print("No Student Found!")
            return

        for student in students:
            print(student)

def Search_student():
    print("Hello")


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
       student = add_student()

       if student: 
            students.append(student)
            print("Student Added Successfully!")

    elif choice == "2":
        view_students()

    elif choice =="3":
        Search_student()


    elif choice =="4":
        print("a")


    elif choice =="5":
        print("a")


    elif choice == "6":
        print("Thank You!")
        break
    else :
        print("Invalide Choice!")

    
    