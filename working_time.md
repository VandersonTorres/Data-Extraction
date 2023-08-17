# WORKING TIME

* **09/08 - 19:30h às 20:35h:** 
    * Abordagem inicial;
    * Criação/ ativação Ambiente Virtual;
    * Criação do módulo de Web Scraping (scrapy);
    * Montagem da estrutura inicial do Spider;
    * Leitura da documentação de raspagem de conteúdo dinâmico (https://docs.scrapy.org/en/latest/topics/dynamic-content.html);
    * Commits usando Git BASH.

* **10/08 - 19:30h às 22:00h:** 
    * Teste de raspagem dos dados usando o 'scrapy shell' e 'fetch';
    * Armazenamento do teste em .JSON (para análise);
    * Pesquisa e estudo sobre raspagem;
    * Leitura da documentação do Scrapy;
    * Leitura da documentação sobre uso de seletores;
    * Tentativa de raspagem seletiva dos dados solicitados... (sem sucesso);
    * Pesquisas internet;
    * Commits usando Git BASH.

* **14/08 - 19:00h às 22:30h:** 
    * Rastreamento da origem do conteúdo dinâmico;
    * Busca nas Dev Tools (Network) pelas requisições;
    * Encontrei o arquivo dos dados .json;
    * Modificação do Spider para raspagem dos dados solicitados de acordo com o objeto JSON encontrado;
    * Execução sem sucesso (não consigo direcionar o Spider para o objeto de 'compra');
    * Commits usando Git BASH.

* **15/08 - 19:00h às 22:10h:** 
    * Modificação do Spider para raspagem dos dados a partir do API Endpoint encontrado nas Dev Tools;
    * Sucesso na requisição dos dados solicitados nas Especificações técnicas, com exceção do último dado;
    * Durante o dia fiz pesquisas no StackOverFlow e também assisti à vídeos como esse: "https://www.youtube.com/watch?v=xjieRVnuPcQ&t=5s";
    * Consegui iterar sobre os objetos JSON aninhados;
    * Commits usando Git BASH.

* **16/08 - 20:30h às 23:10h:** 
    * Modificação do Spider para raspagem do 'Atualizado em' com seletor, e demais dados dos títulos com API JSON do Endpoint;
    * Realizado nova requisição para o documento da API, e criada função de callback
    * Converti o 'bond_was_last_updated_at' para formato ISO e Horário ZULU;
    * Commits usando Git BASH.