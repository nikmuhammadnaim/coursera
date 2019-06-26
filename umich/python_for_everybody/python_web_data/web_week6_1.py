from urllib.request import urlopen
import ssl
import json

# sample data: http://py4e-data.dr-chuck.net/comments_42.json
# actual data: http://py4e-data.dr-chuck.net/comments_233808.json

# Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Request url from user
url = input('Enter URL: ')
print('Retrieving', url)

# Read the data retrieved from the URL
data = urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')

# Parse into JSON
js = json.loads(data)

# Get the list to loop through
my_list = js['comments']
answer = 0
for pair in my_list:
    answer += pair['count']
print('Count:', len(my_list))
print('Sum:', answer)
