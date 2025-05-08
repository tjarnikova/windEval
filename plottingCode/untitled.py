import glob
import xarray as xr

def make_yearlist(tdat, yrst = 1980, yrend = 2019, baseDir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/intProc/'):
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        ty = f'{baseDir}/JETLAT_{tdat}_{yrs[i]}.nc'
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist


ukesm = xr.open_mfdataset(make_yearlist('UKESM'))
ukesmjet = ukesm.lat.sel(time_counter = slice('1980-01-01','2020-01-01')).mean(dim = 'time_counter')
ukesm