import os
import re
import shutil

def get_images():
    path = os.path
    data = os.listdir('characters')
    paths = []
    for e in data:
        if re.fullmatch(r".+\x2e(jpg|png)", e):
            paths.append(os.path.abspath(os.path.join("characters/",e)))
    return paths

def copy_image(file_path):
    file_format = file_path.split("/")[-1]
    file_format = file_format.split(".")[-1]
    file_name = file_path.split("/")[-1]
    file_name = file_name.split(".")
    file_name = file_name[0] 
    file_name += f".{file_format}"
    try:
        ok = shutil.copyfile(file_path,os.path.abspath(os.path.join(f"characters/{file_name}")))
    except:
        return
    if ok :
        return file_name,ok