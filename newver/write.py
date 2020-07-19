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
arr1 = np.arange(4)
arr2 = np.arange(4) + 10
arr3 = np.arange(4, dtype='uint64')
ds = mes.init('nodes', 2)

t1 = ds[0]
#childs = sunlight.init('nodes', 2)
t1.id = 100
t1.name = 'TREE NUMBER 1'
childs1 = t1.init('nodes', 1)
#tree1.value.none = None
child1 = childs1[0]
child1.id = 101
child1.name = 'data'
arr1 = child1.value.init('arr')
arr1.shape = datamas.shape
arr1.dtype = str(datamas.dtype)
arr1.data = datamas.tobytes()

#smm = ds[1]
#smm.id = 2
#smm.name = 'image'
#smm.image.values = strins(imagemas1)
#smm.image.size = str(imagemas1.shape)
#smm.image.type = str(imagemas1.dtype)

#smm2 = ds[2]
#smm2.id = 3
#smm2.name = 'image'
#smm2.image.values = strins(imagemas2)
#smm2.image.size = str(imagemas2.shape)
#smm2.image.type = str(imagemas2.dtype)

#smm3 = ds[3]
#smm3.id = 4
#smm3.name = 'image'
#smm3.image.values = strins(imagemas1)
#smm3.image.size = str(imagemas1.shape)
#smm3.image.type = str(imagemas1.dtype)
#smm3.timestamp = '129420192'

#smm4 = ds[4]
#smm4.id = 5
#smm4.type = 'correction'
#smm4.number = 2
#smm4.flatField.values = strins(imagemas1)
#smm4.flatField.size = str(imagemas1.shape)
#smm4.flatField.type = str(imagemas1.dtype)
#smm4.darkFrame.values = strins(imagemas1)
#smm4.darkFrame.size = str(imagemas1.shape)
#smm4.darkFrame.type = str(imagemas1.dtype)

#smm5 = ds[5]
#smm5.id = 6
#smm5.type = 'signal'
#smm5.reference = 2
#smm5.signal1.values = strins(sinn)
#smm5.signal1.size = str(sinn.shape)
#smm5.signal1.type = str(sinn.dtype)
#smm5.signal2.values = strins(coss)
#smm5.signal2.size = str(coss.shape)
#smm5.signal2.type = str(coss.dtype)

smm6 = ds[1]
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

#smm71 = ds[7]
#smm71.id = 8
#smm71.type = 'signal'
#smm71.reference = 2
#smm71.signal1.values = strins(sinn)
#smm71.signal1.size = str(sinn.shape)
#smm71.signal1.type = str(sinn.dtype)
#smm71.signal2.values = strins(coss)
#smm71.signal2.size = str(coss.shape)
#smm71.signal2.type = str(coss.dtype)
#smm72 = ds[8]
#smm72.id = 9
#smm72.type = 'signal'
#smm72.reference = 2
#smm72.signal1.values = strins(sinn)
#smm72.signal1.size = str(sinn.shape)
#smm72.signal1.type = str(sinn.dtype)
#smm72.signal2.values = strins(coss)
#smm72.signal2.size = str(coss.shape)
#smm72.signal2.type = str(coss.dtype)

#ft = ds[9]
#ft.id = 10
#ft.name = 'image'
#ft.image.values = strins(zeros)
#ft.image.size = str(zeros.shape)
#ft.image.type = str(zeros.dtype)
#ft.metadata.cameraSettingsTree.image.dataType = 1
#ft.metadata.cameraSettingsTree.timings.freeq = 20
#ft.metadata.cameraSettingsTree.buffer.buffControlTimeout = 500
#ft.metadata.cameraSettingsTree.buffer.buffElemSize = 4
#ft.metadata.cameraSettingsTree.buffer.buffFpe = 2
#ft.metadata.cameraSettingsTree.buffer.buffFrameSize = 65536
#ft.metadata.cameraSettingsTree.buffer.buffLen = 100
#ft.metadata.cameraSettingsTree.buffer.buffModulStates = 6
#ft.metadata.cameraSettingsTree.device.cameraName = 'basler'
#ft.metadata.cameraSettingsTree.device.image.binX = 2
#ft.metadata.cameraSettingsTree.device.image.binY = 2
#ft.metadata.cameraSettingsTree.device.image.dataType = 1
#ft.metadata.cameraSettingsTree.device.image.dataTypeBytes = 1
#ft.metadata.cameraSettingsTree.device.image.fileToWrite = 'test.h5'
#ft.metadata.cameraSettingsTree.device.image.imageX = 600
#ft.metadata.cameraSettingsTree.device.image.imageY = 600
#ft.metadata.cameraSettingsTree.device.image.roi.roi1 = '[0, 0, 600, 600]'
#ft.metadata.cameraSettingsTree.device.image.roi.totalRoi = 1
#ft.metadata.cameraSettingsTree.device.sensor.sensorX = 1000
#ft.metadata.cameraSettingsTree.device.sensor.sensorY = 1000
#ft.metadata.cameraSettingsTree.device.sensor.timings.exTime = 150
#ft.metadata.cameraSettingsTree.device.sensor.timings.exUnits = 'nm'
#ft.metadata.cameraSettingsTree.device.sensor.timings.syncType = 2
#ft.metadata.cameraSettingsTree.device.totalFrames = 4
#ft.timeCoord.coordLat.values = strins(arr1)
#ft.timeCoord.coordLat.size = str(arr1.shape)
#ft.timeCoord.coordLat.type = str(arr1.dtype)
#ft.timeCoord.coordLon.values = strins(arr1)
#ft.timeCoord.coordLon.size = str(arr1.shape)
#ft.timeCoord.coordLon.type = str(arr1.dtype)
#ft.timeCoord.coordX.values = strins(arr2)
#ft.timeCoord.coordX.size = str(arr2.shape)
#ft.timeCoord.coordX.type = str(arr2.dtype)
#ft.timeCoord.coordY.values = strins(arr2)
#ft.timeCoord.coordY.size = str(arr2.shape)
#ft.timeCoord.coordX.type = str(arr2.dtype)
#ft.timeCoord.epochTime.values = strins(arr3)
#ft.timeCoord.epochTime.size = str(arr3.shape)
#ft.timeCoord.epochTime.type = str(arr3.dtype)
#ft.timeCoord.isoTime = '[1515151, 1515151, 11515151, 1515151]'
f = open('sd1.bin', 'w+b')
mes.write(f)
