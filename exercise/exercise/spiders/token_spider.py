import scrapy
import json
import datetime

class TokenSpider(scrapy.Spider):
    name = "token"
    allowed_domains = ["taxas-tesouro.com"]
    start_urls = ['https://taxas-tesouro.com/']

    def parse(self, response):
        # Extract last updated time from the initial webpage
        last_updated_at = response.css('div span.text-gray-600::text').getall()
        yield {'last_updated_at': last_updated_at}
        
        # Send a request to get treasure bond data
        yield scrapy.Request(
            'https://taxas-tesouro.com/page-data/index/page-data.json', 
            callback=self.parse_treasure_bonds
        )

    def parse_treasure_bonds(self, response):
        # Load JSON data from the response
        data = json.loads(response.text)
        
        # Extract treasure bond data from the JSON
        treasure_bonds = data['result']['data']['dataJson']['compra']
        
        # Extract last updated time from the JSON and convert to ISO format and UTC Zulu
        last_updated_at = data['result']['data']['dataJson']['mercado']['str_ts']
        parse_dt_last_updated_at = datetime.datetime.strptime(last_updated_at, '%d/%m/%Y %H:%M')
        parse_utc_plus_3_last_updated_at = parse_dt_last_updated_at + datetime.timedelta(hours=3)
        last_updated_at_iso_format = parse_utc_plus_3_last_updated_at.isoformat()

        # Yield each treasure bond record
        for key in treasure_bonds:
            rate_as_float = float(key["rate"])
            record_date_as_datetime = datetime.datetime.now()

            yield {
                'TREASURE_BOND_TITLE': key["name"],
                'HISTORIC_DATA': key["hist"],
                'EXPIRATION_DATE': key["maturity_at"],
                'RECORD_DATE': record_date_as_datetime,
                'INTEREST_RATE': rate_as_float,
                'BOND_WAS_LAST_UPDATED_AT': last_updated_at_iso_format
            }

# CHECK LIST DE VERIFICAÇÃO DO EXERCÍCIO
# 1. Utilização do Scrapy para a Raspagem dos dados:            OK;
# 2. Seguir o esquema e formatos de Especificações Técnicas:    OK;
# 3. Fazer transmissão de dado em framework assíncrono:         OK;
# 4. Permitir a filtragem de items utilizando um ItemPipeline:  OK;

# ESPECIFICAÇÕES TÉCNICAS
# 1. Acessar o site https://taxas-tesouro.com/:                             OK;
# 2. Extrair da página inicial a informação "Atualizado em {DATA} {HORA}":  OK;
# 3. Acessar Títulos Disponíveis para Investimento (sem campo Resgate):     OK;
# 4. Extrair as informações do título, incluindo dados históricos:          OK;

# 4.1 Campos para preenchimento:
#       treasure_bond_title: STR        OK;
#       expiration_date: STR            OK;
#       record_date: DATETIME           OK; 
#       interest_rate: FLOAT            OK;
#       bond_was_last_updated_at: STR   OK;

# 4.2 O útlimo campo será sempre o mesmo valor da página inicial:       OK;
# 5. Utilizar um filtro com argumento arbitrário em um Item Pipeline:   OK.
