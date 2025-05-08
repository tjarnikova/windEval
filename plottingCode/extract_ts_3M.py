import glob
import numpy as np
import xarray as xr



def make_yearlist(yrst, yrend,
                 baseDir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/UKESM3M', s = '1A'):
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        ty = f'{baseDir}/scen{s}_UKESM_wind_daily_1x1_{yrs[i]}.nc'
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist

savenam = '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/PlankTOMmask_regridrecalc.nc'
cdomask = xr.open_dataset(savenam)
tmask = cdomask.tmask

sdir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/intProc/'

scens = ['2AM2','2BM2','1A','1B','2A','2B','1AM2','1BM2']
scens = ['2AM3','2BM3','1AM3','1BM3']

# for s in scens:
#     ukesmst = 1950; en = 2099
#     ukesm = xr.open_mfdataset(make_yearlist(ukesmst, en, s = s))
#     print('opened')
#     print(f'making scen{s}_UKESM_30-70S_mean_wspd_ts_1950-2099.nc')
#     ukesm_ts = ukesm.wspd10m.sel(time_counter=slice(f'{ukesmst}-01-01', f'{en+1}-01-01'))
#     ukesm_ts2 = ukesm_ts.isel(lat = slice(20,60)).weighted(tmask.isel(lat = slice(20,60))).mean(dim = ['lat', 'lon'])
#     #ukesm_ts2 = ukesm_ts2.assign_attrs("made in"="windEval/plottingCode/extract_ts_3M.py")
#     ukesm_ts2.attrs["made in"] = "windEval/plottingCode/extract_ts_3M.py"
#     ukesm_ts2.to_netcdf(f'{sdir}/scen{s}_UKESM_30-70S_mean_wspd_ts_1950-2099.nc')
    
for s in scens:
    ukesmst = 1950; en = 2099
    ukesm = xr.open_mfdataset(make_yearlist(ukesmst, en, s = s))
    print('opened')
    print(f'making scen{s}_UKESM_40-60S_mean_wspd_ts_1950-2099.nc')
    ukesm_ts = ukesm.wspd10m.sel(time_counter=slice(f'{ukesmst}-01-01', f'{en+1}-01-01'))
    ukesm_ts2 = ukesm_ts.isel(lat = slice(30,50)).weighted(tmask.isel(lat = slice(30,50))).mean(dim = ['lat', 'lon'])
    ukesm_ts2.attrs["made in"] = "windEval/plottingCode/extract_ts_3M.py"
    ukesm_ts2.to_netcdf(f'{sdir}/scen{s}_UKESM_40-60S_mean_wspd_ts_1950-2099.nc')

