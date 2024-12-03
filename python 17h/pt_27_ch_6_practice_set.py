"""Problem 1:
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
num4=int(input("Enter number 4:"))

if(num1>num2):
  f1=num1
else:
  f1=num2

if(num3>num4):
  f2=num3
else:
  f2=num4

if(f1>f2):
  print(str(f1)+" is greatest!")
else:
   print(str(f2)+" is greatest!")
"""   

"""Problem 2:
sub1=int(input("Enter first subject marks:"))
sub2=int(input("Enter second subject marks:"))
sub3=int(input("Enter third subject marks:"))
sub4=int(input("Enter fourth subject marks:"))
sub5=int(input("Enter fifth subject marks:"))

if sub1<33 or sub2<33 or sub3<33 or sub4<33 or sub5<33 :
    print("You are fail! because you have less than 33% percent in one or more than one subject..")
elif(sub1+sub2+sub3+sub4+sub5)/5 <40:
    print("You are fail! due to total percentage less than 40..")
else:
    print("Congratulations! You passed the exam..")
"""  

"""Problem 3:
text = input("Enter the text:\n")
spam =False

if("make a lot of money"in text):
  spam =True
elif("buy now"in text):
  spam=True
elif("click this"in text):
  spam=True
elif "subscribe this" in text :
  spam=True

if spam :
  print("This text is spam")
else:
  print("This text is not spam")
"""

"""Problem :4
a=input("Enter a String:")
# k=a.__len__()
# print(k)
if a.__len__() > 10:
  print("it contain more than 10 character")
else:
  print("it contain less than 11 character")  
"""

"""Problem :5
names=["harry","shubham","naqvi","rohit","rohan","aditi"]
name= input("Enter the name to check:\n")
if name in names:
  print("Your name is present in the list")
else:
  print("Your name is not present in the list")  
"""

"""Problem :6
marks =int(input("Enter your marks:"))
# if-elif-else ladder:
if marks>=90:
  grade="Ex"
elif marks>=80:
  grade="A" 
elif marks>=70:
  grade="B" 
elif marks>=60:
  grade="C" 
elif marks>=50:
  grade="D"
else:
  grade="F" 

print("Your grade is "+grade)  
"""

"""Problem :7"""
gossip= input("Enter the text:\n")
h=gossip.casefold()
if "harry" in h:
  print("Yes gossip is about harry")
else:
  print("Gossip is not about harry")  
