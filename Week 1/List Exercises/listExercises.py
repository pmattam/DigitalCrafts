### ###
# Sum the Numbers
givenNum = [1, 3, 4, 5, 6]
result = 0
for num in givenNum:
    result = result + num # result += num
print result

# different solution
print sum(givenNum) 

### ###
# Largest Number
givenNum = [1, 5, 10, 100, 3, 2]
print max(givenNum)

# different solution
numbers = [1, 5, 10, 100, 3, 2]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print largest

### ###
# Smallest Number
givenNum = [1, 5, 10, 100, 3, 2, -2, -1]
print min(givenNum)

# different solution
numbers = [1, 5, 10, 100, 3, 2]
smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print smallest

### ###
# Even Numbers
givenList = [1, 3, 2, 4, 5, 6, 7, 4, 3, 8, 10, 12]
even = []
for num in givenList:
    if (num % 2 == 0):
        even.append (num)
print even

### ###
# Positive Numbers
givenNum = [1, 3, 4, -1, -3, -10, 0]
for num in givenNum:
    if (num > 0):
        print num

### ###
# Positive Numbers II
givenNum = [-1, -3, -10, 1, 3, 4, 0]
new_num_list = []

for num in givenNum:
    if (num > 0):
        new_num_list.append(num)
print new_num_list

### ###
# Multiply a list
givenList = [1, 5, 100, -4, 1000, 2]
factNum = int(raw_input('Enter a number: '))
newList = []
for num in givenList:
    newList.append(num * factNum)
print newList

### ###
# Multiply Vectors
firstList = [2, 4, 5]
secondList = [2, 3, 6]
resultList = []
if (len(firstList) == len(secondList)):
    for i in range(0, len(firstList)):
        resultList.append(firstList[i] * secondList[i])
print resultList

# different logic
vector1 = [4, -7, -10, 5]
vector2 =[2, 3, -3, -5]
multiplied = []

for i in range(len(vector1)):
    print i
    multiplied.append(vector1[i] * vector2[i])

print multiplied
