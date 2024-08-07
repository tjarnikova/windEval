
tdir='/gpfs/data/greenocean/software/products/windsFromComponents/symlinked_hrly_UKESM/newdaily/'

scen='1B'
# for i in {1940..2023}

# do
#     echo "${scen}-y${i}"
#     for j in {1..9}
#     do

#         newfil="${tdir}scen${scen}_uwnd_y${i}m0${j}_rg.nc"
#         oldfil="${tdir}scen${scen}_uwnd_y${i}m0${j}.nc"
#         cdo remapbil,r360x180 ${oldfil} ${newfil}

#     done

#     for j in {10..12}
#     do

#         newfil="${tdir}scen${scen}_uwnd_y${i}m${j}_rg.nc"
#         oldfil="${tdir}scen${scen}_uwnd_y${i}m${j}.nc"
#         cdo remapbil,r360x180 ${oldfil} ${newfil}

#     done
# done

for i in {1940..2023}
do
    echo "${scen}-y${i}"
    for j in {1..9}
    do

        newfil="${tdir}scen${scen}_vwnd_y${i}m0${j}_rg.nc"
        oldfil="${tdir}scen${scen}_vwnd_y${i}m0${j}.nc"
        cdo remapbil,r360x180 ${oldfil} ${newfil}

    done

    for j in {10..12}
    do

        newfil="${tdir}scen${scen}_vwnd_y${i}m${j}_rg.nc"
        oldfil="${tdir}scen${scen}_vwnd_y${i}m${j}.nc"
        cdo remapbil,r360x180 ${oldfil} ${newfil}

    done
done
