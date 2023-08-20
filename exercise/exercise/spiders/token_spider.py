import scrapy
import json
import datetime

class TokenSpider(scrapy.Spider):
    name = "token"
    allowed_domains = ["taxas-tesouro.com"]
    start_urls = ['https://taxas-tesouro.com/']

    def parse(self, response):
        self.last_updated_at = response.css('div span.text-gray-600::text').getall()
        yield {'last_updated_at': self.last_updated_at}
        
        yield scrapy.Request(
            'https://taxas-tesouro.com/page-data/index/page-data.json', 
            callback=self.parse_treasure_bonds,
            meta={'last_updated_at': self.last_updated_at}
        )

    def parse_treasure_bonds(self, response):
        data = json.loads(response.text)
        
        treasure_bonds = data['result']['data']['dataJson']['compra']
        
        last_updated_at = response.meta.get('last_updated_at')
        parse_dt_last_updated_at = datetime.datetime.strptime(last_updated_at[1], '%d/%m/%Y %H:%M')
        parse_utc_plus_3_last_updated_at = parse_dt_last_updated_at + datetime.timedelta(hours=3)
        last_updated_at_iso_format = parse_utc_plus_3_last_updated_at.isoformat()

        for key in treasure_bonds:
            for hist_item in key['hist']:
                yield {
                    'históric_data': hist_item,
                    'treasure_bond_title': key["name"],
                    'expiration_date': key["maturity_at"],
                    'record_date': datetime.datetime.now(),
                    'interest_rate': float(key["rate"]),
                    'bond_was_last_updated_at': last_updated_at_iso_format
                }