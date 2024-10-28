# %%
#Load libraries
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# %%
#Url for ONI and RONI indices from CPC
ONI_URL='https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt'
RONI_URL='https://www.cpc.ncep.noaa.gov/data/indices/RONI.ascii.txt'

# %%
#Open ONI and RONI as dataframes
df_ONI = pd.read_csv(ONI_URL, skiprows=0, header=0, sep='\s+')
df_RONI = pd.read_csv(RONI_URL, skiprows=0, header=0, sep='\s+')

# %%
#Adapt dataframes to plot timeseries

# Mapping of month names/abbreviations to numbers
month_mapping = {
    'DJF': 1, 'JFM': 2, 'FMA': 3,
    'MAM': 4, 'AMJ': 5, 'MJJ': 6,
    'JJA': 7, 'JAS': 8, 'ASO': 9,
    'SON': 10, 'OND': 11, 'NDJ': 12
}

# Convert trimesters to numeric monthly values
df_ONI['month'] = df_ONI['SEAS'].map(month_mapping)
# Change column name 
df_ONI = df_ONI.rename(columns={'YR': 'year'})
# Create a datetime column using 'year' and 'month'
df_ONI['date'] = pd.to_datetime(df_ONI[['year', 'month']].assign(day=1))

# Convert trimesters to numeric monthly values
df_RONI['month'] = df_RONI['SEAS'].map(month_mapping)
# Change column name 
df_RONI = df_RONI.rename(columns={'YR': 'year'})
# Create a datetime column using 'year' and 'month'
df_RONI['date'] = pd.to_datetime(df_RONI[['year', 'month']].assign(day=1))

# %%
#Create figure
fig, (ax1, ax2) = plt.subplots(2, 1,figsize=(16,12))

ax1.plot(df_ONI['date'], df_ONI['ANOM'],'k',linewidth=0.6)
ax1.fill_between(df_ONI['date'], df_ONI['ANOM'],0.5, 
	where=df_ONI['ANOM']>=0.5,color='red')
ax1.fill_between(df_ONI['date'], df_ONI['ANOM'],-0.5, 
	where=df_ONI['ANOM']<=-0.5,color='blue')
ax1.axhline(y=0,color='k',linewidth=0.8)
ax1.axhline(y=0.5,color='r',linewidth=0.8)
ax1.axhline(y=-0.5,color='b',linewidth=0.8)
ax1.grid(True)
ax1.set_title('ONI index', fontsize=18)
ax1.tick_params(axis='x', labelsize=14)
ax1.tick_params(axis='y', labelsize=14)  

ax2.plot(df_RONI['date'], df_RONI['ANOM'],'k',linewidth=0.6)
ax2.fill_between(df_RONI['date'], df_RONI['ANOM'],0.5, 
	where=df_RONI['ANOM']>=0.5,color='red')
ax2.fill_between(df_RONI['date'], df_RONI['ANOM'],-0.5, 
	where=df_RONI['ANOM']<=-0.5,color='blue')
ax2.axhline(y=0,color='k',linewidth=0.8)
ax2.axhline(y=0.5,color='r',linewidth=0.8)
ax2.axhline(y=-0.5,color='b',linewidth=0.8)
ax2.grid(True)
ax2.set_title('Relative ONI (RONI) index', fontsize=18)
ax2.tick_params(axis='x', labelsize=14)
ax2.tick_params(axis='y', labelsize=14)  

plt.tight_layout()
plt.savefig('ONIvsRONI_historico.png', dpi=300)  # Higher resolution



# %%
df_ONI = df_ONI[df_ONI['date'] >= '2010-01-01'] 
df_RONI = df_RONI[df_RONI['date'] >= '2010-01-01']
fig, (ax1, ax2) = plt.subplots(2, 1,figsize=(16,12))

ax1.plot(df_ONI['date'], df_ONI['ANOM'],'k',linewidth=0.6)
ax1.fill_between(df_ONI['date'], df_ONI['ANOM'],0.5, 
	where=df_ONI['ANOM']>=0.5,color='red')
ax1.fill_between(df_ONI['date'], df_ONI['ANOM'],-0.5, 
	where=df_ONI['ANOM']<=-0.5,color='blue')
ax1.axhline(y=0,color='k',linewidth=0.8)
ax1.axhline(y=0.5,color='r',linewidth=0.8)
ax1.axhline(y=-0.5,color='b',linewidth=0.8)
ax1.grid(True)
ax1.set_title('ONI index', fontsize=18)
ax1.tick_params(axis='x', labelsize=14)
ax1.tick_params(axis='y', labelsize=14)  

ax2.plot(df_RONI['date'], df_RONI['ANOM'],'k',linewidth=0.6)
ax2.fill_between(df_RONI['date'], df_RONI['ANOM'],0.5, 
	where=df_RONI['ANOM']>=0.5,color='red')
ax2.fill_between(df_RONI['date'], df_RONI['ANOM'],-0.5, 
	where=df_RONI['ANOM']<=-0.5,color='blue')
ax2.axhline(y=0,color='k',linewidth=0.8)
ax2.axhline(y=0.5,color='r',linewidth=0.8)
ax2.axhline(y=-0.5,color='b',linewidth=0.8)
ax2.grid(True)
ax2.set_title('Relative ONI (RONI) index', fontsize=18)
ax2.tick_params(axis='x', labelsize=14)
ax2.tick_params(axis='y', labelsize=14)  

plt.tight_layout()
plt.savefig('ONIvsRONI.png', dpi=300)  # Higher resolution

