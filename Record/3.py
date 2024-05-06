import keyword as kw
list = kw.kwlist
a = (input("Enter a keyword : "))
if a in list :
    print(a,"is a keyword")
else:
    print(a,"is not a keyword")