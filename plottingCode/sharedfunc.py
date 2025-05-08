import numpy as np
import pymannkendall as mk
from scipy import stats
import xarray as xr

def moving_average(timeseries, n = 3):
    # Ensure n is valid and doesn't exceed the length of the timeseries
    if n <= 0 or n > len(timeseries):
        raise ValueError("Window size n must be between 1 and the length of the timeseries.")
    
    # Compute the n-point moving average
    return np.convolve(timeseries, np.ones(n) / n, mode='valid')

def give_trends(ts_y):

    ts_x = np.arange(0,len(ts_y))
    trend, h, mk_p, z, Tau, s, var_s, mk_slope, intercept = mk.original_test(ts_y)
    lin_slope, intercept, r_value, lin_p, std_err = stats.linregress(ts_x,ts_y)
    
    return mk_slope, mk_p, lin_slope, lin_p


def get_extrema(tvar,yr):
    tn = '/gpfs/home/mep22dku/scratch/SOZONE/windAnalyis/wspdComponents/PlankTOMmask_regridrecalc.nc'
    cdomask = xr.open_dataset(tn)
    adir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/'    
    w = xr.open_dataset(f'{adir}/{tvar}/{tvar}_wind_daily_1x1_{yr}.nc')

    at95 = np.zeros([len(w.time_counter)])
    above95 = np.zeros([len(w.time_counter)])
    above95wt = np.zeros([len(w.time_counter)])
    tmask = cdomask.tmask[30:50,:].values

    for i in range(0,len(w.time_counter)):

        twspd = w.wspd10m[i,30:50,:]
        where0 = np.where(tmask == 0)
        twspd2 = np.copy(twspd)
        twspd2[np.where(tmask == 0)] = np.nan
        perc95 = weighted_quantile(np.ravel(twspd), 0.95, \
                                sample_weight=np.ravel(tmask))

        tmask2 = np.copy(tmask)
        ts = twspd2[twspd2>perc95]
        q = np.where(twspd2 < perc95)
        tmask2[q] = 0

        at95[i] = perc95
        above95wt[i] = np.average(np.ravel(twspd), weights = np.ravel(tmask2))
        above95[i] = np.nanmean(twspd2[twspd2>perc95])

    savenam = f'{adir}/intProc/{tvar}_windex_{yr}.nc'
    print(savenam)
    data_vars = {'at95':(['time_counter'], at95,
    {'units': 'm/s',
    'long_name':'daily 95% of winds south of 40S to 60s'}),
                 'above95':(['time_counter'], above95,
    {'units': '',
    'long_name':''}),
                 'above95wt':(['time_counter'], above95wt,
    {'units': '',
    'long_name':'mean of everything above 95wt'}),
    }
    # define coordinates
    coords = {'time_counter': (['time_counter'], w.time_counter),
            }
    # define global attributes
    attrs = {'made in':'windEval/plottingCode/Fig-means-extremes.ipynb',
    'desc': ''
    }
    ds = xr.Dataset(data_vars=data_vars,
    coords=coords,
    attrs=attrs)
    ds.to_netcdf(savenam)


def make_exlist(prod,yrst = 1980, yrend = 2019, \
                 baseDir = '/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/intProc/'):
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        ty = f'{baseDir}/{prod}_windex_{yrs[i]}.nc'
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist    
    
def weighted_quantile(values, quantiles, sample_weight=None, 
                      values_sorted=False, old_style=False):
    """ Very close to numpy.percentile, but supports weights.
    NOTE: quantiles should be in [0, 1]!
    :param values: numpy.array with data
    :param quantiles: array-like with many quantiles needed
    :param sample_weight: array-like of the same length as `array`
    :param values_sorted: bool, if True, then will avoid sorting of
        initial array
    :param old_style: if True, will correct output to be consistent
        with numpy.percentile.
    :return: numpy.array with computed quantiles.
    """
    values = np.array(values)
    quantiles = np.array(quantiles)
    if sample_weight is None:
        sample_weight = np.ones(len(values))
    sample_weight = np.array(sample_weight)
    assert np.all(quantiles >= 0) and np.all(quantiles <= 1), \
        'quantiles should be in [0, 1]'

    if not values_sorted:
        sorter = np.argsort(values)
        values = values[sorter]
        sample_weight = sample_weight[sorter]

    weighted_quantiles = np.cumsum(sample_weight) - 0.5 * sample_weight
    if old_style:
        # To be convenient with numpy.percentile
        weighted_quantiles -= weighted_quantiles[0]
        weighted_quantiles /= weighted_quantiles[-1]
    else:
        weighted_quantiles /= np.sum(sample_weight)
    return np.interp(quantiles, weighted_quantiles, values)