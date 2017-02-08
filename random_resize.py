import os
from os.path import exists, join
from PIL import Image
import random


def resize(path, out_path="export"):
    r = os.walk(path)
    if not exists(out_path):
        os.makedirs(out_path)
    for dir_path, dirnames, filenames in r:
        dirname = os.path.split(dir_path)[1]

        for filename in filenames:
            if filename.endswith('.jpg'):
                pic = Image.open(join(dir_path, filename))
                size = pic.size
                for i in range(10):
                    r_size = generate_size(size)
                    t_pic = pic.resize(r_size)
                    prefix = str(r_size[0]) + "*" + str(r_size[1])
                    t_pic.save(join(out_path, prefix + "_" + filename))


def generate_size(size):
    r_int = random.randint(0, 1)
    r_increase = random.randint(5, 90)

    if r_int == 1:
        return int(size[0] * (100 + r_increase) / 100), int(size[1] * (100 + r_increase) / 100)

    if r_int == 0:
        return int(size[0] * (100 - r_increase) / 100), int(size[1] * (100 - r_increase) / 100)


if __name__ == '__main__':
    resize("image")
