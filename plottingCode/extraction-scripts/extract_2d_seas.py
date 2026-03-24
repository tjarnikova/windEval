import glob
import numpy as np
import xarray as xr

def make_yearlist(yrst, yrend, prod, \
                 baseDir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/'):
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        ty = f'{baseDir}/{prod}/{prod}_wind_daily_1x1_{yrs[i]}.nc'
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist

savenam = '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/PlankTOMmask_regridrecalc.nc'
cdomask = xr.open_dataset(savenam)
tmask = cdomask.tmask

sdir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/intProc/'

print('pojd')
savenam = '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/PlankTOMmask_regridrecalc.nc'
cdomask = xr.open_dataset(savenam)
cdomask
tmask = cdomask.tmask

tn = ['MERRA','NCEP-NCAR','NCEP-DOE','ERA5','UKESM']
tn = ['JRA']
tn = ['UKESMEM']
starts = [1980,1948, 1979, 1940, 1940]


for i in range(0,1):
    en = 2020
    ds = xr.open_mfdataset(make_yearlist(starts[i], en, tn[i]))
    ncarst = starts[i]
    ds_DJF = ds.wspd10m.sel(time_counter=slice(f'{ncarst}-01-01', f'{en+1}-01-01')).\
    sel(time_counter=(ds['time_counter.season'] == 'DJF')).groupby('time_counter.year').mean()

    ds_MAM = ds.wspd10m.sel(time_counter=slice(f'{ncarst}-01-01', f'{en+1}-01-01')).\
    sel(time_counter=(ds['time_counter.season'] == 'MAM')).groupby('time_counter.year').mean()

    ds_JJA = ds.wspd10m.sel(time_counter=slice(f'{ncarst}-01-01', f'{en+1}-01-01')).\
    sel(time_counter=(ds['time_counter.season'] == 'JJA')).groupby('time_counter.year').mean()

    ds_SON = ds.wspd10m.sel(time_counter=slice(f'{ncarst}-01-01', f'{en+1}-01-01')).\
    sel(time_counter=(ds['time_counter.season'] == 'SON')).groupby('time_counter.year').mean()

    ds_FY = ds.wspd10m.sel(time_counter=slice(f'{ncarst}-01-01', f'{en+1}-01-01')).groupby('time_counter.year').mean()

    new_ds = xr.Dataset({
        'DJF': ds_DJF,
        'MAM': ds_MAM,
        'JJA': ds_JJA,
        'SON': ds_SON,
        'FY': ds_FY,

    })
    new_ds.to_netcdf(f'{sdir}/{tn[i]}_2d-seas-wspd-ts.nc')
