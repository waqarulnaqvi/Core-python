# l=10 #Global variable /global scope.
# def func1(n):
#    # l=5 #local variable/local scope.
#    global l
#    l=l+45
#    print(l,n,"i am printed")
#    print("value of l is",l)
#
# func1("this is me")
# print(l)
# nested function:
'''
# small quiz :
# x=89# agar x ki value 89 kardoge top me to loop ke baad x ki value kya print hogi.
#Answer:88
'''
def waqarul():
   x=20
   def harry():
      global x #global variable jo hota hai wo sidhe pointer(cursor) ko bhar le jata hai top pe ekdum.
      x=88
   print("before calling harry()",x)
   harry()#calling harry function.
   print("after calling harry()",x) #line 15 ke reason ki wajhe se x ki value 88 ni hui 20 hi rahi.
waqarul()
print("the value of x is :",x)

print(__doc__)