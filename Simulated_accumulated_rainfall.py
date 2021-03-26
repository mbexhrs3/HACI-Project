# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 21:01:12 2014

@author: Rudra
"""

import sys
import os 
import matplotlib
from netCDF4 import *
import numpy as np
import matplotlib.pyplot as plt
import numpy.ma as ma
from mpl_toolkits.basemap import Basemap, shiftgrid, addcyclic
from scipy.interpolate import interp1d


matplotlib.rcParams.update({'font.size': 18,'font.family':'Times New Roman'})

filename='/HOME/rrs/WRF/wrfpractice/Modelling_paper_II/RAINNC_MORRISON.nc';

nc_file=Dataset(filename)
var_name='RAINNC'
var_names=nc_file.variables.keys()

rain_morrison = nc_file.variables['RAINNC']
rain_MOR=rain_morrison[78,:,:]

##########

filename='/HOME/rrs/WRF/wrfpractice/Modelling_paper_II/RAINNC_LIN.nc';

nc_file=Dataset(filename)
var_name='RAINNC'
var_names=nc_file.variables.keys()

rain_lin = nc_file.variables['RAINNC']
rain_LIN=rain_lin[78,:,:]

##########

filename='/HOME/rrs/WRF/wrfpractice/Modelling_paper_II/RAINNC_WDM6.nc';

nc_file=Dataset(filename)
var_name='RAINNC'
var_names=nc_file.variables.keys()

rain_wdm6 = nc_file.variables['RAINNC']
rain_WDM6=rain_wdm6[78,:,:]

##########

filename='/HOME/rrs/WRF/wrfpractice/Modelling_paper_II/RAINNC_WSM6.nc';

nc_file=Dataset(filename)
var_name='RAINNC'
var_names=nc_file.variables.keys()

rain_wsm6 = nc_file.variables['RAINNC']
rain_WSM6=rain_wsm6[78,:,:]

######## Just for ground contour ###
filename='/HOME/rrs/WRF/wrfpractice/Modelling_paper_II/wrfout_d03_constPurturb_medium_ctrlT.nc';

nc_file=Dataset(filename)
##############

#rain_diff_MOR_LIN = rain_MOR - rain_LIN

##########
vmin = 10.0
vmax = 200.0

lats=nc_file.variables['XLAT'][:]
lons=nc_file.variables['XLONG'][:]
V=np.linspace(1,200,30)
fig=plt.figure(10,figsize=(10,8))
fig.subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=-0.12,hspace=0.1)
ax = fig.add_subplot(221)
my_cmap = matplotlib.cm.get_cmap('rainbow')
CS=plt.contourf(lons,lats,rain_LIN,V)  #make a filled contour plot 
plt.clim(vmin, vmax)
my_cmap.set_under('w')
ax=plt.gca()
ax.tick_params(which='major', width=2, length=5)
plt.tick_params(direction='out', top=False, right=False) # Turn ticks out
matplotlib.rcParams.update({'font.size': 16,'xtick.major.width': 1.5,'figure.figsize': (10.0, 8.0)})
cbar = plt.colorbar(CS, ticks=np.linspace(10,250,9))
fig.delaxes(fig.axes[1])
plt.plot([85.5], [27.7],'ro', ms=10)
plt.text(0.65, 0.41,'N', horizontalalignment='center',verticalalignment='center', transform=ax.transAxes,fontsize=25,fontweight='bold',color='red')
plt.text(0.17, 0.1,'a) Lin', horizontalalignment='center',verticalalignment='center', transform=ax.transAxes,fontsize=14,fontweight='bold',color='k')
hgt=nc_file.variables['HGT']
hgt_mean=np.average(hgt,axis=0)
V1=np.linspace(300,6000,20)
plt.contour(lons,lats,hgt_mean,V1,colors='k')
#plt.xlabel('Longitude ($^{o}$)',fontsize=18)
plt.ylabel('Latitude [$^{o}$N]',fontsize=18)

ax.set_xticklabels([''])

#plt.savefig('Morrison',dpi=150)

#########

ax = fig.add_subplot(222)
my_cmap = matplotlib.cm.get_cmap('rainbow')
CS=plt.contourf(lons,lats,rain_MOR,V)  #make a filled contour plot 
plt.gcf().subplots_adjust(wspace=-0.12,hspace=0.1)
plt.clim(vmin, vmax)
my_cmap.set_under('w')
ax=plt.gca()
ax.tick_params(which='major', width=2, length=5)
plt.tick_params(direction='out', top=False, right=False) # Turn ticks out
matplotlib.rcParams.update({'font.size': 16,'xtick.major.width': 1.5,'figure.figsize': (10.0, 8.0)})
cbar = plt.colorbar(CS, ticks=np.linspace(10,250,9))
plt.plot([85.5], [27.7],'ro', ms=10)
plt.text(0.65, 0.41,'N', horizontalalignment='center',verticalalignment='center', transform=ax.transAxes,fontsize=25,fontweight='bold',color='red')
plt.text(0.17, 0.1,'b) Morrison', horizontalalignment='center',verticalalignment='center', transform=ax.transAxes,fontsize=14,fontweight='bold',color='k')
hgt=nc_file.variables['HGT']
hgt_mean=np.average(hgt,axis=0)
V1=np.linspace(300,6000,20)
plt.contour(lons,lats,hgt_mean,V1,colors='k')
#plt.xlabel('Longitude ($^{o}$)',fontsize=18)
#plt.ylabel('Latitude ($^{o}$)',fontsize=18)
ax.set_xticklabels([''])
ax.set_yticklabels([''])

#plt.savefig('Lin',dpi=150)



#########

#########

ax = fig.add_subplot(223)
my_cmap = matplotlib.cm.get_cmap('rainbow')
CS=plt.contourf(lons,lats,rain_WDM6,V)  #make a filled contour plot 
plt.gcf().subplots_adjust(wspace=-0.12,hspace=0.1)
plt.clim(vmin, vmax)
my_cmap.set_under('w')
ax=plt.gca()
ax.tick_params(which='major', width=2, length=5)
plt.tick_params(direction='out', top=False, right=False) # Turn ticks out
matplotlib.rcParams.update({'font.size': 16,'xtick.major.width': 1.5,'figure.figsize': (10.0, 8.0)})
cbar = plt.colorbar(CS, ticks=np.linspace(10,250,9))
fig.delaxes(fig.axes[4])
plt.plot([85.5], [27.7],'ro', ms=10)
plt.text(0.65, 0.41,'N', horizontalalignment='center',verticalalignment='center', transform=ax.transAxes,fontsize=25,fontweight='bold',color='red')
plt.text(0.17, 0.1,'c) WDM6', horizontalalignment='center',verticalalignment='center', transform=ax.transAxes,fontsize=14,fontweight='bold',color='k')
hgt=nc_file.variables['HGT']
hgt_mean=np.average(hgt,axis=0)
V1=np.linspace(300,6000,20)
plt.contour(lons,lats,hgt_mean,V1,colors='k')
plt.xlabel('Longitude [$^{o}$E]',fontsize=18)
plt.ylabel('Latitude [$^{o}$N]',fontsize=18)
#ax.set_xticklabels([''])
#ax.set_yticklabels([''])

#plt.savefig('WSM6',dpi=150)

####################################################################


ax = fig.add_subplot(224)
my_cmap = matplotlib.cm.get_cmap('rainbow')
CS=plt.contourf(lons,lats,rain_WSM6,V)  #make a filled contour plot 
plt.gcf().subplots_adjust(wspace=-0.12,hspace=0.1)
plt.clim(vmin, vmax)
my_cmap.set_under('w')
ax=plt.gca()
ax.tick_params(which='major', width=2, length=5)
plt.tick_params(direction='out', top=False, right=False) # Turn ticks out
matplotlib.rcParams.update({'font.size': 16,'xtick.major.width': 1.5,'figure.figsize': (10.0, 8.0)})
cbar = plt.colorbar(CS, ticks=np.linspace(10,250,9))
#fig.delaxes(fig.axes[4])
plt.plot([85.5], [27.7],'ro', ms=10)
plt.text(0.65, 0.41,'N', horizontalalignment='center',verticalalignment='center', transform=ax.transAxes,fontsize=25,fontweight='bold',color='red')
plt.text(0.17, 0.1,'d) WSM6', horizontalalignment='center',verticalalignment='center', transform=ax.transAxes,fontsize=14,fontweight='bold',color='k')
hgt=nc_file.variables['HGT']
hgt_mean=np.average(hgt,axis=0)
V1=np.linspace(300,6000,20)
plt.contour(lons,lats,hgt_mean,V1,colors='k')
plt.xlabel('Longitude [$^{o}$E]',fontsize=18)
#plt.ylabel('Latitude ($^{o}$)',fontsize=18)
#ax.set_xticklabels([''])
ax.set_yticklabels([''])

plt.savefig('Accumulated_Rainfall',dpi=150)


os.system("convert Accumulated_Rainfall.png Accumulated_Rainfall.pdf")
#os.system ("rm -f *.png")