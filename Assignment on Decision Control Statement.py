# Problem :1
# i=input("Enter a value:")
# if i.isupper():
#     print("It is in uppercase")
# elif i.islower():
#     print("It is in lowercase")
# elif i.isspace():
#     print("It is a space")
# elif i.isdigit():
#     print("It is a digit")
# elif i.isalnum():
#     print("It is an alpha numberic")

# Problem 2:
# while True:
#     str =  input("Enter a string \"Quit\" to exit from the loop:").lower()
#     print(f"The length of the string is {len(str)}")
#     if str=="quit":
#         print("Quiting the loop..")
#         break

# Problem 3:
# sum=avg=count=even=odd=aev=aod=0
# while True:
#     inp=int(input("(-1 to exit from the loop)Enter a number:"))
#     if inp==-1:
#         print(f"Total count of number is {count}\nAverage of  even number is {even/aev}\nAverage of  odd number is {odd/aod}\nTotal sum of the number is {sum}\nTotal average of the number is {avg/count}")
#         break
#     count += 1
#     if inp%2==0:
#         even+=inp
#         aev+=1
#     elif inp%2!=0:
#         odd+=inp
#         aod+=1
#     avg=(even+odd)/count
#     sum=even+odd

# Problem 4:
# inp=float(input("Enter a number"))
# if inp>4.14:
#     print("The number is :",inp+10)
# else:
#     print("The number is :",inp)

# Problem :5
# class Eligib:
#     def percentage(self,coarse):
#         print("\nEnter {} marks ".format(coarse))
#         sum=0
#         for i in range(5):
#             sum+=int(input("Enter marks of your subject {} :".format(i+1)))
#         print("Percentage in {} class is :",sum/5)
#         return sum/5
#
#     def Eligible(self):
#         tenth=self.percentage("1oth")
#         inter=self.percentage("12th")
#         ug=self.percentage("ug")
#         run=True
#         while (run):
#             str = input("\nDid you change the stream to arts and Commerse\nEnter yes for y and no for n:")
#             if str == "y":
#                 ug = ug - 5
#                 run = False
#             elif str == "n":
#                 run = False
#             else:
#                 print("Enter correct option")
#
#
#         if tenth>=80 and inter>=80 and ug>=70:
#             print("You are Eligible for pg coarse!!")
#         else:
#             print("You are not Eligible for pg coarse!!")
#
# e=Eligib()
# e.Eligible()

# Problem:6
# class Electricitybill:
#     def monthlyconsumption(self):
#         unit=int(input("Enter your unit that is shown on your meter :"))
#         if unit>=0 and unit<=150:
#             print(f"Electricity bill is : {unit*3}Rs. ")
#         elif unit>150 and unit<=350:
#             self.bill=(unit-150)*3.75 +(150*3)
#             print(f"Electricity bill is : {self.bill}Rs. ")
#         elif unit > 350 and unit <= 450:
#             self.bill=(unit-350)*4+(150*3)+(200*3.75)
#             print(f"Electricity bill is : {self.bill}Rs. ")
#         elif unit >450 and unit <=600:
#             self.bill=(unit-450)*4.25+(100*4)+(150*3)+(200*3.75)
#             print(f"Electricity bill is : {self.bill}Rs. ")
#         else:
#             self.bill=(unit-600)*5+(150*4.25)+(100*4)+(150*3)+(200*3.75)
#             print(f"Electricity bill is : {self.bill}Rs. ")
#
# ebill=Electricitybill()
# ebill.monthlyconsumption()





