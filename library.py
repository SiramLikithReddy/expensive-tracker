class Library:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def members(self):
        print(f"{self.name} : {self.email}")

    def work(self):
        self.books = {
            "A_author": {
                "Ao01": 1,
                "Ao02": 4,
                "Ao03": 5
            },
            "B_author": {
                "Bo01": 4,
                "Bo02": 5,
                "Bo03": 6
            },
            "C_author": {
                "Co01": 6,
                "Co02": 7,
                "Co03": 8
            }
        }
        return self.books

    def list_items(self):
        data = self.work()
        for author, availables in data.items():
            for title, copies in availables.items():
                print(f"{author} : {title} : {copies}")
        print("These are the list of the books that are in our library with their copies at last")

    def borrow(self):
        data = self.work()
        head = input("Enter the author name: ")
        body = input("Enter the title name: ")
        found = False
        for author, availables in data.items():
            for title, copies in availables.items():
                if head == author and body == title:
                    found = True
                    if copies > 0:
                        self.books[author][title] = copies - 1
                        print(f"✅ Book available and ready to deliver and we still have {self.books[author][title]} copies left")
                        print("Hope u get that book")
                    else:
                        print("❌ The book you need is, out of stock")
                        print("visit again!!")
        if not found:
            print("❌ Book unavailable")

    def add_book(self, author, title, copies):
        data = self.work()
        data[author] = {title: copies}
        print(f"Added book of title {title} with {copies} copies")

    def return_item(self, label, Emessage):
        print("For security issues please type your name(label) and e-message(email), type same as in your members list")
        data = self.work()
        head = input("Enter author name for returning:")
        body = input("Enter title name for returning: ")
        found = False
        for author, f in data.items():
            for title, copies in f.items():
                if head == author and body == title:
                    if label == self.name and Emessage == self.email:
                        found = True
                        print("User, book is matched and return accepted")
                    else:
                        print("Book doesn't match")
        if not found:
            print("User doesn't match")
        print("Hope you have a fine day")


lb = Library("Likith", "Likith@gmail.com")
lb.members()
lb.list_items()
lb.borrow()
lb.add_book("D_author", "Doo1", 4)
lb.return_item("Likith", "Likith@gmail.com")
with open("library.py","w") as file:
	write("Keep books atmost safely\n")