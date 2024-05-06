import re
regex = '^[A-Za-z_][A-Za-z0-9_]*'
string=(input("Enter the string: ")) 
if(re.search(regex, string)): 
	print(string," is Valid Identifier") 
else: 
	print(string,"is Invalid Identifier") 
