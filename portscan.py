import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

COMMON_PORTS = {
    21: "ftp",
    22: "ssh",
    23: "telnet",
    25: "smtp",
    53: "dns",
    80: "http",
    110: "pop3",
    135: "msrpc",
    139: "netbios-ssn",
    143: "imap",
    443: "https",
    445: "microsoft-ds",
    993: "imaps",
    995: "pop3s",
    1433: "mssql",
    1521: "oracle",
    3000: "dev-http",
    3306: "mysql",
    3389: "rdp",
    4444: "metasploit/backdoor",
    5000: "dev-http",
    5432: "postgresql",
    5900: "vnc",
    6379: "redis",
    8000: "http-alt",
    8080: "http-proxy",
    8443: "https-alt",
    9200: "elasticsearch",
    27017: "mongodb",
}


def get_service_name(port):
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return COMMON_PORTS.get(port, "desconhecido")


def grab_banner(client):
    try:
        client.settimeout(0.5)
        banner = client.recv(128)
        return banner.decode(errors="replace").strip()
    except Exception:
        return ""


def normalize_host(host_input):
    host = host_input

    if "://" in host:
        host = host.split("://", 1)[1]

    host = host.split("/", 1)[0]   # remove path
    host = host.split("?", 1)[0]   # remove query string

    if ":" in host:
        host = host.split(":", 1)[0]  # remove porta embutida (ex: localhost:8000)

    return host


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


def scan_port(host, port, timeout):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(timeout)

        code = client.connect_ex((host, port))

        if code == 0:
            service = get_service_name(port)
            banner = grab_banner(client)
            client.close()
            return port, service, banner

        client.close()

    except Exception:
        pass

    return None


def scan(host, ports, timeout=0.5, max_workers=200):
    try:
        socket.gethostbyname(host)
    except socket.gaierror as e:
        print(f"Erro! nao foi possivel resolver o host '{host}':", e)
        return

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(scan_port, host, port, timeout) for port in ports]

        for future in as_completed(futures):
            result = future.result()
            if not result:
                continue

            port, service, banner = result

            if banner:
                print(f"[+] {port} open ({service}) - banner: {banner}")
            else:
                print(f"[+] {port} open ({service})")


if __name__ == "__main__":
    # Evita crash ao imprimir banners com caracteres fora do
    # charset padrao do console do Windows (cp1252/charmap).
    try:
        sys.stdout.reconfigure(errors="replace")
    except AttributeError:
        pass

    if len(sys.argv) >= 2:

        host = normalize_host(sys.argv[1])

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