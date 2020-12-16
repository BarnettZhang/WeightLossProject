import sys
import os

for i in range(1, 216):
    if i == 213:
        dirr = 'E:\Restructured_data\\NIFTI_DIR\\' + str(i)
        if os.path.isdir(dirr):
            for item in os.listdir(dirr):
                if '.nii.gz' in item:
                    original_item = 'E:\Restructured_data\\NIFTI_DIR\\' + str(i) + '\\' + item
                    new_filename = 'E:\Restructured_data\\NIFTI_DIR\\' + str(i) + '\\' + str(i) + '.nii.gz'
                    os.rename(original_item, new_filename)
                else:
                    pass


