# Edutech Solution Python Development Internship  

# Task 4: Data Structures Deep Dive

## Objective
- Lists Comprehension
- Dictionaries Comprehension
- Tuples
- Sets
- Nested List & Dictionaries


### 1. Nested Lists
A nested list is a list that contains other lists as its elements. It is useful for representing matrix or table-like data.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix element [1][2]:", matrix[1][2])  # Output: 6
```
---

### 2. Nested Dictionaries
A nested dictionary is a dictionary where the values are themselves dictionaries. This is ideal for representing records with multiple attributes.

```python
students = {
    "1": {"name": "Shrey", "age": 20},
    "2": {"name": "Darsh", "age": 20},
    "3": {"name": "Shruu", "age": 20},
    "4": {"name": "Jinal", "age": 20}
}
print("Student 1 name:", students["1"]["name"])  # Output: Shrey
print("Student 1 age:", students["1"]["age"])     # Output: 20
```

---

### 3. List Comprehension
List comprehension provides a concise way to create lists based on existing sequences or ranges.

```python
squares = [i * i for i in range(5)]
print("Squares list:", squares)  # Output: [0, 1, 4, 9, 16]
```
---

### 4. Dictionary Comprehension
Dictionary comprehension creates dictionaries in a single, readable line.

```python
square_dict = {i: i * i for i in range(5)}
print("Square dict:", square_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```
---

### 5. Sets
A set is an unordered collection of unique elements. Duplicates are automatically ignored.

```python
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
fruits.add("banana")  # duplicate — ignored automatically
print("Fruits set:", fruits)  # Output: {'banana', 'orange', 'cherry', 'apple'}
```

---

### 6. Tuples
A tuple is an ordered, immutable  collection. Once created, its elements cannot be changed.

```python
fruit_tuple = ("apple", "banana", "cherry")
print("Fruit tuple:", fruit_tuple)
print("Tuple element 0:", fruit_tuple[0])  # Output: apple

fruit_tuple[0] = "orange"  # TypeError: 'tuple' object does not support item assignment
```

---

### 7. Cleaned Data Script
A practical example of using **lists**, **dicts**, and **sets** together to clean raw data — filtering out incomplete records and extracting unique values.

```python
students_data = [
    {"id": "1", "name": "Shrey", "age": "20", "grade": "A"},
    {"id": "2", "name": "Darsh", "age": "20", "grade": "B"},
    {"id": "3", "name": "Shruu", "age": "20", "grade": "A"},
    {"id": "4", "name": "Jinal", "age": "twenty", "grade": None}  # bad record
]

unique_names = set()
cleaned_students = []

for student in students_data:
    if student["grade"] is None:
        continue                        # skip incomplete records
    cleaned_students.append(student)
    unique_names.add(student["name"])

print("Cleaned students data:", cleaned_students)
print("Unique student names:", unique_names)
```

**What it does**:
- Skips any student whose `grade` is `None`
- Collects valid records into `cleaned_students`
- Uses a **set** to track unique names (no duplicates)

---

## Output
```
Matrix element [1][2]: 6

Student 1 name: Shrey
Student 1 age: 20

Squares list: [0, 1, 4, 9, 16]

Square dict: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

Fruits set: {'banana', 'orange', 'cherry', 'apple'}

Fruit tuple: ('apple', 'banana', 'cherry')
Tuple element 0: apple
Cannot change tuple item: 'tuple' object does not support item assignment

Cleaned students data: [{'id': '1', 'name': 'Shrey', 'age': '20', 'grade': 'A'}, {'id': '2', 'name': 'Darsh', 'age': '20', 'grade': 'B'}, {'id': '3', 'name': 'Shruu', 'age': '20', 'grade': 'A'}]
Unique student names: {'Shrey', 'Darsh', 'Shruu'}
```

---

## Interview Questions & Answers

### Q1: List vs Tuple — What's the difference?

| Feature        | List                            | Tuple                          |
|:---------------|:--------------------------------|:-------------------------------|
| Syntax         | `[1, 2, 3]`                    | `(1, 2, 3)`                   |
| Mutability     | **Mutable** (can be changed)   | **Immutable** (cannot change)  |
| Speed          | Slower                          | Faster                         |
| Use Case       | Dynamic collections             | Fixed/constant data            |
| Methods        | Many (`append`, `pop`, etc.)   | Few (`count`, `index`)         |
| Memory         | More memory                     | Less memory                    |
| Hashable       | No (cannot be dict key)      |  Yes (can be dict key)       |

**Rule of thumb**: Use a **list** when data may change; use a **tuple** when data should remain constant.

---

### Q2: When to use a Dictionary?

Use a **dictionary** when you need:
- **Key-value mapping** — e.g., student ID → student details
- **Fast lookups** — O(1) average time for access by key
- **Labelled data** — instead of remembering index positions
- **Counting / grouping** — e.g., word frequencies
- **Configuration / settings** — readable key-based access

```python
# Example: fast lookup
config = {"theme": "dark", "language": "en", "font_size": 14}
print(config["theme"])  # O(1) access
```

---

### Q3: What is a Set and when would you use it?

A **set** is an unordered collection of unique elements. Use it when:
- You need to **eliminate duplicates** from a list
- You need fast **membership testing** (`in` operator is O(1))
- You need **mathematical set operations** (union, intersection, difference)

```python
names = ["Shrey", "Darsh", "Shrey", "Shruu"]
unique = set(names)  # {'Shrey', 'Darsh', 'Shruu'}
```

---

### Q4: What are List and Dict Comprehensions?

**Comprehensions** are concise, Pythonic one-liners for creating lists/dicts from iterables.

```python
# List comprehension — filter even numbers
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Dict comprehension — name lengths
names = ["Shrey", "Darsh", "Shruu"]
name_lengths = {name: len(name) for name in names}
# {'Shrey': 5, 'Darsh': 5, 'Shruu': 5}
```

---

### Q5: How do you handle missing or None values in data?

Filter out records with `None` values before processing:

```python
data = [{"name": "A", "grade": "A"}, {"name": "B", "grade": None}]
clean = [d for d in data if d["grade"] is not None]
```
---

## Keys Features
- **Lists** → ordered, mutable, allows duplicates
- **Tuples** → ordered, immutable, memory-efficient
- **Dicts** → key-value pairs, fast O(1) lookups
- **Sets** → unique elements, unordered, fast membership testing
- **Comprehensions** → clean, Pythonic way to build collections
- **Data Cleaning** → combine structures to filter and deduplicate real-world data

---

## Submitted By
Shrey Gamit