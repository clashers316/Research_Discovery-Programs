from astropy import constants as const
import astropy.units as u
import math
import pandas as pd
import numpy as np
df = pd.read_csv (r'C:\Users\madha\OneDrive\Desktop\Exo_Earth.csv')
df.head()

lst=[]
def ES(Rpe,Mpe,Tp):
    Mp = Mpe*const.M_earth
    Rp = Rpe*const.R_earth
    Te = 288
    V_earth = (4*math.pi*const.R_earth*const.R_earth*const.R_earth)
    De= (const.M_earth/V_earth)
    Vee= np.sqrt(((2*const.G*const.M_earth)/const.R_earth))
    Vep= np.sqrt(((2*const.G*Mp)/Rp))
    Vp= ((4*math.pi*Rp*Rp*Rp))
    Dp=(Mp/Vp)
    Vep = Vee*1.97
    ESIr= (1-(abs(((const.R_earth-Rp)/abs((const.R_earth+Rp))))))
    ESIr= (ESIr**0.57)
    ESIp= (1-(abs(((De-Dp)/abs((De+Dp))))))
    ESIp=(ESIp**1.07)
    ESIi= ((ESIr*ESIp)**0.5)
    ESIv= (1-(abs(((Vee-Vep)/abs((Vee+Vep))))))
    ESIv= (ESIv** 0.7)
    ESIt= (1-(abs(((Te-Tp)/abs((Te+Tp))))))
    ESIt= (ESIt** 5.58)
    ESIs= np.sqrt(ESIv*ESIt)
    ESIg= np.sqrt(ESIv*ESIt)
    return ESIg

for i in range(525):
    lst.append(ES(df.loc[i,'Rpe'],df.loc[i,'Mpe'],df.loc[i,'Temp']))

def Mass(Mpe):
    Mp = Mpe*const.M_earth/u.kg
    return Mp
def Radius(Rpe):
    Rp = Rpe*const.R_earth/u.m
    return Rp
lst2 = []
lst3 = []

for i in range(525):
    lst2.append(Mass(df.loc[i,'Mpe']))
    lst3.append(Mass(df.loc[i,'Rpe']))

df2=df.assign(ESIg = lst, Mp = lst2, Rp = lst3)
df2.head()

df2.to_csv(r'C:\Users\madha\OneDrive\Desktop\Research Discovery\ESI_Habitable3.csv', index=True)

import matplotlib.pyplot as plt
import pylab as pl

pl.title("Rpj v ESI Graph")
pl.xlabel("ESI")
pl.ylabel("Rpj")
pl.scatter(df2 ['ESIg'], df2['Rp'])

pl.title("Mp v ESI Graph")
pl.xlabel("ESI")
pl.ylabel("Mp")
pl.scatter(df2 ['ESIg'], df2['Mp'])

pl.title("Temp v ESI Graph")
pl.xlabel("ESI")
pl.ylabel("Temp")
pl.scatter(df2 ['ESIg'], df2['Temp'])
