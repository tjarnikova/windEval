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

erast = 1980; en = 2023
era = xr.open_mfdataset(make_yearlist(erast, en, 'MERRA'))
era_ts = era.wspd10m.sel(time_counter=slice(f'{erast}-01-01', f'{en+1}-01-01'))
era_ts2 = era_ts.isel(lat = slice(30,50)).weighted(tmask.isel(lat = slice(30,50))).mean(dim = ['lat', 'lon'])
era_ts2.attrs = {"made in": 'plottingCode/extract_ts.py'}
era_ts2.to_netcdf(f'{sdir}/MERRA_40-60S_mean_wspd_ts.nc')


ncarst = 1948; 
ncar = xr.open_mfdataset(make_yearlist(ncarst, en, 'NCEP-NCAR'))
ncar_ts = ncar.wspd10m.sel(time_counter=slice(f'{ncarst}-01-01', f'{en+1}-01-01'))
ncar_ts2 = ncar_ts.isel(lat = slice(30,50)).weighted(tmask.isel(lat = slice(30,50))).mean(dim = ['lat', 'lon'])
ncar_ts2.attrs = {"made in": 'plottingCode/extract_ts.py'}
ncar_ts2.to_netcdf(f'{sdir}/NCEP-NCAR_40-60S_mean_wspd_ts.nc')

doest = 1979; 
doe = xr.open_mfdataset(make_yearlist(doest, en, 'NCEP-DOE'))
doe_ts = doe.wspd10m.sel(time_counter=slice(f'{doest}-01-01', f'{en+1}-01-01'))
doe_ts2 = doe_ts.isel(lat = slice(30,50)).weighted(tmask.isel(lat = slice(30,50))).mean(dim = ['lat', 'lon'])
doe_ts2.attrs = {"made in": 'plottingCode/extract_ts.py'}
doe_ts2.to_netcdf(f'{sdir}/NCEP-DOE_40-60S_mean_wspd_ts.nc')

ukesmst = 1940; 
ukesm = xr.open_mfdataset(make_yearlist(ukesmst, en, 'UKESM'))
ukesm_ts = ukesm.wspd10m.sel(time_counter=slice(f'{ukesmst}-01-01', f'{en+1}-01-01'))
ukesm_ts2 = ukesm_ts.isel(lat = slice(30,50)).weighted(tmask.isel(lat = slice(30,50))).mean(dim = ['lat', 'lon'])
ukesm_ts2.attrs = {"made in": 'plottingCode/extract_ts.py'}
ukesm_ts2.to_netcdf(f'{sdir}/UKESM_40-60S_mean_wspd_ts.nc')

erast = 1940; 
era = xr.open_mfdataset(make_yearlist(erast, en, 'ERA5'))
era_ts = era.wspd10m.sel(time_counter=slice(f'{erast}-01-01', f'{en+1}-01-01'))
era_ts2 = era_ts.isel(lat = slice(30,50)).weighted(tmask.isel(lat = slice(30,50))).mean(dim = ['lat', 'lon'])
era_ts2.attrs = {"made in": 'plottingCode/extract_ts.py'}
era_ts2.to_netcdf(f'{sdir}/ERA5_40-60S_mean_wspd_ts.nc')
print('pohoda')
