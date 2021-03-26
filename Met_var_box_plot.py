# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 10:39:50 2014

@author: Rudra
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


xls = pd.ExcelFile('E:/PhD_measurement_paper/Field_data/March_2011_GRIMM_ICE_1.xls')
df = xls.parse('Sheet1', index_col=None, na_values=['NA'])
df.to_csv('E:/PhD_measurement_paper/Field_data/March_2011_GRIMM_ICE_33.csv')     
f=open('E:/PhD_measurement_paper/Field_data/March_2011_GRIMM_ICE_33.csv','r')


xls = pd.ExcelFile('E:\PhD_measurement_paper\After_Reviewer_comments_APAS\May_2011_GRIMM.xlsx');
df = xls.parse('Sheet1', index_col=None, na_values=['NA'])
df.to_csv('E:\PhD_measurement_paper\After_Reviewer_comments_APAS\May_2011_GRIMM.csv')
f = open('E:\PhD_measurement_paper\After_Reviewer_comments_APAS\May_2011_GRIMM.csv','r')





#file = /SEAES/Field_work/Data_and_Analysis/Nagarkot_compiled_data_1/VAISALA_compiled_data/DATA/1_VAISALA_MARCH_2011/VAISALA_March_2011.dat'
f = 'E:\PhD_measurement_paper\2nd_paper\Data_and_Graph\VAISALA_compiled_data\DATA\1_VAISALA_MARCH_2011\VAISALA_March_2011.dat'

df = pd.read_csv(f, header = 2, skipinitialspace=True, sep = ',')

grimm_data = np.genfromtxt(f, delimiter=',')         
Total_conc = grimm_data[:,3]    

#T = np.reshape(Total_conc,(25,24)) #March

T = np.reshape(Total_conc,(16,24)) #May  
t = T[0:6,:]
t1 = T[7:16,:]
#T1 = [t1, t]
#T2 = np.append([t],[t1],axis=0)
T3 = np.concatenate((t1, t), axis=0)
 
plt.boxplot(T3) 
plt.ylim([0, 2000])



 