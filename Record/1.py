print("The grammar is as follows:\nS -> aS\nS -> Sb\nS -> ab\n")
str = input("Enter a string: ")
if not str.startswith('a') or 'aaa' in str or 'bb' in str:
    print("String doesnot belongs to the grammar")
else:
    print("String exists")