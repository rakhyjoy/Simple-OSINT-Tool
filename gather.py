import dns.resolver
import socket
import whois
import requests

def gather_info(domain):
    print(f"\n" + "="*50)
    print(f" TARGET OSINT REPORT: {domain.upper()}")
    print("="*50)
    
    # 1. IP & Geolocation (Where is it?)
    print("\n[+] 1. IP & GEOLOCATION")
    try:
        ip = socket.gethostbyname(domain)
        # Using a free service to get location data
        geo_req = requests.get(f"http://ip-api.com/json/{ip}")
        geo = geo_req.json()
        print(f"    - IP Address: {ip}")
        print(f"    - Location:   {geo.get('city')}, {geo.get('regionName')}, {geo.get('country')}")
        print(f"    - ISP/Org:    {geo.get('isp')}")
    except:
        print("    [-] Could not retrieve location data.")

    # 2. WHOIS Data (Who owns it?)
    print("\n[+] 2. WHOIS DATA")
    try:
        w = whois.whois(domain)
        print(f"    - Registrar:  {w.registrar}")
        print(f"    - Created:    {w.creation_date}")
    except:
        print("    [-] WHOIS record not found.")

    # 3. HTTP Security Headers (Is it safe?)
    print("\n[+] 3. SECURITY HEADERS")
    try:
        response = requests.get(f"https://{domain}", timeout=5)
        headers = response.headers
        # Check for common security protections
        h_list = ['Content-Security-Policy', 'Strict-Transport-Security', 'X-Frame-Options']
        for h in h_list:
            status = "PRESENT" if h in headers else "MISSING (Risk!)"
            print(f"    - {h}: {status}")
    except:
        print("    [-] Could not connect to fetch headers.")

    # 4. Subdomains (Hidden infrastructure)
    print("\n[+] 4. COMMON SUBDOMAINS")
    subs = ['www', 'mail', 'ftp', 'admin', 'dev', 'portal']
    for s in subs:
        try:
            target = f"{s}.{domain}"
            sub_ip = socket.gethostbyname(target)
            print(f"    [!] Found: {target} ({sub_ip})")
        except:
            pass

if __name__ == "__main__":
    target = input("\nEnter the target domain (e.g. google.com): ")
    gather_info(target)
