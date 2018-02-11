leetspeak = {
    'A' : '4', 
    'E' : '3',
    'G' : '6',
    'I' : '1',
    'O' : '0',
    'S' : '5',
    'T' : '7'
}

text = raw_input("Enter a Text ?")
updatedText = ''
upperText = text.upper()

for letter in upperText:
    if (letter in leetspeak):
        updatedText += leetspeak[letter]
    else:
        updatedText += letter
print updatedText

# different solution
text = raw_input("Enter a Text ?")
updatedText = ''
upperText = text.upper()
updatedText = upperText.replace('A', '4')
updatedText = updatedText.replace('E', '3')
updatedText = updatedText.replace('G', '6')
updatedText = updatedText.replace('I', '1')
updatedText = updatedText.replace('O', '0')
updatedText = updatedText.replace('S', '5')
updatedText = updatedText.replace('T', '7')
print updatedText

# different solution
text = "hello world"
letters_to_convert = ['A', 'E', 'G', 'I', 'O', 'S', 'T']
numbers = [ 4,   3,   6,   1,   0,   5,   7]

translation = ""

uppercased_text = text.upper()
for letter in uppercased_text:
  print "the letter is ", letter
  # print "the index is ", letters_to_convert.index(letter)
  counter = 0
  letter_to_add_to_translation = ""
  for letter_to_convert in letters_to_convert:
    # print "looking at ", letter_to_convert
    if letter == letter_to_convert:
      print "\n********** found it! %s \n\n" % letter
      print "want to replace with %s" % numbers[counter]
      # translation = translation + str(numbers[counter])
      letter_to_add_to_translation = str(numbers[counter])
      break # break out of loop after finding good replacement
      # otherwise, you overwrite with the original letter
    else:
      print "just use", letter 
      # translation = translation + letter
      letter_to_add_to_translation = letter
    
    counter = counter + 1
  translation = translation + letter_to_add_to_translation
  print translation