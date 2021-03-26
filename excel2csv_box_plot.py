# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 10:39:50 2014

@author: Rudra
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

matplotlib.rcParams.update({'font.size': 20,'font.family':'Times New Roman'})


xls = pd.ExcelFile('E:/PhD_measurement_paper/Field_data/March_2011_GRIMM_ICE_1.xls')
df = xls.parse('Sheet1', index_col=None, na_values=['NA'])
df.to_csv('E:/PhD_measurement_paper/Field_data/March_2011_GRIMM_ICE_33.csv')     
f=open('E:/PhD_measurement_paper/Field_data/March_2011_GRIMM_ICE_33.csv','r')


xls = pd.ExcelFile('E:\PhD_measurement_paper\After_Reviewer_comments_APAS\May_2011_GRIMM.xlsx');
df = xls.parse('Sheet1', index_col=None, na_values=['NA'])
df.to_csv('E:\PhD_measurement_paper\After_Reviewer_comments_APAS\May_2011_GRIMM.csv')
f = open('E:\PhD_measurement_paper\After_Reviewer_comments_APAS\May_2011_GRIMM.csv','r')


grimm_data = np.genfromtxt(f, delimiter=',')         
Total_conc = grimm_data[:,3]    

#T = np.reshape(Total_conc,(25,24)) #March

T = np.reshape(Total_conc,(16,24)) #May  
t = T[0:6,:]
t1 = T[7:16,:]
#T1 = [t1, t]
#T2 = np.append([t],[t1],axis=0)
T3 = np.concatenate((t1, t), axis=0)

plt.figure(1,figsize=(8,8))

plt.boxplot(T3) 
#plt.ylim([0, 2000])

ax = plt.gca()
ax.set_yticklabels([])
plt.xticks(range(24),('00:00','','','','04:00','','','','08:00','','','','12:00','','','','16:00','','','','20:00','','','23:00'))
plt.xlabel('UTC Time (h)',fontsize=22,fontweight='bold')

np.linspace(0,22,7)
 