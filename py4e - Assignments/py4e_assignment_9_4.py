#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dictionary = dict()

for line in handle:
    if not line.startswith("From"): continue
    elif line.startswith("From:"): continue
    else:
        wordsinline = line.split()
        dictionary[wordsinline[1]] = dictionary.get(wordsinline[1], 0) + 1
mostcommonkey = None
mostvalue = None
for key,value in dictionary.items():
    if mostcommonkey == None or value > mostvalue:
        mostcommonkey = key
        mostvalue = value

print(mostcommonkey,mostvalue)
