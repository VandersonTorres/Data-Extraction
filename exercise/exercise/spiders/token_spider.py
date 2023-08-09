import scrapy

class TokenSpider(scrapy.Spider):
    name = "token"

    start_urls = [
        'https://taxas-tesouro.com/'
    ]

    def parse(self, response):
        for token in response.css('div.VERIFICAR TAG'):
            yield {
                'treasure_bond_title': token.css('VERIFICAR TAG').getall(),
                'expiration_date': token.css('VERIFICAR TAG').getall(),
                'record_date': token.css('VERIFICAR TAG').getall(),
                'interest_rate': token.css('VERIFICAR TAG').getall(),
                'bond_was_last_updated_at': token.css('VERIFICAR TAG').getall(),
            }

        # Extrair dados de uma próxima página, se houver...
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

# PARA EXECUTAR A EXTRAÇÃO DOS DADOS, NO TERMINAL: 
# Entre na pasta do projeto com "cd .\<pasta>"
# Execute o comando "scrapy crawl token"

# PARA SALVAR OS DADOS EM UM ARQUIVO .JSON (por exemplo), NO TERMINAL:
# Execute o comando "scrapy crawl token -O token.json"