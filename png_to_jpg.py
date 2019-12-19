import os
from PIL import Image

ROOT_PATH = './data/VOC2007/JPEGImages'

pngs = os.listdir(ROOT_PATH)

for png in pngs:
    if png == '.DS_Store':
        continue
    img = Image.open('{}/{}'.format(ROOT_PATH, png))
    rgb_im = img.convert('RGB')
    filename = png.replace('.png', '.jpg')
    rgb_im.save(filename)


