import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import date, timedelta
import pandas as pd
import csv
import time
from drive_upload import upload

today = date.today()
last_month = date.today()-timedelta(21)

class BillboardSpider(scrapy.Spider):
    name = "Home_Assignement"
    
    def start_requests(self):
        yield scrapy.Request(f'https://www.billboard.com/charts/artist-100/{today}')
        
    def parse(self, response):
        artists = response.css('.o-chart-results-list-row-container')
        for artist in artists: 
            name = artist.css("#title-of-a-story::text").extract()
            rank = artist.css(".c-label.a-font-primary-bold-l::text").extract()
            
            yield {
                'name': name[0][14:-5],
                'rank': rank[0][4:-1]
            } 
        
        for i in range(1, 4):
            yield(scrapy.Request(f'https://www.billboard.com/charts/artist-100/{today - timedelta(i * 7)}'))

process = CrawlerProcess(settings = {
    'FEED_URI': f'artists({today})-({last_month}).csv',
    'FEED_FORMAT': 'csv'
})

process.crawl(BillboardSpider)
process.start()

def get_top_artists():
    df = pd.read_csv(f'artists({today})-({last_month}).csv')
    with open(f'top-artists({today})-({last_month}).csv', 'w', newline='') as file:
        artists = df.loc[df['rank'] < 6].set_index('name')
        unsorted_artists = set(artists.index)
        sorted_artists = list(unsorted_artists)
        sorted_artists.sort()
        writer = csv.writer(file)
        writer.writerow(sorted_artists)

def main():
    time.sleep(1)
    get_top_artists()
    time.sleep(1)
    upload()
    
main()
