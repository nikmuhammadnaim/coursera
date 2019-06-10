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

# Read the data retrieved from the given URL
my_xml = urlopen(url, context=ctx).read()

print('Retrieved', len(my_xml), 'characters')

# Parse into tags (tree object)
tree = ET.fromstring(my_xml)

# "//" = Select nodes in the document no matter where
# "." = Select the current node
counts = tree.findall('.//count')
print('Count:', len(counts))

print('Sum:', sum([int(value.text) for value in counts]))
