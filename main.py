from student import Student
from manager import StudentManager


def menu():
    print("\n===== Student Management System =====")
    print("1. Add student")
    print("2. List students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("0. Exit")


def main():
    manager = StudentManager()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            student_id = input("ID: ")
            name = input("Name: ")
            age = input("Age: ")
            email = input("Email: ")
            field = input("Field: ")

            student = Student(student_id, name, age, email, field)
            manager.add_student(student)

        elif choice == "2":
            manager.list_students()

        elif choice == "3":
            student_id = input("Enter student ID: ")
            manager.search_student(student_id)

        elif choice == "4":
            student_id = input("ID to update: ")
            name = input("New name: ")
            age = input("New age: ")
            email = input("New email: ")
            field = input("New field: ")
            manager.update_student(student_id, name, age, email, field)

        elif choice == "5":
            student_id = input("ID to delete: ")
            manager.delete_student(student_id)

        elif choice == "0":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
