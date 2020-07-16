#!/usr/bin/env python3
import os
import capnp
this_dir = os.path.dirname(__file__)

addressbook = capnp.load(os.path.join(this_dir, 'addressbook.capnp'))
addresses = addressbook.AddressBook.new_message()
#print (addressbook.qux)
people = addresses.init('people', 2)
alice = people[0]
alice.id = 123
alice.name = 'Alice'
alice.email = 'alice@example.com'
alicePhone = alice.init('phones', 1)[0]
alicePhone.type = 'mobile'
alicePhone.number = '79993343431'
alice.employment.school = "MIT"
yulia = people[1]
yulia.id = 312
yulia.name = 'Yulia'
yulia.email = 'yulia2399@mail.ru'
yullPhones = yulia.init('phones', 2)
yp1 = yullPhones[0]
yp1.type = 'mobile'
yp1.number = '79641043430'
yp2 = yullPhones[1]
yp2.type = 'home'
yp2.number = '798223'
yulia.employment.school = "ISU"
f = open('example.bin', 'w+b')
addresses.write(f)
