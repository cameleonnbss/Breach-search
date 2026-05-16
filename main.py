
import requests
import os
from getpass import getpass

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ASCII_ART = f"""
{Colors.GREEN}
░█▀▄░█▀▄░█▀▀░█▀█░█▀▀░█░█░░░█▀▀░█▀▀░█▀█░█▀▄░█▀▀░█░█
░█▀▄░█▀▄░█▀▀░█▀█░█░░░█▀█░░░▀▀█░█▀▀░█▀█░█▀▄░█░░░█▀█
░▀▀░░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀░░░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀
{Colors.RESET}
{Colors.YELLOW}By camzzz - https://github.com/cameleonnbss{Colors.RESET}
"""

BASE_URL = "https://brixhub.net/api/v1"

def call_brixhub_api(endpoint, method="GET", payload=None, api_key=None):
    headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
    url = f"{BASE_URL}/{endpoint}"

    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=payload)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=payload)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API Error: {str(e)}", "status": getattr(e.response, "status_code", 500)}

def display_profile(profile, index):
    print(f"\n{Colors.CYAN}=== Result #{index + 1} ==={Colors.RESET}")
    for key, value in profile.items():
        if key.startswith('_'):
            print(f"{Colors.YELLOW}{key}:{Colors.RESET} {value}")
        else:
            print(f"{Colors.WHITE}{key}:{Colors.RESET} {value}")

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASCII_ART)
    print(f"{Colors.BOLD}{Colors.PURPLE}🔍 BrixHub OSINT Tool (CLI){Colors.RESET}\n")

    api_key = os.getenv("BRIX_API_KEY")
    if not api_key:
        api_key = getpass(f"{Colors.YELLOW}Enter your BrixHub API key (will not be displayed): {Colors.RESET}")
        os.environ["BRIX_API_KEY"] = api_key

    while True:
        print(f"\n{Colors.BOLD}Main Menu:{Colors.RESET}")
        print(f"{Colors.GREEN}1.{Colors.RESET} Search by Identity")
        print(f"{Colors.GREEN}2.{Colors.RESET} Search by Contact")
        print(f"{Colors.GREEN}3.{Colors.RESET} Search by Address")
        print(f"{Colors.GREEN}4.{Colors.RESET} Search by Unique IDs")
        print(f"{Colors.GREEN}5.{Colors.RESET} Search by Vehicle")
        print(f"{Colors.GREEN}6.{Colors.RESET} Search by Professional")
        print(f"{Colors.GREEN}7.{Colors.RESET} Reverse Lookup (email, phone, IBAN)")
        print(f"{Colors.GREEN}8.{Colors.RESET} BrixHub Account Info")
        print(f"{Colors.RED}0.{Colors.RESET} Exit")

        choice = input(f"\n{Colors.YELLOW}Choice: {Colors.RESET}").strip()

        if choice == "1":
            search_identity(api_key)
        elif choice == "2":
            search_contact(api_key)
        elif choice == "3":
            search_address(api_key)
        elif choice == "4":
            search_unique_ids(api_key)
        elif choice == "5":
            search_vehicle(api_key)
        elif choice == "6":
            search_pro(api_key)
        elif choice == "7":
            reverse_lookup(api_key)
        elif choice == "8":
            get_account_info(api_key)
        elif choice == "0":
            print(f"\n{Colors.RED}Goodbye!{Colors.RESET}")
            break
        else:
            print(f"{Colors.RED}Invalid choice. Try again.{Colors.RESET}")

def search_identity(api_key):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASCII_ART)
    print(f"{Colors.BOLD}{Colors.PURPLE}👤 Search by Identity{Colors.RESET}\n")

    payload = {}
    fields = {
        "nom_famille": "Last name",
        "prenom": "First name",
        "nom_naissance": "Birth name",
        "nom_affichage": "Display name",
        "nom_utilisateur": "Username",
        "date_naissance": "Birth date (YYYY-MM-DD)",
        "annee_naissance": "Birth year",
        "jour_naissance": "Birth day (1-31)",
        "mois_naissance": "Birth month (1-12)",
        "genre": "Gender (M/F)",
        "civilite": "Title (Mr./Mrs./Ms.)"
    }

    for field, label in fields.items():
        value = input(f"{Colors.YELLOW}{label}:{Colors.RESET} ").strip()
        if value:
            payload[field] = value

    payload["flexible"] = input(f"{Colors.YELLOW}Fuzzy search? (y/n):{Colors.RESET} ").strip().lower() == "y"
    payload["per_page"] = int(input(f"{Colors.YELLOW}Results per page (max 10):{Colors.RESET} ").strip() or "10")
    payload["page"] = int(input(f"{Colors.YELLOW}Page:{Colors.RESET} ").strip() or "1")

    result = call_brixhub_api("search", method="POST", payload=payload, api_key=api_key)
    display_results(result)

