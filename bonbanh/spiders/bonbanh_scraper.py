# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.shell import inspect_response
from scrapy.linkextractors import LinkExtractor
from config import config
from bonbanh.loaders import BonBanhLoader
from bonbanh.helpers import get_item_info


class BonbanhScraperSpider(scrapy.Spider):
    name = 'bonbanh_scraper'
    allowed_domains = ['bonbanh.com']
    start_urls = ['http://bonbanh.com/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse_index, meta={
                "current_page": 1,
            })

    def parse_index(self, response):
        current_page = response.meta.get("current_page")

        product_details_url_containers = LinkExtractor(restrict_css=".car-item")\
                .extract_links(response)
        if product_details_url_containers:
            for product_url_container in product_details_url_containers:
                yield scrapy.Request(url=product_url_container.url,\
                        callback=self.parse_product_detail)

        if current_page < config.get("max_pagination"):
            yield scrapy.Request('http://bonbanh.com/'+f"oto/page,{current_page+1}",
                    callback=self.parse_index, meta={"current_page": current_page+1})

    def parse_product_detail(self, response):
        bonbanh_loader = BonBanhLoader(response=response)

        image_urls = response.css(config.get("item_image_urls_css"))\
                .xpath(config.get("item_image_urls_xpath")).getall()
        item_info = get_item_info(response)

        bonbanh_loader.add_value("url", response.url)
        bonbanh_loader.add_xpath("brand", config.get("item_brand_xpath"))
        bonbanh_loader.add_xpath("serie", config.get("item_serie_xpath"))
        bonbanh_loader.add_xpath("model_year", config.get("item_model_year_xpath"))
        bonbanh_loader.add_xpath("price_vnd", config.get("item_price_vnd_xpath"))
        bonbanh_loader.add_xpath("price_dol", config.get("item_price_dol_xpath"))
        bonbanh_loader.add_xpath("date", '//*[@id="car_detail"]/div[3]/div/text()')
        bonbanh_loader.add_value("image_urls", image_urls)
        bonbanh_loader.add_value("info", item_info)
        bonbanh_loader.add_css("description", config.get("item_description_css"))

        yield bonbanh_loader.load_item()
