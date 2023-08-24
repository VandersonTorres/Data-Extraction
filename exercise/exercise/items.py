import scrapy

class TreasureBondItem(scrapy.Item):
    treasure_bond_title = scrapy.Field()
    expiration_date = scrapy.Field()
    record_date = scrapy.Field()
    interest_rate = scrapy.Field()
    bond_was_last_updated_at = scrapy.Field()

    def order_response(self):
        ordered_fields = [
            'treasure_bond_title',
            'expiration_date',
            'record_date',
            'interest_rate',
            'bond_was_last_updated_at'
        ]
        ordered_data = {field: self[field] for field in ordered_fields}
        return ordered_data
