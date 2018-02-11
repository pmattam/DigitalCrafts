import random
my_random_number = random.randint(1, 10)
print my_random_number
guessed = False
guess_counter = 0
print "I am thinking of a number between 1 and 10"
while not guessed and guess_counter < 5:
    print "You have %d guesses left." % (5 - guess_counter)
    guess_number = int(raw_input("What's the number? "))
    if guess_number > my_random_number:
        print '%d is too high.' % guess_number
    elif guess_number < my_random_number:
        print '%d is too low.' % guess_number
    else:
        print 'Yes! You win!'
        guessed = True # or break
    if guessed or guess_counter is 4:
        play_again = raw_input("Do you want to play again (Y or N)? ").upper()
        if play_again == 'Y' or play_again == 'YES':
            guessed = False
            guess_counter = 0
            continue
    guess_counter += 1