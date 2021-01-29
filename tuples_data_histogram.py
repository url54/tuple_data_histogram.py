# This program was designed for an assignment.  Using the text file, mbox-short.txt
# We are tasked with searching the text file for the hours that "from" emails were
# sent.  We are then to count the rate of occurence on those hours, and then print them
# off in ascending numerical order based on the key in (k,v) pairs.

# Mbox-short.txt is included in this repository.  Below are the actual instructions for
# the assignment.

# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by
# hour of the day for each of the messages. You can pull the hour out from the 'From ' line
# by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008. Once you have accumulated the
# counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = dict()
lst = list()
for lne in handle:
    lne = lne.split()
    if len(lne) < 3 or lne[0] != 'From':
        continue
    wds = lne[5]
    wds = wds.split(":")
    hrs = wds[0]
    di[hrs] = di.get(hrs,0) + 1

lst = list()
for k,v in di.items():
    ntup = (k,v)
    lst.append(ntup)
lst = sorted(lst)

for k, v in lst:
    print(k,v)
