#1:to find the modified string
user = input("Enter a string: ")
modified_char = []

for i, char in enumerate(user):
    if char.lower() in "aeiou":
        modified_char.append("*")
    else:
        modified_char.append(char)

modified_char = "".join(modified_char)

print('modified string: ', modified_char)

print('-'*50)

#2:to find the count of letters, digits and special characters
user = input("Enter a string: ")

letter_count = 0
digit_count = 0
special_count = 0

for i, char in enumerate(user):
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1

print('letter count: ', letter_count)
print('digit count: ', digit_count)
print('special count: ', special_count)

