import time
import xarray as xr
import numpy as np

#vwnd, uwnd


td = '/gpfs/data/greenocean2/software/products/windsFromComponents/'
ncep_doe = 'NCEP-DOE/'

tv = xr.open_dataset(f'{td}/{ncep_doe}/data_vwnd.nc')
tu = xr.open_dataset(f'{td}/{ncep_doe}/data_uwnd.nc')
twind = xr.ufuncs.sqrt(xr.ufuncs.square(tu.uwnd) + xr.ufuncs.square(tv.vwnd))
twind.name = 'windspeed'

w5 = twind.to_dataset()
w5.to_netcdf(f'{td}/{ncep_doe}/data_windspeed.nc')

