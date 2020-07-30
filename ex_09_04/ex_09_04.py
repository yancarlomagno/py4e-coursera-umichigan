#9.4 Write a program to read through the mbox-short.txt and figure out who
#has sent the greatest number of mail messages. The program looks for 'From '
#lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to
#a count of the number of times they appear in the file. After the dictionary
#is produced, the program reads through the dictionary using a maximum loop to
#find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mailer = dict()

for line in handle:
    words = line.split(' ')
    if not line.startswith('From ') : continue
    if words[1] in mailer:
        mailer[words[1]] = mailer[words[1]]+1
    else:
        mailer[words[1]] = 1

maxval = 0
s = ""

for sender in mailer:
    if mailer[sender] > maxval:
        s = sender
        maxval = mailer[sender]

print(s,maxval)
