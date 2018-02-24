# Write a function caseConvert that accepts two arguments. The first is a string, the second is type. 
# If the type is "camelcase" then convert the string to 
# camelcase (each word except the first is capitalized, no spaces). 
# If type is "snakecase" then convert the string to 
# snakecase (each word is separated by a _ and all lowercase). 
# As a bonus, accept a string or an array. If it's an array, use .join and proceed accordingly.

# def caseConvert(str, conversionType):

#  //Your code here!!

#  return convertedStr


def caseConverter(stringVal, conversionType):

    # If the value passed to stringVal is a list of strings
    if type(stringVal) == list:
        stringVal = ' '.join(stringVal)

    if type(stringVal) != str or stringVal.isdigit():
        return "It is a not a string value"

    if stringVal == "" or conversionType == "":
        return "Either user given string or case or both empty"

    stringVal = stringVal.lower()
    conversionType = conversionType.lower()

    stringlist = []
    stringlist = stringVal.split()
    convertedStr = ""        

    if (conversionType == "camelcase") and (stringlist):
        for i, word in enumerate(stringlist):
            if i == 0:
                convertedStr = word
            else:
                convertedStr = convertedStr + word.capitalize()
    elif (conversionType == "snakecase") and (stringlist):
        for i, word in enumerate(stringlist):
            if i == 0:
                convertedStr = word
            else:
                convertedStr = convertedStr + "_" + word

    return convertedStr

# stringInput = raw_input("Enter the string ")

# convertType = raw_input("Enter camelcase or snakecase ")

# print caseConverter(stringInput, convertType)

# print caseConverter(["AwesOMe", "CodiNg"], "camelcase")
