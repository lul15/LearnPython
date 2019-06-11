# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai':12.5}
print(population)


a = [1,2,3]
b = a
c = [1,2,3]

print(a == b) #equality - True
print(a is b) #identity - True
print(a == c) #equality - True
print(a is c) #identity - False: points to different objects
