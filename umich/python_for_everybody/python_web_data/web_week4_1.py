from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# url: http://py4e-data.dr-chuck.net/comments_233805.html

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Store the sum of the values in the 'comment' column
answer = []

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    answer.append(int(tag.contents[0]))

print('Count:', len(answer))
print('Sum:', sum(answer))
