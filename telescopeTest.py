#%%
from alpaca import Telescope
# %%
t = Telescope('127.0.0.1:11111', 0)
# %%
t.altitude()
# %%
t.canslew()
# %%
t.name()
# %%
t.slewtocoordinates(0,90)
# %%
t.slewing()
# %%
t.trackingrates()
# %%
t.tracking()
# %%
t.declinationrate()
# %%
t.rightascensionrate()
# %%
t.declinationrate()
# %%
t.slewtocoordinates(14.8,74.1)
# %%
t.axisrates(0)
# %%
t.findhome()
# %%
t.trackingrate()
# %%
t.slewtotarget()
#%%
t.tracking(False)
# %%
kochab = {'ra':14.8,'dec':74.1}
hr6132 = {'ra':16.3,'dec':61.2}
alderamin = {'ra':21.2,'dec':62.5}
# northPole = {'ra':0,'dec':90}
# %%
observationList = [kochab,hr6132,alderamin]
#%%
t.tracking(Tracking=True)
for target in observationList:
    t.slewtocoordinates(target['ra'],target['dec'])
t.findhome()
t.tracking(Tracking=False)
# %%
t.setpark()
#%%
t.park()
# %%
t.unpark()
# %%