'''
Function copypasteall(src, dest):

    Input:
    src: source directory (string)
    dest: destination directory (string)

    This function copy all files in src and paste them into dest.

'''
import os
import shutil


def copypasteall(src, dest):
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)