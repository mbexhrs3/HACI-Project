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


grimm_data = np.genfromtxt(f, delimiter=',')    
    
    
Total_conc = grimm_data[:,3]    
#Nbin = 24   
    
#Time_day_1 = np.linspace(1,24,24)    
    
#Time_day = np.tile(Time_day_1,25)    # create tiles of day time 

#N_total = np.asarray([Time_day, Total_conc])
#N = np.transpose(N_total)

T = np.reshape(Total_conc,(25,24)) 
 
plt.boxplot(T) 




 