

#put python script here

import time
import xarray as xr
import numpy as np

for y in range(1940,2024):
    
    print(y)
    tu = xr.open_dataset(f'/gpfs/data/greenocean2/software/products/windsFromComponents/ERA5_v2024/scripts/daily/10m_u_component_of_wind_ERA5_{y}_daily.nc', chunks={"time": 24})
    tv = xr.open_dataset(f'/gpfs/data/greenocean2/software/products/windsFromComponents/ERA5_v2024/scripts/daily/10m_v_component_of_wind_ERA5_{y}_daily.nc', chunks={"time": 24})

    q = time.time()
    twind = xr.ufuncs.sqrt(xr.ufuncs.square(tu.u10) + xr.ufuncs.square(tv.v10))
    twind.name = 'windspeed'

    w5 = twind.to_dataset()
    w5.to_netcdf(f'/gpfs/data/greenocean2/software/products/windsFromComponents/ERA5_v2024/scripts/daily/10m_windspeed_ERA5_{y}_daily.nc')

    q1 = time.time()
    print(q1-q)

#/gpfs/data/greenocean2/software/products/windsFromComponents/ERA5_v2024/scripts/daily/10m_u_component_of_wind_ERA5_2014_daily.nc