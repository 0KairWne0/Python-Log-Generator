# Gerador de Logs para Análise

Este script tem como objetivo gerar um arquivo de logs fictício para ser utilizado em análises de dados ou testes de sistemas de monitoramento. O arquivo gerado terá 100000 linhas de logs web com variedade de solicitações HTTP, user agents, IPs e log messages.

## Funcionamento

O script gera um arquivo de logs com base em listas pré-definidas de URLs, métodos HTTP, user agents e mensagens de log. Para cada linha do arquivo de logs, são escolhidos aleatoriamente um método HTTP, uma URL, um código de status, um user agent, uma mensagem de log e um endereço IP. O arquivo resultante pode ser personalizado facilmente através da modificação das listas de valores pré-definidos.

## Detalhes do Script

O script foi implementado em Python e utiliza a biblioteca `logging` para escrever as linhas de log em um arquivo. Ele também utiliza a biblioteca `random` para gerar valores aleatórios a serem utilizados na criação das linhas de log.

O arquivo gerado terá 100000 linhas de logs web com os seguintes dados:

-   Endereço IP
-   Data e hora da requisição
-   Método HTTP utilizado
-   URL acessada
-   Código de status da resposta
-   Tamanho da resposta
-   User agent utilizado
-   Mensagem de log

## Modificação do Script

O script pode ser facilmente modificado para atender às necessidades específicas do usuário. Algumas possibilidades de modificação incluem:

-   Alteração da quantidade de linhas de logs geradas
-   Adição de novos valores às listas pré-definidas de URLs, métodos HTTP, user agents e mensagens de log
-   Alteração da formatação das linhas de log para atender a padrões específicos
-   Personalização do arquivo de saída (nome, diretório, etc.)

## Modo de uso

Kali linux
```kali
chmod +x Glog.py
./Glog.py
```

O script vai gerar um arquivo exemplo.log no local que ele estiver
