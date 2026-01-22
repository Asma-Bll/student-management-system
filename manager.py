import json
from student import Student


class StudentManager:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, student):
        self.students.append(student.to_dict())
        self.save_students()
        print("✅ Student added successfully.")

    def list_students(self):
        if not self.students:
            print("⚠️ No students found.")
            return
        for s in self.students:
            print(s)

    def search_student(self, student_id):
        for s in self.students:
            if s["id"] == student_id:
                print(s)
                return
        print("❌ Student not found.")

    def delete_student(self, student_id):
        for s in self.students:
            if s["id"] == student_id:
                self.students.remove(s)
                self.save_students()
                print("🗑️ Student deleted.")
                return
        print("❌ Student not found.")

    def update_student(self, student_id, name, age, email, field):
        for s in self.students:
            if s["id"] == student_id:
                s["name"] = name
                s["age"] = age
                s["email"] = email
                s["field"] = field
                self.save_students()
                print("✏️ Student updated.")
                return
        print("❌ Student not found.")
