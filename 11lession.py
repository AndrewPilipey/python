test = "Howdy Ho"
#Comment
#continue
print(test + " _________________________") #and also comment is here

my_var = str("First value of variable")
print(my_var)

def any_func():
    """Description function. This is able to a document"""
    print("ACTION OF THIS FUNC")
    print(any_func.__doc__)

any_func()

my_var = any_func

print(my_var)

print("_________________________________") #just_separator

my_var()