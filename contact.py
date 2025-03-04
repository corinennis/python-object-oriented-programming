from typing import List

class Contact:
    all_contacts: List["Contact"] = []

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
    
    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r})"
        )

class Supplier(Contact):
    def order(self, order: "Order") -> None:
        print(
            "If this were a real system we would send "
            f"'{order}' order to '{self.name}'"
        )

class ContactWithSelf:
    all_contacts: List["Contact"] = []

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.all_contacts.append(self)
    
    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r})"
        )

class SupplierWithSelf(ContactWithSelf):
    def order(self, order: "Order") -> None:
        print(
            "If this were a real system we would send "
            f"'{order}' order to '{self.name}'"
        )

class Order:
    pass

def main():
    c_1 = Contact("first", "first@example.com")
    c_2 = Contact("second", "second@example.com")
    c_3 = Contact("third", "third@example.com")
    s_1 = Supplier("fourth", "fourth@example.com")
    print("Contact.all_contacts:", Contact.all_contacts)
    print("Supplier.all_contacts:", Supplier.all_contacts)

    c_with_self_1 = ContactWithSelf("first", "first@example.com")
    c_with_self_2 = ContactWithSelf("second", "second@example.com")
    c_with_self_3 = ContactWithSelf("third", "third@example.com")
    s_with_self_1 = SupplierWithSelf("fourth", "fourth@example.com")
    print("ContactWithSelf.all_contacts:", ContactWithSelf.all_contacts)
    print("SupplierWithSelf.all_contacts:", SupplierWithSelf.all_contacts)    

test_contact = """
Contact.all_contacts: [Contact('first', 'first@example.com'), Contact('second', 'second@example.com'), Contact('third', 'third@example.com'), Supplier('fourth', 'fourth@example.com')]
Supplier.all_contacts: [Contact('first', 'first@example.com'), Contact('second', 'second@example.com'), Contact('third', 'third@example.com'), Supplier('fourth', 'fourth@example.com')]
"""

test_contact_with_self = """
ContactWithSelf.all_contacts: [ContactWithSelf('first', 'first@example.com'), ContactWithSelf('second', 'second@example.com'), ContactWithSelf('third', 'third@example.com'), SupplierWithSelf('fourth', 'fourth@example.com')]
SupplierWithSelf.all_contacts: [ContactWithSelf('first', 'first@example.com'), ContactWithSelf('second', 'second@example.com'), ContactWithSelf('third', 'third@example.com'), SupplierWithSelf('fourth', 'fourth@example.com')]
"""

if __name__ == "__main__":
    main()
