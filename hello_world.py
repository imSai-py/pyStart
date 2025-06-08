user = input("Enter a string: ")
modified_char = []

for i, char in enumerate(user):
    if char.lower() in "aeiou":
        modified_char.append("*")
    else:
        modified_char.append(char)

modified_char = "".join(modified_char)

print('modified string: ', modified_char)
