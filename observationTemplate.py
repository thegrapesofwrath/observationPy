#%%
# domeInitial = 19.8
# oIII focus 11900
import os
import time
from datetime import datetime

from matplotlib import pyplot as plt

import numpy as np
# import pandas as pd
# from pandas import DataFrame,Series

from alpaca import Telescope,Camera,Dome

import astropy
from astropy import units as u
from astropy.coordinates import SkyCoord,AltAz,EarthLocation
from astropy.io import fits
from astropy.time import Time as aTime

from alercepy import AlerceObject
#%%
ao = AlerceObject()
# %%
siriusObservatory: EarthLocation = EarthLocation(lat=35.132103*u.deg, lon=-92.381070*u.deg, height=75*u.m)
utcOffset = -6*u.hour

t = Telescope('127.0.0.1:11111', 0)
c: Camera = Camera('127.0.0.1:11111', 0)
d: Dome = Dome('127.0.0.1:11111', 0)

c.name()
d.name()
#%%
# observationList = ['ZTF21acdmwae']
observationList = ['ZTF21acpfndw']
#%%
def lookupAndSlew(id: str):
    obj = ao.singleObject(id)
    obj: SkyCoord = SkyCoord(ra=obj['meanra']*u.degree, dec=obj['meandec']*u.degree, frame='icrs')
    t.slewtocoordinates(obj.ra.hour,obj.dec.degree)
#%%
lookupAndSlew(observationList[0])