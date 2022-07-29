#%%
from alpaca import Camera, Telescope
from astropy.io import fits

import pandas as pd
from pandas import DataFrame,Series

from matplotlib import pyplot as plt
#%%

# %%
c = Camera('127.0.0.1:11111', 1)
# %%
c.cameraxsize()
# %%
c.cameraysize()
# %%
c.ccdtemperature()
# %%
c.cansetccdtemperature()
# %%
c.electronsperadu()
# %%
c.exposuremax()
# %%
c.exposuremin()
# %%
c.gain()
# %%
c.gainmax()
# %%
c.gainmin()

# %%
c.imageready()
# %%
# c.lastexposureduration()
# %%
c.startexposure(5,True)
# c.percentcompleted()
# %%
c.imageready()
# %%
imgArray: DataFrame = DataFrame(c.imagearray())

# %%
imgArray
# %%
#https://docs.astropy.org/en/stable/nddata/index.html
#https://docs.astropy.org/en/stable/table/index.html
#https://docs.astropy.org/en/stable/io/fits/index.html
#https://daleghent.com/2020/08/understanding-camera-offset
#https://cloudbreakoptics.com/blogs/news/astrophotography-pixel-by-pixel-part-3

#https://www.astro.princeton.edu/PBOOK/welcome.htm
# f = fits.
# imgArray.plot()
# %%
# imgArray.values
# %%
plt.imshow(imgArray.values)
# %%
# imgArray.plot().imshow(imgArray.values)
# %%
imgArray.max().max()/16
# %%
imgArray.min().min()/16
# %%
2**12
# %%
