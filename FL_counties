import urllib2
import csv
from BeautifulSoup import BeautifulSoup

url = "http://www.floridacountiesmap.com/counties_list.shtml"

html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)

names = soup.find('tr', {'class':'small'})

output_counties = []

for name in names.findAll('small'):
    output_counties.append(name.text)

    print output_counties
    
#from wiki, see below

from BeautifulSoup import BeautifulSoup
import urllib2,csv

wiki = 'http://en.wikipedia.org/wiki/List_of_counties_in_Florida'

page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page)

county = ""

table=soup.find("table", { "class" : "wikitable sortable"})

rows=[]
for row in table.findAll("tr"):
    cells = row.findAll("td")
    county = row.findAll("title", text=True)
    rows.append(county)

print rows
print len(rows)

f = open('out.csv', 'w')
print rows
writer = csv.writer(f)
writer.writerows(rows)
f.close()
