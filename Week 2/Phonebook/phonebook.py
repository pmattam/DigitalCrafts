import pickle
from operator import attrgetter

class Contact(object):

    def __init__(self, fname, lname, email, phone):
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.phone = phone
    
    def __repr__(self):
        return '%s %s %s %s' % (self.first_name, self.last_name, self.email, self.phone)

class Phonebook(object):

    def __init__(self):
        self.contacts = []
    
    def lookUp(self, contact_first_name, contact_last_name):
        for contact in self.contacts:
            if contact.last_name == contact_last_name and contact.first_name == contact_first_name:
                print "Entry found %s: %s " % (contact.first_name, contact.phone)
                return contact

    def setUp(self, first, last, email, phone):
        person = Contact(first, last, email, phone)
        self.contacts.append(person)
        print "Entry stored for %s. " % first
        
    def delete(self, contact_first_name, contact_last_name):
        contact_to_be_removed = self.lookUp(contact_first_name, contact_last_name)
        self.contacts.remove(contact_to_be_removed)
        print "Deleted entry for %s " % contact_to_be_removed.first_name

    def listAll(self):
        self.sorted_list = sorted(self.contacts, key=attrgetter('first_name', 'last_name'))
        for contact in self.sorted_list:
            # print "Found entry for %r " % contact
            print "Found entry for %s: %s" % (contact.first_name, contact.phone)
    
    # saving entries from the self.contacts list 
    # serialization - converting the object into bytestream for storing in a file
    def saveEntries(self):
        myfile = open('phonebook.pickle', 'w')
        pickle.dump(self.contacts, myfile)
        myfile.close()
    
    # restoring entries to self.contacts list
    # deserialization - reconstructing from bytestream to object
    def restoreSavedEntries(self):
        myfile = open('phonebook.pickle', 'r')
        self.contacts = pickle.load(myfile)

    def __repr__(self):
        return '%s ' % self.contacts

def menu():
        print "Electronic Phone Book \n====================="
        print "1. Look up an entry \n2. Set an entry"
        print "3. Delete an entry \n4. List all entries"
        print "5. Save entries \n6. Restore saved entries"
        print "7. Quit"

def main():
    #creating instance of phonebook
    phonebook = Phonebook()
    while True:
        menu()
        input = int(raw_input("What do you want to do (1-5)? "))

        if input is 1:
            first_name = raw_input("Enter a First Name: ")
            last_name = raw_input("Enter a Last Name: ")
            phonebook.lookUp(first_name, last_name)
        elif input is 2:
            first_name = raw_input("Enter a First Name: ")
            last_name = raw_input("Enter a Last Name: ")
            email = raw_input("Enter an Email: ")
            phone = raw_input("Enter a Phone Number:")
            phonebook.setUp(first_name, last_name, email, phone)
        elif input is 3:
            first_name = raw_input("Enter a First Name: ")
            last_name = raw_input("Enter a Last Name: ")
            phonebook.delete(first_name, last_name)
        elif input is 4:
            phonebook.listAll()
        elif input is 5:
            phonebook.saveEntries()
        elif input is 6:
            phonebook.restoreSavedEntries()
        else:
            print "Bye."
            break

main()



