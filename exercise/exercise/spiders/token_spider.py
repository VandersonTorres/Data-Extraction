import scrapy

class TokenSpider(scrapy.Spider):
    name = "token"

    start_urls = [
        'https://taxas-tesouro.com/'
    ]

    def parse(self, response):
        treasure_bond_title = response.css('.text-sm span::text').getall()
        bond_was_last_updated_at = response.css('.sm\:text-right span::text').getall()

        for token in response.css('div.flex'):
            yield {
                'treasure_bond_title': token.css('div.text-sm span::text').get(),
                # 'expiration_date': token.css(''),
                # 'record_date': token.css(''),
                # 'interest_rate': token.css(''),
                'bond_was_last_updated_at': token.css('.sm\:text-right span::text').getall()
            }

# PARA EXECUTAR A EXTRAÇÃO DOS DADOS, NO TERMINAL: 
# Entre na pasta do projeto com "cd .\<pasta>"
# Execute o comando "scrapy crawl token"

# PARA SALVAR OS DADOS EM UM ARQUIVO .JSON (por exemplo), NO TERMINAL:
# Execute o comando "scrapy crawl token -O token.json"