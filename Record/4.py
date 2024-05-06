text = input("Enter the text (press Enter then Ctrl+D to finish input):\n")
space_count = 0
line_count = 0
for char in text:
    if char == ' ':
        space_count += 1
    elif char == '\n':
        line_count += 1
print("Number of blank spaces:", space_count)
print("Number of lines:", line_count)
