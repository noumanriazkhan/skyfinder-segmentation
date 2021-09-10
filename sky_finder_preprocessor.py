import os
from shutil import copy, move, rmtree
from tqdm import tqdm
from random import sample
from PIL import Image
from collections import Counter

# num of samples to get
VAL_SAMPLES = 13500
TEST_SAMPLES = 13500
base_path = '.'

# get folders
folders = os.listdir(base_path)
folders = [folder for folder in folders if os.path.isdir(folder) and folder.isdigit()] 

# make required folders
new_folders = ['train', 'trainannot', 'val', 'valannot', 'test', 'testannot']
for folder in new_folders:
    os.mkdir(folder)

# copy files
for folder in tqdm(folders):
    # training part
    for file in os.listdir(folder):
        copy(base_path+'/'+folder+'/'+file, base_path+'/train/'+file)
        copy(base_path+'/'+folder+'.png', base_path+'/''trainannot/'+file[:-4]+'.png')

# get validation and test names
train_names = os.listdir(base_path+'/'+'train')


val_names = sample(train_names, VAL_SAMPLES)
train_names = list((Counter(train_names) - Counter(val_names)).elements())

test_names = sample(train_names, TEST_SAMPLES)
train_names = list((Counter(train_names) - Counter(test_names)).elements())

# move validation files
for file in val_names:
    move(base_path+'/train/'+file, base_path+'/val/'+file)
    move(base_path+'/trainannot/'+file[:-4]+'.png', base_path+'/valannot/'+file[:-4]+'.png')

# move test files
for file in test_names:
    move(base_path+'/train/'+file, base_path+'/test/'+file)
    move(base_path+'/trainannot/'+file[:-4]+'.png', base_path+'/testannot/'+file[:-4]+'.png')

# remove old folders
for folder in folders:
    rmtree(folder)
    os.remove(folder+'.png')
   
