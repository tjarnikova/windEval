for i in {1979..2024}

do
    tdir='/gpfs/data/greenocean2/software/products/windsFromComponents/NCEP-DOE/daily/'
    newfil="${tdir}vwnd.10m.gauss.${i}_daily_rg.nc"
    oldfil="${tdir}vwnd.10m.gauss.${i}_daily.nc"
    echo ${oldfil}
    cdo remapbil,r360x180 ${oldfil} ${newfil}

    newfil="${tdir}uwnd.10m.gauss.${i}_daily_rg.nc"
    oldfil="${tdir}uwnd.10m.gauss.${i}_daily.nc"
    cdo remapbil,r360x180 ${oldfil} ${newfil}

    newfil="${tdir}wspd.10m.gauss.${i}_daily_rg.nc"
    oldfil="${tdir}wspd.10m.gauss.${i}_daily.nc"
    cdo remapbil,r360x180 ${oldfil} ${newfil}

done
