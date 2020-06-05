import os
import re

def get_image(name):
    path = os.path
    data = os.listdir('extra_images')
    for e in data :
        if re.match(name,e):
            path = os.path.abspath(os.path.join("extra_images/",e))
            return path

def get_initial_image():
    return get_image(r"initial\x2epng")

def get_final_image():
    return get_image(r"final\x2epng")

def get_solution_image():
    return get_image(r"solution\x2epng")

def get_left_key():
    return get_image(r"flat.*left\x2epng")

def get_right_key():
    return get_image(r"flat.*right\x2epng")

def get_up_key():
    return get_image(r"flat.*up\x2epng")

def get_down_key():
    return get_image(r"flat.*down\x2epng")

def get_black_background():
    return get_image(r"flat.*cover\x2epng")