def count(inp):
    letters = 0
    digits = 0
    spaces = 0
    others = 0
    for char in inp:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            others += 1
    return letters, digits, spaces, others
inp = input("Enter a string: ")
letter, digit, space, other = count(inp)
print("Letters:", letter)
print("Digits:", digit)
print("White spaces:", space)
print("Other characters:", other)