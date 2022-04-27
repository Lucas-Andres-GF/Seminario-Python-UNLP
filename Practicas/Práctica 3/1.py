import csv
import os

data_set = 'netflix_titles.csv'

ruta = os.path.join(os.getcwd(),data_set)

with open (ruta,'r',encoding='utf8') as data_set :  
    reader = csv.reader(data_set,delimiter=',')
    print(reader.__next__())



