from urllib.parse import urlparse
from ipaddress import ip_address
import sys


def url_stripper():

    today_log = open('C://python27/today.log', 'r')
    stripped_url = {}

    for log_line_number, log in enumerate(today_log.readlines(), start=1):

        try:
            ipv4 = log.strip()[:log.find(' ')]
            ip_address(ipv4)
            url = log.strip()[log.find(r'http://'):log.find('HTTP') - 1]
            url_parsed = urlparse(url)
            url_without_query = url_parsed.netloc + url_parsed.path

            if not url_without_query[-1:].isalnum():
                url_without_query = url_without_query.strip()[:-1]

            if url_without_query in stripped_url.keys():
                stripped_url[url_without_query] += 1
            else:
                stripped_url.setdefault(url_without_query, 1)

        except ValueError:
            sys.stderr.write('Error in: %d line in today.log file. Invalid IPv4 address!' % log_line_number)

    for items in sorted(stripped_url.items(), key=lambda item: (-item[1], item[0])):
        print(items[0], items[1])

        # TODO: csv file format

    today_log.close()
    return stripped_url


if __name__ == "__main__":
    url_stripper()
