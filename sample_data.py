
import random

def random_name():
    first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie", "Mike", "Laura", "David", "Sophia"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Wilson", "Moore"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def random_address():
    streets = ["Main St", "Highland Ave", "Maple Dr", "Oak St", "Pine Ln", "Cedar Ct", "Elm St", "Washington Ave"]
    cities = ["Springfield", "Riverside", "Franklin", "Greenville", "Bristol", "Clinton", "Fairview", "Salem"]
    return f"{random.randint(100,999)} {random.choice(streets)}, {random.choice(cities)}, USA"

def random_phone():
    return f"+1-{random.randint(200,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}"

def random_email(name):
    domains = ["gmail.com", "yahoo.com", "outlook.com", "school.edu"]
    username = name.lower().replace(" ", ".")
    return f"{username}@{random.choice(domains)}"

def random_grade():
    return random.choice(["A", "B", "C", "D", "E", "F"])

def generate_student_records(num_students=40):
    student_records = []
    for i in range(1, num_students + 1):
        name = random_name()
        student = {
            "student_id": f"S{i:03d}",
            "student_name": name,
            "age": random.randint(14, 22),
            "grade": random_grade(),
            "address": random_address(),
            "phone_number": random_phone(),
            "email": random_email(name)
        }
        student_records.append(student)
    return student_records