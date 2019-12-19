import os

ROOT = './data'
def change_annotation_name():
    ANNOTATION_PATH = '{}/VOC2007/Annotations'.format(ROOT)
    annotations = os.listdir(ANNOTATION_PATH)
    for annotation in annotations:
        if annotation == '.DS_Store':
            continue
        name = annotation.replace('ball_', '')
        os.rename('{}/{}'.format(ANNOTATION_PATH, annotation), '{}/{}'.format(ANNOTATION_PATH, name))

def change_image_name():
    IMAGE_PATH = '{}/VOC2007/JPEGImages'.format(ROOT)
    images = os.listdir(IMAGE_PATH)
    for image in images:
        if image == '.DS_Store':
            continue
        name = image.replace('ball_', '')
        os.rename('{}/{}'.format(IMAGE_PATH, image), '{}/{}'.format(IMAGE_PATH, name))

if __name__ == "__main__":
    # change_annotation_name()
    change_image_name()