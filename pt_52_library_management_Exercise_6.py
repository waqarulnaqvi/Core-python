# Write a Library class with no_of_books and books as 2 variables.WAP to create a library from this library class and show how you can print
# all books, add a book and get the number of books using different methods. Show that your program doesn't persist the books after the program.
# 11 39
class Library:
    def __init__(self):
        self.l=["Rich dad poor Dad","lauch your life to the next level","Power of subconscious mind"]
        self.author=["Rober kiyo sakhi","Krishn Das","Bheema Mohan"]
        self.l1=["Rich dad poor Dad","lauch your life to the next level","Power of subconscious mind"]
        self.authorl1=["Rober kiyo sakhi","Krishn Das","Bheema Mohan"]
        self.count=0

    def add_books(self,bookname,authorname):
        qut =input("Enter book quantity:")
        i=1
        for i in range(1,int(qut)+1):
            self.l.append(bookname)
            self.author.append(authorname)
            self.authorl1.append(authorname)
            self.l1.append(bookname)

        print(f'\nThe book has been successfully added in the library!! Total quantity= {i}')
        print(f"Book name :\n {bookname}\n   -by {authorname}")
        self.display_book()

    def issue_book(self,bookname,authorname):
        index=0
        if len(self.l)==len(self.l1)-2:
            print("More than 2 book can't be issued!! returned the book first :)\n")
            return
        for book in self.l:
            athr=self.author[index]
            if  book==bookname and authorname==athr:
                self.count=1
                self.l.remove(book)
                self.author.remove(authorname)
                print(f'The book has been issued named: "{bookname}"   -by "{authorname}" in the library!!\n')
            index += 1
        if self.count==0:
            print(f'The book named: "{bookname}   -by "{authorname}" is not available in the library!!\n')
        self.display_book()

    def display_book(self):
        print("Available books:")
        index=0
        for i in self.l:
            print(f"{index+1}) {i}")
            print("   -by",self.author[index],end="\n\n")
            index += 1
        print()
        #
        # print("Available books:")
        # index=0
        # for i in self.l1:
        #     print(f"{index+1}) {i}")
        #     print("   -by",self.authorl1[index],end="\n\n")
        #     index += 1
        # print()

    def return_book(self):
        # print(len(self.l))
        if self.l==self.l1:
            print("No book has been issued from the library!!\n")
        else:
            self.l = self.l1
            self.author = self.authorl1
            print(f"The book has been returned successfully in the library!!\n")
            self.display_book()

    def usermenu(self):
        while True:
            x = int(input(
                "Enter 1 for add book\nEnter 2 for issue book\nEnter 3 for return book\nEnter 4 for available book\nEnter Any other key to exit the loop:\n"))
            match x:
                case 2:
                    self.display_book()
                    inp=input("Enter the book name:")
                    athr=input("Enter the book authorname:")
                    self.issue_book(bookname=inp,authorname=athr)
                case 4:
                    self.display_book()
                case 3:
                    self.return_book()
                case 1:
                    inp = input("Enter the book name:")
                    athr=input("Enter author name:")
                    self.add_books(inp,athr)
                case _:
                    print("Thanks for visiting the Waqarul's Library!!\n")
                    exit()
lib=Library()
lib.usermenu()




