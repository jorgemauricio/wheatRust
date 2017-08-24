#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:13:02 2017

@author: jorgemauricio
"""

# Librerias
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from numpy import meshgrid

#%% clear screen
os.system('clear')

#%% change dir
os.chdir('/Users/jorgemauricio/Documents/Research/generateMaps')

#%% Function
def checkWR(tp1, tp2, tp3, tp4, tp5, tmn1, tmn2, tmn3, tmn4, tmn5, dp1, dp2, dp3, dp4, dp5, downLimit, upperLimit):
    level = "'"
    if (tp1 >= 25 and tp1 <= 30 and tmn1 >= 15 and tmn1 <= 20 and dp1 >= downLimit and dp1 <= upperLimit):
        level += "1"
    else:
        level += "0"
    if (tp2 >= 25 and tp2 <= 30 and tmn2 >= 15 and tmn2 <= 20 and dp2 >= downLimit and dp2 <= upperLimit):
        level += "1"
    else:
        level += "0"
    if (tp3 >= 25 and tp3 <= 30 and tmn3 >= 15 and tmn3 <= 20 and dp3 >= downLimit and dp3 <= upperLimit):
        level += "1"
    else:
        level += "0"
    if (tp4 >= 25 and tp4 <= 30 and tmn4 >= 15 and tmn4 <= 20 and dp4 >= downLimit and dp4 <= upperLimit):
        level += "1"
    else:
        level += "0"
    if (tp5 >= 25 and tp5 <= 30 and tmn5 >= 15 and tmn5 <= 20 and dp5 >= downLimit and dp5 <= upperLimit):
        level += "1"
    else:
        level += "0"
    return level

#%% function from text to %
def checkValueWR(tp1, tp2, tp3, tp4, tp5, tmn1, tmn2, tmn3, tmn4, tmn5, dp1, dp2, dp3, dp4, dp5, downLimit, upperLimit):
    level = 0
    if (tp1 >= 25 and tp1 <= 30 and tmn1 >= 15 and tmn1 <= 20 and dp1 >= downLimit and dp1 <= upperLimit):
        level += 20
    else:
        level += 0
    if (tp2 >= 25 and tp2 <= 30 and tmn2 >= 15 and tmn2 <= 20 and dp2 >= downLimit and dp2 <= upperLimit):
        level += 20
    else:
        level += 0
    if (tp3 >= 25 and tp3 <= 30 and tmn3 >= 15 and tmn3 <= 20 and dp3 >= downLimit and dp3 <= upperLimit):
        level += 20
    else:
        level += 0
    if (tp4 >= 25 and tp4 <= 30 and tmn4 >= 15 and tmn4 <= 20 and dp4 >= downLimit and dp4 <= upperLimit):
        level += 20
    else:
        level += 0
    if (tp5 >= 25 and tp5 <= 30 and tmn5 >= 15 and tmn5 <= 20 and dp5 >= downLimit and dp5 <= upperLimit):
        level += 20
    else:
        level += 0
    return level



#%% Leer archivo
data1 = pd.read_csv('data/d1.txt')
data2 = pd.read_csv('data/d2.txt')
data3 = pd.read_csv('data/d3.txt')
data4 = pd.read_csv('data/d4.txt')
data5 = pd.read_csv('data/d5.txt')

#%% New Data Frame
dataWheatRust = data1
dataWheatRust["Tpro1"] = data1["Tpro"]
dataWheatRust["Tpro2"] = data2["Tpro"]
dataWheatRust["Tpro3"] = data3["Tpro"]
dataWheatRust["Tpro4"] = data4["Tpro"]
dataWheatRust["Tpro5"] = data5["Tpro"]

dataWheatRust["Tmn1"] = data1["Tmax"] - data1["Tmin"]
dataWheatRust["Tmn2"] = data2["Tmax"] - data2["Tmin"]
dataWheatRust["Tmn3"] = data3["Tmax"] - data3["Tmin"]
dataWheatRust["Tmn4"] = data4["Tmax"] - data4["Tmin"]
dataWheatRust["Tmn5"] = data5["Tmax"] - data5["Tmin"]

dataWheatRust["Dpoint1"] = data1["Dpoint"]
dataWheatRust["Dpoint2"] = data2["Dpoint"]
dataWheatRust["Dpoint3"] = data3["Dpoint"]
dataWheatRust["Dpoint4"] = data4["Dpoint"]
dataWheatRust["Dpoint5"] = data5["Dpoint"]

#%% array of Titles
arrayTitles = ['5_7', '7_9', '9_11', '11_13', '13_15', '15_17', '17_19', '19_100']
dRange = [5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0, 19.0]
uRange = [7.0, 9.0, 11.0, 13.0, 15.0, 17.0, 19.0, 100.0]
arrayIndexTitles = []

#%% generate values for index
print('***** Generate ranges')
for i in range(0, len(arrayTitles)):
    for j in range(1, 6):
        tempTitleData = '{}_{}'.format(j,arrayTitles[i])
        temptitleDpoint = 'Dpoint{}'.format(j)
        dataWheatRust[tempTitleData] = [x if (x > dRange[i] and x <= uRange[i]) else 0 for x in dataWheatRust[temptitleDpoint]]

#%% generate index
print('***** Generate Indexes')
for j in range(0, len(arrayTitles)):
    print('***** Index: {}'.format(arrayTitles[j]))
    tempTitleIndex = 'indexWR_{}'.format(arrayTitles[j])
    tempTitleIndexValue = 'indexValueWR_{}'.format(arrayTitles[j])
    arrayIndexTitles.append(tempTitleIndexValue)
    dpTitle1 = '1_{}'.format(arrayTitles[j])
    dpTitle2 = '2_{}'.format(arrayTitles[j])
    dpTitle3 = '3_{}'.format(arrayTitles[j])
    dpTitle4 = '4_{}'.format(arrayTitles[j])
    dpTitle5 = '5_{}'.format(arrayTitles[j])
    dataWheatRust[tempTitleIndex] = dataWheatRust.apply(lambda x: str(checkWR(x['Tpro1'], x['Tpro2'], x['Tpro3'], x['Tpro4'], x['Tpro5'], x['Tmn1'], x['Tmn2'], x['Tmn3'], x['Tmn4'], x['Tmn5'], x[dpTitle1], x[dpTitle2], x[dpTitle3], x[dpTitle4], x[dpTitle5], dRange[j], uRange[j])), axis=1)
    dataWheatRust[tempTitleIndexValue] = dataWheatRust.apply(lambda x: checkValueWR(x['Tpro1'], x['Tpro2'], x['Tpro3'], x['Tpro4'], x['Tpro5'], x['Tmn1'], x['Tmn2'], x['Tmn3'], x['Tmn4'], x['Tmn5'], x[dpTitle1], x[dpTitle2], x[dpTitle3], x[dpTitle4], x[dpTitle5], dRange[j], uRange[j]), axis=1)

#%% Save to csv
print('***** Save to csv in results')
dataWheatRust.to_csv('results/dataWheatRust.csv')    

#%% Maps
for z in arrayIndexTitles:
    plt.figure(figsize=(48,24))
    # create polar stereographic Basemap instance.
    m = Basemap(projection='mill',llcrnrlat=12,urcrnrlat=34,llcrnrlon=-120,urcrnrlon=-85,resolution='i')
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    #m.drawmapboundary(fill_color='aqua')
    #m.fillcontinents(color='lightgray', lake_color='lightblue')
    data = dataWheatRust.filter(['Long','Lat',z], axis=1)
    dataNew = data[data[z] != 0]
    indexWR = np.array(dataNew[z])
    lon = np.array(dataNew["Long"])
    lat = np.array(dataNew["Lat"])
    
    # display min, max values
    print('***** Summary: {}'.format(z))
    print('***** Max: {}'.format(indexWR.max()))
    print('***** Min: {}'.format(indexWR.min()))

    #
    x,y = m(lon, lat)
    # draw filled contours.
    plt.scatter(x,y,s=indexWR, c=indexWR, cmap='RdYlGn_r', vmin=20,vmax=100, alpha=0.5)
    #m.fillcontinents(color='lightgray', lake_color='lightblue')
    cb = plt.colorbar()
    cb.set_label('% WR')

    # add title
    tempPngTitle = 'maps/{}_Map.png'.format(z)
    plt.title(z)
    plt.savefig(tempPngTitle,dpi=300)
    print('***** Saving Map:{}'.format(tempPngTitle))
