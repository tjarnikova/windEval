#put python script here

import time
import xarray as xr
import numpy as np

for y in range(1940,2023):
    eradir = '/gpfs/data/greenocean2/software/products/windsFromComponents/ERA5_v2024/scripts/'
    tv = xr.open_dataset(f'{eradir}/10m_v_component_of_wind_ERA5_{y}.nc', chunks={"time": 24})
    tu = xr.open_dataset(f'{eradir}/10m_u_component_of_wind_ERA5_{y}.nc', chunks={"time": 24})

    tvd = tv.v10.resample(time='1D').mean()
    tud = tu.u10.resample(time='1D').mean()
    
    tvd.to_netcdf(f'{eradir}/daily/10m_v_component_of_wind_ERA5_{y}_daily.nc')
    tud.to_netcdf(f'{eradir}/daily/10m_u_component_of_wind_ERA5_{y}_daily.nc')
    
