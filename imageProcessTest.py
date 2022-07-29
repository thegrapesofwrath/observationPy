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
# %%
# ZTF21abkggoa = ao.singleObject('ZTF21abkggoa')
# %%
# ZTF21abkggoa: SkyCoord = SkyCoord(ra=ZTF21abkggoa['meanra']*u.degree, dec=ZTF21abkggoa['meandec']*u.degree, frame='icrs')
# %%
# t.slewtocoordinates(ZTF21abkggoa.ra.hour,ZTF21abkggoa.dec.degree)
#%%
#https://astroquery.readthedocs.io/en/latest/index.html#available-services
#https://pyvo.readthedocs.io/en/latest/
from astroquery.simbad import Simbad

# %%
result_table: astropy.table.Table = Simbad.query_object("M1")
# %%
result_table['RA'].data.data[0]
# %%
result_coord: SkyCoord = SkyCoord(ra=result_table['RA']*u.hour,dec=result_table['DEC'])
# %%
m1: SkyCoord = SkyCoord.from_name('M1')
# %%
m1.get_constellation()
# %%
m1.apply_space_motion()
#%%
m1.info(option='stats')
# %%
m1.match_to_catalog_3d()
m1.match_to_catalog_sky()
#%%
m1.contained_by()
#%%
enif: SkyCoord = SkyCoord.from_name('HR7949')
# %%
astroTime: aTime = aTime(datetime.now()) - utcOffset
#%%
enifAZ = enif.transform_to(AltAz(obstime=astroTime,location=siriusObservatory))
#%%
enifAZ.az.deg
# %%
# t.slewtocoordinates(enif.ra.hour, enif.dec.degree)
# %%
observationList: list = ['Enif','Polaris','HR7949','Alderamin','Vega','Crescent Nebula', 'Algenib']
outputDir: str = r'D:\\Observations'

observationDate: datetime = datetime.now()

try:
    os.mkdir(f"{outputDir}\\{observationDate.strftime('%Y-%m-%d')}")
except:
    pass

try:
    os.mkdir(f"{outputDir}\\{observationDate.strftime('%Y-%m-%d')}\\{observationDate.strftime('%H-%M-%S')}")
except:
    pass
#%%
outputDir = f"{outputDir}\\{observationDate.strftime('%Y-%m-%d')}\\{observationDate.strftime('%H-%M-%S')}" 
# %%
# cameraExposure: int = 5
# cameraGain: int = 225
# %%
def processImage(c: Camera = None, gain: int = 225, exposure: int = 5,objectId: str = 'TestCapture',outputDir: str = r'./'):
    c.gain(gain)
    c.startexposure(exposure,True)
    time.sleep(1)
    while True:
        if c.imageready() == True:
            imgTime: datetime = datetime.now()
            img: np.ndarray = np.array(c.imagearray())
            fitsHeader: fits.Header = fits.Header({
                            "AUTHOR" : "Shawn Hartley",
                            # "BITPIX" : "16",
                            "KEYWORD" : f"{objectId}",
                            "DATE" : f"{imgTime.strftime('%Y-%m-%dT%H:%M:%S[.%f]')}",
                            # "" : "",
                            # "" : "",
                            # "" : "",
                            # "" : "",
                            # "" : "",
                            # "" : "",
                            # "" : "",
            })
            imgFits: fits.ImageHDU = fits.ImageHDU(
                data=img,
                name=f"{objectId}_{imgTime.strftime('%Y-%m-%dT%H:%M:%S[.%f]')}",
                header=fitsHeader
            )
            imgFits.writeto(f"{outputDir}/{objectId}_{datetime.timestamp(imgTime)}.fits")
            break
        else:
            print(f'target: {objectId}')
            time.sleep(1)

#%%
#https://docs.astropy.org/en/stable/generated/examples/coordinates/plot_obs-planning.html#sphx-glr-generated-examples-coordinates-plot-obs-planning-py
def captureData(id: str, outputDir: str = './'):
    astroTime: aTime = aTime(datetime.now()) - utcOffset
    obj = SkyCoord.from_name(id)
    objAZ = obj.transform_to(AltAz(obstime=astroTime,location=siriusObservatory))
    d.slaved(False)
    t.slewtocoordinatesasync(obj.ra.hour,obj.dec.degree)
    d.slewtoazimuth(objAZ.az.deg)
    while t.slewing() == True or d.slewing() == True:
        print(f"Telescope: ra={t.rightascension()} dec={t.declination()}")
        print(f"Dome: az={d.azimuth()}")
        time.sleep(1)
    d.slaved(True)
    processImage(c=c,objectId=id,outputDir=outputDir)
# %%
for target in observationList:
    captureData(id=target,outputDir=outputDir)
# %%
# %%
# %%
