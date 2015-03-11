# The Python implementation of the gRPC AddressBook client.

import adress_book_pb2
_TIMEOUT_SECONDS = 10

def add(stub):
    contact = adress_book_pb2.Person()
    contact.name = raw_input('Enter name:')
    contact.id = int(raw_input('Enter ID of the person:'))
    contact.email = raw_input('Enter e-mail address:')

    #phone_number = contact.phone.add()
    contact.phone.number = raw_input('Enter Phone Number:')
    contact.phone.type = 0
    response = stub.AddContact(contact, _TIMEOUT_SECONDS)
    if 1 == response.status_val:
        print 'Contact was added successfully to the address book'

def search(stub):
    name = adress_book_pb2.TextMessage()
    name.text = raw_input('Enter name to search:')
    response = stub.SearchContact(name, _TIMEOUT_SECONDS)
    print response.name + ':' + str(response.id) + ' found in the address book'

def display(stub):
    msg = adress_book_pb2.TextMessage()
    msg.text = 'Some text message'
    response = stub.DisplayAll(msg, _TIMEOUT_SECONDS)

    for contact in response.contacts:
        print 'contact_name:', contact.name
        print 'contact_id:', contact.id
        print 'contact_email:', contact.email
        print 'contact_phone number:', contact.phone.number

def run():
    execute = 1
    with adress_book_pb2.early_adopter_create_AddressBook_stub('localhost', 50051) as stub:
        while execute:
            print '1. Add Contact\n2. Search Contact\n3. Display All\n4. Exit'
            input_var = raw_input('Enter your choice:')
            if '1' == input_var:
                add(stub)
            elif '2' == input_var:
                search(stub)
            elif '3' == input_var:
                display(stub)
            elif '4' == input_var:
                execute = 0
        print 'Exiting from client...'
if __name__ == '__main__':
  run()
