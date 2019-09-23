from PIL import Image,ImageFont
import os
import matplotlib.font_manager as fm
from tkinter import ttk,font  
import tkinter as tk  
import random

def generateTrainImage(fontSize):

    font_size = fontSize

    font = ImageFont.truetype(fm.findfont(fm.FontProperties(family=combo.get())),font_size)
    for char in "ABCDEFGHIJ":
        im = Image.Image()._new(font.getmask(char))
        im.save("train_pics/train_pics_%s/"%font_size + char + ".jpg")


def generateTestImage():
    from scipy import misc
    import numpy as np

    # 0. Read the image
    alphabet = ["A","B","C","D","E","F","G","H","I","J"]
    fonts_size = ["16", "32", "64"]
    noises = [0.1,0.3,0.6]
    for noise in noises:
        for font_size in fonts_size:
            for alpha in alphabet:

                image  = misc.imread('train_pics/train_pics_%s/%s.jpg'%(font_size,alpha),mode="L")
                # print(image)
                pixels_number = int(image.shape[0]) * int(image.shape[1])
                # noise = 1/10
                random_values =random.sample(range(0,pixels_number), int(noise*pixels_number))
                new_image = image
        
                for i in random_values:
                    row = int(i/image.shape[1])
                    column = int(i%image.shape[1])
                    if new_image[row][column] < 125 :
                        new_image[row][column] = 255
                    elif new_image[row][column] > 125:
                        new_image[row][column] = 0    

                # print(new_image)
                img = Image.fromarray(new_image, mode="L")
                img.save("test_pics/test_pics_%s_%s/%s.jpg"%(font_size,int(noise*100),alpha))


    # 1. Add noises to the image
    # 47 *44
    # print(image.shape)
    # noisy1 = image + 3 * image.std() * np.random.random(image.shape)

    # alot  = 2 * image.max() * np.random.random(image.shape)
    # noisy2 = image + alot

    # 2. Plot the noisy image
    # import matplotlib.pyplot as plt
    # f, axarr = plt.subplots(2, 2)
    # axarr[0, 0].imshow(image,cmap = plt.get_cmap('gray'))
    # axarr[0, 0].set_title('Image gray')

    # axarr[0, 1].imshow(noisy1,cmap = plt.get_cmap('gray'))
    # axarr[0, 1].set_title('Image noise 1')

    # axarr[1, 0].imshow(noisy2,cmap = plt.get_cmap('gray'))
    # axarr[1, 0].set_title('Image noise 2')

    # axarr[1, 1].imshow(alot,cmap = plt.get_cmap('gray'))
    # axarr[1, 1].set_title('Added Noise')

    # plt.show() 
if __name__ == "__main__":
    root = tk.Tk()
    fonts=list(font.families())  
    fonts.sort()  
    combo = ttk.Combobox(root,value=fonts)    
    combo.pack()
    for i in [16,32,64]:
        generateTrainImage(i)
    generateTestImage()
