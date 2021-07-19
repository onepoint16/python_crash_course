party = ["sam", "kathryn", "tony", "bailey"]

for people in party:
    print(people)

print("thank you for attending")


numbers = list(range(1,11))

print(numbers)

even_numbers = list(range(2,11,2))

print(even_numbers)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

print(min(squares))

print(max(squares))

print(sum(squares))

#squares in one line
squares1 = [value**2 for value in range(1,11)]
print(squares1, "Squares in 1 line of code")

for value in range(1,21):
    print(value)

one_million = list(range(1,1000001))
#for value in one_million:
#   print("number:", value)

print(min(one_million))

print(max(one_million))

print(sum(one_million))

odd_numbers = list(range(1,21,2))

print(odd_numbers)

threes = list(range(3,31,3))
print(threes)

cubes_1_liner = [value**3 for value in range(1,11)]

cubes = []
for value in range(1,11):
    cubes.append(value**3)
    print(cubes[-1])
print(cubes)


