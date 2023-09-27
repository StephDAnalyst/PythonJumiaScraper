import scrapy
from JumiaPhone.items import JumiaItem

custom_settings = {
    'ROBOTSTXT_OBEY': False,
    'DOWNLOAD_DELAY': 2,
    'ITEM_PIPELINES': {
        'JumiaPhone.pipelines.SaveToMySQLJumiaPipeline': 400,
    }
}

class PhonespiderSpider(scrapy.Spider):
    name = "Valphonespider"
    allowed_domains = ["jumia.com.ng"]
    start_urls = ["https://www.jumia.com.ng/catalog/?q=phone"]
    page_counter = 0  # Counter for pages scraped

    custom_settings = custom_settings  # Assign custom settings

    def parse(self, response):
        self.page_counter += 1  # Increment the page counter

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
        item = JumiaItem()
        item['url'] = response.url
        item['name'] = response.xpath('//h1[@class="-fs20 -pts -pbxs"]/text()').get()
        item['seller_name'] = response.xpath('//p[@class="-m -pbs"]/text()').get()
        item['seller_score'] = response.xpath('//div[@class="-df -j-bet -fs12"]/div/p/bdo/text()').get()
        item['followers'] = response.xpath('//div[@class="-df -j-bet -fs12"]/div/p[2]/span/text()').get()
        item['rating'] = response.xpath('//div[@class="stars _m _al"]/text()').get()
        item['rating_count'] = response.xpath('//a[@class="-plxs _more"]/text()').get()

        yield item
