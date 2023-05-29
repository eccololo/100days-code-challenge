import random

names = ["Beth", "Alessio", "Matteo", "Johanna", "Mel", "Pam"]

students_score = {key: random.randint(1, 100) for key in names}
passed_students = {name: value for (name, value) in students_score.items() if value > 70}
print(passed_students)
