#!/usr/bin/env python3
import os
import numpy as np
import capnp

this_dir = os.path.dirname(__file__)

sd = capnp.load(os.path.join(this_dir, 'nodesd.capnp'))
mes = sd.Node.new_message()
datamas = np.array([1, 2, 3, 4, 5, 6])
imagemas1 = np.random.random_sample((20, 20))
imagemas2 = np.arange(5 * 10 * 10, dtype="uint8").reshape(5, 10, 10)
sinn = np.sin(np.arange(100))
coss = np.cos(np.arange(100))
zeros = np.zeros((4, 256, 320), dtype='float32')
larr1 = np.arange(4)
larr2 = np.arange(4) + 10
larr3 = np.arange(4, dtype='uint64')
ds = mes.init('nodes', 4)

t1 = ds[0]
t1.id = 100
t1.name = 'TREE NUMBER 1'
childs1 = t1.init('nodes', 1)
child1 = childs1[0]
child1.id = 101
child1.name = 'data'
arr1 = child1.value.init('arr')
arr1.shape = datamas.shape
arr1.dtype = str(datamas.dtype)
arr1.data = datamas.tobytes()

t2 = ds[1]
t2.id = 101
t2.name = 'TREE NUMBER 2'
childs2 = t2.init('nodes', 1)
child21 = childs2[0]
child21.id = 102
child21.name = 'image'
arr2 = child21.value.init('arr')
arr2.shape = imagemas1.shape
arr2.dtype = str(imagemas1.dtype)
arr2.data = imagemas1.tobytes()

smm6 = ds[2]
smm6.id = 701
smm6.name = 'TREE NUMBER 7'
childs7 = smm6.init('nodes', 3)
child71 = childs7[0]
child71.name = 'image'
arr7 = child71.value.init('arr')
arr7.shape = imagemas1.shape
arr7.dtype = str(imagemas1.dtype)
arr7.data = imagemas1.tobytes()
child72 = childs7[1]
child72.name = 'metadata'
mchilds = child72.init('nodes', 3)
mchild1 = mchilds[0]
mchild1.name = 'ipol'
mchild1.value.num = 2
mchild2 = mchilds[1]
mchild2.name = 'pixelSize'
mchild2.value.fnum = 0.75
mchild3 = mchilds[2]
mchild3.name = 'units'
mchild3.value.text = 'nm'
child73 = childs7[2]
child73.name = 'timestamp'
child73.value.text = '12323132'

t9 = ds[3]
t9.id = 900
t9.name = 'FINAL TREE'
ftc = t9.init('nodes', 3)
fimage = ftc[0]
fimage.name = 'image'
farr = fimage.value.init('arr')
farr.shape = zeros.shape
farr.dtype = str(zeros.dtype)
farr.data = zeros.tobytes()
meta = ftc[1]
meta.name = 'metadata'
cst = meta.init('nodes', 1)[0]
cst.name = "cameraSettingsTree"
cstd = cst.init('nodes',4)
im = cstd[0]
im.name = 'image'
dt = im.init('nodes',1)[0]
dt.name = 'dataType'
dt.value.num = 1
tim = cstd[1]
tim.name = 'timings'
fr = tim.init('nodes', 1)[0]
fr.name = 'freequency'
fr.value.num = 20
buf = cstd[2]
buf.name = 'buffer'
bd = buf.init('nodes',2)
bfs = bd[0]
bfs.name='BufferFrameSize'
bfs.value.num = 65536
bl = bd[1]
bl.name = 'BufferLength'
bl.value.num = 100
dev = cstd[3]
dev.name = 'device'
dd = dev.init('nodes', 3)
imd = dd[0]
imd.name = 'image'
imm = imd.init('nodes',2)
binx = imm[0]
binx.name = 'BinX'
binx.value.num = 2
biny = imm[1]
biny.name = 'BinY'
biny.value.num = 2
sen = dd[1]
sen.name = 'sensor'
ss = sen.init('nodes', 2)
senx = ss[0]
senx.name = 'sensorX'
senx.value.num = 1000
tt = ss[1]
tt.name = 'timings'
tc = tt.init('nodes', 2)
et = tc[0]
et.name = 'exTime'
et.value.num = 150
eu = tc[1]
eu.name = 'exUnits'
eu.value.text = 'nm'
tf = dd[2]
tf.name = 'TotalFrames'
tf.value.num = 4
cord = ftc[2]
cord.name = 'timeCoord'
tc = cord.init('nodes', 3)
cl = tc[0]
cl.name = 'coordLat'
carr = cl.value.init('arr')
carr.shape = larr1.shape
carr.dtype = str(larr1.dtype)
carr.data = larr1.tobytes()
ept = tc[1]
ept.name = 'epochTime'
earr = ept.value.init('arr')
earr.shape = larr3.shape
earr.dtype = str(larr3.dtype)
earr.data = larr3.tobytes()
ist = tc[2]
ist.name = 'isoTime'
ist.value.text = '[1515151, 15151515, 51515151, 15151515]'

f = open('sd1.bin', 'w+b')
mes.write(f)
