
# The Hierarchical Data Format version 5 (HDF5), is an open source file format that supports large, complex, heterogeneous data.

import pydicom as dicom
import pydicom
import matplotlib.pyplot as plt
import glob
import h5py
import numpy as np
import os
from functools import reduce


# :::::::::::::::::::::::::::::::::::::::: :::::::::::::::::::::::::::
# Load images from paths and store in .hdf5 file


folderpath = r"/home/jabbar/project_tomo/CTGAN/data/Scapis" # make sure to put the 'r' in front
bb = os.listdir(folderpath)
filepaths = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

# paths0 = glob.glob("/DX/Chest/PseudoID0001 Chest Frontal.dcm")
# path1 = '/Volumes/PHD_Projects/X2CT Example/data/SCAPIS_patients_data/PseudoID0001/DX/Chest/PseudoID0001 Chest Lateral.dcm'
# paths2 = glob.glob("/Volumes/PHD_Projects/X2CT Example/data/SCAPIS_patients_data/PseudoID0001/CT/Thorax insp/*.dcm")

ct_img_size = []
xray1_img_size = []

for patient_data in range(len(filepaths)):
    path0 = os.path.join("/home/jabbar/project_tomo/CTGAN/data/Scapis",  bb[patient_data], "DX/Tomosynthesis/")
    paths0 = glob.glob(path0 + "/*.dcm")
    # path1 = os.path.join("/Volumes/LaCie/Scapis",  bb[patient_data], "DX/Chest/", bb[patient_data] + " Chest Lateral.dcm")
    path2 = os.path.join("/home/jabbar/project_tomo/CTGAN/data/Scapis", bb[patient_data], "CT/Thorax insp")
    paths2 = glob.glob(path2 + "/*.dcm")

    pixel_data = []
    pixel_data2 = []

    # Data reading from Tomosynthesis Folder
    for path in paths0:
        dataset = dicom.dcmread(path)

        pixel_array = dataset.pixel_array

        #we need to check condition again


        if pixel_array.shape[0] <= 1942:

            width = 1942-pixel_array.shape[0]
            right = round(width/2)

        elif pixel_array.shape[0 ]>=1942:
            width = pixel_array.shape[0]
            right = 0

        if pixel_array.shape[1] <= 1966:

            height = 1966 -pixel_array.shape[1]

            top = round(height/2)

        elif pixel_array.shape[1]>=1966:
            height = pixel_array.shape[1]
            top = 0


        pixel_array=np.pad(pixel_array, [(right,),(top,)],mode = 'constant')


        pixel_data.append(pixel_array)

        xray1_img_size.append(pixel_array.shape)





    # dataset = dicom.dcmread(paths0)
    # dset1 = f.create_dataset("tomo", dataset.pixel_array)
    # pixel_data.append(dataset.pixel_array)
    # pixel_data = np.reshape(pixel_data, (2021, 2021))
    # pixel_data = dataset.pixel_array
    # pixel_data = np.reshape(pixel_data, (pixel_data.shape[0], pixel_data.shape[1]))

    # Data reading from Lateral xray
    # dataset3 = pydicom.dcmread(path1)

    # Data reading from CT Folder
    for path in paths2:
        dataset2 = pydicom.dcmread(path)
        # dset1 = f.create_dataset("ct", dataset.pixel_array)
        pixel_data2.append(dataset2.pixel_array)

        ct_img_size.append(dataset2.pixel_array.shape)


    # Parent Directory path
    # parent_dir = "/home/jabbar/project_tomo/CTGAN
    parent_dir = "/home/jabbar/project_tomo/CTGAN/data/Scapis101"
    # New Directory
    count = str(patient_data+1)
    count = count.zfill(4)
    directory = "PseudoID" + count

    path = os.path.join(parent_dir, directory)
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    f = h5py.File('ct_xray_data.h5','w') # Create .hdf5 file to store data

    # Storing Data (Keys)
    f['ct'] = pixel_data2
    f['ori_size'] = 320
    f['spacing'] = 1.0, 0.999999612121212, 0.999999612121212
    f['xray1'] = pixel_data
    # f['xray2'] = dataset3.pixel_array
    f.close()


print("OUTPUT>>>>>>>>>>>>>>>>")
print("CT: ",max(ct_img_size))
print("XRAY Width: ",max(xray1_img_size, key = lambda item:item[0]))
print("XRAY Height: ",max(xray1_img_size, key = lambda item:item[1]))
print("Unique values: ",set(xray1_img_size))
'''
#plt.figure()    
plt.imshow(dataset2.pixel_array, cmap='gray')
plt.colorbar()
plt.title("ct")
plt.show()

#plt.figure()
plt.imshow(dataset2.pixel_array, cmap='gray')
plt.colorbar()
plt.title("CT")
plt.show()

#plt.figure()
plt.imshow(dataset3.pixel_array, cmap='gray')
plt.colorbar()
plt.title("Lateral Tomo Xray")
plt.show()

'''

'''
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.
# Code to print keys in .hdf5 file


filename = '/Volumes/LaCie/SCAPISData/Patient99/ct_xray_data.h5'
data = h5py.File(filename, 'r')
print(type(data))

for key in data.keys():
     print(key)

print(type(data['ct']))
print(type(data['xray1']))
print(type(data['xray2']))
print(type(data['ori_size']))
print(type(data['spacing']))

# Preferred methods to get dataset values:
ds_obj = data['ct']  # Return dataset object
ds_obj1 = data['xray1']  # Return dataset object
ds_obj2 = data['xray2']  # Return dataset object
ds_arr = data['ct'][()] # Return as a numpy array

'''
