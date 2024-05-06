def check(exp):
    stack = []
    for char in exp:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return not stack
exp = input("Enter an expression : ")
if check(exp):
    print("The exp is correctly parenthesized.")
else:
    print("The exp is not correctly parenthesized.")