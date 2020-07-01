import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print("Retrieving", address)
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall(".//count")
total=0
n=len(counts) - 1
print(n)
while n >= 0 :
    total = total + int(counts[n].text)
    n = n - 1
print(total)
