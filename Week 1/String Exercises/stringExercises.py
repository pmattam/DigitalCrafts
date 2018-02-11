# Given a string, print the string uppercased.
# Given a string, print the string capitalized.
inputString = raw_input("Enter a string ")

print inputString.upper()

print inputString.capitalize()

# Given a string, print the string reversed.
inputString = raw_input("Enter a string ")
reverse_string = ''
lengthOfStr = len(inputString)

while lengthOfStr:
    lengthOfStr -=1
    reverse_string += inputString[lengthOfStr]
print reverse_string