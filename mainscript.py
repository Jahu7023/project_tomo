ymlpath = './experiment/singleview2500/d2_singleview2500.yml'
gpu = 0
dataroot = './data/LIDC-HDF5-256'
dataset =  'train'
tag = 'd2_singleview2500'
data = 'LIDC256 --dataset_class=align_ct_xray_std'
model_class = 'SingleViewCTGAN'
datasetfile = './data/train.txt'
valid_datasetfile = './data/test.txt'
valid_dataset = 'test'