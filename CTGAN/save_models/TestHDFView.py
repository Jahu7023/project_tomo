import numpy as np
import h5py
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

'''
filename = "/home/jabbar/tomo_project/CTGAN/data/LIDC-HDF5-256/LIDC-IDRI-0001.20000101.3000566.1/ct_xray_data.h5"

with h5py.File(filename, "r") as f:
    print(f.name)
    # Print all root level object names (aka keys)
    # these can be group or dataset names
    print("Keys: %s" % f.keys())
    a = f.keys()
    # get first object name/key; may or may NOT be a group
    a_group_key = list(f.keys())[0]

    # get the object type for a_group_key: usually group or dataset
    print(type(f[a_group_key]))

    # If a_group_key is a group name,
    # this gets the object names in the group and returns as a list
    data = list(f[a_group_key])

    # If a_group_key is a dataset name,
    # this gets the dataset values and returns as a list
    data = list(f[a_group_key])
    # preferred methods to get dataset values:
    ds_obj = f[a_group_key]      # returns as a h5py dataset object
    ds_arr = f[a_group_key][()]  # returns as a numpy array
    dsh = ds_obj.shape
    dt = ds_obj.dtype

# plt.imshow(ds_arr[3, :, :])
# plt.title("CT")
# plt.show()

plt.imshow(ds_arr)
plt.title("Xray2")
plt.show()

# fig = plt.figure()
# plt.title("CT")
# ax = plt.axes(projection = '3d')
# ax.voxels(ds_arr, edgecolors='gray', shade=False)

     # plt.show()

f.close()

'''
# import scisoftpy as dnp

# path_and_file = "/home/jabbar/tomo_project/CTGAN/data/LIDC-HDF5-256/LIDC-IDRI-0001.20000101.3000566.1/ct_xray_data.h5"
# def print_attrs(name, obj):
#     # Create indent
#     shift = name.count('/') * '    '
#     item_name = name.split("/")[-1]
#     print(shift + item_name)
#     try:
#         for key, val in obj.attrs.items():
#             print(shift + '    ' + f"{key}: {val}")
#     except:
#         pass
#
# f = h5py.File(path_and_file,'r')
# f.visititems(print_attrs)

# filename_hdf = '/home/jabbar/tomo_project/CTGAN/data/LIDC-HDF5-256/LIDC-IDRI-0001.20000101.3000566.1/ct_xray_data.h5'
# f = nx.nxload('/home/jabbar/tomo_project/CTGAN/data/LIDC-HDF5-256/LIDC-IDRI-0001.20000101.3000566.1/ct_xray_data.h5')
# print(f.tree)
#

filename = '/home/jabbar/tomo_project/CTGAN/data/LIDC-HDF5-256/LIDC-IDRI-0810.20000101.30307.1/ct_xray_data.h5'
data = h5py.File(filename, 'r')
print(type(data))
#
for key in data.keys():
     print(key)

print(type(data['ct']))
print(type(data['xray1']))
print(type(data['xray2']))
print(type(data['ori_size']))
print(type(data['spacing']))



'''
f = nx.nxload('/home/jabbar/tomo_project/CTGAN/data/LIDC-HDF5-256/LIDC-IDRI-0001.20000101.3000566.1/ct_xray_data.h5')
print(f.tree)

with h5py.File('/home/jabbar/tomo_project/CTGAN/data/LIDC-HDF5-256/LIDC-IDRI-0001.20000101.3000566.1/ct_xray_data.h5' , 'r') as hdf:
    ls = list(hdf.keys())
    print('List of datasets in this file: ', ls)
    import nexusformat.nexus as nx
#    data = hdf.get('dataset1')

#h5showTree('/home/jabbar/tomo_project/CTGAN/data/LIDC-HDF5-256/LIDC-IDRI-0001.20000101.3000566.1/ct_xray_data.h5')

#h5showTree(filename [, location])
'''