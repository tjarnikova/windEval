for i in {1965..1970}

do
    tdir='/gpfs/data/greenocean2/software/products/windsFromComponents/ERA5_v2024/scripts/daily/'
    cdir='/gpfs/data/greenocean2/software/products/windsFromComponents/ERA5_v2024/scripts/daily/'
    newfil="${cdir}10m_v_component_of_wind_ERA5_${i}_daily_rg.nc"
    oldfil="${tdir}10m_v_component_of_wind_ERA5_${i}_daily.nc"
    echo ${oldfil}
    cdo remapbil,r360x180 ${oldfil} ${newfil}

    newfil="${cdir}10m_u_component_of_wind_ERA5_${i}_daily_rg.nc"
    oldfil="${tdir}10m_u_component_of_wind_ERA5_${i}_daily.nc"
    echo ${oldfil}
    cdo remapbil,r360x180 ${oldfil} ${newfil}

#     newfil="${cdir}10m_windspeed_ERA5_${i}_daily_rg.nc"
#     oldfil="${tdir}10m_windspeed_ERA5_${i}_daily.nc"
#     echo ${oldfil}
#     cdo remapbil,r360x180 ${oldfil} ${newfil}

done

for i in {1965..1970}

do
    tdir='/gpfs/data/greenocean2/software/products/windsFromComponents/ERA5_v2024/scripts/daily/'
    cdir='/gpfs/data/greenocean2/software/products/windsFromComponents/ERA5_v2024/scripts/daily/'


    newfil="${cdir}10m_windspeed_ERA5_${i}_daily_rg.nc"
    oldfil="${tdir}10m_windspeed_ERA5_${i}_daily.nc"
    echo ${oldfil}
    cdo remapbil,r360x180 ${oldfil} ${newfil}

done
