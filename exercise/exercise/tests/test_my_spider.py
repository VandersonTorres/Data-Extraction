import datetime
import json
import unittest
from unittest.mock import Mock
from scrapy.http import TextResponse
from spiders.token_spider import TokenSpider

class TestTokenSpider(unittest.TestCase):

    def setUp(self):
        self.spider = TokenSpider()

    def test_parse(self):
        fake_response = TextResponse(url='https://taxas-tesouro.com', body=b'<div><span class="text-gray-600">Updated</span></div>')
        result = list(self.spider.parse(fake_response))
        self.assertEqual(result[0]['last_updated_at'], ['Updated'])

    def test_parse_treasure_bonds(self):
        mock_data = {
            "result": {
                "data": {
                    "dataJson": {
                        "compra": [
                            {
                                "name": "Tesouro Selic 2026",
                                "hist": [
                                    {
                                        "ts": "11111111",
                                        "rate": "11111111"
                                    },
                                    {
                                        "ts": "222222222",
                                        "rate": "22222222"
                                    },
                                    {
                                        "ts": "333333333",
                                        "rate": "333333333"
                                    },
                                ],
                                "rate": 0.0585,  
                                "maturity_at": "2026-03-01",
                            },
                            {
                                "name": "Tesouro Selic 2029",
                                "hist": [
                                    {
                                        "ts": "11111111",
                                        "rate": "11111111"
                                    },
                                    {
                                        "ts": "222222222",
                                        "rate": "22222222"
                                    },
                                    {
                                        "ts": "333333333",
                                        "rate": "333333333"
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
            self.assertIsInstance(result['treasure_bond_title'], str)
            self.assertIsInstance(result['expiration_date'], str)
            self.assertIsInstance(result['record_date'], datetime.datetime)
            self.assertIsInstance(result['interest_rate'], float)
            self.assertIsInstance(result['bond_was_last_updated_at'], str)

if __name__ == '__main__':
    unittest.main()

# Para executar o teste, no terminal, no diretório do projeto:
# python -m unittest tests.test_my_spider