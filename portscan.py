import socket
import sys

def parse_ports(port_input):
    ports = []

    parts = port_input.split(",")

    for part in parts:
        if ".." in part:
            start, end = part.split("..")
            ports.extend(range(int(start), int(end) + 1))
        else:
            ports.append(int(part))

    return ports


def scan(host, ports, timeout=0.5):
    try:
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(timeout)

            code = client.connect_ex((host, port))

            if code == 0:
                print(f"[+] {port} open")

            client.close()

    except Exception as e:
        print("Erro!", e)


if __name__ == "__main__":

    if len(sys.argv) >= 2:

        host = sys.argv[1]

        if len(sys.argv) >= 3:
            ports = parse_ports(sys.argv[2])
        else:
            ports = [21,22,23,25,80,443,445,8080,8443,3306,139,135,4444]

        timeout = float(sys.argv[3]) if len(sys.argv) >= 4 else 0.5

        scan(host, ports, timeout)

    else:
        print("Uso: python3 portscan.py host portas")
        print("Exemplos:")
        print("python3 portscan.py site.com 80,443,8080")
        print("python3 portscan.py site.com 1..1000")
        print("python3 portscan.py site.com 20..25,80,443")