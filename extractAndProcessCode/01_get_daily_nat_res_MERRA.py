
import glob
import arrow
import xarray as xr





def get_daily(yr):

    date_list = []
    
    # Loop through all months and days of the year
    for month in range(1, 13):  # Months from 1 to 12
        for day in range(1, 32):  # Days from 1 to 31
            try:
                # Create a date with year, month, and day
                date = arrow.get(yr, month, day)
                # Format the date as YYYYMMDD
                formatted_date = date.format('YYYYMMDD')
                # Append to the list
                date_list.append(formatted_date)
            except:
                #print(f'no {month} {day}')
                # Skip invalid dates (e.g., 1980-02-30)
                continue
    
    print(len(date_list))
    print(date_list[364])

    for i in range(0,len(date_list)):
        td = date_list[i]
        # print(td)
        tl = glob.glob(f'/gpfs/data/greenocean2/software/products/windsFromComponents/NASA-MERRA2/raw/downloads/*{td}*nc*')
        print(tl)
        
        tdat = (tl[0])
        w = xr.open_dataset(tdat)
        
        # Resample both variables from hourly to daily, taking the mean for simplicity
        UL_daily = w['U10M'].resample(time='1D').mean()
        VL_daily = w['V10M'].resample(time='1D').mean()
        twind = xr.ufuncs.sqrt(xr.ufuncs.square(UL_daily) + xr.ufuncs.square(VL_daily))
        twind.name = 'windspeed'

        # Create a new dataset with the resampled variables
        new_ds = xr.Dataset({
            'u10m': UL_daily,
            'v10m': VL_daily,
            'wspd10m': twind,
        
            
        })
        
        newdat = f'/gpfs/data/greenocean2/software/products/windsFromComponents/NASA-MERRA2/daily/MERRA2_{td}_daily.nc'
        # if i%20 == 0:
        #     print(newdat)
        new_ds.to_netcdf(newdat)        
        

ex = True
if ex:
    # for yr in range(1981,2024):
    #     print(yr)
    #     test_daily(yr)
    for yr in range(1986,2024):
        print(yr)
        get_daily(yr)
