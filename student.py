class Student:
    def __init__(self, student_id, name, age, email, field):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.field = field

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "field": self.field
        }
