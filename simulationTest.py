#%%
from math import pi
import numpy as np
from numpy import ndarray, number
from astropy.modeling.models import *
import matplotlib.pyplot as plt

from random import random,randint

import pandas as pd
from pandas import DataFrame,Series
# %%
# y, x = np.mgrid[0:500, 0:600]

# data = (Gaussian2D(1, 150, 100, 20, 10, theta=0.5)(x, y) +
#     Gaussian2D(0.5, 400, 300, 8, 12, theta=1.2)(x,y) +
#     Gaussian2D(0.75, 250, 400, 5, 7, theta=0.23)(x,y) +
#     Gaussian2D(0.9, 525, 150, 3, 3)(x,y) +
#     Gaussian2D(0.6, 200, 225, 3, 3)(x,y))
# x
#%%
# a,b = np.mgrid[0:30,0:50]
# #%%
# imageData = np.zeros((5496,3672))
# #%%
# imageData.shape
# #%%
# ab = Gaussian2D(1, 2, 3, 0.5, 1, theta=0.5)(imageData[0],imageData[1])
# ab
# #%%
# a[0],b[0]
# #%%
# ab[0,0]
# #%%
# Gaussian2D(1, 2, 3, 0.5, 1, theta=0.5)(0,0)
Gaussian2D().evaluate(0,0,1, 2, 3, 0.5, 1, theta=0.5)
#%%
np.mgrid[0:3,0:5]
#%%
# data = Gaussian2D(1, 150, 100, 20, 10, theta=0.5)(x, y)
#%%
def randomGalaxy(xMin: int = 0,xMax: int = 5496,yMin: int = 0,yMax: int = 3672) -> ndarray:
    '''
    # Random Galaxy

    Returns a random gaussian 2D galaxy.
    '''
    return Gaussian2D(
        amplitude=random()*(2**16),
        x_mean=randint(xMin,xMax),
        y_mean=randint(yMin,yMax),
        x_stddev=random()*20,
        y_stddev=random()*20,
        theta=2*pi*random()
    )
#%%

def populateGalaxies(inputImage: ndarray, numberOfGalaxies: int = 100) -> ndarray:
# def populateGalaxies(inputImage: DataFrame, numberOfGalaxies: int = 10) -> ndarray:
# def populateGalaxies(x,y, numberOfGalaxies: int = 1) -> ndarray:
    # inputImage = np.array(inputImage)
    outputImage = np.zeros(inputImage.shape)
    # outputImage = np.zeros((len(x),len(y)))
    # outputImage = inputImage.copy()
    for i in range(0,numberOfGalaxies):
        outputImage = outputImage + randomGalaxy()(inputImage[0],inputImage[1])
        # outputImage = outputImage.apply()
        # galaxy: Gaussian2D = randomGalaxy()
        # for j in range(0,len(x) - 1):
        #     for k in range(0,len(y) - 1):
        #         outputImage[j][k] = galaxy (x[j],y[k])

    return outputImage
#%%
# def imageBasis(x: int = 5496, y: int = 3672):
#     outputImage = []
#     for _x in range(0,x):
#         for _y in range:
#             pass
#%%
imageData = np.mgrid[0:5496,0:3672]
# imageData = DataFrame([[x for x in range(0,5496)],[y for y in range(0,3672)]])
#%%
# imageData.shape
#%%
# imageData[0]
# x,y = [x for x in range(0,5496)],[y for y in range(0,3672)]
# %%
# data += 0.01 * np.random.randn(500, 600)
# cosmic_ray_value = 0.997
# data[100, 300:310] = cosmic_ray_value
# inputImage = np.array()
data = populateGalaxies(imageData)
# data = populateGalaxies(x,y)
#%%
data.shape
#%%
data2 = data[0] + data[1]
#%%
data2.shape
#%%
plt.imshow(data2, origin='lower')
# %%
