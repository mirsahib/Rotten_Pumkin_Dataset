import csv
import os

myMovieList = os.listdir('/media/mirsahib/VIDEO/English Movie')

for movie in myMovieList:
    with open('myMovieList.csv','a',newline='') as out_csv:
        writer = csv.writer(out_csv,delimiter = ',')
        writer.writerow([movie])