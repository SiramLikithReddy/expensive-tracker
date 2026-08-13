# Contact Book Manager (CLI)
class Contacts:
    def __init__(self, username, firstname, lastname):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    def dial(self):
        try:
            number = int(input("Enter your number: "))
            print(f"Number : {number}")
            return number
        except ValueError:
            print("check your datatype")
            return None

    def save(self):
        items = ["First name", "Last Name", "Username", "Email", "Address"]
        connections = {}
        for item in items:
            connections[item] = input(f"{item} :")
        return connections


A = Contacts("Amma", "Kachana", "Renuka")
A.dial()

for key, value in A.save().items():
    print(f"{key} : {value}")

with open("contactbook.py", "a") as file:
    file.write(f"contact {A.username} saved!!\n")