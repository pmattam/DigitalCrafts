####
def Beer(number):
    if number % 7 == 0 and number % 5 == 0:
        return 'Miller Lite'
    elif number % 7 == 0:
        return 'Miller'
    elif number % 5 == 0:
        return 'Lite beer'
    else:
        return "beer"

i = 99

while i > 0:
    print  "%d Bottles of %s, take one down, pass it around, %d bottles of %s, on the wall" % (i, Beer(i), (i-1), Beer(i))
    i -= 1
for i in range(1):
    print "no more beer on the wall!"

# Without using if & else
def Beer(number):
    return ((number % 7 == 0), (number % 5 == 0))

i = 99
type_of_beer = {
    (True, True): 'Miller Lite',
    (True, False): 'Miller',
    (False, True): 'Lite beer',
    (False, False): 'beer'
}
while i > 0:
    check = Beer(i)
    print "%d Bottles of %s, take one down, pass it around, %d bottles of %s, on the wall" % (i, type_of_beer[check], (i-1), type_of_beer[check])
    i -= 1

print "no more beer on the wall!"

