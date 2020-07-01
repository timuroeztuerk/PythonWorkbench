import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
info = json.loads(data)
info = info["comments"]
print(info)

n = len(info)
total = 0
for item in info:
    total = total + int(item["count"])

print(total)

#total = total + int(item["comments"]["count"])
