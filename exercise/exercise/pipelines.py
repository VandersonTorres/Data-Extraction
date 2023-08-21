import datetime
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class FilterItemPipeline:

    def __init__(self, filter_date):
        self.filter_date = datetime.datetime.strptime(filter_date, '%Y-%m-%d %H:%M:%S')

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        record_date = adapter.get('record_date')
        
        if record_date is None:
            return item

        if record_date < self.filter_date:
            raise DropItem(f"ITEM DROPPED. RECORD DATE IS EARLIER THAN {self.filter_date}")

        return item
    