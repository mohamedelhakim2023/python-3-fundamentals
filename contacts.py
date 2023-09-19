contacts = {
    "number": 4,
    "students": [
         {"name": "Sarah Holderness", "email": "sarahholdrness@gmail.com"},
         {"name": "Harry Potter", "email": "harrypotter@gmail.com"},
         {"name": "Hermione Granger", "email": "harrypotter@gmail.com"},
         {"name": "Ron Weasley", "email": "harrypotter@gmail.com"},
    ]
}
    
print("emails of students: ")

for student in contacts["students"]:
    print(student["email"])    