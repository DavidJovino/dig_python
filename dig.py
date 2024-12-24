import socket
import argparse

# Função para resolver domínio para IP
def resolve_domain(host):
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        return None

def main(input_file, output_file):
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                # Extrair apenas o host da URL
                host = line.strip().replace("https://", "").replace("http://", "").split('/')[0]

                # Verificar se é um IP diretamente
                if host.replace('.', '').isdigit():
                    print(f"Adicionando IP diretamente: {host}")
                    outfile.write(host + "\n")
                else:
                    # Resolver domínio para IP
                    print(f"Resolvendo domínio: {host}")
                    resolved_ip = resolve_domain(host)
                    if resolved_ip:
                        print(f"Domínio {host} resolvido para IP {resolved_ip}")
                        outfile.write(resolved_ip + "\n")
                    else:
                        print(f"Falha ao resolver domínio: {host}")

        print(f"IPs resolvidos salvos em: {output_file}")
    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado - {e.filename}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    # Configurar argumentos de linha de comando
    parser = argparse.ArgumentParser(description="Resolver domínios para IPs a partir de uma lista.")
    parser.add_argument("-i", "--input", required=True, help="Arquivo de entrada com URLs/domínios.")
    parser.add_argument("-o", "--output", required=True, help="Arquivo de saída para salvar os IPs resolvidos.")
    args = parser.parse_args()

    # Chamar função principal
    main(args.input, args.output)
