#no return no arguments
def palindrome():
    name=input("enter name:")
    revname=name[::-1]
    print("name=",name)
    print("reverse name=",revname)
    if(name==revname):
        print("yes") 
    else:
        print("no")
print(palindrome())

#no argument yes return
def palindrome():
    name=input("enter name:")
    revname=name[::-1]
    print("name=",name)
    print("reverse name=",revname)
    if(name==revname):
        return "yes"
    else:
        return "no"

print(palindrome())

#yes argument yes return
def palindrome(name):
    revname=name[::-1]
    print("name=",name)
    print("reverse name=",revname)
    if(name==revname):
        return "yes"
    else:
        return "no"
name=input("enter name:")
a=palindrome(name)
print(a)

#yes argument no return
def palindrome(name):
    revname=name[::-1]
    print("name=",name)
    print("reverse name=",revname)
    if(name==revname):
        print("yes its a palindrom")
    else:
        print("no its not a palindrome")
name=input("enter name:")
a=palindrome(name)
print(a)