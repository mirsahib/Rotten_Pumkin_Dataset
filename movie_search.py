import csv
import re

row_names = ['movieId', 'title','genres']

with open('movies.csv','r') as f:
    next(f)
    reader = csv.DictReader(f, fieldnames=row_names, delimiter=',')
    for row in reader:
        movie_title = row['title']
        movie_id = row['movieId']
        genre = row['genres']
        try:
            match = re.search('\\d{4}',movie_title)
            year = int(match.group(0))
            if year==2016:
                try:
                    with open('movies_16.csv','a',newline='') as out_csv:
                        writer = csv.writer(out_csv, delimiter=',')
                        writer.writerow([movie_id, movie_title,genre])
                except:
                    pass
        except:
            pass





