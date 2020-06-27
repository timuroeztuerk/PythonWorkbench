from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Sample url : http://py4e-data.dr-chuck.net/comments_42.html
# Actual url : http://py4e-data.dr-chuck.net/comments_713681.html
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
tags = soup('span')
#You need to adjust this code to look for span tags and pull out the text content of the span tag,
#convert them to integers and add them up to complete the assignment.
total = 0
for tag in tags:
    total = total + int(tag.contents[0])

print(total)
