# eurosiatools_cli.py
#
# Interface terminal "EurosiaTools" + intégration de la fonction track_ip fournie.
#
#Toute modification de ce fichier doit respecter la licence MIT d'origine.
#
# Auteur: Therox
#
# Licence: MIT
#
# github.com/Therox/EurosiaTools

try:
    from pyfiglet import figlet_format
except ModuleNotFoundError:
    raise SystemExit("Le module 'pyfiglet' est introuvable. Installe-le avec : python -m pip install pyfiglet")

try:
    from colorama import init as colorama_init, Fore, Style
except ModuleNotFoundError:
    raise SystemExit("Le module 'colorama' est introuvable. Installe-le avec : python -m pip install colorama")

try:
    import requests
except ModuleNotFoundError:
    raise SystemExit("Le module 'requests' est introuvable. Installe-le avec : python -m pip install requests")

import sys
import time

colorama_init(autoreset=True)



def track_ip(ip_address):
    """
    Récupère des informations sur une IP via ipinfo.io
    Retourne une chaîne texte à afficher.
    """
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json", timeout=5)
        if response.status_code != 200:
            return f"Impossible de récupérer les informations pour l’adresse IP : {ip_address} (status {response.status_code})"
        data = response.json()
        return (
            f"IP : {data.get('ip', 'Non disponible')}\n"
            f"Ville : {data.get('city', 'Non disponible')}\n"
            f"Région : {data.get('region', 'Non disponible')}\n"
            f"Pays : {data.get('country', 'Non disponible')}\n"
            f"Localisation : {data.get('loc', 'Non disponible')}\n"
            f"Organisation : {data.get('org', 'Non disponible')}\n"
            f"Code postal : {data.get('postal', 'Non disponible')}\n"
        )
    except requests.RequestException as e:
        return f"Erreur de connexion : {e}"


# --- Interface terminal ---
def banner():
    art = figlet_format("EurosiaTools", font="standard")
    print(Fore.RED + art)
    print(Fore.WHITE + "github.com/tonpseudo/EurosiaTools\n")


def menu():
    # Mise en page simple inspirée du style CLI
    print(Fore.CYAN + "[01]" + Fore.WHITE + " IP Tracker")
    print(Fore.CYAN + "[00]" + Fore.WHITE + " Quitter\n")


def prompt_enter(msg="\nAppuyez sur Entrée pour revenir au menu..."):
    try:
        input(Fore.YELLOW + msg)
    except (KeyboardInterrupt, EOFError):
        pass


def clear_screen():
    # tentative simple de nettoyage de terminal (compatible os courants)
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        clear_screen()
        banner()
        menu()
        try:
            choix = input(Fore.GREEN + "→ Choisis une option: ").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            print(Fore.YELLOW + "Interruption reçue. Au revoir.")
            sys.exit(0)

        if choix in ("1", "01"):
            # utilisation de la fonction track_ip en CLI
            ip_to_track = input(Fore.GREEN + "Entrez une adresse IP (ou domaine) : ").strip()
            if not ip_to_track:
                print(Fore.YELLOW + "Aucune adresse IP saisie.")
                prompt_enter()
                continue
            print(Fore.CYAN + "\nRecherche en cours...\n")
            result = track_ip(ip_to_track)
            print(Fore.WHITE + "—— Résultat ———\n")
            print(Fore.WHITE + result)
            prompt_enter()

        elif choix in ("0", "00"):
            print(Fore.MAGENTA + "Au revoir.")
            time.sleep(0.4)
            sys.exit(0)
        else:
            print(Fore.YELLOW + "Option inconnue.")
            prompt_enter()


if __name__ == "__main__":
    main()

input("\nAppuyez sur Entrée pour fermer le programme...")
# EurosiaTools.py