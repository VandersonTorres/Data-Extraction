# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import datetime
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class FilterItemPipeline:

    def __init__(self, filter_date):
        # Initializing the pipeline
        self.filter_date = filter_date

    @classmethod
    def from_crawler(cls, crawler):
        # Create a instance of 'settings.py' with the crawler to pass an argument there
        settings = crawler.settings
        filter_date = datetime.datetime.strptime(settings.get('FILTER_ARG'), '%Y-%m-%d %H:%M:%S')
        return cls(filter_date)

    def process_item(self, item, spider):
        # Get specific item ("record_date") in the spyder
        adapter = ItemAdapter(item)
        record_date = adapter.get('RECORD_DATE')
        
        if record_date is None:
            # Do not ignore any item if it is none
            return item

        if isinstance(record_date, str):
            # Parse data to datetime type
            record_date = datetime.datetime.strptime(record_date, '%Y-%m-%d %H:%M:%S')

        if record_date < self.filter_date:
            # Drop items if the condition is satisfying
            raise DropItem(f"ITEM DROPPED. RECORD DATE IS EARLIER THAN {self.filter_date}")

        return item
    