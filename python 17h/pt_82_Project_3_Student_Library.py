"""Project 3 - Student Library
Implement a student library system using oops where students can borrow a book from the list of books.
Create a separate library and Student class. Your program must be menu driven. you are free to choose methods and attributes of your choice to implement the functionality..
"""
class Admin_Login:
    def __init__(self,books):
        self.books = books
        self.k=None
        self.k1=None
        self.rb=[]#without this error occured..
        self.rb.extend(books)
        # self.rb.insert(0,self.books)
        # self.rb.append(books)
  
    def insert_book(self,book_name,author_name):
           self.books.insert(self.books.__len__(),book_name)
           self.books.insert(self.books.__len__(),("\t-"+author_name+"\n"))     
           self.rb.insert(self.rb.__len__(),book_name)     
           self.rb.insert(self.rb.__len__(),("\t-"+author_name+"\n"))    
           print("BOOK HAS BEEN INSERTED SUCCESSFULLY!!") 
           self.Available_books()       
             
        
    def issue_book(self): 
        self.Available_books()   
        if self.rb.__len__()-4 == self.books.__len__():    
            print("More than 2 books cannot be issued!")
            print("Please return books!\n")
            return  
        book_name=input("Enter book name:")
        book_name=book_name.capitalize()
        for i in range(self.books.__len__()):
            if self.k==self.books[i] and self.k1 ==self.books[i+1]:
                j=i
                while j<self.books.__len__():
                    if self.k==self.books[j] and self.k1 !=self.books[j+1]:
                     self.books.pop(j)
                     self.books.pop(j)
                     print("Has been issued successfully!\n")
                     return
                    j=j+1                       
                print("Same book can be issued twice!\n")
                return
            if(book_name==self.books[i]):
                print(self.books[i]+"\n"+self.books[i+1])
                self.k=self.books.pop(i)
                self.k1=self.books.pop(i)
                print("Has been issued successfully!\n")
                break
        else:
            print("Book does not exist!\n")  
               

    def return_book(self):
        if(self.books.__len__()==self.rb.__len__()):
           print("NO Book has been issued!\n")
        else:
            self.books=[]
            # self.books.insert(0,self.rb)
            # self.books.append(self.rb)#for inserting in a list we use append funtion..
            self.books.extend(self.rb)
            print("Book has been returned successfully!")
            self.Available_books()   

    def Available_books(self):
        print("\nAvailable books are:")
        # Method:1
        # for i in range(self.books.__len__()):
        #     print(self.books[i])
        # Method:2
        for i in self.books:
            print(i) 
        """(YOU CAN ALSO USE ENUMERATE FUNCTION TO PRINT THE INDEX OF THE BOOK IT'S UPTO YOU):
        for index,item in enumerate(list1):
                print(index,item)
        """
            

    def remove_books_from_library(self):
        self.Available_books()
        book_name=input("Enter book name:")
        an=input("Enter author name:")
        book_name=book_name.capitalize()
        an=an.capitalize()
        for i in range(self.books.__len__()):
            if(book_name==self.books[i] and "\t-"+an+"\n"==self.books[i+1]):
                print(self.books[i]+"\n"+self.books[i+1])
                self.books.pop(i)
                self.books.pop(i)
                self.rb.pop(i)
                self.rb.pop(i)
                print("Has been removed from the library successfully!\n") 
                return         
        else:
             print("\nBook does not exists in the library!\n")
             
             
class Student_Login(Admin_Login):
    def __init__(self,books):
        super().__init__(books)
        
    def display(self):
                print("\nSTUDENT LOGIN:")
                lib=True
                while(lib):
                    # Method:1
                    inp=int(input('''1)Insert booK
2)Issue_book
3)Return book
4)Show available books
ENTER ANY KEY TO BREAK FROM THE LOOP..\n'''))
                    # Method:2
                    # inp=int(input("1)Insert booK\n2)Issue_book\n3)Return book\n4)Show available books\n5)Remove book from the library\nENTER ANY KEY TO BREAK FROM THE LOOP..\n"))
                    if inp==1:
                        bn=input("Enter book name:")
                        an=input("Enter author name:")
                        self.insert_book(bn.capitalize(),an.capitalize())
                    elif inp==2:
                        self.issue_book()
                    elif inp==3:
                        self.return_book()
                    elif inp==4:
                        self.Available_books()             
                    else:
                        lib=False
        
             
Available_books=["Harry potter","\t-Pankaj\n","Chandrawati","\t-Kabir daas\n","Bharamastra","\t-Soor daas\n"]        
# st=Admin_Login(Available_books)     
st=Student_Login(Available_books)   
print("****************WELCOME TO WAQARUL'S LIBRARY!****************")

while True:
    who=input("""\nLOGIN:
1)Student
2)Teacher/admin
Press Any key to exit from the loop..
""")    
    if who=="1":
         st.display()
                
    elif who=="2":
        print("\nADMIN/TEACHER LOGIN:")
        lib=True
        while(lib):
            # Method:1
            inp=int(input('''1)Insert booK
2)Issue_book
3)Return book
4)Show available books
5)Remove book from the library
ENTER ANY KEY TO BREAK FROM THE LOOP..\n'''))
            # Method:2
            # inp=int(input("1)Insert booK\n2)Issue_book\n3)Return book\n4)Show available books\n5)Remove book from the library\nENTER ANY KEY TO BREAK FROM THE LOOP..\n"))
            if inp==1:
                bn=input("Enter book name:")
                an=input("Enter author name:")
                st.insert_book(bn.capitalize(),an.capitalize())
            elif inp==2:
                st.issue_book()
            elif inp==3:
                st.return_book()
            elif inp==4:
                st.Available_books()       
            elif inp==5:
                st.remove_books_from_library()       
            else:
                lib=False
                           
    else:
        print("Thanks for visting us :)") 
        exit()
    