import numpy as np
import skimage.io
import os
import matplotlib.pyplot as plt
import matplotlib . pyplot as plt
from skimage import exposure
import numpy as np
import sys




def adjust_gamma(Image,gamma):
    I=skimage.color.rgb2gray(Image);
    I = I / np.max(I) ;
    I2= exposure.adjust_gamma(I, gamma);
    return I2


if __name__ == "__main__":
    Image=skimage.io.imread('Moon.jpg')
    plt.imshow(Image,cmap='gray')
    Image.shape
    plt.show();
    I2=adjust_gamma(Image,2)
    plt.imshow(I2);
    plt.show();
