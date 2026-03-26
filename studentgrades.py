students={}
while True:
    print("Enter student details:")
    name=input("Enter the student's name: ")
    grade=input("Enter the student's grade: ")
    students[name]=grade  
    print(students)
    cont=input("Do you want to add another student? (yes/no): ")
    if cont.lower() != 'yes':
        break





