import scrapy
import json
import datetime

class TokenSpider(scrapy.Spider):
    name = "token"
    allowed_domains = ["taxas-tesouro.com"]
    start_urls = ['https://taxas-tesouro.com/']

    def parse(self, response):        
        last_updated_at = response.css('div span.text-gray-600::text').getall()
        yield {'last_updated_at': last_updated_at}
        yield scrapy.Request(
            'https://taxas-tesouro.com/page-data/index/page-data.json', 
            callback=self.parse_treasure_bonds
        )

    def parse_treasure_bonds(self, response):
        data = json.loads(response.text)
        treasure_bonds = data['result']['data']['dataJson']['compra']
        
        last_updated_at = data['result']['data']['dataJson']['mercado']['str_ts']
        parse_dt_last_updated_at = datetime.datetime.strptime(last_updated_at, '%d/%m/%Y %H:%M')
        parse_utc_plus_3_last_updated_at = parse_dt_last_updated_at + datetime.timedelta(hours=3)
        last_updated_at_iso_format = parse_utc_plus_3_last_updated_at.isoformat()

        for key in treasure_bonds:
            yield {
                'treasure_bond_title': key["name"],
                'expiration_date': key["maturity_at"],
                'record_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'interest_rate': key["rate"],
                'bond_was_last_updated_at': last_updated_at_iso_format
            }