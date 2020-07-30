#10.2 Write a program to read through the mbox-short.txt and figure out the
#distribution by hour of the day for each of the messages. You can pull the
#hour out from the 'From ' line by finding the time and then splitting the
#string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)
distr = dict()

for line in fhand:
    words = line.split(' ')
    if words[0].upper() == "FROM":
        hrs = words[6].split(':')[0]
        if hrs in distr:
            distr[hrs] = distr[hrs] + 1
        else:
            distr[hrs] = 1

for key, value in sorted(distr.items()):
    print(key, value)
