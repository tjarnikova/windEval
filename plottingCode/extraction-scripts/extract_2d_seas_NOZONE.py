import glob
import numpy as np
import xarray as xr


ex = True

def make_yearlist(yrst, yrend, scen, \
                 baseDir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/UKESM3M/'):
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        ty = f'{baseDir}/scen{scen}_UKESM_wind_daily_1x1_{yrs[i]}.nc'
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist


if ex:
    savenam = '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/PlankTOMmask_regridrecalc.nc'
    cdomask = xr.open_dataset(savenam)
    tmask = cdomask.tmask

    sdir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/intProc/'

    scens = ['2A','2AM2','1A','1AM2','2B','2BM2','1B','1BM2']



    starts = [1980,2020,2060]
    ends = [2019,2059,2099]

    for s in scens:
        for y in range(0,3):
            st = starts[y]; en = ends[y]
            #print(f'{s} {st}-{en}')
            print(f'scen{s}_2d-seas-wspd-ts-{st}-{en}.nc')

            ds = xr.open_mfdataset(make_yearlist(st, en, s))

            ds_DJF = ds.wspd10m.sel(time_counter=slice(f'{st}-01-01', f'{en+1}-01-01')).\
            sel(time_counter=(ds['time_counter.season'] == 'DJF')).groupby('time_counter.year').mean()

            ds_MAM = ds.wspd10m.sel(time_counter=slice(f'{st}-01-01', f'{en+1}-01-01')).\
            sel(time_counter=(ds['time_counter.season'] == 'MAM')).groupby('time_counter.year').mean()

            ds_JJA = ds.wspd10m.sel(time_counter=slice(f'{st}-01-01', f'{en+1}-01-01')).\
            sel(time_counter=(ds['time_counter.season'] == 'JJA')).groupby('time_counter.year').mean()

            ds_SON = ds.wspd10m.sel(time_counter=slice(f'{st}-01-01', f'{en+1}-01-01')).\
            sel(time_counter=(ds['time_counter.season'] == 'SON')).groupby('time_counter.year').mean()

            ds_FY = ds.wspd10m.sel(time_counter=slice(f'{st}-01-01', f'{en+1}-01-01')).groupby('time_counter.year').mean()

            new_ds = xr.Dataset({
                'DJF': ds_DJF,
                'MAM': ds_MAM,
                'JJA': ds_JJA,
                'SON': ds_SON,
                'FY': ds_FY,

            })

            new_ds.to_netcdf(f'{sdir}/scen{s}_2d-seas-wspd-ts-{st}-{en}.nc')











# def make_yearlist(yrst, yrend, prod, \
#                  baseDir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/'):
#     yrs = np.arange(yrst,yrend+1,1)
#     ylist = []
#     for i in range(0,len(yrs)):
#         ty = f'{baseDir}/{prod}/{prod}_NOZONE_wind_daily_1x1_{yrs[i]}.nc'
#         t2 = glob.glob(ty)
#         #print(t2)
#         ylist.append(t2[0])
#     return ylist

# savenam = '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/PlankTOMmask_regridrecalc.nc'
# cdomask = xr.open_dataset(savenam)
# tmask = cdomask.tmask

# sdir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/intProc/'

# print('pojd')
# savenam = '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/PlankTOMmask_regridrecalc.nc'
# cdomask = xr.open_dataset(savenam)
# cdomask
# tmask = cdomask.tmask

# tn = ['UKESM']
# starts = [1980,1948, 1979, 1940, 1940]


# for i in range(0,1):
#     en = 2023
#     ds = xr.open_mfdataset(make_yearlist(starts[i], en, tn[i]))
#     ncarst = starts[i]
#     ds_DJF = ds.wspd10m.sel(time_counter=slice(f'{ncarst}-01-01', f'{en+1}-01-01')).\
#     sel(time_counter=(ds['time_counter.season'] == 'DJF')).groupby('time_counter.year').mean()

#     ds_MAM = ds.wspd10m.sel(time_counter=slice(f'{ncarst}-01-01', f'{en+1}-01-01')).\
#     sel(time_counter=(ds['time_counter.season'] == 'MAM')).groupby('time_counter.year').mean()

#     ds_JJA = ds.wspd10m.sel(time_counter=slice(f'{ncarst}-01-01', f'{en+1}-01-01')).\
#     sel(time_counter=(ds['time_counter.season'] == 'JJA')).groupby('time_counter.year').mean()

#     ds_SON = ds.wspd10m.sel(time_counter=slice(f'{ncarst}-01-01', f'{en+1}-01-01')).\
#     sel(time_counter=(ds['time_counter.season'] == 'SON')).groupby('time_counter.year').mean()

#     ds_FY = ds.wspd10m.sel(time_counter=slice(f'{ncarst}-01-01', f'{en+1}-01-01')).groupby('time_counter.year').mean()

#     new_ds = xr.Dataset({
#         'DJF': ds_DJF,
#         'MAM': ds_MAM,
#         'JJA': ds_JJA,
#         'SON': ds_SON,
#         'FY': ds_FY,

#     })
#     new_ds.to_netcdf(f'{sdir}/{tn[i]}_NOZONE_2d-seas-wspd-ts.nc')
