import numpy as np 
import pandas as pd 
import seaborn as sns 
import random 

df = pd.DataFrame(np.random.rand(1000,1),columns=['x'])

def gen_lin(x):
    '''
    A function to generate a linearly correlated value based on given feature'''
    return x*0.657 + random.random() * 3

def gen_nonlin(x):
    '''
    a function to generate a non-linear relationship'''
    return gen_lin(x)+ 20 * x**2

print('\nLINEAR CORRELATION')
df['y'] = df['x'].apply(lambda x:gen_lin(x))
sns.scatterplot(x=df['x'],y=df['y'])

corr_methods = ['pearson','kendall','spearman']
for m in corr_methods:
    print(f"{m}: {df.corr(method=m)['x']['y']:0.3f}",end=" // ")

print('\n\nNON-LINEAR CORRELATION')
df['y_nonlin'] = df['x'].apply(lambda x:gen_nonlin(x))
sns.scatterplot(x=df['x'],y=df['y_nonlin'])

corr_methods = ['pearson','kendall','spearman']
for m in corr_methods:
    print(f"{m}: {df.corr(method=m)['x']['y_nonlin']:0.3f}", end=" // ")

