import datetime
import json
import unittest
from scrapy.http import TextResponse, Request
from exercise.spiders.treasure_bonds import TreasureBondsSpider

class TestTreasureBondsSpider(unittest.TestCase):

    def setUp(self):
        self.spider = TreasureBondsSpider()

    def test_parse_treasure_bonds(self):
        json_sample = {
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
                                "maturity_at": "2026-03-01",
                                "rate": 0.0585,  
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
                    }
                }
            }
        }

        simulated_request = Request(url="https://taxas-tesouro.com/page-data/index/page-data.json")
        simulated_request.meta["last_updated_at"] = "18/08/2023 15:20"

        simulated_response = TextResponse(url=simulated_request.url, request=simulated_request, body=json.dumps(json_sample).encode('utf-8'))

        results = self.spider.parse_treasure_bonds(simulated_response)


        for result in results:
            self.assertIsInstance(result['treasure_bond_title'], str)
            self.assertIsInstance(result['expiration_date'], str)
            self.assertIsInstance(result['record_date'], datetime.datetime)
            self.assertIsInstance(result['interest_rate'], float)
            self.assertIsInstance(result['bond_was_last_updated_at'], str)

if __name__ == '__main__':
    unittest.main()