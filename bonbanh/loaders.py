from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Identity, MapCompose, Compose
from bonbanh.items import BonbanhItem 
from bonbanh.utils import get_date, get_price_vnd, get_price_dol, image_url_formater

class BonBanhLoader(ItemLoader):
    default_item_class = BonbanhItem
    url_out = TakeFirst()
    brand_out = TakeFirst()
    serie_out = TakeFirst()
    model_year_out = TakeFirst()
    price_vnd_out = get_price_vnd
    price_dol_out = get_price_dol
    date_out = get_date
    info_out = TakeFirst()
    description_out = Compose(Join(" "))
    image_urls_out = MapCompose(image_url_formater)
