ex = True
from scipy.stats.kde import gaussian_kde
from scipy.stats import norm
import numpy as np
import xarray as xr
import glob

def custhist(tdat, nbins, start, end, tweights = None):
    #bins = 25
    hist_met_vflx, bins = np.histogram(np.ravel(tdat), bins=nbins,\
                                 range = [start, end], weights=tweights)

    bin_cent = bins + (bins[1]-bins[0])/2
    tot_count = np.sum(hist_met_vflx)


    binsback = bins
    bin_cent = bin_cent[0:nbins]
    histback = hist_met_vflx/tot_count

    return binsback, bin_cent, histback

def make_yearlist_prod(prod, yrst, yrend, ozone = True):

    baseDir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/'

    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        if ozone:
            ty = f'{baseDir}/{prod}/{prod}_wind_daily_1x1_{yrs[i]}.nc'
        else:
            ty = f'{baseDir}/{prod}/{prod}_NOZONE_wind_daily_1x1_{yrs[i]}.nc'
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist

def get_gaussian_kde(prod = 'UKESM', seas = 'FY', yst = 1940, yen = 1949, 
                     xmi = 0, xma = 25, nobins = 100, latsta = 30, late = 50, ozone = True):

    tdir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/intProc/'
    if ozone:
        savenam = f'KDE-{prod}-{seas}-{yst}-{yen}_bins{nobins}_latind{latsta}-{late}.nc'#seas
    else:
        savenam = f'KDE-{prod}-{seas}-{yst}-{yen}_bins{nobins}_latind{latsta}-{late}.nc'#seas
    print(savenam)
    
    yl = make_yearlist_prod(prod, yst, yen, ozone)
    td = xr.open_mfdataset(yl)

    if seas == 'FY':
        q = td.wspd10m.isel(lat = slice(latsta,late))
        masksiz = (len(q.time_counter))

    else:
        q = td.wspd10m.sel(time_counter=(td['time_counter.season'] == seas)).isel(lat = slice(latsta,late))
        masksiz = (len(q.time_counter))
        print(masksiz)
        print(nobins)

    tval = q.values

    cdomask = xr.open_dataset('/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/PlankTOMmask_regridrecalc.nc')
    tmask = cdomask.tmask.isel(lat = slice(latsta,late)).values

    y = (np.shape(tmask)[0])
    x = (np.shape(tmask)[1])
    timask = np.zeros([masksiz,y,x])
    for i in range(0,masksiz):
        timask[i,:,:] = tmask

    kde_x = np.linspace(xmi, xma, nobins)
    kde = gaussian_kde(np.ravel(tval), weights=np.ravel(timask))
    kde_val = kde(kde_x)

    binsback, bin_cent, histback, = custhist(np.ravel(tval), nobins, xmi, xma, tweights = np.ravel(timask))


    data_vars = {'kde':(['kde_x'],kde_val),
                        'hist':(['hist_x'],histback),
    }
    # define coordinates
    coords = {'kde_x': (['kde_x'], kde_x),
              'hist_x': (['hist_x'], bin_cent),

             }
    # define global attributes
    attrs = {'made in':'SOZONE/MEDUSA/makeYearlyMEDUSAsubsetfiles.ipynb',
    'desc': 'yearly medusa files, saving only variables of interest'
    }
    ds = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)
    ds.to_netcdf(f'{tdir}{savenam}')

    return 

prods = ['ERA5','NCEP-NCAR','MERRA','UKESM','JRA']
prods = ['UKESMm3']#,
# prods = ['UKESM']
#yrs = [1940,1950,1960,1970,1980,1990,2000,2010]
seass = ['FY','DJF']
yrs = [1980]

for prod in prods:

    print(prod)

    for yr in yrs:
        for s in seass:
            yre = yr+39
            get_gaussian_kde(prod, seas = s, yst = yr, yen = yre, xmi = 0, xma = 25, ozone = True)
            #get_gaussian_kde(prod, seas = s, yst = yr, yen = yre, xmi = 0, xma = 25, ozone = False)


#### no nozone

# print('lets go, lets go')


