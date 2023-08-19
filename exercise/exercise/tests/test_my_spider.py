# EXEMPLO DE UM MODELO DE TESTE UNITÁRIO
# PRECISO ADAPTAR PARA O CONTEXTO DO MEU SPIDER

import unittest
from scrapy.http import TextResponse
from spiders.token_spider import TokenSpider

class TestYourSpider(unittest.TestCase):
    def setUp(self):
        self.spider = TokenSpider()

    def test_parse_method(self):
        url = 'https://taxas-tesouro.com/'
        response_body = '<html><body><p>Hello, world!</p></body></html>'
        encoding = 'utf-8'
        encoded_response_body = response_body.encode(encoding)
        
        fake_response = TextResponse(
            url=url, 
            body=encoded_response_body
        )
        results = list(self.spider.parse(fake_response))

        # Verificação de resultados conforme o esperado
        self.assertEqual(len(results), 2)
        # self.assertIsInstance(results[0])  # Verificar o tipo do item

if __name__ == '__main__':
    unittest.main()

# Para executar o teste, no terminal, no diretório do projeto:
# python -m unittest tests.test_my_spider