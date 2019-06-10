import xml.etree.ElementTree as ET
from urllib.request import urlopen
import ssl

# sample data: http://py4e-data.dr-chuck.net/comments_42.xml
# actual data: http://py4e-data.dr-chuck.net/comments_233807.xml

# Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
print('Retrieving', url)

my_xml = urlopen(url, context=ctx).read()

print('Retrieved', len(my_xml), 'characters')
tree = ET.fromstring(my_xml)
counts = tree.findall('.//count')
print('Count:', len(counts))
answer = 0


for value in counts:
    answer += int(value.text)

print('Sum:', answer)
