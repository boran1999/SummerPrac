#!/usr/bin/env python3
import os
import numpy as np
import capnp

def strins(a):
	kt = ''
	kt = str(a.shape)
	kt = kt[1:-1]
	mst = kt.split(',')
	st=''
	if(len(mst)==3):
		for i in range(a.shape[0]):
			for j in range(a.shape[1]):
				for z in range(a.shape[2]-1):
					st += str(a[i][j][z]) + ', '
				st += str(a[i][j][a.shape[2] - 1])
				st += ';'
			st+= '-'
	elif (mst[1]):
    		for i in range(a.shape[0]):
        		for j in range(a.shape[1] - 1):
            			st += str(a[i][j]) + ', '
        		st += str(a[i][a.shape[1] - 1])
        		st+= ';'
	else:
    		for i in range(a.shape[0] - 1):
        		st += str(a[i]) + ', '
    		st += str(a[a.shape[0] - 1])
	return st

this_dir = os.path.dirname(__file__)

sd = capnp.load(os.path.join(this_dir, 'scidata.capnp'))
mes = sd.SDList.new_message()
datamas = np.array([1, 2, 3, 4, 5, 6])
imagemas1 = np.random.random_sample((20, 20))
imagemas2 = np.arange(5 * 10 * 10, dtype="uint8").reshape(5, 10, 10)
sinn = np.sin(np.arange(100))
coss = np.cos(np.arange(100))
zeros = np.zeros((4, 256, 320), dtype='float32')
arr1 = np.arange(4)
arr2 = np.arange(4) + 10
arr3 = np.arange(4, dtype='uint64')
ds = mes.init('sundates', 10)

sunlight = ds[0]
sunlight.id = 1
sunlight.name = 'data'
sunlight.data.values = strins(datamas)
sunlight.data.size = str(datamas.shape)
sunlight.data.type = str(datamas.dtype)

smm = ds[1]
smm.id = 2
smm.name = 'image'
smm.image.values = strins(imagemas1)
smm.image.size = str(imagemas1.shape)
smm.image.type = str(imagemas1.dtype)

smm2 = ds[2]
smm2.id = 3
smm2.name = 'image'
smm2.image.values = strins(imagemas2)
smm2.image.size = str(imagemas2.shape)
smm2.image.type = str(imagemas2.dtype)

smm3 = ds[3]
smm3.id = 4
smm3.name = 'image'
smm3.image.values = strins(imagemas1)
smm3.image.size = str(imagemas1.shape)
smm3.image.type = str(imagemas1.dtype)
smm3.timestamp = '129420192'

smm4 = ds[4]
smm4.id = 5
smm4.type = 'correction'
smm4.number = 2
smm4.flatField.values = strins(imagemas1)
smm4.flatField.size = str(imagemas1.shape)
smm4.flatField.type = str(imagemas1.dtype)
smm4.darkFrame.values = strins(imagemas1)
smm4.darkFrame.size = str(imagemas1.shape)
smm4.darkFrame.type = str(imagemas1.dtype)

smm5 = ds[5]
smm5.id = 6
smm5.type = 'signal'
smm5.reference = 2
smm5.signal1.values = strins(sinn)
smm5.signal1.size = str(sinn.shape)
smm5.signal1.type = str(sinn.dtype)
smm5.signal2.values = strins(coss)
smm5.signal2.size = str(coss.shape)
smm5.signal2.type = str(coss.dtype)

smm6 = ds[6]
smm6.id = 7
smm6.name = 'image'
smm6.image.values = strins(imagemas1)
smm6.image.size = str(imagemas1.shape)
smm6.image.type = str(imagemas1.dtype)
smm6.timestamp = '123241241'
smm6.metadata.ipol = 2
smm6.metadata.pixelSize = 0.75
smm6.metadata.units = 'nm'

