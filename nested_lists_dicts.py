# Nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix element [1][2]:", matrix[1][2])
print()

# Nested dictionaries
students = {
    "1": {"name": "Shrey", "age": 20},
    "2": {"name": "Darsh", "age": 20},
    "3": {"name": "Shruu", "age": 20},
    "4": {"name": "Jinal", "age": 20}
}
print("Student 1 name:", students["1"]["name"])
print("Student 1 age:", students["1"]["age"])
print()

# List comprehension
squares = [i * i for i in range(5)]
print("Squares list:", squares)
print()

# Dictionary comprehension
square_dict = {i: i * i for i in range(5)}
print("Square dict:", square_dict)
print()

# Working with sets
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
fruits.add("banana")  # duplicate ignored automatically
print("Fruits set:", fruits)
print()

# Working with tuples
fruit_tuple = ("apple", "banana", "cherry")
print("Fruit tuple:", fruit_tuple)
print("Tuple element 0:", fruit_tuple[0])
try:
    fruit_tuple[0] = "orange"
except TypeError as e:
    print("Cannot change tuple item:", e)
print()

# Cleaned data script example
students_data = [
    {"id": "1", "name": "Shrey", "age": "20", "grade": "A"},
    {"id": "2", "name": "Darsh", "age": "20", "grade": "B"},
    {"id": "3", "name": "Shruu", "age": "20", "grade": "A"},
    {"id": "4", "name": "Jinal", "age": "twenty", "grade": None}
]

unique_names = set()
cleaned_students = []

for student in students_data:
    if student["grade"] is None:
        continue
    cleaned_students.append(student)
    unique_names.add(student["name"])

print("Cleaned students data:", cleaned_students)
print("Unique student names:", unique_names)
