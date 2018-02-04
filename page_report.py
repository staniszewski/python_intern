from urllib.parse import urlparse
from ipaddress import ip_address
import sys

# Url_stripper function which strips names of requested URLs from log file
# and counts number of requests for every URL in log.
def url_stripper(log_file):

    # Directory where today.log file is. File name passed as function's argument.
    today_log = open(r'C://Users/sux^/PyCharmProjects/Python Intern - Task 2/' + log_file, 'r')
    stripped_url = {}

    for log_line_number, log in enumerate(today_log.readlines(), start=1):

        # It catches the exception raised when log in log file is invalid.
        # If beginning of the log is not IPv4 (ValueError), exception marks it as invalid log.
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

    # Sorting items in descending order and if number of requests is the same they are sorted lexicographically.
    for items in sorted(stripped_url.items(), key=lambda item: (-item[1], item[0])):
        print('"{0}",{1}' .format(items[0], items[1]))

    today_log.close()
    return stripped_url


if __name__ == "__main__":
    # Function takes name of file as sys.arg[1]
    url_stripper(sys.argv[1])
