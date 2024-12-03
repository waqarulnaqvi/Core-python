def increment(num):
    try:
        return int(num) + 1
    except :
        # print("This is not good - Waqarul")
        raise ValueError("This is not good - Waqarul")
        # raise SyntaxError("This is not good - Waqarul")
        # raise SyntaxWarning("This is not good - Waqarul")
        # print("This is not good - Waqarul")

a=increment('34hjkh3')
# a=increment('343')
print(a)