students = {"student1" : {"first name" : "Joe", "Surname" : "Doe", "Level_one" : "Merit", "Year" : 12, "subjects" : ["math, science, english "] },
            "student2" : {"first name" : "Sky", "Surname" : "Pistoll", "level_one" : "n/a","Year" : 13,"subjects" : ["math", "ge"]}
}

print(f"{students["student1"]['first name']} {students["student1"]['Surname']} is studying:")
for subject in students["student1"]["subjects"]:
    print(subject)

