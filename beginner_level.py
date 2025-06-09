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

# first def function:(a concept used to avoid DRY - Don't Repeat Yourself) it provides code resusability
list =[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

def show_tree():
    for row in list:
        for pixels in row:
            if (pixels == 1):
                print('*', end='')
            else:
                print(' ', end='')
        print()
show_tree()
show_tree()
show_tree()
show_tree()

# def function with parameters:
def greetings(name, emoji):
    print(f'Hello {name}{emoji}')
# calling the function with parameters using arguments:
greetings('Sai', '😊')