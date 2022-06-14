import pandas as pd 
from shapely.geometry import Point
import geopandas as gpd 
import matplotlib.pyplot as plt 
import os
import os.path

ok = True
comunas_caba_shp = "comunas.shp"
rampas_relevamiento_2016 = "rampas-de-accesibilidad-relevamiento-2016.csv"
path_datasets = os.path.join(os.getcwd())

print(path_datasets)

comunas = gpd.read_file(os.path.join(path_datasets, comunas_caba_shp))
comunas.head(3) #primeros tres

comunas.plot(figsize=(10,10), color='beige', edgecolor='red')

comunas['coords'] = comunas['geometry'].apply(lambda x: x.representative_point().coords[:])
print(type(comunas))

comunas['coords'] = [coords[0] for coords in comunas['coords']]

comunas['label'] = comunas.apply(lambda df : 'Comuna ' + str(int(df['COMUNAS'])),axis=1) #Axis = 1 

fig, ax = plt.subplots(figsize = (10,10))
comunas.plot(ax = ax, color='beige', edgecolor='black')
for idx, row in comunas.iterrows():
    plt.annotate(text = row['label'], xy = row['coords'],horizontalalignment = 'center', color='black')

rampas_2016 = pd.read_csv(os.path.join(path_datasets,rampas_relevamiento_2016),delimiter=';')
rampas_2016    

geometry = [Point(xy) for xy in zip(rampas_2016['X'],rampas_2016['Y'])]
geometry[:3]


rampas_2016_gdf = gpd.GeoDataFrame(rampas_2016,crs='epsg:4326',geometry=geometry,)
rampas_2016_gdf

rampas_2016_gdf['ESTADO'].unique()# Saber cuales son los tipos de estado


fig, ax = plt.subplots(figsize = (15,15))
comunas.plot(ax = ax, color='beige', edgecolor='black')

for idx, row in comunas.iterrows():
    plt.annotate(text=row['label'], xy=row['coords'],horizontalalignment='center', color='black')

rampas_2016_gdf[rampas_2016_gdf['ESTADO']=='FINALIZADO'].plot(ax=ax,markersize=30, color='blue', marker='o', label='Finalizado')
rampas_2016_gdf[rampas_2016_gdf['ESTADO']=='EN EJECUCIÓN'].plot(ax=ax,markersize=30, color='red', marker='1', label='En ejecución')
plt.legend(prop={'size': 15})