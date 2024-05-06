def count(filename):
    chars = 0
    spaces = 0
    tabs = 0
    lines = 0
    with open(filename, 'r') as file:
        for line in file:
            chars += len(line)
            spaces += line.count(' ')
            tabs += line.count('\t')
            lines += 1
    return chars, spaces, tabs, lines
filename = input("Enter file name: ")
try:
    char, space, tab, line = count(filename)
    print("Number of chars : ",char)
    print("Number of spaces : ",space)
    print("Number of tabs : ",tab)
    print("Number of lines : ",line)
except Exception as e:
    print("An error occurred : ",e)