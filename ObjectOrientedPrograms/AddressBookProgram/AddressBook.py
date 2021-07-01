"""
@Author: Swapnil Bhoyar
@Date: 2021-06-30 19:00:00
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-07-01 17:15:00
@Title: Write a Program to implement addressbook.
"""
import logging
import json
from json import JSONEncoder

logger = logging.Logger(__name__)
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('AddressBook.log')
logger.addHandler(file_handler)

logging.basicConfig(filename='addressBookErrors.log',  format='%(asctime)s %(levelname)s %(name)s %(message)s')
loggerError = logging.getLogger(__name__)

class Contacts:
    def __init__(self, contactData):
        self.firstName = contactData["firstName"]
        self.lastName = contactData["lastName"]
        self.address = contactData["address"]
        self.city = contactData["city"]
        self.state = contactData["state"]
        self.zip = contactData["zip"]
        self.phoneNumber = contactData["phoneNumber"]
        self.email = contactData["email"]

        logger.info('Created Contact: {} - {} - {} - {} - {} - {} - {} - {}'.format(self.firstName, self.lastName, self.address, self.city, self.state, self.zip, self.phoneNumber,self.email))

        def __str__(self):
            return "first name = " + self.firstName + \
                " last name = " + self.lastName + \
                " address = " + self.address + \
                " city = " + self.state + \
                " state = " + self.state + \
                " zip = " + self.zip + \
                " phoneNumber = " + self.phoneNumber + \
                " email = " + self.email 

class ContactEncoder(JSONEncoder):

    def default(self, object):
        if isinstance(object, Contacts):

            return object.__dict__

        else:

            # call base class implementation which takes care of

            # raising exceptions for unsupported types

            return json.JSONEncoder.default(self, object)

class AddressBook:
    addressBookData = {}
    def addContact(self, addressBookName, contactList):
        """
        Desciption:
            this function add contact
        Parameter:
            addressBookName: string
            contactList: list
        """
        try:

            contactData = {
                "firstName": input("First name:"),
                "lastName": input("last name:"),
                "address": input("address:"),
                "city":input("city:"),
                "state": input("state:"),
                "zip": input("zip:"),
                "phoneNumber": input("phoneNumber:"),
                "email": input("email:")
            }

            contact = Contacts(contactData)
            contactList.append(contact)
            self.addressBookData = {addressBookName: contactList}

            # Serializing json 
            json_string = ContactEncoder().encode(contact)
    
            with open("contactFile.json", "w") as outfile:
                outfile.write(json_string)

        except Exception as e:
            loggerError.error(e)

    def editContact(self, contact):
        """
        Desciption:
            this function edit contact
        Parameter:
            contact: object
        """
        try:
            contact.lastName = input("updated last name:")
            contact.address = input("updated address:")
            contact.city = input("updated city:")
            contact.state = input("updated state:")
            contact.zip = input("updated zip:")
            contact.phoneNumber = input("updated phone number:")
            contact.email = input("updated email:")
        except Exception as e:
            loggerError.error(e)

    def updateContact(self, contactList):
        """
        Desciption:
            this function update contact
        Parameter:
            contactList: list
        """
        first_name = input("Enter first name to edit:")
        for contact in contactList:
            if contact.firstName == first_name:
                self.editContact(contact)
        else:
            print("contact does not exist")

    def removeContact(self, contactList):
        """
        Desciption:
            this function delete contact
        Parameter:
            contactList: list
        """
        try:
            first_name = input("Enter name of contact to remove:")
            index = 0
            for contact in contactList:
                if contact.firstName == first_name:
                    del contactList[index]
                    break
                index += 1

                with open('contactFile.json') as data_file:
                    data = json.load(data_file)

                # Iterate through the objects in the JSON                                                                            
                
                for element in data:
                    if 'fiestName' in element == first_name:
                        del element

                with open('contactFile.json', 'w') as data_file:
                    data = json.dump(data, data_file)
        except Exception as e:
            loggerError.error(e)

    def contactDataOperations(self, addressBookName, contactList):
        """
        Desciption:
            this function perform contact operations 
        Parameter:
            addressBookName: string
            contactList: list
        """
        try:
            status = True
            while status:
                userChoice = int(input("1.ADD CONTACT\n2.UPDATE CONTACT\n3.REMOVE CONTACT\n4.PRINT\n5.EXIT\n"))
                if userChoice == 1:
                    self.addContact(addressBookName, contactList)
                elif userChoice == 2:
                    self.updateContact(contactList)
                elif userChoice == 3:
                    self.removeContact(contactList)
                elif userChoice == 4:
                    # for contact in contactList:
                    #     print(contact)
                    with open('contactFile.json') as data_file:
                        data = json.load(data_file)

                    # Iterate through the objects in the JSON                                                                            
                    
                    for element in data.values():
                        print(element)
                elif userChoice == 5:
                    status = False
        except Exception as e:
            loggerError.error(e)

    def getNewAddressBook(self):
        """
        Desciption:
            this function create addressbook
        """
        contactList = []
        try:
            addressBookName = input("Enter addressbook name:")
            self.addContact(addressBookName, contactList)
            self.contactDataOperations(addressBookName, self.addressBookData[addressBookName])
        except Exception as e:
            loggerError.error(e)

    def createAddressBook(self):
        """
        Desciption:
            this function add addressbook
        """
        status = True
        try:
            while status:
                userChoice = int(input("\n1.NEW ADDRESS BOOK\n2. SELECT ADDRESS BOOK\n3. EXIT\n"))
                if userChoice == 1:
                    self.getNewAddressBook()
                elif userChoice == 2:
                    address_book_name = input("Enter addressbook name to access:")
                    for addressbook in self.addressBookData:
                        if addressbook == address_book_name:
                            self.contactDataOperations(addressbook, self.addressBookData[addressbook])
                    else:
                        print("addressbook does not exist")
                else:
                    status = False
        except Exception as e:
            loggerError.error(e)

addressBookObj = AddressBook()
addressBookObj.createAddressBook()