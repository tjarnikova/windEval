#put python script here

import time
import xarray as xr
import numpy as np

for y in range(2018,2024):
    print(y)
    ncepdir = '/gpfs/data/greenocean2/software/products/windsFromComponents/NCEP-DOE/'
    tv = xr.open_dataset(f'{ncepdir}/windV/vwnd.10m.gauss.{y}.nc')
    tu = xr.open_dataset(f'{ncepdir}/windU/uwnd.10m.gauss.{y}.nc')

    tvd = tv.vwnd.resample(time='1D').mean()
    tud = tu.uwnd.resample(time='1D').mean()
    
    tvd.to_netcdf(f'{ncepdir}/daily/vwnd.10m.gauss.{y}_daily.nc')
    tud.to_netcdf(f'{ncepdir}/daily/uwnd.10m.gauss.{y}_daily.nc')
    print('-')
