
subjects = ["Physics", "Calculus", "Poetry", "History"]

grades = [98, 97, 85, 88]

subjects.append("Computer science")
grades.append(100)

gradebook = list(zip(subjects, grades))

subjects.append("Visual Arts")
grades.append(93)

gradebook.append(("Visual Arts", 93))

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

full_gradebook = gradebook + last_semester_gradebook

print(full_gradebook)