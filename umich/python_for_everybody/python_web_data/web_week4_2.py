from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# sample url: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# actual url: http://py4e-data.dr-chuck.net/known_by_Anmolpreet.html

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get the URL, count and position input from user
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(count):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags in list format
    tags = soup('a')

    # Get the URL of the input position
    my_tag = tags[position-1]

    # Make that as the new URL
    url = my_tag.get('href', None)
    print('Retrieving:', url)

# Get the title from the final URL
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print(re.findall('that (.+) knows', soup.title.string)[0])
