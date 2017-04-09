import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
count = 0 
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
f=open('./grey.csv','ab')
for files in os.listdir('./dataImage'):
    path=os.path.join('./dataImage',files)
    img = mpimg.imread(path)     
    gray = rgb2gray(img)
    print "opening Image"
    np.savetxt(f,gray,delimiter=',')
    count+=1
    print files + "Image done"
f.close()
print "completed"