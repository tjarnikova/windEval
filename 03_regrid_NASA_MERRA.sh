for i in {1979..2024}

#UKESM_wind_daily_1x1_2020.nc
do
    tdir='/gpfs/data/greenocean2/software/products/windsFromComponents/NASA-MERRA2/daily/'
    ndir='/gpfs/data/greenocean2/software/products/windsFromComponents/dailyStandard/MERRA/'
    
    newfil="${ndir}MERRA_wind_daily_1x1_${i}.nc"
    oldfil="${tdir}MERRA2_FY_${i}_daily.nc"
    echo ${oldfil}
    cdo remapbil,r360x180 ${oldfil} ${newfil}

done
