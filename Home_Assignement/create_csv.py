import csv
import datetime

print(datetime.date.today().isocalendar().week)

def create_csv():
    with open('Home_Assignement\\artists.csv') as r_file:
        artists_unsorted = []
        for artist in r_file.readlines():
            artists_unsorted.append(artist[:-1])
        artists_sorted = set(artists_unsorted)
        with open("Home_Assignement\\top_artists.csv", 'w', newline='') as w_file:
            cw = csv.writer(w_file)
            cw.writerow(sorted(list(artists_sorted)))