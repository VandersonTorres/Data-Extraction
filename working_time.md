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

* **17/08 - 20:10h às 23:50h:** 
    * Desenvolvimento do filtro para dropping com Item Pipeline;
    * Passagem de argumento arbitrário em settings.py;
    * Funções para conversão de dados de acordo com as Especificações Tecnicas;
    * Conversão de datas;
    * Extração dos dados históricos de cada Título;
    * Testes para verificação de formatação e extração;
    * Acredito ter cumprido os requisitos do teste, porém vou tentar implementar testes unitários antes de enviar pull request;
    * Commits usando Git BASH.

* **18/08 - 20:40h às 23:40h:** 
    * Adicionei comentários nos códigos
    * Li sobre o unittest e Spider Contracts
    * Assisti vídeos sobre unittest
    * Criei um template de teste usando o unittest
    * Commits usando Git BASH.

* **19/08 - 14:00h às 19:45h:** 
    * Criei dois testes unitário, um para verificar a função parse() e outro para verificar a função parse_treasure_bonds();
    * Extração atualizada dos dados para o arquivo /treasure_bonds.json;
    * Commits usando Git BASH;
    * Pull request.

* **20/08 - 10:30h às 16:20h:** 
    * Revisão de código requerida;
    * Exclusão de comments desnecessários;
    * Exclusão de arumento arbitrário do 'settings.py';
    * Desativação temporária dos pipelines para ajuste do spider;
    * Ajuste do spider para entrada individual de dados históricos;
    * Ajuste do spider para acrescentar os quesitos do item 4. das especificações tecnicas nos dados históricos;
    * Teste de extração dos dados;
    * Uso de Meta Argument do Scrapy para preservar o dado 'Atualizado_em' da requisição do primeiro método;
    * Commits usando Git BASH.

* **20/08 - 16:20h às 19:15h:** 
    * Compreensão do dado solicitado 'record_date';
    * Adaptação do spider para extrair corretamente o record_date e o interest_rate;
    * Conversão do record_date de 'str' para 'datetime'     
    * Commits usando Git BASH.

* **20/08 - 19:15h às 22:20h:** 
    * Tentativa de realizar um unittest para testar os tipos dos dados retornados no spider, mas sem sucesso;     
    * Commits usando Git BASH.

* **20/08 - 22:50h às 00:25h:** 
    * Adaptando o spider para retornar os dados na classe item;
    * Criando novamente um pipeline;     
    * Commits usando Git BASH.