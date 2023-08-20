# import datetime
# from itemadapter import ItemAdapter
# from scrapy.exceptions import DropItem

# class FilterItemPipeline:

#     def __init__(self, filter_date):
#         self.filter_date = filter_date

#     @classmethod
#     def from_crawler(cls, crawler):
#         settings = crawler.settings
#         filter_date = datetime.datetime.strptime(settings.get('FILTER_ARG'), '%Y-%m-%d %H:%M:%S')
#         return cls(filter_date)

#     def process_item(self, item, spider):
#         adapter = ItemAdapter(item)
#         record_date = adapter.get('RECORD_DATE')
        
#         if record_date is None:
#             return item

#         if isinstance(record_date, str):
#             record_date = datetime.datetime.strptime(record_date, '%Y-%m-%d %H:%M:%S')

#         if record_date < self.filter_date:
#             raise DropItem(f"ITEM DROPPED. RECORD DATE IS EARLIER THAN {self.filter_date}")

#         return item
    