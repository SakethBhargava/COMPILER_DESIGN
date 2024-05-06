import keyword as kw
import re
list = kw.kwlist
regex = '^[A-Za-z_][A-Za-z0-9_]*'
def operators(operator):
    op = {'+', '-', '*', '/','(',')','='}
    if operator in op:
        return True
    else:
        return False
inp = ("Enter a Keyword : ")
if(inp in list):
    print(inp,"is a keyword")
exp=(input("Enter an expression: "))
for element in exp:
    if(operators(element)):
         print(element,"is an operator")
    if(re.search(regex, element)): 
        print(element," is an Identifier")