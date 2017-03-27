import glob
import numpy as np

def load_image_dataset(dataset_dir):
    classes = glob.glob(dataset_dir + '*')
    n_classes = len(classes)
    image_names = []
    n_images_per_class = np.zeros(n_classes, dtype=np.int)

    label_index = 0
    for c in classes:
        #print c
        names = glob.glob(c + '/*.jpg')
        for n in names:
            image_names.append(n)
        n_images_per_class[label_index] = len(names)
        #print '\t number of images = ' + str(len(names))
        label_index += 1
    
    n_images = sum(n_images_per_class)
    return n_images, classes, image_names


