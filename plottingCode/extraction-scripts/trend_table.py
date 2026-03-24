# trend table
import xarray as xr
#import pymannkendall as mk
#from scipy import stats
import numpy as np
#import pandas as pd

sdir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/intProc/'


ncar_ts = xr.open_dataset(f'{sdir}NCEP-NCAR_40-60S_mean_wspd_ts.nc')
doe_ts = xr.open_dataset(f'{sdir}NCEP-DOE_40-60S_mean_wspd_ts.nc')
ukesm_ts = xr.open_dataset(f'{sdir}UKESM_40-60S_mean_wspd_ts.nc')
era_ts = xr.open_dataset(f'{sdir}ERA5_40-60S_mean_wspd_ts.nc')
merra_ts = xr.open_dataset(f'{sdir}MERRA_40-60S_mean_wspd_ts.nc')




def give_trends(ts_y):

    ts_x = np.arange(0,len(ts_y))
    trend, h, mk_p, z, Tau, s, var_s, mk_slope, intercept = mk.original_test(ts_y)
    lin_slope, intercept, r_value, lin_p, std_err = stats.linregress(ts_x,ts_y)
    
    return mk_slope, mk_p, lin_slope, lin_p

dss = ['ERA5','NCEP-NCAR','MERRA','NCEP-DOE','UKESM']
tdar = [era_ts, ncar_ts, merra_ts, doe_ts,  ukesm_ts]

data = np.zeros([5,5])
sig = np.zeros([5,5])
for i in range(0,5):
    print(dss[i])
    ds = dss[i]
    
    tdat = tdar[i]
    td = tdat.wspd10m.sel(time_counter=slice(f'{1980}-01-01', f'{2019}-12-31'))
    td = td.groupby('time_counter.year').mean()
    td.to_netcdf(f'{sdir}/{ds}_40-60S_mean_wspd_ts-FY.nc')
    
    td = tdat.wspd10m.sel(time_counter=slice(f'{1980}-01-01', f'{2019}-12-31'))
    td = td.sel(time_counter=(td['time_counter.season'] == 'DJF')).\
    groupby('time_counter.year').mean()
    td.to_netcdf(f'{sdir}/{ds}_40-60S_mean_wspd_ts-DJF.nc')
    
    td = tdat.wspd10m.sel(time_counter=slice(f'{1980}-01-01', f'{2019}-12-31'))
    td = td.sel(time_counter=(td['time_counter.season'] == 'MAM')).\
    groupby('time_counter.year').mean()
    td.to_netcdf(f'{sdir}/{ds}_40-60S_mean_wspd_ts-MAM.nc')
    
    td = tdat.wspd10m.sel(time_counter=slice(f'{1980}-01-01', f'{2019}-12-31'))
    td = td.sel(time_counter=(td['time_counter.season'] == 'JJA')).\
    groupby('time_counter.year').mean()
    td.to_netcdf(f'{sdir}/{ds}_40-60S_mean_wspd_ts-JJA.nc')
    
    td = tdat.wspd10m.sel(time_counter=slice(f'{1980}-01-01', f'{2019}-12-31'))
    td = td.sel(time_counter=(td['time_counter.season'] == 'SON')).\
    groupby('time_counter.year').mean()
    td.to_netcdf(f'{sdir}/{ds}_40-60S_mean_wspd_ts-SON.nc')    
    


######
def make_exlist(prod,yrst = 1980, yrend = 2019, \
                 baseDir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/intProc/'):
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        ty = f'{baseDir}/{prod}_windex_{yrs[i]}.nc'
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist

MERRAex = xr.open_mfdataset(make_exlist('MERRA'))
ERA5ex = xr.open_mfdataset(make_exlist('ERA5'))
NCEPDOEex = xr.open_mfdataset(make_exlist('NCEP-DOE'))
NCEPNCARex = xr.open_mfdataset(make_exlist('NCEP-NCAR'))
UKESMex = xr.open_mfdataset(make_exlist('UKESM'))


dss = ['ERA5','NCEP-NCAR','MERRA','NCEP-DOE','UKESM']
tdar = [ERA5ex, NCEPNCARex, MERRAex, NCEPDOEex, UKESMex]

data = np.zeros([5,5])
sig = np.zeros([5,5])
for i in range(0,5):
    print(dss[i])
    ds = dss[i]
    
    tdat = tdar[i]
    td = tdat.above95wt.sel(time_counter=slice(f'{1980}-01-01', f'{2019}-12-31'))
    td = td.groupby('time_counter.year').mean()
    td.to_netcdf(f'{sdir}/{ds}_40-60S_ex_wspd_ts-FY.nc')
    
    td = tdat.above95wt.sel(time_counter=slice(f'{1980}-01-01', f'{2019}-12-31'))
    td = td.sel(time_counter=(td['time_counter.season'] == 'DJF')).\
    groupby('time_counter.year').mean()
    td.to_netcdf(f'{sdir}/{ds}_40-60S_ex_wspd_ts-DJF.nc')
    
    td = tdat.above95wt.sel(time_counter=slice(f'{1980}-01-01', f'{2019}-12-31'))
    td = td.sel(time_counter=(td['time_counter.season'] == 'MAM')).\
    groupby('time_counter.year').mean()
    td.to_netcdf(f'{sdir}/{ds}_40-60S_ex_wspd_ts-MAM.nc')
    
    td = tdat.above95wt.sel(time_counter=slice(f'{1980}-01-01', f'{2019}-12-31'))
    td = td.sel(time_counter=(td['time_counter.season'] == 'JJA')).\
    groupby('time_counter.year').mean()
    td.to_netcdf(f'{sdir}/{ds}_40-60S_ex_wspd_ts-JJA.nc')
    
    td = tdat.above95wt.sel(time_counter=slice(f'{1980}-01-01', f'{2019}-12-31'))
    td = td.sel(time_counter=(td['time_counter.season'] == 'SON')).\
    groupby('time_counter.year').mean()
    td.to_netcdf(f'{sdir}/{ds}_40-60S_ex_wspd_ts-SON.nc')    
    