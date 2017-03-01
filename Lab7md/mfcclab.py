import scipy.io
from scipy.io import wavfile
import math

def get_num_frames(file_prefix, N, M):
    sumNumFrames = 0 #the total of frames is 0
    for i in range(1,9):# i is ranging from 1 to 8 
        filename = file_prefix + "/s%d.wav" % i #i is replaced in position of %d
        fs, data = wavfile.read(filename)#fs is the sampling rate
        numframes = int(1 + math.ceil((1.0*len(data) - N)/M)) # number of frames for one frame
        sumNumFrames = sumNumFrames + numframes
    sumNumFrames = int(sumNumFrames) # total number of frames of the data set
    return sumNumFrames

from sklearn import manifold
from itertools import cycle
import matplotlib.pyplot as plt

def plot_codebook_2D(codebook, target, target_names):
    iso = manifold.Isomap(n_neighbors=5, n_components=2)
    data = iso.fit_transform(codebook)
    colors = cycle('rgbcmykw')
    target_ids = range(len(target_names))
    plt.figure(figsize=(10, 10))
    for i, c, label in zip(target_ids, colors, target_names):
        plt.scatter(data[target == i, 0], data[target == i, 1], c=c, label=label)
    plt.legend()
    plt.title('Codewords for Speakers in 2D')
