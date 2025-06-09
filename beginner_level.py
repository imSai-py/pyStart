#while loop:

while True:
    response = input("say something: ")
    if response == "bye":
        print("Goodbye!")
        break

# finding duplicate without set:
some_list = ['a','b','b','c','d','d','e']
duplicates = []

for values in some_list:
    if some_list.count(values) > 1 and values not in duplicates:
        duplicates.append(values)
print("Duplicates found:", duplicates)

# finding duplicate with set:
some_list = ['a','b','b','c','d','d','e']

seen = set()
duplicates = set()

for value in some_list:
    if value in seen:
        duplicates.add(value)
    else:
        seen.add(value)
print("Duplicates found:", duplicates)