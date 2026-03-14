# Python Port Scanner

Um **scanner de portas simples em Python** que permite verificar quais portas estão abertas em um host.

Este projeto usa apenas bibliotecas padrão do Python (`socket` e `sys`), sendo leve e fácil de usar.

## 🚀 Funcionalidades

* Escaneamento de portas TCP
* Suporte a **lista de portas** (`80,443,8080`)
* Suporte a **intervalo de portas** (`1..1000`)
* Permite **combinar intervalo e portas específicas**
* Timeout configurável

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

## 📊 Saída esperada

```
[+] 80 open
[+] 443 open
```

## ⚠️ Aviso

Este projeto é destinado **apenas para fins educacionais e testes em ambientes autorizados**.
Não utilize este scanner em redes ou sistemas sem permissão.

## 📜 Licença

Livre para uso educacional.
