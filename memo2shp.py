# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 22:49:24 2021

@author: cadfj
"""


import re
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import point





string = input('Copie e cole o texto do seu memorial descritivo aqui:')
EPSG = int(input('EPSG de saída: '))
caminho_saida = input('insira o caminho de saída mais o nome do arquivo com a extensão (ex: C:\geo\shape_python\saida1.shp): ')
caminho_saida_xlsx = input('insira o caminho de saída mais o nome do arquivo com a extensão (ex: C:\geo\shape_python\saida1.xlsx): ')
substituicao = re.sub(r'(?<=\d)[.]','', string)
substituicao2 = re.sub(r'(?<=\d)[,]','.', substituicao)
x = (re.findall(r" \d{6}\ | \d{6}\.\d{2,3}", substituicao2))
y = (re.findall(r" \d{7}\ | \d{7}.\d{2,3}", substituicao2))

d = {'col1':x,'col2':y}
df = pd.DataFrame(d)
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.col1, df.col2), crs= EPSG)


df.to_excel(caminho_saida_xlsx)
gdf.to_file(caminho_saida)

print(substituicao2)
print(df)

gdf.plot(figsize=(16,14), facecolor='white', edgecolor='black') #ax=ax

plt.title('Coordenadas Memorial')
plt.show()


