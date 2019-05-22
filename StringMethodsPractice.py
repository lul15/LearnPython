verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
length_of_verse = len(verse)
print(length_of_verse)

first_occurrence = verse.find("and")
print(first_occurrence)

last_occurrence = verse.rfind("you")
print(last_occurrence)

number_of_occurrences = verse.count("you")
print(number_of_occurrences)
