import datetime
import json
import unittest
from scrapy.http import TextResponse, Request
from spiders.treasure_bonds import TreasureBondsSpider

class TestTreasureBondsSpider(unittest.TestCase):

    def setUp(self):
        self.spider = TreasureBondsSpider()

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
                                        "ts": "2023-08-17T15:19:00",
                                        "rate": "0.0585"
                                    },
                                ],
                                "rate": 0.0585,  
                                "maturity_at": "2026-03-01",
                            }
                        ],
                        'mercado': {'str_ts': "18/08/2023 15:20"}
                    }
                }
            }
        }

        response = TextResponse(url="https://taxas-tesouro.com/page-data/index/page-data.json", body=json.dumps(mock_data).encode('utf-8'))
        self.spider.last_updated_at = ["Atualizado em", "18/08/2023 15:20"]  # Simulating self.last_updated_at
        results = list(self.spider.parse_treasure_bonds(response))

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