import dns.resolver
from colorama import Fore, Style, init
from pyfiglet import Figlet


def print_colored(message, color):
    print(f"{color}{message}{Style.RESET_ALL}\n", end='')


def pyfiglet():
    init()
    f = Figlet(font='small')
    oso = f.renderText('DOMAIN CHECKER')
    print_colored(f"{oso}", Fore.RED)


def print_center(message, color):
    total_width = 80 
    padding = (total_width - len(message)) // 2
    print(f"{' ' * padding}{color}{message}{Style.RESET_ALL}")


    

def main():
    
    pyfiglet()
    print_center(f"MADE BY @0so", Fore.LIGHTCYAN_EX)


    try:
        print()
        target_domain = input(f"{Fore.LIGHTYELLOW_EX}Domain -> {Style.RESET_ALL}")
        print("\n")


        # Registros "A"
        try:
            target_a = dns.resolver.resolve(target_domain, "A")
            print_colored(f"Registros \"A\" para {target_domain}:", Fore.LIGHTBLUE_EX)
            for d in target_a:
                print_colored(d.address, Fore.GREEN)
        except dns.resolver.NoAnswer:
            print_colored(f"No hay registros \"A\" directos para {target_domain}.", Fore.RED)

        # Registros "CNAME"
        try:
            target_cname = dns.resolver.resolve(target_domain, "CNAME")
            print_colored(f"Registros \"CNAME\" para {target_domain}:", Fore.LIGHTBLUE_EX)
            for d in target_cname:
                print_colored(d.target, Fore.GREEN)
        except dns.resolver.NoAnswer:
            print_colored(f"No hay registros \"CNAME\" para {target_domain}.", Fore.RED)

        # Registros "MX"
        try:
            target_mx = dns.resolver.resolve(target_domain, "MX")
            print_colored(f"Registros \"MX\" para {target_domain}:", Fore.LIGHTBLUE_EX)
            for d in target_mx:
                print(f"Priority: {d.preference}, Mail Server: {Fore.GREEN}{d.exchange}{Style.RESET_ALL}")
        except dns.resolver.NoAnswer:
            print_colored(f"No hay registros \"MX\" para {target_domain}.", Fore.RED)

        # Registros "TXT"
        try:
            target_txt = dns.resolver.resolve(target_domain, "TXT")
            print_colored(f"Registros \"TXT\" para {target_domain}:", Fore.LIGHTBLUE_EX)
            for d in target_txt:
                for txt_string in d.strings:
                    print_colored(txt_string, Fore.GREEN)
        except dns.resolver.NoAnswer:
            print_colored(f"No hay registros \"TXT\" para {target_domain}.", Fore.RED)

        # Registros "NS"
        try:
            target_ns = dns.resolver.resolve(target_domain, "NS")
            print_colored(f"Registros \"NS\" para {target_domain}:", Fore.LIGHTBLUE_EX)
            for d in target_ns:
                print_colored(d.target, Fore.GREEN)
        except dns.resolver.NoAnswer:
            print_colored(f"No hay registros \"NS\" para {target_domain}.", Fore.RED)

        # Registros "AAAA"
        try:
            target_aaaa = dns.resolver.resolve(target_domain, "AAAA")
            print_colored(f"Registros \"AAAA\" para {target_domain}:", Fore.LIGHTBLUE_EX)
            for d in target_aaaa:
                print_colored(d.address, Fore.GREEN)
        except dns.resolver.NoAnswer:
            print_colored(f"No hay registros \"AAAA\" para {target_domain}.", Fore.RED)

        # Registros "SRV"
        try:
            target_srv = dns.resolver.resolve("_sip._tcp." + target_domain, "SRV")
            print_colored(f"Registros \"SRV\" para {target_domain}:", Fore.LIGHTBLUE_EX)
            for d in target_srv:
                print_colored(f"Priority: {d.priority}, Weight: {d.weight}, Port: {d.port}, Target: {d.target}", Fore.GREEN)
        except dns.resolver.NoAnswer:
            print_colored(f"No hay registros \"SRV\" para {target_domain}.", Fore.RED)

    except Exception as e:
        print_colored(f"No se pudo extraer información. Error: {e}", Fore.RED)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
