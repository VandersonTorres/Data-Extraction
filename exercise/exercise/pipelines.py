from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class FilterItemPipeline:

    def __init__(self, filter_date):
        self.filter_date = filter_date

    @classmethod
    def from_crawler(cls, crawler):
        filter_date = crawler.spider.filter_date
        if filter_date:
            return cls(filter_date)
        else:
            return cls(None)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        record_date = adapter.get('record_date')

        if record_date is None:
            return item

        if self.filter_date and record_date < self.filter_date:
            raise DropItem(f"ITEM DROPPED. RECORD DATE IS EARLIER THAN {self.filter_date}")

        return item