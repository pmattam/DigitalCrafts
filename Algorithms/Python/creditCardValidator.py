# Write a Python program to validate a credit card number:
# It must have 16 digits, unless it starts with 37 or 34. Then, and only then, it MUST have 15 digits
# It must start with one of the following. Print off "valid" and the type of card
# 6011 = Discover Card
# 37 or 34 = American Express
# 4 = Visa
# 50-55 = MasterCard

def creditCardValidator(givenStr):
    if givenStr.isdigit() and len(givenStr) == 16:
        if givenStr.startswith("4"):
            return "valid - Visa"
        if givenStr.startswith("6011"):
            return "valid - Discover Card"
        if 50<=int(givenStr[0:2])<=55:
            return "valid - MasterCard"
        return "invalid"
    elif givenStr.isdigit() and len(givenStr) == 15:
        if givenStr.startswith("37") or givenStr.startswith("34"):
            return "valid - American Express" 
        return "invalid"
    else:
        return "invalid" 
        
assert creditCardValidator("4123456789234567") == "valid - Visa", "Test failed"
assert creditCardValidator("372345678923456") == "valid - American Express", "Test failed"
assert creditCardValidator("342345678923456") == "valid - American Express", "Test failed"
assert creditCardValidator("6011456789234567") == "valid - Discover Card", "Test failed"
assert creditCardValidator("5011456789234567") == "valid - MasterCard", "Test failed"
assert creditCardValidator("5111456789234567") == "valid - MasterCard", "Test failed"
assert creditCardValidator("5211456789234567") == "valid - MasterCard", "Test failed"
assert creditCardValidator("5311456789234567") == "valid - MasterCard", "Test failed"
assert creditCardValidator("5411456789234567") == "valid - MasterCard", "Test failed"
assert creditCardValidator("5511456789234567") == "valid - MasterCard", "Test failed"
assert creditCardValidator("4356") == "invalid", "Test failed"
assert creditCardValidator("36234567892345") == "invalid", "Test failed"
assert creditCardValidator("ABCDEFGHIJKLMNOP") == "invalid", "Test with string failed"
assert creditCardValidator("4123456789234XYZ") == "invalid", "Test with partial string failed"
assert creditCardValidator("5611456789234567") == "invalid", "Test failed"
