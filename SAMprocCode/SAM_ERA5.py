#put python script here
import xarray as xr
import numpy as np

ex = True

if ex:
    sam40 = np.zeros(492)
    sam65 = np.zeros(492)
    ind = 0
    for yr in range(1980,2021):
        print(yr)

        tdir = '/gpfs/data/greenocean2/software/products/windsFromComponents/SAM/ERA5/'
        td = f'mean_sea_level_pressure_ERA5_{yr}.nc'

        w = xr.open_dataset(f'{tdir}{td}')
        yr65 = w.msl.sel(latitude = -65).mean(dim = 'longitude').resample(time='M').mean()
        yr40 = w.msl.sel(latitude = -40).mean(dim = 'longitude').resample(time='M').mean()

        sam40[ind:ind+12] = yr40.values/100
        sam65[ind:ind+12] = yr65.values/100

        ind = ind+12
        
    print(np.nanmax(sam40))
    data = xr.Dataset(
    {
        "slp40S": (["time"], [float(i) for i in range(len(time))]),  # ensure data is float
        "slp65S": (["time"], [float(i) for i in range(len(time))]), 
    },
    coords={
        "time": time  # time coordinate
    }
    )


    data['slp40S'].values = sam40
    data['slp65S'].values = sam65

    data["slp40S"].attrs["units"] = "hPa"
    data["slp65S"].attrs["units"] = "hPa"

    data.to_netcdf('/gpfs/data/greenocean2/software/products/windsFromComponents/SAM/ERA5/SLP.nc')