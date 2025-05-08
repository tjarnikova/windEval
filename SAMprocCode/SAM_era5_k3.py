#put python script here
import xarray as xr
import numpy as np

ex = True

if ex:
    # sam40 = np.zeros(492)
    # sam65 = np.zeros(492)
    ind = 0
    for yr in range(1990,2000):
        print(yr)

        tdir = '/gpfs/data/greenocean2/software/products/windsFromComponents/SAM/ERA5/'
        td = f'mean_sea_level_pressure_ERA5_{yr}.nc'

        w = xr.open_dataset(f'{tdir}{td}', chunks={"time": 24})
        yr65 = w.msl.sel(latitude = -65).mean(dim = 'longitude').resample(time='M').mean()
        yr40 = w.msl.sel(latitude = -40).mean(dim = 'longitude').resample(time='M').mean()

        yr65.to_netcdf(f'{tdir}65msl_{yr}.nc')
        yr40.to_netcdf(f'{tdir}40msl_{yr}.nc')
        
