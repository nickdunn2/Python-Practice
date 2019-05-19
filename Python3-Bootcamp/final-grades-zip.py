midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['Dan', 'Angie', 'Kate']

# Using zip and dictionary comprehension, make a final_grades_zip dictionary that matches all of these up
# and returns the student's name as a key and their highest score for the value. { 'Dan': 98 }

final_grades_zip = {tup[0]: max(tup[1], tup[2])
                    for tup in zip(students, midterms, finals)}

print(final_grades_zip)

# Now accomplish the same thing without using dictionary comprehension, using only zip() and map() (with lambda)

final_grades_map = dict(
    zip(
        students,
        map(lambda p: max(p), zip(midterms, finals))
    )
)

print(final_grades_map)
