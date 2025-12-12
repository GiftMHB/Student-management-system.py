# file = open("students.txt", "w")


def start():
    print('Student management system started.')
    
    instructor_menu = '''

    1. Add Student
    2. View all Students
    3. Search Student by ID
    4. Update Student Information
    5. Delete Student
    6. Exit
    '''
    
    while True:
        
        print(instructor_menu)
        try:
            instructor_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue  
        
        match instructor_choice:
            case 1:
                add_student()
            case 2:
                view_students()
            # case 3:
            #     search_student()
            # case 4:
            #     update_student_info()
            # case 5:
            #     delete_student()
            case 6:
                exit_program()
                print("Exiting system...")
                break  
            case _:
                print('Invalid input:', instructor_choice)
    
   
def add_student():
    
    student_ID = input('Enter the studentID: ')
    student_name = input('Enter student name: ')
    student_age = input('Enter student age: ')
    student_C = input('Enter student course: ')
    
    if not student_ID or not student_name or not student_age or not student_C:
        print('Not successful!! All fields are required.')
    
    f = open("students.txt", "a")
    
    
    f.write(student_ID + "," + student_name + "," + student_age + "," + student_C + "\n")
    
    f.close()
    print(student_name, ' of ID: ', student_ID, ' was added successfully!')
    
def exit_program():
    print("Goodbye, visit soon!!!")
    
def view_students():
    
    print("Viewing all students...")
    f = open("students.txt", "r")
    content = f.read()
    
    if not content:
        print('No students found')
    else:
        print(content)
        
    f.close()
    
    
start()
    