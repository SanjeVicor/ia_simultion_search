import os
import re
import shutil

def get_images():
    path = os.path
    data = os.listdir('characters')
    paths = []
    print(data)
    for e in data:
        print(e)
        if re.fullmatch(r".+\x2e(jpg|png)", e):
            paths.append(os.path.abspath(os.path.join("characters/",e)))

    print(paths)
    return paths

def copy_image(file_path):
    file_format = file_path.split("/")[-1]
    file_format = file_format.split(".")[-1]
    print("Nuevo nombre ", file_path)
    file_name = file_path.split("/")[-1]
    print("Nuevo nombre ", file_name)

    file_name = file_name.split(".")
    print("Nuevo nombre ", file_name)
    file_name = file_name[0]
    print("Nuevo nombre ", file_name) 
    file_name += f".{file_format}"
    ok = shutil.copyfile(file_path,os.path.abspath(os.path.join(f"characters/{file_name}")))
    if ok :
        return file_name,ok