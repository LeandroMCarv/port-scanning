# Python Port Scanner

Um **scanner de portas simples em Python** que permite verificar quais portas estão abertas em um host.

Este projeto usa apenas bibliotecas padrão do Python (`socket`, `sys` e `concurrent.futures`), sendo leve e fácil de usar.

## 🚀 Funcionalidades

* Escaneamento de portas TCP em **paralelo** (multithread), rápido mesmo em ranges grandes
* Suporte a **lista de portas** (`80,443,8080`)
* Suporte a **intervalo de portas** (`1..1000`)
* Permite **combinar intervalo e portas específicas**
* Timeout configurável
* **Identificação do serviço** de cada porta aberta (ex: `ssh`, `http`, `mysql`)
* **Banner grabbing**: tenta capturar a mensagem inicial enviada pelo serviço, quando disponível
* Aceita host como domínio/IP puro ou como URL (`http://site.com:8080/caminho`)

## 📦 Requisitos

* Python 3.x

Nenhuma biblioteca externa é necessária.

## 💻 Como usar

### Escanear portas específicas

```
python3 portscan.py site.com 80,443,8080
```

### Escanear intervalo de portas

```
python3 portscan.py site.com 1..1000
```

### Misturar intervalo com portas específicas

```
python3 portscan.py site.com 20..25,80,443
```

### Definir timeout

```
python3 portscan.py site.com 1..1000 1
```

### Passar uma URL como host

```
python3 portscan.py http://site.com:8080/caminho 80,443,8080
```

## 📊 Saída esperada

```
[+] 22 open (ssh) - banner: SSH-2.0-OpenSSH_9.6
[+] 80 open (http)
[+] 443 open (https)
```

Portas que o Python não reconhece pelo sistema, mas que são comuns (ex: `8080`, `8443`, `3389`), usam uma lista própria de fallback. Quando não é possível identificar, o serviço aparece como `desconhecido`.

## ⚠️ Aviso

Este projeto é destinado **apenas para fins educacionais e testes em ambientes autorizados**.
Não utilize este scanner em redes ou sistemas sem permissão.

## 📜 Licença

Livre para uso educacional.