smm71 = ds[7]
smm71.id = 8
smm71.type = 'signal'
smm71.reference = 2
smm71.signal1.values = strins(sinn)
smm71.signal1.size = str(sinn.shape)
smm71.signal1.type = str(sinn.dtype)
smm71.signal2.values = strins(coss)
smm71.signal2.size = str(coss.shape)
smm71.signal2.type = str(coss.dtype)
smm72 = ds[8]
smm72.id = 9
smm72.type = 'signal'
smm72.reference = 2
smm72.signal1.values = strins(sinn)
smm72.signal1.size = str(sinn.shape)
smm72.signal1.type = str(sinn.dtype)
smm72.signal2.values = strins(coss)
smm72.signal2.size = str(coss.shape)
smm72.signal2.type = str(coss.dtype)

ft = ds[9]
ft.id = 10
ft.name = 'image'
ft.image.values = strins(zeros)
ft.image.size = str(zeros.shape)
ft.image.type = str(zeros.dtype)
ft.metadata.cameraSettingsTree.image.dataType = 1
ft.metadata.cameraSettingsTree.timings.freeq = 20
ft.metadata.cameraSettingsTree.buffer.buffControlTimeout = 500
ft.metadata.cameraSettingsTree.buffer.buffElemSize = 4
ft.metadata.cameraSettingsTree.buffer.buffFpe = 2
ft.metadata.cameraSettingsTree.buffer.buffFrameSize = 65536
ft.metadata.cameraSettingsTree.buffer.buffLen = 100
ft.metadata.cameraSettingsTree.buffer.buffModulStates = 6
ft.metadata.cameraSettingsTree.device.cameraName = 'basler'
ft.metadata.cameraSettingsTree.device.image.binX = 2
ft.metadata.cameraSettingsTree.device.image.binY = 2
ft.metadata.cameraSettingsTree.device.image.dataType = 1
ft.metadata.cameraSettingsTree.device.image.dataTypeBytes = 1
ft.metadata.cameraSettingsTree.device.image.fileToWrite = 'test.h5'
ft.metadata.cameraSettingsTree.device.image.imageX = 600
ft.metadata.cameraSettingsTree.device.image.imageY = 600
ft.metadata.cameraSettingsTree.device.image.roi.roi1 = '[0, 0, 600, 600]'
ft.metadata.cameraSettingsTree.device.image.roi.totalRoi = 1
ft.metadata.cameraSettingsTree.device.sensor.sensorX = 1000
ft.metadata.cameraSettingsTree.device.sensor.sensorY = 1000
ft.metadata.cameraSettingsTree.device.sensor.timings.exTime = 150
ft.metadata.cameraSettingsTree.device.sensor.timings.exUnits = 'nm'
ft.metadata.cameraSettingsTree.device.sensor.timings.syncType = 2
ft.metadata.cameraSettingsTree.device.totalFrames = 4
ft.timeCoord.coordLat.values = strins(arr1)
ft.timeCoord.coordLat.size = str(arr1.shape)
ft.timeCoord.coordLat.type = str(arr1.dtype)
ft.timeCoord.coordLon.values = strins(arr1)
ft.timeCoord.coordLon.size = str(arr1.shape)
ft.timeCoord.coordLon.type = str(arr1.dtype)
ft.timeCoord.coordX.values = strins(arr2)
ft.timeCoord.coordX.size = str(arr2.shape)
ft.timeCoord.coordX.type = str(arr2.dtype)
ft.timeCoord.coordY.values = strins(arr2)
ft.timeCoord.coordY.size = str(arr2.shape)
ft.timeCoord.coordX.type = str(arr2.dtype)
ft.timeCoord.epochTime.values = strins(arr3)
ft.timeCoord.epochTime.size = str(arr3.shape)
ft.timeCoord.epochTime.type = str(arr3.dtype)
ft.timeCoord.isoTime = '[1515151, 1515151, 11515151, 1515151]'
f = open('sd3.bin', 'w+b')
mes.write(f)
