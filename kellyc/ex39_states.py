import csv

def TitleCaser 
result={}
with open('states.csv','r') as f:
    red=csv.DictReader(f)
    for d in red:
        result.setdefault(d['State'],[]).append(d['Abbreviation'])

#results={'1': ['1450'], '3': ['204', '250', '1437'], '2': ['1440']}
