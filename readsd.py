#!/usr/bin/env python3
import os
import numpy as np
import capnp

def getmas(tval, tsize, ttype):
	kt = ''
	kt = str(tsize)
	kt = kt[1:-1]
	mst = kt.split(',')
	st=''
	if len(mst) == 3:
		emp = tval.split('-')
		efin=[]
		for i in emp[:-1]:
			efin.append(i.split(';'))
		res = []
		cou=0
		for j in efin:
			res.append([])
			for l in j[:-1]:
				res[cou].append(l.split(','))
			cou+=1
		anum = np.array(res, dtype = ttype)
	elif mst[1]:
		temp = tval.split(';')
		fin = []
		for i in temp[:-1]:
			fin.append(i.split(','))
		anum = np.array(fin, dtype = ttype)
	else:
		anum = np.array(tval.split(','), dtype = ttype)
	return anum

this_dir = os.path.dirname(__file__)
sd = capnp.load(os.path.join(this_dir, 'scidata.capnp'))
f = open('sd3.bin', 'rb')
mes = sd.SDList.read(f)
treenum = 0
for d in mes.sundates:
	treenum += 1
	if treenum == 10:
		print ('tree number 9')
	elif treenum == 9:
		print ('data2 : { ')
	else:
		print ('tree nymber', treenum)
	if treenum == 8:
		print ('data1 : { ')
	if d.data.values:
		print (d.name, ':', getmas(d.data.values, d.data.size, d.data.type))
	if d.image.values:
		print (d.name, ':', getmas(d.image.values, d.image.size, d.image.type))
	if d.type:
		print ('type :', d.type)
	if d.number:
		print ('number :', d.number)
	if d.reference:
		print ('reference :', d.reference)
	if d.flatField.values:
		print ('flat_field :', getmas(d.flatField.values, d.flatField.size, d.flatField.type))
	if d.darkFrame.values:
		print ('dark_frame :', getmas(d.darkFrame.values, d.darkFrame.size, d.darkFrame.type))
	if d.timestamp:
		print ('timestamp :' , d.timestamp)
	if d.signal1.values:
		print ('signal_1 :', getmas(d.signal1.values, d.signal1.size, d.signal1.type))
	if d.signal2.values:
		print ('signal_2 :', getmas(d.signal2.values, d.signal2.size, d.signal2.type))
	if d.metadata.ipol:
		print ('metadata : { ipol :', d.metadata.ipol, ' pixel_size :', d.metadata.pixelSize, ' units :', d.metadata.units, ' }')
	if (treenum == 8) or (treenum == 9):
		print ('}')
	if treenum == 10:
		print ('metadata :  {  camera_settings_tree : { image : { data_type :', d.metadata.cameraSettingsTree.image.dataType, ' }\n\t\t\t\t\ttimings :{ freequency :',
 d.metadata.cameraSettingsTree.timings.freeq, ' }\n\t\t\t\t\tbuffer: { buffer_control_timeout :', d.metadata.cameraSettingsTree.buffer.buffControlTimeout,
 '\n\t\t\t\t\t\tbuffer_element_size :', d.metadata.cameraSettingsTree.buffer.buffElemSize, '\n\t\t\t\t\t\tbufferFpe: ', d.metadata.cameraSettingsTree.buffer.buffFpe,
' }\n\t\t\t\t\tdevice : { camera_name :', d.metadata.cameraSettingsTree.device.cameraName, '\n\t\t\t\t\t\timage : { bin_x :', d.metadata.cameraSettingsTree.device.image.binX,
'\n\t\t\t\t\t\t\tbin_y', d.metadata.cameraSettingsTree.device.image.binY, '\n\t\t\t\t\t\t\troi : { roi_1 :', d.metadata.cameraSettingsTree.device.image.roi.roi1,
'\n\t\t\t\t\t\t\t\ttotal_roi :', d.metadata.cameraSettingsTree.device.image.roi.totalRoi, ' }}\n\t\t\t\t\t\tsensor : { ', d.metadata.cameraSettingsTree.device.sensor.sensorX,
'\n\t\t\t\t\t\t\ttimings : { exposition_time :', d.metadata.cameraSettingsTree.device.sensor.timings.exTime, '\n\t\t\t\t\t\t\t\t\texposition_units :',
d.metadata.cameraSettingsTree.device.sensor.timings.exUnits, ' }}\n\t\t\t\t\t\ttotal_frames :', d.metadata.cameraSettingsTree.device.totalFrames,
 ' }}}\nspetrum_model={}\ntime_coord : { coord_lat :', getmas(d.timeCoord.coordLat.values, d.timeCoord.coordLat.size, d.timeCoord.coordLat.type), '\n\tcoord_lon :',
getmas(d.timeCoord.coordLon.values, d.timeCoord.coordLon.size, d.timeCoord.coordLon.type), '\n\tcoord_x :',
getmas(d.timeCoord.coordX.values, d.timeCoord.coordX.size, d.timeCoord.coordX.type), '\n\tcoord_y :',
getmas(d.timeCoord.epochTime.values, d.timeCoord.epochTime.size, d.timeCoord.epochTime.type), '\n\tiso_time :', d.timeCoord.isoTime, ' }}')
