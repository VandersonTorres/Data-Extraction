import scrapy
import json
import datetime

class TokenSpider(scrapy.Spider):
    name = "token"
    allowed_domains = ["taxas-tesouro.com"]
    start_urls = ['https://taxas-tesouro.com/page-data/index/page-data.json']

    def parse(self, response):
        data = json.loads(response.text)
        atualizacao = data['result']['data']['dataJson']['mercado']
        titulos = data['result']['data']['dataJson']['compra']
        resgate = data['result']['data']['dataJson']['venda']
        
        # ESPECIFICAÇÕES TÉCNICAS:
        # Ítem 3. AS LINHAS DO CAMPO RESGATE DEVEM SER IGNORADAS
        # (Coloquei apenas para evidenciar que o 'resgate' está no Dict 'venda')

        atualizado_em = yield {'last_updated_at': atualizacao["str_ts"]}

        # Armazenei o 'yield' acima numa variável para tentar usar o valor na última requisição do spider
        # Porém ainda sem sucesso...

        for key in titulos:
            yield {
                'treasure_bond_title': key["name"],
                'expiration_date': key["maturity_at"],
                'record_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'interest_rate': key["rate"],
                # 'bond_was_last_updated_at': response.css('div span.text-gray-600::text').getall()
            }