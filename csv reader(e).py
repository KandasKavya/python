import csv

with open("GLWEC info.csv",encoding="utf-8") as f:
    text=csv.reader(f)
    elements=list(text)
    print(elements)
