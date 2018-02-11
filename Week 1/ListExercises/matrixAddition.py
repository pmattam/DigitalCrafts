# Matrix Addition
first_matrix_list = [[1, 3], [2, 4]]
second_matrix_list = [[5, 2], [1, 0]]
result_matrix_list = []

for listIndex in range(0, len(first_matrix_list)):
    sub_list = []
    for sublistIndex in range(0, len(first_matrix_list[listIndex])):
         sub_list.append(first_matrix_list[listIndex][sublistIndex] + second_matrix_list[listIndex][sublistIndex])
    result_matrix_list.append(sub_list)
print result_matrix_list

# different logic
matrix1 = [
    [2, -2],
    [5, 3]
]
matrix2 = [
    [5, 2],
    [1, 0]
]

height = len(matrix1)
width = len(matrix1[0])

result = []
for i in range(height):
    result.append([])
    for j in  range(0, width):
        cell1 = matrix1[i][j]
        cell2 = matrix2[i][j]

        cell = cell1 + cell2
        result[i].append(cell)
print result

# different logic
matrix1 = [
    [2, -2],
    [5, 3]
]
matrix2 = [
    [5, 2],
    [1, 0]
]

height = len(matrix1)
width = len(matrix1[0])

for i in range(0, height):
    result.append([])
    for j in range(0, width):
        result[i].append(None)
# result = [
#     [None, None], 
#     [None, None]]
for i in range(0, height):
   
    for j in  range(0, width):
        cell1 = matrix1[i][j]
        cell2 = matrix2[i][j]

        result[i][j] = cell1 + cell2
        
        
print result

# Matrix Addition II
firstMatrix = [[1, 1, 2, 3], [4, 5, 6], [7, 8, 9]]
secondMatrix = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
resultList = []
matrixList = len(firstMatrix)
matrixSublist = len(firstMatrix[0])
lengthMatched = True

if len(firstMatrix) == len(secondMatrix):
    for k in range(len(firstMatrix)):
        if len(firstMatrix[k]) != len(secondMatrix[k]):
            lengthMatched = False
else:
    lengthMatched = False  
        
if lengthMatched:
    for i in range(matrixList):
        subList = []
        for j in range(matrixSublist):
            subList.append(firstMatrix[i][j] + secondMatrix[i][j])
        resultList.append(subList)
else:
    print "Matrix are not of same size"
    
print resultList