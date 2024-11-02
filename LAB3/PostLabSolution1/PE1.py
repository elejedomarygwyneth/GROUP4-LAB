class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __eq__(self, other):
        """Compares equality of two students based on their names."""
        return self.name == other.name

    def __lt__(self, other):
        """Compares if one student's name is less than the other."""
        return self.name < other.name

    def __ge__(self, other):
        """Compares if one student's name is greater than or equal to the other."""
        return self.name >= other.name

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

if __name__ == "__main__":
    student1 = Student("Alice", 20, "A")
    student2 = Student("Bob", 22, "B")

    print("Equality Test:", student1 == student2)  
    print("Less Than Test:", student1 < student2)  
    print("Greater Than or Equal Test:", student1 >= student2)  

