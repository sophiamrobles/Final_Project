import scrapy
import csv

class spider_one(scrapy.spider):
## First Read through our dataset and select the url's
    name = 'uno'
    def start_requests(self):
        with open(python/datasets/benign_list_big_final.csv, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                url = row[0]
                yield scrapy.Request(url=url, callback=self.parse)

## Scrape the URL IP address
    def parse(self, response):
        ip_address = response.json().get('origin')
        return ip_address
