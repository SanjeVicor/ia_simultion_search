import os
import re
import shutil

def get_images():
    path = os.path
    data = os.listdir('lands')
    paths = []
    #print(data)
    for e in data:
        #print(e)
        if re.fullmatch(r".+\x2e(jpg|png)", e):
            paths.append(os.path.abspath(os.path.join("lands/",e)))

    #print(paths)
    return paths

def copy_image(file_path,file_name):
    file_format = file_path.split("/")[-1]
    file_format = file_format.split(".")[-1]
    file_name += f".{file_format}"
    try:
        ok = shutil.copyfile(file_path,os.path.abspath(os.path.join(f"lands/{file_name}")))
    except :
        return
    if ok :
        return ok