#!/usr/bin/env python3
import os
import numpy as np
import capnp

def rek(parents):
	rekpar = []
	while len(parents) != 0:
		for parent in parents:
			for i in parent.nodes:
				which = i.value.which()
				if which == 'num':
					st = i.value.num
				elif which == 'text':
					st = i.value.text
				elif which == 'fnum':
					st = i.value.fnum
				elif which == 'arr':
					st = np.frombuffer(i.value.arr.data, dtype = str(i.value.arr.dtype)).reshape(i.value.arr.shape)
				if len(i.nodes) != 0:
					print (i.name, ' : { ')
				else:
					print (i.name, ' : ' , st)
				if len(i.nodes) != 0:
					rekpar.append(i)
					rek(rekpar)
					print ('}')
			parents.pop(0)
	return

this_dir = os.path.dirname(__file__)
sd = capnp.load(os.path.join(this_dir, 'nodesd.capnp'))
f = open('sd1.bin', 'rb')
mes = sd.Node.read(f)
parents = []
rekpar = []
for d in mes.nodes:
	print (d.name, ' : { ')
	parents.append(d)
	while len(parents) != 0:
		for parent in parents:
			for i in parent.nodes:
				which = i.value.which()
				if which == 'num':
					st = i.value.num
				elif which == 'text':
					st = i.value.text
				elif which == 'fnum':
					st = i.value.fnum
				elif which == 'arr':
					st = np.frombuffer(i.value.arr.data, dtype = str(i.value.arr.dtype)).reshape(i.value.arr.shape)
				if len(i.nodes) != 0:
					print (i.name, ' : { ')
				else:
					print (i.name, ' : ' , st)
				if len(i.nodes) != 0:
					rekpar.append(i)
					rek(rekpar)
					print (' }')
			parents.pop(0)
	print (' } ')

