cipherCode = {
    'a' : 'b',
    'b' : 'c',
    'c' : 'd',
    'd' : 'e',
    'e' : 'f',
    'f' : 'g',
    'g' : 'h',
    'h' : 'i',
    'i' : 'j',
    'j' : 'k',
    'k' : 'l',
    'l' : 'm',
    'm' : 'n',
    'n' : 'o',
    'o' : 'p',
    'p' : 'q',
    'q' : 'r',
    'r' : 's',
    's' : 't',
    't' : 'u',
    'u' : 'v',
    'v' : 'w',
    'w' : 'x',
    'x' : 'y',
    'y' : 'z',
    'z' : 'a',
    ' ' : ' '
}
inputStr = "lbh zhfg hayrnea jung lbh unir yrnearq"
updatedStr = ""

for letter in inputStr:
    updatedStr += cipherCode[letter]

print updatedStr

#different solution
inputStr = "lbh zhfg hayrnea jung lbh unir yrnearq"
shift = 2
resultStr = ""

for letter in inputStr:
    if letter.isalpha():
       ordValAfterShift = ord(letter) + shift
       if (ordValAfterShift > 122):
           ordValAfterShift = ordValAfterShift - 123 + 97
       resultStr += chr(ordValAfterShift)
    else:
        resultStr += letter
print(resultStr)