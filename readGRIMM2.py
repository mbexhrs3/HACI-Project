
import numpy as np
import pandas as pd
from StringIO import StringIO

#f = open('E:/PhD_measurement_paper/Data_and_Graph/GRIMM_compiled_data/Pre_monsoon_2011/1_GRIMM_MARCH_2011/08030000.gtm','r')

f = 'E:/PhD_measurement_paper/Data_and_Graph/GRIMM_compiled_data/Pre_monsoon_2011/1_GRIMM_MARCH_2011/08030000.gtm'



df = pd.read_csv(f, header = 2, skipinitialspace=True, sep = ',')

df = pd.read_csv(f, header = 2)

ss = pd.DataFrame(df,columns=grimm)

df1 = df.reindex(columns=grimm)


df = DataFrame(df1,columns = 'grimm')

df = pd.read_csv(StringIO(f), header = 0, skipinitialspace=True, sep = ',', columns = 'grimm')

df2 = df.set_index(GRIMM)


df.reindex(columns=cols)

import numpy as np
import os
import sys
import glob

def main(): 
    filepath = 'E:/PhD_measurement_paper/Data_and_Graph/GRIMM_compiled_data/\
    Pre_monsoon_2011/1_GRIMM_MARCH_2011'
    filepattern = '*.gtm'
    out_file = 'E:/PhD_measurement_paper/Data_and_Graph/GRIMM_compiled_data/Python_out_file'




def readGRIMM(filepath, filepattern, total_conc_file):
    
    full_path = '%s/%s' %(filepath, filepattern)
    for files in glob.glob(filepattern):
        with open('files') as f:
            data = np.genfromtxt(f,)
    
    print 'concatenating %s' %(full_path) + 'files'
    cat 
#    f = open(filename,'r')
# 
# fid =fopen(fileName,'r')
# 
# fgetl(fid);
# str1=fgetl(fid)
# fclose(fid);
# [tok,rem]=strtok(str1,',');
# GRIMM.SIZE1=eval(['[',rem,'];']);
# GRIMM.SIZE2=[GRIMM.SIZE1(2:end) GRIMM.SIZE1(end)+5];

data = data.reindex(columns=data.columns[new_order])

    df2=df.reset_index(['Time', [0.25, 0.28, 0.3, 0.35, 0.4, 0.45, 0.5, 0.58, 0.65, 0.7, 0.8, 1.0, 1.3, 1.6, 2, 2.5, 3, 3.5, 4, 5, 6.5, 7.5, 8.5, 10, 12.5, 15, 17.5, 20, 25, 30, 32]] , drop = 'false')
    
   grimm = ['Time', 0.25, 0.28, 0.3, 0.35, 0.4, 0.45, 0.5, 0.58, 0.65, 0.7, 0.8, 1.0, 1.3, 1.6, 2, 2.5, 3, 3.5, 4, 5, 6.5, 7.5, 8.5, 10, 12.5, 15, 17.5, 20, 25, 30, 32]
     
     
     new_order= range(25)
     
     df2 = df.set_index([new_order])
     
    df2 = df.reindex(columns=df.columns[new_order])
    
    GRIMM.SIZE2=[GRIMM.SIZE1[1:], 35]
    [day,mon,year1,hour,min,sec,GRIMM.conc]=\
    textread(fileName,'%d/%d/%d %d:%d:%d %[^\n] ','headerlines',2,'delimiter',',');

    GRIMM.conc=cellstr(strvcat(GRIMM.conc));

for i=1:length(day)
    ind1=findstr(GRIMM.conc{i},',');
    if(length(ind1)<14)
        len1=14-length(ind1);
        str1='';
        for j=1:len1
            str1=[str1,',0'];
        end
        
        GRIMM.conc{i}=[GRIMM.conc{i},str1];
    end
    GRIMM.conc{i}=[GRIMM.conc{i},';'];
end

D=cat(2,GRIMM.conc{:});
GRIMM.conc=eval(['[',D,'];']);


GRIMM.TIME=datenum(year1,mon,day,hour,min,sec);

GRIMM.conc=GRIMM.conc./1000; % #/cc

