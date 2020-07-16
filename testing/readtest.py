#!/usr/bin/env python3
import os
import capnp
this_dir = os.path.dirname(__file__)

addressbook = capnp.load(os.path.join(this_dir, 'addressbook.capnp'))
f = open('example.bin', 'rb')
addresses = addressbook.AddressBook.read(f)
for person in addresses.people:
	print(person.name, ':', person.email)
	for phone in person.phones:
        	print(phone.type, ':', phone.number)
	which = person.employment.which()
	if which == 'unemployed':
    		print('unemployed')
	elif which == 'employer':
    		print('employer:', person.employment.employer)
	elif which == 'school':
    		print('student at:', person.employment.school)
	elif which == 'selfEmployed':
    		print('self employed')
