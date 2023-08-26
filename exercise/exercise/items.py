import scrapy

class TreasureBondItem(scrapy.Item):
    treasure_bond_title = scrapy.Field()
    expiration_date = scrapy.Field()
    record_date = scrapy.Field()
    interest_rate = scrapy.Field()
    bond_was_last_updated_at = scrapy.Field()
