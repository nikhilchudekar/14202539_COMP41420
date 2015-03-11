# The python implementation of the gRPC AddressBook server.
import time
import adress_book_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class AddressBook(adress_book_pb2.EarlyAdopterAddressBookServicer):

    def __init__(self):
        # print 'AddressBook Constructor'
        self.address_book = adress_book_pb2.RemoteAddressBook()

    def AddContact(self, request, context):
        # print 'Before adding into address book'
        #self.address_book.contacts.extend([request])
        person = self.address_book.contacts.add()
        person.name = request.name
        person.id = request.id
        person.email = request.email
        person.phone.number = request.phone.number
        person.phone.type = request.phone.type
        return adress_book_pb2.Status(status_val=1)

    def SearchContact(self, request, context):
        for contact in self.address_book.contacts:
            if request.text == contact.name:
                found_person = adress_book_pb2.Person()
                found_person.name = contact.name
                found_person.id = contact.id
                found_person.email = contact.email
                found_person.PhoneNumber.number = contact.PhoneNumber.number
                found_person.PhoneNumber.type = contact.PhoneNumber.number
                return found_person

    def DisplayAll(self, request, context):
        return adress_book_pb2.RemoteAddressBook(contacts=self.address_book.contacts)

def serve():
    server = adress_book_pb2.early_adopter_create_AddressBook_server(
      AddressBook(), 50051, None, None)
    server.start()
    try:
        while True:
            # print 'server running...'
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop()

if __name__ == '__main__':
  serve()
