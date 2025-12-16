# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:58:00 2024

@author: jyshin
"""
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("dog.jpg")

plt.imshow(img)
plt.show()
