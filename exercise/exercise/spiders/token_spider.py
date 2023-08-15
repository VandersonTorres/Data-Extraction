import scrapy
import json

class TokenSpider(scrapy.Spider):
    name = "token"
    page = 1
    allowed_domains = ["taxas-tesouro.com"]
    start_urls = ['https://taxas-tesouro.com/page-data/index/page-data.json']

    def parse(self, response):
        data = json.loads(response.text)
        for token in data["result"]:
            yield {
                'treasure_bond_title': token["name"],
                # 'expiration_date': token["maturity_at"],
                # 'record_date': token["name"],
                # 'interest_rate': token["rate"],
                # 'bond_was_last_updated_at': token.css('.sm\:text-right span::text').getall()
            }

# PARA EXECUTAR A EXTRAÇÃO DOS DADOS, NO TERMINAL: 
# Entre na pasta do projeto com "cd .\<pasta>"
# Execute o comando "scrapy crawl token"

# PARA SALVAR OS DADOS EM UM ARQUIVO .JSON (por exemplo), NO TERMINAL:
# Execute o comando "scrapy crawl token -O token.json"