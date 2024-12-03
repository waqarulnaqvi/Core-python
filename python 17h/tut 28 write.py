# # f=open("tut 28.txt","w")#write mode.(write mode ka ,matlab jo bhi file me hai usko saaf kar do or jo ab likha ja raha usko rakho.)
# a=f.write("Waqarul ka naam azaan bhi hai \n")#f.write function return karta hai number of character.
# print(a)
# f.close() #All the tide up file resources will be free.
# #this closes all the  file resources and it is a good practise.

f=open("tut 28.txt","a")#append mode (append ka matlab jor dena.)
a=f.write("Waqarul ka naam azaan bhi hai \n")#f.write function return karta hai number of character.
print(a)
f.close() #All the tide up file resources will be free.
#this closes all the  file resources and it is a good practise.

#Handle read and write both
# f=open("tut 28.txt","r+")
# print(f.read())
# f.write("Thank you \n")
# f.close()