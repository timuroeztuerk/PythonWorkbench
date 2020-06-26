#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()
lst = list()
hrlist = list()
for line in handle:
    if not line.startswith("From"): continue
    elif line.startswith("From:"): continue
    else :
        words = line.split()
        time = words[5]
        lst.append(time)
for item in lst:
    result = item.split(":")
    hrlist.append(result[0])

for hour in hrlist:
    dic[hour] = dic.get(hour,0) + 1

newlist = sorted(dic.items())

for k,v in newlist:
    print(k,v)
