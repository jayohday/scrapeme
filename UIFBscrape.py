
import urllib2
import csv
from BeautifulSoup import BeautifulSoup

## STEP 1: GET URL ##

url = "https://www.uif.uillinois.edu/storydetail.aspx?id=86"

html = urllib2.urlopen(url).read()

## STEP 2: PARSE HTML ##

soup = BeautifulSoup(html)

H4 = soup.find('h4') 
uls = []
for nextSibling in H4.findNextSiblings():
    if nextSibling.name == 'ul':
        uls.append(nextSibling)

for ul in uls:
    for li in ul.findAll('li'):
        print(li)

''' alternative option
name_table = soup.find('li') # NOTE THE CHANGES HERE

## STEP 3: GET STUFF

output_names = []

for name in name_table.findAll('strong'):
    output_names.append(name.text)

print output_names # to test

#outfile = open('out.csv', 'a')
#writer = csv.writer(outfile)

#writer.writerows(output_names)
'''
