from urllib.parse import urlparse
from ipaddress import ip_address
import sys

today_log = open('C://python27/today.log', 'r')
stripped_url = {}
for line in today_log.readlines():
    try:
        ipv4 = line.strip()[:line.find(' ')]
        ip_address(ipv4)
        url = line.strip()[line.find(r'http://'):line.find('HTTP') - 1]
        url_parsed = urlparse(url)
        url_without_query = url_parsed.netloc + url_parsed.path
        if url_without_query in stripped_url.keys():
            stripped_url[url_without_query] += 1
        else:
            stripped_url.setdefault(url_without_query, 1)
        print(url_without_query)
    except ValueError:
        sys.stderr.write('Invalid IPv4 address!')

print(stripped_url)
today_log.close()
