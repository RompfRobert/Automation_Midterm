import scrapy
from ..items import HomeAssignementItem
from datetime import date, timedelta
import csv

# Clear the CSV
open('artists.csv', 'w').close()
open('all_artists.csv', 'w').close()

class HomeAssignement(scrapy.Spider):
    name = "Home_Assignement"
    
    start_urls = []
    for i in range(4):
        if i == 0:   
            start_urls.append(f"https://www.billboard.com/charts/artist-100/{date.today()}")
        else:
            start_urls.append(f"https://www.billboard.com/charts/artist-100/{date.today()-timedelta(i * 7)}")
    
    def create_csv(self):
        with open('artists.csv') as r_file:
            artists_unsorted = []
            for artist in r_file.readlines():
                artists_unsorted.append(artist[:-1])
            artists_sorted = set(artists_unsorted)
            with open("top_artists.csv", 'w', newline='') as w_file:
                cw = csv.writer(w_file)
                cw.writerow(sorted(list(artists_sorted)))
        
    def parse(self, response):
        # Create blueprint
        items = HomeAssignementItem()
                        
        # Container
        artists = response.css('.o-chart-results-list-row-container')
    
        counter = 0
        with open("all_artists.csv", 'a', newline='') as all_file:
            cw_all = csv.writer(all_file)
            with open("artists.csv", 'a', newline='') as file: 
                csv_writer = csv.writer(file)
                for artist in artists:
                    all_artists = []
                    top5_artists = []  
            
                    name = artist.css("#title-of-a-story::text").extract()
                    items['name'] = name[0][14:-5]
                    rank = artist.css(".c-label.a-font-primary-bold-l::text").extract()
                    items['rank'] = rank[0][4:-1]
                    
                    all_artists.append(items['name'])
                    all_artists.append(items['rank'])
                    cw_all.writerow(all_artists)
                    
                    if counter <= 5:
                        top5_artists.append(items['name'])
                        csv_writer.writerow(top5_artists)
                    counter += 1
                    yield items
        
        if counter == 3:
            self.create_csv()                