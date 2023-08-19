import datetime
import json
import unittest
from unittest.mock import Mock
from scrapy.http import TextResponse
from spiders.token_spider import TokenSpider

class TestTokenSpider(unittest.TestCase):

    def setUp(self):
        # Creating an instace of my spider class
        self.spider = TokenSpider()

    def test_parse(self):
        # Testing 'parse method' of spider
        # Verifying if the object extracted of Selector contains 'Updated'

        fake_response = TextResponse(url='https://taxas-tesouro.com', body=b'<div><span class="text-gray-600">FAKE MESSAGE</span></div>')
        result = list(self.spider.parse(fake_response))
        self.assertEqual(result[0]['last_updated_at'], ['Updated'])

    def test_parse_treasure_bonds(self):
        # Testing 'parse_treasure_bonds method' of spider
        # Verifying if types of data are according to expected

        mock_data = {
            "result": {
                "data": {
                    "dataJson": {
                        "compra": [
                            {
                                "name": "Tesouro Selic 2026",
                                "hist": [
                                    {
                                        "ts": "2023-08-17T15:19:00",
                                        "rate": "0.0585"
                                    },
                                ],
                                "rate": 0.0585,  
                                "maturity_at": "2026-03-01",
                            },
                            {
                                "name": "Tesouro Selic 2029",
                                "hist": [
                                    {
                                        "ts": "2023-08-17T15:19:00",
                                        "rate": "0.1576"
                                    },
                                ],
                                "maturity_at": "2029-03-01",
                                "rate": 0.1576
                            }
                        ],
                        'mercado': {'str_ts': "18/08/2023 15:20"}
                    }
                }
            }
        }
        
        mock_response = Mock()
        mock_response.text = json.dumps(mock_data)
        results = list(self.spider.parse_treasure_bonds(mock_response))
        self.assertEqual(len(results), 2)

        for result in results:
            self.assertIsInstance(result['TREASURE_BOND_TITLE'], str)
            self.assertIsInstance(result['HISTORIC_DATA'], list)
            self.assertIsInstance(result['EXPIRATION_DATE'], str)
            self.assertIsInstance(result['RECORD_DATE'], datetime.datetime)
            self.assertIsInstance(result['INTEREST_RATE'], float)
            self.assertIsInstance(result['BOND_WAS_LAST_UPDATED_AT'], str)

if __name__ == '__main__':
    unittest.main()

# Para executar o teste, no terminal, no diretório do projeto:
# python -m unittest tests.test_my_spider