def search_contact(api_key):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASCII_ART)
    print(f"{Colors.BOLD}{Colors.PURPLE}📞 Search by Contact{Colors.RESET}\n")

    payload = {}
    fields = {
        "email": "Email",
        "telephone": "Phone",
        "mobile": "Mobile",
        "adresse_ip": "IP Address"
    }

    for field, label in fields.items():
        value = input(f"{Colors.YELLOW}{label}:{Colors.RESET} ").strip()
        if value:
            payload[field] = value

    payload["flexible"] = input(f"{Colors.YELLOW}Fuzzy search? (y/n):{Colors.RESET} ").strip().lower() == "y"
    payload["per_page"] = int(input(f"{Colors.YELLOW}Results per page (max 10):{Colors.RESET} ").strip() or "10")
    payload["page"] = int(input(f"{Colors.YELLOW}Page:{Colors.RESET} ").strip() or "1")

    result = call_brixhub_api("search", method="POST", payload=payload, api_key=api_key)
    display_results(result)

def search_address(api_key):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASCII_ART)
    print(f"{Colors.BOLD}{Colors.PURPLE}🏠 Search by Address{Colors.RESET}\n")

    payload = {}
    fields = {
        "adresse": "Address (street and number)",
        "complement_adresse": "Address complement",
        "code_postal": "Postal code",
        "ville": "City",
        "ville_naissance": "Birth city",
        "lieu_naissance": "Birth place",
        "pays": "Country (e.g., FR)",
        "region": "Region",
        "departement": "Department"
    }

    for field, label in fields.items():
        value = input(f"{Colors.YELLOW}{label}:{Colors.RESET} ").strip()
        if value:
            payload[field] = value

    payload["flexible"] = input(f"{Colors.YELLOW}Fuzzy search? (y/n):{Colors.RESET} ").strip().lower() == "y"
    payload["per_page"] = int(input(f"{Colors.YELLOW}Results per page (max 10):{Colors.RESET} ").strip() or "10")
    payload["page"] = int(input(f"{Colors.YELLOW}Page:{Colors.RESET} ").strip() or "1")

    result = call_brixhub_api("search", method="POST", payload=payload, api_key=api_key)
    display_results(result)

def search_unique_ids(api_key):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASCII_ART)
    print(f"{Colors.BOLD}{Colors.PURPLE}🆔 Search by Unique IDs{Colors.RESET}\n")

    payload = {}
    fields = {
        "nir": "Social Security Number (NIR)",
        "iban": "IBAN",
        "bic": "BIC/SWIFT",
        "siret": "SIRET",
        "siren": "SIREN"
    }

    for field, label in fields.items():
        value = input(f"{Colors.YELLOW}{label}:{Colors.RESET} ").strip()
        if value:
            payload[field] = value

    payload["flexible"] = input(f"{Colors.YELLOW}Fuzzy search? (y/n):{Colors.RESET} ").strip().lower() == "y"
    payload["per_page"] = int(input(f"{Colors.YELLOW}Results per page (max 10):{Colors.RESET} ").strip() or "10")
    payload["page"] = int(input(f"{Colors.YELLOW}Page:{Colors.RESET} ").strip() or "1")

    result = call_brixhub_api("search", method="POST", payload=payload, api_key=api_key)
    display_results(result)

def search_vehicle(api_key):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASCII_ART)
    print(f"{Colors.BOLD}{Colors.PURPLE}🚗 Search by Vehicle{Colors.RESET}\n")

    payload = {}
    fields = {
        "vin_plaque": "VIN or License Plate",
        "immatriculation": "License Plate",
        "numero_serie": "Serial Number",
        "marque": "Brand",
        "modele": "Model"
    }

    for field, label in fields.items():
        value = input(f"{Colors.YELLOW}{label}:{Colors.RESET} ").strip()
        if value:
            payload[field] = value

    payload["flexible"] = input(f"{Colors.YELLOW}Fuzzy search? (y/n):{Colors.RESET} ").strip().lower() == "y"
    payload["per_page"] = int(input(f"{Colors.YELLOW}Results per page (max 10):{Colors.RESET} ").strip() or "10")
    payload["page"] = int(input(f"{Colors.YELLOW}Page:{Colors.RESET} ").strip() or "1")

    result = call_brixhub_api("search", method="POST", payload=payload, api_key=api_key)
    display_results(result)

