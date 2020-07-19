#!/usr/bin/env python3
import os
import numpy as np
import capnp

this_dir = os.path.dirname(__file__)
sd = capnp.load(os.path.join(this_dir, 'nodesd.capnp'))
f = open('sd1.bin', 'rb')
mes = sd.SDList.read(f)
for d in mes.sundates:
	for node in d.nodes:
		which = node.value.which()
		if which == 'none':
			st = ''
		elif which == 'num':
			st = node.value.num
		elif which == 'text':
			st = node.value.text
		elif which == 'arr':
			st = np.frombuffer(node.value.arr.data, dtype = str(node.value.arr.dtype)).reshape(node.value.arr.shape)
		print (node.name, ' ' , st)

