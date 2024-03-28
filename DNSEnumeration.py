import dns.resolver
import sys

record_types=['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT'] #A records are ipv4 and AAAA are ipv6 and MX are mail server and NS for nameservers
try:
    domain = sys.argv[1]
except IndexError:
    print("Syntax Error - python script_name.py domainname.com")
    quit()
for records in record_types:
    try:
        answer = dns.resolver.resolve(domain, records)  
        print(f'\n{records} Records')
        print('-'*30)
        for server in answer:
            print(server.to_text())
    except dns.resolver.NoAnswer:
        # print('No record found.')
        pass

    except dns.resolver.NXDOMAIN:
        print(f"{domain} does not exist. Please verify and enter the correct one!") 
        quit()   

    except KeyboardInterrupt:
        print("Either you Misclicked or you meant to quit. Either way, Goodbye!")
        quit()
    