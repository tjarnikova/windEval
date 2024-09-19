#put python script here

import time
import xarray as xr
import numpy as np

for y in range(1979,2024):
    
    print(y)
    tv = xr.open_dataset(f'/gpfs/data/greenocean2/software/products/windsFromComponents/NCEP-DOE/daily/vwnd.10m.gauss.{y}_daily.nc')
    tu = xr.open_dataset(f'/gpfs/data/greenocean2/software/products/windsFromComponents/NCEP-DOE/daily/uwnd.10m.gauss.{y}_daily.nc')

    q = time.time()
    twind = xr.ufuncs.sqrt(xr.ufuncs.square(tu.uwnd) + xr.ufuncs.square(tv.vwnd))
    twind.name = 'windspeed'

    w5 = twind.to_dataset()
    w5.to_netcdf(f'/gpfs/data/greenocean2/software/products/windsFromComponents/NCEP-DOE/daily/wspd.10m.gauss.{y}_daily.nc')

    q1 = time.time()
    print(q1-q)
