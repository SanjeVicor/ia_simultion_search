import os
import re

def get_initial_image():
    path = os.path
    print(path)
    data = os.listdir('extra_images')
    print(data)
    for e in data :
        print(e)
        print(re.match(r"initial",e))
        if re.match(r"initial",e):
            path = os.path.abspath(os.path.join("extra_images/",e))
            return path

def get_final_image():
    path = os.path
    print(path)
    data = os.listdir('extra_images')
    print(data)
    for e in data :
        print(e)
        print(re.match(r"final",e))
        if re.match(r"final",e):
            path = os.path.abspath(os.path.join("extra_images/",e))
            return path
