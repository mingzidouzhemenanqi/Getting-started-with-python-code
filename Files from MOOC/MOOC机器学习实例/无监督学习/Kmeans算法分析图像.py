# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:42:36 2019

@author: Forry
"""

import numpy as np
from sklearn.cluster import KMeans#load KMeans
import PIL.Image as image

#function of loading data
def loaddata(filepath):
    #Open the file in binary form
    f = open(filepath, 'rb')
    data = []
    #Return photo pixel values as a list
    img = image.open(f)
    #Get image size
    m, n = img.size
    #Normalize each pixel RGB
    for i in range(m):
        for j in range(n):
            x, y, z, =img.getpixel((i, j))
            data.append([x/256.0, y/256.0, z/256.0])
    f.close()
    return np.mat(data),m,n

#load data
imgdata, row, col = loaddata('Kmeans/bull.jpg')

#Get the category of each pixel by clustering
label = km.fit_predict(imgdata)
label = label.reshape([row, col])
#Create a new grayscale image to save the cluster results
pic_new = image.new('L', (row, col))
#Add a gray value to the image based on its category
for i in range(row):
    for j in range(col):
        pic_new.putpixel((i, j), 256 / (label[i][j]+1))
#Save the image in jpeg format
pic_new.save("result-bull-4.jpg", "JPEG")
    
    
    
    
    
    
    
    

