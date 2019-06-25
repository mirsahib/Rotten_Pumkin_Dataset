import csv
import pandas as pd 
myList = []
globalList = []
movieDict = []
row_name = ['title']
with open('myMovieList.csv','r') as f:
    reader = csv.DictReader(f,fieldnames=row_name, delimiter=',')
    for row in reader:
        title = row['title']
        myList.append(title.lower())


row_names = ['movieId', 'title','genres']

with open('movies.csv','r') as f:
    next(f)
    reader = csv.DictReader(f, fieldnames=row_names, delimiter=',')
    for row in reader:
        movie_title = row['title']
        id = row['movieId']
        gen = row['genres']
        globalList.append(movie_title.lower())
        dt = {'id':id,'title':movie_title,'genres':gen}
        movieDict.append(dt)

ID = []
for movie in myList:
    try:
        ID.append(globalList.index(movie))
    except:
        pass
x = []
for i in ID:
    x.append(movieDict[i])

data = pd.DataFrame(x)
data.to_csv("myMovieListWithID.csv",index=False)