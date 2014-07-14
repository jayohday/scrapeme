import csv,re

class Row(object):

    def __init__(self,month,year,offense,county,drug,drug_name,weight,entry,drug_type):

        self.month=month

        self.year=year

        self.offense=offense

        self.county=county

        self.drug=drug

        self.drug_name=drug_name

        self.weight=weight

        self.entry=entry

        self.drug_type=drug_type



def parse_rows(rows,lines,start,end):

    for line in lines:

        if not re.match("^\s*$",line[start]):

            rows.append(line[start:end])

            



lines=csv.reader(open("2008_c.csv",'U'))

header=lines.next()



all_lines=[]

for line in lines:

    all_lines.append(line)



header=all_lines[0]



start=0

rows=[]

for i in range(len(header)):

    if re.match("^\s*$",header[i]):

        parse_rows(rows,all_lines,start,i+1)

        start=i+1

        

'''

rows=[]

for item in split:

    for line in lines:

        row_list=parse_rows(lines[1:],start,i+1)

        rows.append(row_list)

'''





writer = csv.writer(open("2008_parsed.csv",'w'))

writer.writerows(rows)d

