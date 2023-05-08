import logging
import random

# Configuração básica de logging
logging.basicConfig(filename='exemplo.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

# Lista de URLs de exemplo
urls = [
    "/",
    "/about",
    "/contact",
    "/products",
    "/services",
]

# Lista de métodos HTTP
http_methods = [
    "GET",
    "POST",
    "OPTIONS",
    "HEAD",
    "PUT",
    "DELETE",
    "TRACE",
    "CONNECT",
]

# Lista de user agents de exemplo
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
]

# Lista de log messages de exemplo
log_messages = [
    "Connection refused by server",
    "Timeout waiting for response from server",
    "Invalid request received",
    "Access denied due to invalid credentials",
    "Server error occurred",
    "Application crashed",
]

# Lista de IPs
ips = []
for i in range(1000):
    ips.append(".".join(str(random.randint(0, 255)) for _ in range(4)))

# Gera 1000 linhas de logs web com variedade de solicitações HTTP, user agents, IPs e log messages
logs = []
for ip_address in ips:
    for i in range(100):
        http_method = random.choice(http_methods)
        url = random.choice(urls)
        status_code = random.choice([200, 400, 404, 500])
        user_agent = random.choice(user_agents)
        log_message = random.choice(log_messages)
        log_entry = f"{ip_address} - - [{i}] \"{http_method} {url} HTTP/1.1\" {status_code} 2612 \"{url}\" \"{user_agent}\" - {log_message}"
        if i == 50 and ip_address == ips[0]:
            log_entry += " KEY[12312JB3N21I3]"
        logs.append(log_entry)

# Escreve os logs no arquivo
for log in logs:
    logging.info(log)