def search_pro(api_key):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASCII_ART)
    print(f"{Colors.BOLD}{Colors.PURPLE}💼 Search by Professional{Colors.RESET}\n")

    payload = {}
    fields = {
        "societe": "Company",
        "profession": "Profession",
        "fonction": "Position"
    }

    for field, label in fields.items():
        value = input(f"{Colors.YELLOW}{label}:{Colors.RESET} ").strip()
        if value:
            payload[field] = value

    payload["flexible"] = input(f"{Colors.YELLOW}Fuzzy search? (y/n):{Colors.RESET} ").strip().lower() == "y"
    payload["per_page"] = int(input(f"{Colors.YELLOW}Results per page (max 10):{Colors.RESET} ").strip() or "10")
    payload["page"] = int(input(f"{Colors.YELLOW}Page:{Colors.RESET} ").strip() or "1")

    result = call_brixhub_api("search", method="POST", payload=payload, api_key=api_key)
    display_results(result)

def reverse_lookup(api_key):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASCII_ART)
    print(f"{Colors.BOLD}{Colors.PURPLE}🔍 Reverse Lookup{Colors.RESET}\n")

    print(f"{Colors.GREEN}1.{Colors.RESET} Search by Email")
    print(f"{Colors.GREEN}2.{Colors.RESET} Search by Phone")
    print(f"{Colors.GREEN}3.{Colors.RESET} Search by IBAN")
    print(f"{Colors.RED}0.{Colors.RESET} Back")

    choice = input(f"\n{Colors.YELLOW}Choice: {Colors.RESET}").strip()

    if choice == "1":
        email = input(f"{Colors.YELLOW}Enter email: {Colors.RESET} ").strip()
        if email:
            result = call_brixhub_api(f"lookup/email/{email}", api_key=api_key)
            display_results(result)
    elif choice == "2":
        phone = input(f"{Colors.YELLOW}Enter phone number: {Colors.RESET} ").strip()
        if phone:
            result = call_brixhub_api(f"lookup/phone/{phone}", api_key=api_key)
            display_results(result)
    elif choice == "3":
        iban = input(f"{Colors.YELLOW}Enter IBAN: {Colors.RESET} ").strip()
        if iban:
            result = call_brixhub_api(f"lookup/iban/{iban}", api_key=api_key)
            display_results(result)
    elif choice != "0":
        print(f"{Colors.RED}Invalid choice.{Colors.RESET}")

def get_account_info(api_key):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASCII_ART)
    print(f"{Colors.BOLD}{Colors.PURPLE}📊 BrixHub Account Info{Colors.RESET}\n")

    result = call_brixhub_api("me", api_key=api_key)
    if "error" in result:
        print(f"{Colors.RED}Error: {result['error']}{Colors.RESET}")
    else:
        info = result.get("data", {})
        print(f"{Colors.CYAN}Plan:{Colors.RESET} {info.get('plan', 'N/A')}")
        print(f"{Colors.CYAN}Daily quota:{Colors.RESET} {info.get('daily_used', 0)}/{info.get('daily_quota', 0)} requests")
        print(f"{Colors.CYAN}Remaining requests:{Colors.RESET} {info.get('daily_remaining', 0)}")
        print(f"{Colors.CYAN}Max results per query:{Colors.RESET} {info.get('results_per_query', 0)}")
        print(f"{Colors.CYAN}Pagination enabled:{Colors.RESET} {'Yes' if info.get('pagination_enabled') else 'No'}")

def display_results(result):
    if "error" in result:
        print(f"\n{Colors.RED}Error: {result['error']}{Colors.RESET}")
    elif "data" in result and "results" in result["data"]:
        results = result["data"]["results"]
        if not results:
            print(f"\n{Colors.YELLOW}No results found.{Colors.RESET}")
        else:
            print(f"\n{Colors.GREEN}✅ {len(results)} result(s) found:{Colors.RESET}\n")
            for i, profile in enumerate(results):
                display_profile(profile, i)
    else:
        print(f"\n{Colors.RED}Unexpected response format.{Colors.RESET}")

    input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")

if __name__ == "__main__":
    print(f"{Colors.BOLD}{Colors.GREEN}🚀 Starting BrixHub OSINT Tool (CLI)...{Colors.RESET}")
    main_menu()
      
