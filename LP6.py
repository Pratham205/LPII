import csv

student_fields = ['roll', 'name', 'age', 'email', 'phone']
student_database = 'students.csv'

def display_menu():
    print("------------------------------------")
    print("Welcome to Student Management System")
    print("------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")

def add_student():
    print("------------------------------------")
    print("Add Student Information")
    print("------------------------------------")
    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)
    with open(student_database, "a", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(student_data)
    print("Data saved successfully")
    input("Press any key to continue")

def view_students():
    print("--Student Records--")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end="\t |")
        print("\n-------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press any key to continue")

def search_student():
    print("--Search Student--")
    roll = input("Enter roll no. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("-----Student Found-----")
                    print("Roll: ", row[0])
                    print("Name: ", row[1])
                    print("Age: ", row[2])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    break
        else:
            print("Roll No. not found in our database")
    input("Press any key to continue")

def update_student():
    print("-----Update Student-----")
    roll = input("Enter Roll no. to Update: ")
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("Student Found: ", row)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
    with open(student_database, "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(updated_data)
    input("Press any key to continue")

def delete_student():
    print("-----Delete Student-----")
    roll = input("Enter roll no. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                else:
                    student_found = True

    if student_found:
        with open(student_database, "w", encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Roll no. ", roll, " deleted successfully")
    else:
        print("Roll No. not found in our database")
    input("Press any key to continue")

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    else:
        break

print("------------------------------------")
print("Thank You for using our System")
print("------------------------------------")
