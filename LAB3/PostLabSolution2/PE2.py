import random

def main():
    students = [
        Student("Zoe", 19, "B"),
        Student("Alice", 20, "A"),
        Student("John", 21, "C"),
        Student("Bob", 22, "B+"),
        Student("Emma", 23, "A-")
    ]

    print("Before Shuffling:")
    for student in students:
        print(student)

    random.shuffle(students)

    print("\nAfter Shuffling:")
    for student in students:
        print(student)

    students.sort()

    print("\nAfter Sorting:")
    for student in students:
        print(student)

if __name__ == "__main__":
    main()
