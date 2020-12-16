from pydicom import dcmread
import sys
import os
from shutil import copy

sys.path.append('/E/HNSCC/')
if not os.path.isdir('E:\RTSTRUCT_DIR'):
    os.mkdir('E:\RTSTRUCT_DIR')

for i in range(1, 216):
    dirr = 'E:\HNSCC\HNSCC-01-' + "{:04d}".format(i) # E:\HNSCC\HNSCC-01-0001
    for item in os.listdir('E:\HNSCC\HNSCC-01-' + "{:04d}".format(i)):
        if 'RT SIMULATION' not in item:
            pass
        else:
            dirrr = dirr + '\\' + item # E:\HNSCC\HNSCC-01-0001\12-05-1998-RT SIMULATION-43582
            for folders in os.listdir(dirrr):
                dirrrr = dirrr + '\\' + folders # E:\HNSCC\HNSCC-01-0001\12-05-1998-RT SIMULATION-43582\1.000000-78710
                for file in os.listdir(dirrrr):
                    ds = dcmread(dirrrr + '\\' + file)
                    # Put all RT struct in one folder
                    # if ds.Modality == 'RTSTRUCT':
                    #     dirrrrr = dirrrr + '\\' + file
                    #     new_file_name = dirrrr + '\\' + f'{str(i)}'
                    #     os.rename(dirrrrr, new_file_name)
                    #     copy(new_file_name, 'E:\RTSTRUCT_DIR')
                    #     break
                    # Put all CT scan folder in one folder
                    if ds.Modality == 'CT':
                        if not os.path.isdir(f'E:\Restructured_data\CT_DIR\{str(i)}'):
                            os.mkdir(f'E:\Restructured_data\CT_DIR\{str(i)}')
                        copy(dirrrr + '\\' + file, f'E:\Restructured_data\CT_DIR\{str(i)}')
            print(i)
