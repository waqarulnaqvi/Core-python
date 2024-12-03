# In ram memory is volatile but in harddisk memory is non-volatile.
# File IO Basics
"""
"r"-Open fie for reading -default mode
"w"-Open a file for writing
"x"-Creates file if not exists
"a"-Add more content to a file
"t"-text mode -default mode
"b"-binary mode
"+"-read and write
"""
"Question of a day"
def fun(a,b):
    """I am a user define function"""
    print("The multiplication of this function is:")
    return a*b
print(fun(4,5))
print(fun.__doc__)
