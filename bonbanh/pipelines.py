import pathlib
import json
from scrapy.loader.processors import MapCompose
from scrapy.exporters import JsonLinesItemExporter


class DeleteImageUrlsPipeline:
    def process_item(self, item, spider):
        if "image_urls" in item.keys():
            del item["image_urls"]
        return item


class FilterImageAttribs(object):
    def process_item(self, item, spider):
        if "images" in item.keys():
            if len(item.get("images")) == 0:
                del(item["images"])
            else:
                proc = MapCompose(lambda v: v.get("path"))
                item["images"] = proc(item.get("images"))
        return item

class JsonLineWriterPipeline(object):
    base_data_path = "./data/"
    def open_spider(self, spider):
        pathlib.Path("./data/").mkdir(parents=True, exist_ok=True)
        self.item_file = open(self.base_data_path + "items.jl", "wb")
        self.item_exporter = JsonLinesItemExporter(self.item_file, encoding="utf-8", ensure_ascii=False)
        self.item_exporter.start_exporting()

    def close_spider(self, spider):
        self.item_exporter.finish_exporting()
        self.item_file.close()

    def process_item(self, item, spider):
        self.item_exporter.export_item(item)
