# import whois
# import dns.resolver
# # import builtwith
# # import dns.reversename
# from ipwhois import IPWhois

# domain = input("Please enter a domain name: ")

# # Get all the WHOIS information

# try:
#     answers = dns.resolver.resolve(domain, "A")
#     domain_ip = answers[0].address
# except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
#     print("Invalid domain name")
#     exit()

# whoisInfo = whois.whois(domain)

# # Get nameservers
# nameservers = whoisInfo.name_servers

# # Get the IP Address of where the domain is hosted
# # domain_ip = socket.gethostbyname(domain)
# ipwhois = IPWhois(domain_ip)
# results = ipwhois.lookup_rdap()

# print(f"Domain name: {whoisInfo.domain_name}")
# print("-------------------------------")
# print("******| Registrar Information |******")
# print(f"Registrar: {whoisInfo.registrar}")
# print(f"Registrar Email Address: {whoisInfo.registrar_email}")
# print(f"Registrar Website: {whoisInfo.registrar_url}")
# print("-------------------------------")
# print("******| Registrant Information |******")
# print(f"Registrant Organization: {whoisInfo.registrant_organization}")
# print(f"Registrant Country: {whoisInfo.registrant_country}")
# print("-------------------------------")
# print("******| Domain Information |******")
# print(f"Domain Registration Date: {whoisInfo.creation_date}")
# print(f"Domain Expiration Date: {whoisInfo.expiration_date}")
# print(f"Domain Updated Dated: {whoisInfo.updated_date}")
# print(f"The nameservers for the domain are: ")
# for ns in nameservers:
#     try:
#         answers = dns.resolver.resolve(ns, 'A')
#         ns_ip = answers[0].address
#         result = whois.whois(ns_ip)
#         print(result.registrar)
#     except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
#         print(f"Invalid nameserver: {ns}")

# if isinstance(whoisInfo.status, list):
#     print("The status of the domain is: ")
#     for status in whoisInfo.status:
#         print(status)
# elif isinstance(whoisInfo.status, str):
#     print(f"The status of the domain is: {whoisInfo.status}")
# print(f"Domain is hosted with: {results['asn_description']}")


# OPTIMIZED

import whois
import dns.resolver
from ipwhois import IPWhois

domain = input("Please enter a domain name: ")

try:
    # Get the IP Address of where the domain is hosted
    resolver = dns.resolver.Resolver()
    domain_ip = resolver.resolve(domain, 'A')[0].address
except dns.resolver.NXDOMAIN:
    print("Invalid domain name")
    exit()

# Get all the WHOIS information
whois_info = whois.whois(domain)

# Get nameservers
nameservers = whois_info.name_servers

ipwhois = IPWhois(domain_ip)
results = ipwhois.lookup_rdap()

print(f"Domain name: {whois_info.domain_name}")
print("-------------------------------")
print("******| Registrar Information |******")
print(f"Registrar: {whois_info.registrar}")
print(f"Registrar Email Address: {whois_info.registrar_email}")
print(f"Registrar Website: {whois_info.registrar_url}")
print("-------------------------------")
print("******| Registrant Information |******")
print(f"Registrant Organization: {whois_info.registrant_organization}")
print(f"Registrant Country: {whois_info.registrant_country}")
print("-------------------------------")
print("******| Domain Information |******")
print(f"Domain Registration Date: {whois_info.creation_date}")
print(f"Domain Expiration Date: {whois_info.expiration_date}")
print(f"Domain Updated Dated: {whois_info.updated_date}")
print(f"The nameservers for the domain are: ")
for ns in nameservers:
    try:
        resolver = dns.resolver.Resolver()
        ns_ip = resolver.resolve(ns, 'A')[0].address
        result = whois.whois(ns_ip)
        print(result.registrar)
    except dns.resolver.NXDOMAIN:
        print(f"Invalid nameserver: {ns}")

if isinstance(whois_info.status, list):
    print("The status of the domain is: ")
    for status in whois_info.status:
        print(status)
elif isinstance(whois_info.status, str):
    print(f"The status of the domain is: {whois_info.status}")

print(f"Domain is hosted with: {results['asn_description']}")
