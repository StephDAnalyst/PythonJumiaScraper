import scrapy
import time

custom_settings = {
    'ROBOTSTXT_OBEY': False,  # Disable robots.txt checking
    'DOWNLOAD_DELAY': 2,  # Add a delay of 2 seconds between requests
}

class PhonespiderSpider(scrapy.Spider):
    name = "phonespider"
    allowed_domains = ["jumia.com.ng"]
    start_urls = ["https://www.jumia.com.ng/catalog/?q=phone"]

    
    def parse(self, response):
        phones = response.xpath('//article[@class="prd _fb col c-prd"]')
        for phone in phones:
            relative_url = phone.xpath('descendant::a[@class="core"]/@href').get()
            phone_url = response.urljoin(relative_url)
            yield response.follow(phone_url, callback=self.parse_phone_page)

        next_page = response.xpath('//a[@aria-label="Next Page"]/@href').get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.parse)
    
    def parse_phone_page(self, response):
        yield {
            'url': response.url,
            'name': response.xpath('//h1[@class="-fs20 -pts -pbxs"]/text()').get(),
            'seller_name': response.xpath('//p[@class="-m -pbs"]/text()').get(),
            'seller_score': response.xpath('//div[@class="-df -j-bet -fs12"]/div/p/bdo/text()').get(),
            'followers': response.xpath('//div[@class="-df -j-bet -fs12"]/div/p[2]/span/text()').get(),
            'rating': response.xpath('//div[@class="stars _m _al"]/text()').get(),
            'rating_count': response.xpath('//a[@class="-plxs _more"]/text()').get()
        }
