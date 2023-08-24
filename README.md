# SCRAPING TREASURE BONDS

    This project uses Scrapy framework to extract the following data from 'https://taxas-tesouro.com/':

        - Treasure Bond Title as 'treasure_bond_title';
        - Expiration Date as 'expiration_date';
        - Record Date as 'record_date';
        - Interest Rate as 'interest_rate';
        - Bond Last Update as 'bond_was_last_updated_at';
    
    The return includes respective historic data through the last 90 days.

## SPIDER EXECUTION INSTRUCTIONS

To run the Spider in your own machine, execute the following steps: 

### Open a terminal at the root of project with 'cd command' (/exercise)
* Running Spider:
    - type in terminal: **scrapy crawl treasure_bonds**, then press ENTER. You will have in the terminal all data described above.

* Storing scraped data into an archive:
    - Type in terminal: **scrapy crawl treasure_bonds -O <archive_name>.<archive_format>**, then press ENTER (format example: .json | .csv).

* Filtering escraped data based on a cutoff date:
    - Type in terminal: **scrapy crawl treasure_bonds -a filter_date='yyyy-mm-dd hh:mm:ss'**, then press ENTER. The 'filter_date' is mandatory to keep the format described.

* Storing filtered scraped data into an archive:
    - Type in terminal: **scrapy crawl treasure_bonds -a filter_date='yyyy-mm-dd hh:mm:ss' -O <archive_name>.<archive_format>**, then press ENTER. It is going to filter your desired data and store it into an archive of yours preference. 

## UNITTEST EXECUTION INSTRUCTIONS

We just included a 'tests' folder within the project, which archive 'test_treasure_bonds.py' verify the type of each returned data. To run the Unittest, execute the following steps:

### Open a terminal at the root of project with 'cd command' (/exercise)

* Type in terminal: **python -m unittest discover**. 

You will receive a response that contains information about the types of the returned data. 
The expected types of data are the followings:

    - treasure_bond_title: 'str';
    - expiration_date: 'str';
    - record_date: 'datetime';
    - interest_rate: 'float';
    - bond_was_last_updated_at: 'str';
