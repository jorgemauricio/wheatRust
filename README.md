# wheatRust
Generate a favourable condicion map for the wheat rust to expand

## Input

Values from the WRF as: <br>
d1.txt<br>
d2.txt<br>
d3.txt<br>
d4.txt<br>
d5.txt

### Data structure
Long,Lat,Graupel,Hail,Rain,Tmax,Tmin,Tpro,Dpoint,Hr,Windpro,WindDir, Hrmin, Hrmax, TprSoil0_10,TprSoil10_40, WprSoil0_10,WprSoil10_40

### Model
25 < Tpro < 30<br>
15 < Tmax - Tmin < 20<br>
Dpoint > 5<br>

## Output

### Data structure
Long', 'Lat', 'Graupel', 'Hail', 'Rain', 'Tmax', 'Tmin', 'Tpro', 'Dpoint', 'Hr', 'Windpro', 'WindDir', ' Hrmin', ' Hrmax',      ' TprSoil0_10', 'TprSoil10_40', ' WprSoil0_10', 'WprSoil10_40', 'Tpro1', 'Tpro2', 'Tpro3', 'Tpro4', 'Tpro5', 'Tmn1', 'Tmn2', 'Tmn3', 'Tmn4','Tmn5', 'Dpoint1', 'Dpoint2', 'Dpoint3', 'Dpoint4', 'Dpoint5', '1_5_7', '2_5_7', '3_5_7', '4_5_7', '5_5_7', '1_7_9', '2_7_9', '3_7_9', '4_7_9', '5_7_9', '1_9_11', '2_9_11', '3_9_11', '4_9_11', '5_9_11', '1_11_13',
       '2_11_13', '3_11_13', '4_11_13', '5_11_13', '1_13_15', '2_13_15', '3_13_15', '4_13_15', '5_13_15', '1_15_17', '2_15_17', '3_15_17', '4_15_17', '5_15_17', '1_17_19', '2_17_19', '3_17_19', '4_17_19', '5_17_19', '1_19_100', '2_19_100', '3_19_100', '4_19_100', '5_19_100', 'indexWR_5_7', 'indexValueWR_5_7', 'indexWR_7_9', 'indexValueWR_7_9', 'indexWR_9_11', 'indexValueWR_9_11', 'indexWR_11_13', 'indexValueWR_11_13', 'indexWR_13_15', 'indexValueWR_13_15', 'indexWR_15_17',  'indexValueWR_15_17', 'indexWR_17_19', 'indexValueWR_17_19', 'indexWR_19_100', 'indexValueWR_19_100'

### Maps
File name: indexValueWR_L_U_Map.png<br>
where:<br>
L : Low limit <br>
U : Upper limit

