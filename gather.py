import dns.resolver
import socket
import whois
import requests

def gather_info(domain):
    print(f"\n" + "="*50)
    print(f" PASSIVE OSINT REPORT: {domain.upper()}")
    print("="*50)
    
    # 1. IP & Geolocation (Passive - checking public databases)
    print("\n[+] 1. IP & GEOLOCATION")
    try:
        ip = socket.gethostbyname(domain)
        geo_req = requests.get(f"http://ip-api.com/json/{ip}")
        geo = geo_req.json()
        print(f"    - IP Address: {ip}")
        print(f"    - Location:   {geo.get('city')}, {geo.get('country')}")
        print(f"    - ISP:        {geo.get('isp')}")
    except:
        print("    [-] Could not retrieve location data.")

    # 2. WHOIS Data (Passive - checking registrar records)
    print("\n[+] 2. WHOIS DATA")
    try:
        w = whois.whois(domain)
        print(f"    - Registrar:  {w.registrar}")
        print(f"    - Created:    {w.creation_date}")
        print(f"    - Expiry:     {w.expiration_date}")
    except:
        print("    [-] WHOIS record not found.")

    # 3. DNS Records (Passive - checking public DNS servers)
    print("\n[+] 3. MAIL SERVERS (MX RECORDS)")
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        for rdata in answers:
            print(f"    [!] Found Mail Server: {rdata.exchange}")
    except:
        print("    [-] No MX records found.")

    # 4. Security Headers (Passive - reading public response headers)
    print("\n[+] 4. SECURITY HEADERS")
    try:
        # We use a standard web request to see what security "tags" the site sends back
        response = requests.get(f"https://{domain}", timeout=5)
        headers = response.headers
        for h in ['Content-Security-Policy', 'Strict-Transport-Security', 'X-Content-Type-Options']:
            status = "PRESENT" if h in headers else "MISSING"
            print(f"    - {h}: {status}")
    except:
        print("    [-] Could not fetch headers.")

if __name__ == "__main__":
    target = input("\nEnter the target domain (e.g. google.com): ")
    gather_info(target)
