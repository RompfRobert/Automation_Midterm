import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import date, timedelta
import time
from drive_upload import upload
from get_top_artists import get_top_artists

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

def main():
    time.sleep(1)
    get_top_artists()
    time.sleep(1)
    upload()
    
main()
