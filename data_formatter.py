import os
from tqdm import tqdm
from shutil import copy, rmtree

base_path = '.'
target = '/trainannot/'

# get folders
folders = os.listdir(base_path)
folders = [folder for folder in folders if os.path.isdir(folder) and folder.isdigit()]

# copy files
for folder in tqdm(folders):
    # training part
    for file in os.listdir(folder):
        copy(base_path+'/'+folder+'/'+file, base_path+'/'+file)
        copy(base_path+'/'+folder+'.png', base_path+target+file[:-4]+'.png')

# remove old folders
for folder in folders:
    rmtree(base_path+'/'+folder)
    os.remove(base_path+'/'+folder+'.png')