# def custhist(tdat, nbins, start, end, tweights = None):
#     #bins = 25
#     hist_met_vflx, bins = np.histogram(np.ravel(tdat), bins=nbins,\
#                                  range = [start, end], weights=tweights)

#     bin_cent = bins + (bins[1]-bins[0])/2
#     tot_count = np.sum(hist_met_vflx)


#     binsback = bins
#     bin_cent = bin_cent[0:nbins]
#     histback = hist_met_vflx/tot_count

#     return binsback, bin_cent, histback

# def make_yearlist_prod(yrst, yrend, prod = 'ERA5'):

#     baseDir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/'
#     yrs = np.arange(yrst,yrend+1,1)
#     ylist = []
#     for i in range(0,len(yrs)):
#         ty = f'{baseDir}/{prod}/{prod}_wind_daily_1x1_{yrs[i]}.nc'
#         t2 = glob.glob(ty)
#         #print(t2)
#         ylist.append(t2[0])
#     return ylist

# def get_gaussian_kde(prod = 'ERA5', seas = 'FY', yst = 1940, yen = 1949, xmi = 0, xma = 25):

#     tdir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/intProc/'
#     savenam = f'KDE-{prod}-{seas}-{yst}-{yen}.nc'#seas
#     print(savenam)

#     yl = make_yearlist_prod(yst, yen, prod)
#     td = xr.open_mfdataset(yl)

#     if seas == 'FY':
#         q = td.wspd10m.isel(lat = slice(30,50))
#         masksiz = (len(q.time_counter))

#     else:
#         q = td.wspd10m.sel(time_counter=(td['time_counter.season'] == seas)).isel(lat = slice(30,50))
#         masksiz = (len(q.time_counter))
#         print(masksiz)

#     tval = q.values

#     cdomask = xr.open_dataset('/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/PlankTOMmask_krg.nc')
#     tmask = cdomask.aream2.mean(dim = 'time_counter').isel(lat = slice(30,50)).values

#     y = (np.shape(tmask)[0])
#     x = (np.shape(tmask)[1])
#     timask = np.zeros([masksiz,y,x])
#     for i in range(0,masksiz):
#         timask[i,:,:] = tmask

#     kde_x = np.linspace(xmi, xma, 100)
#     kde = gaussian_kde(np.ravel(tval), weights=np.ravel(timask))
#     kde_val = kde(kde_x)

#     binsback, bin_cent, histback, = custhist(np.ravel(tval), 100, xmi, xma, tweights = np.ravel(timask))


#     data_vars = {'kde':(['kde_x'],kde_val),
#                         'hist':(['hist_x'],histback),
#     }
#     # define coordinates
#     coords = {'kde_x': (['kde_x'], kde_x),
#               'hist_x': (['hist_x'], bin_cent),

#              }
#     # define global attributes
#     attrs = {'made in':'SOZONE/MEDUSA/makeYearlyMEDUSAsubsetfiles.ipynb',
#     'desc': 'yearly medusa files, saving only variables of interest'
#     }
#     ds = xr.Dataset(data_vars=data_vars,
#     coords=coords,
#     attrs=attrs)
#     ds.to_netcdf(f'{tdir}{savenam}')

#     return 


# #prods = ['ERA5','NCEP-DOE','NCEP-NCAR','MERRA']
# prods = ['UKESM']
# yrs = [1980]
# seass = ['FY','DJF']

# for prod in prods:

#     print(prod)

#     for yr in yrs:
#         for s in seass:
#             yre = yr+39
#             get_gaussian_kde(prod, seas = s, yst = yr, yen = yre, xmi = 0, xma = 25)

# def custhist(tdat, nbins, start, end, tweights = None):
#     #bins = 25
#     hist_met_vflx, bins = np.histogram(np.ravel(tdat), bins=nbins,\
#                                  range = [start, end], weights=tweights)

#     bin_cent = bins + (bins[1]-bins[0])/2
#     tot_count = np.sum(hist_met_vflx)


#     binsback = bins
#     bin_cent = bin_cent[0:nbins]
#     histback = hist_met_vflx/tot_count

#     return binsback, bin_cent, histback
