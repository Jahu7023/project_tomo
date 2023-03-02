## Instructions

# Project_Tomo: Reconstructing CT from Stack of Tomosynthesis images and a 2D X-Rays2 with Generative Adversarial Networks

## Introduction
-----

## Requirements
----
1. pytorch>=0.4 versions had been tested 
2. python3.6 was tested
3. python dependencies, please see the requirements.txt file
4. CUDA8.0 and cudnn7.0 had been tested

## Installation
----
- Install Python 3.6.0
- pip install -r requirements.txt
- Install pytorch 0.41 or above
- Make sure CUDA and cudnn are installed

----

### Input Arguments
+ --ymlpath: path to the configuration file of the experiment
+ --gpu: specific which gpu device is used for testing, multiple devices use "," to separate, e.g. --gpu 0,1,2,3
+ --dataroot: path to the test data
+ --dataset: flag indicating data is for training, validation or testing purpose
+ --tag: name of the experiment that includes the trained model
+ --data: input dataset prefix for saving and loading purposes, e.g. Scapis100 
+ --dataset_class: input data format, e.g. single view X-Rays or multiview X-Rays, see lib/dataset/factory.py for the complete list of supported data input format
+ --model_class: flag indicating the selected model, see lib/model/factory.py for the complete list of supported models
+ --datasetfile: the file list used for testing
+ --resultdir: output path of the algorithm
+ --check_point: the selected training iteration to load the correct checkpoint of the model
+ --how_many: how many test samples will be run for visualization (useful for visual mode only)
+ --valid_datasetfile: the file list used for validation


### Train from Scratch
The code is set to run from Pycharm's terminal.
Go to the following directory (CTGAN) before running the code. ---> /home/jabbar/project_tomo/CTGAN
Then please use the example settings below to train, test the model or to view the results. 

1. **Single-view Input Parameters for Training Script：**  
python3 train.py --ymlpath=./experiment/singleview2500/d2_singleview2500.yml  --gpu=0  --dataroot=/home/jabbar/results_project_tomo/data/Scapis100 --dataset=train --tag=d2_singleview2500 --data=LIDC256 --dataset_class=align_ct_xray_std --model_class=SingleViewCTGAN --datasetfile=/home/jabbar/results_project_tomo/data/train.txt --valid_datasetfile=/home/jabbar/results_project_tomo/data/test.txt --valid_dataset=test    

3. **Multi-view Input Parameters for Training Script：**
   **Multi-view model is not trained yet, as only TomoData(xray1) is available in .hdf5 folder.**
python3 train.py --ymlpath=./experiment/multiview2500/d2_multiview2500.yml --gpu=0 --dataroot=/home/jabbar/results_project_tomo/data/SCAPISData1 --dataset=train --tag=d2_multiview2500 --data=LIDC256 --dataset_class=align_ct_xray_views_std --model_class=MultiViewCTGAN --datasetfile=/home/jabbar/results_project_tomo/data/train.txt --valid_datasetfile=/home/jabbar/results_project_tomo/data/test.txt --valid_dataset=test

### Test the Models
Please use the following example settings to test our model. 
 
1. **Single-view Input Parameters for Test Script：**
python3 test.py --ymlpath=./experiment/singleview2500/d2_singleview2500.yml --gpu=0 --dataroot=/home/jabbar/results_project_tomo/data/Scapis100 --dataset=test --tag=d2_singleview2500 --data=LIDC256 --dataset_class=align_ct_xray_std --model_class=SingleViewCTGAN --datasetfile=/home/jabbar/results_project_tomo/data/test.txt --resultdir=/home/jabbar/results_project_tomo/singleview --check_point=30 --how_many=3

2. **Multi-view Input Parameters for Test Script：**  
python3 test.py --ymlpath=./experiment/multiview2500/d2_multiview2500.yml --gpu=0 --dataroot=/home/jabbar/results_project_tomo/data/SCAPISData1 --dataset=test --tag=d2_multiview2500 --data=LIDC256 --dataset_class=align_ct_xray_views_std --model_class=MultiViewCTGAN --datasetfile=./data/test.txt --resultdir=./multiview --check_point=90 --how_many=3

### To visualize
1. **Single-view Input Parameters for result view Script：**
python3 visual.py --ymlpath=./experiment/singleview2500/d2_singleview2500.yml --gpu=0 --dataroot=/home/jabbar/results_project_tomo/data/Scapis100 --dataset=test --tag=d2_singleview2500 --data=LIDC256 --dataset_class=align_ct_xray_std --model_class=SingleViewCTGAN --datasetfile=/home/jabbar/results_project_tomo/data/test.txt --resultdir=/home/jabbar/results_project_tomo/singleview --check_point=30 --how_many=3

2. **Multi-view Input Parameters for result view Script：**  
python3 visual.py --ymlpath=./experiment/multiview2500/d2_multiview2500.yml --gpu=0 --dataroot=/home/jabbar/results_project_tomo/data/SCAPISData1 --dataset=test --tag=d2_multiview2500 --data=LIDC256 --dataset_class=align_ct_xray_views_std --model_class=MultiViewCTGAN --datasetfile=./data/test.txt --resultdir=./multiview --check_point=90 --how_many=3


## Results
----
Qualitative results will be available soon. 
Quantitative results will be available soon.

## TODO

## Acknowledgement
----
I thank SCAPIS for providing the data used to build our algorithm.