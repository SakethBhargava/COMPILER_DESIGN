def operators(operator):
    op = {'+', '-', '*', '/','(',')'}
    if operator in op:
        return True
    else:
        return False
operator = input("Enter an operator : ")
if operators(operator):
    print(f"The operator {operator} is valid.")
else:
    print(f"The operator {operator} is not valid. Please enter a valid operator.")
