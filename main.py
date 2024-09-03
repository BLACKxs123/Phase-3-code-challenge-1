#Function: add_numbers
def add_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 + num2

print("Sum:", add_numbers())

# Function: is_even
def is_even():
    number = int(input("Enter a number: "))
    return number % 2 == 0

print("Is Even:", is_even())

#Function: reverse_string
def reverse_string():
    text = input("Enter a string: ")
    return text[::-1]

print("Reversed String:", reverse_string())

#Function: count_vowels 
def count_vowels():
    text = input("Enter a string: ").lower()
    return sum(1 for char in text if char in 'aeiou')

print("Vowel Count:", count_vowels())

#Function: calculate_factorial
def calculate_factorial():
    n = int(input("Enter a number: "))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print("Factorial:", calculate_factorial())

#Function: apply_decorator
def decorator_func(func):
    def wrapper():
        print("Decorator Applied")
        func()
    return wrapper

@decorator_func
def apply_decorator():
    message = input("Enter a message: ")
    print("Message:", message)

apply_decorator()

#Sequences: Sort List of Tuples
def sort_by_age():
    people = [(input("Enter name: "), int(input("Enter age: "))) for _ in range(int(input("How many people? ")))]
    return sorted(people, key=lambda x: x[1])

print("Sorted by age:", sort_by_age())

#Sets and Dictionaries: Merge Dictionaries
def merge_dicts():
    dict1 = {input("Enter key for dict1: "): int(input("Enter value for dict1: ")) for _ in range(int(input("How many items in dict1? ")))}
    dict2 = {input("Enter key for dict2: "): int(input("Enter value for dict2: ")) for _ in range(int(input("How many items in dict2? ")))}
    
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = merged.get(key, 0) + value
    return merged

print("Merged Dictionary:", merge_dicts())

#Object-Oriented Programming: Class Creation 
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")

def create_car():
    car = Car(input("Enter car make: "), input("Enter car model: "), input("Enter car year: "))
    car.display_info()

create_car()

