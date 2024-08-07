

#tdir='/gpfs/data/greenocean2/software/products/windsFromComponents/NCEP-DOE/'
#newfil="${tdir}data_vwnd_rg.nc"
#oldfil="${tdir}data_vwnd.nc"
#cdo remapbil,r360x180 ${oldfil} ${newfil}

tdir='/gpfs/data/greenocean2/software/products/windsFromComponents/NCEP-DOE/'
newfil="${tdir}data_uwnd_rg.nc"
oldfil="${tdir}data_uwnd.nc"
cdo remapbil,r360x180 ${oldfil} ${newfil}

tdir='/gpfs/data/greenocean2/software/products/windsFromComponents/NCEP-DOE/'
newfil="${tdir}data_windspeed_rg.nc"
oldfil="${tdir}data_windspeed.nc"
cdo remapbil,r360x180 ${oldfil} ${newfil}
