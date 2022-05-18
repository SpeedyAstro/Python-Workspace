
class library:
    book = ["Microprocessor","Data Structure in Java", "Python OOPS","Python Automations","Alan Tuning Theory","Theory of Computation"]
    dict = {}
    def __init__(self,pname,pbranch,proll_no) -> None:
        self.name = pname
        self.branch = pbranch
        self.roll_no = proll_no
        # self.listofbooks = listbo
    @classmethod
    def displayBooks(cls):
        for books in library.book:
            print(books)
    @staticmethod
    def booklended():
        return library.dict
    @staticmethod
    def studentadded():
        return "student has been added sucessfully"
    
    def lendbook(self,lbook):
        if lbook not in library.dict:
            library.dict.update({lbook:self.name})
            return "Book has been added to your account"
        else :
            return f"Book is already lended by {library.dict[lbook]}"
    @staticmethod
    def addbook(addbook):
        library.book.append(addbook)
        return "book has been added!"

    def returnBook(self,lbook):
        library.dict.pop(lbook)
    # @classmethod
    # def student(cls,string):
    #     data = string.split("-")
    #     return cls(data[0],data[1],data[2])
        # return cls(*string.split("-"))


# while True :
#     pass 
if __name__ == '__main__':
    name = input("Enter your name :\n")
    branch = input("Enter branch\n")
    rollno = input("enter roll no\n")
    stu = library(name,branch,rollno)

    while(True):
        print(f"Welcome to the {stu.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            stu.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            stu.lendbook(book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            stu.addbook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            stu.returnBook(book)

        else:
            print("Not a valid option")


        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue