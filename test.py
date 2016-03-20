import csv

IrregularCSV = [] # create an empty list for CSV
IrregularCSV = csv.reader(open('C:\Users\howt51\Desktop\wtf.txt', 'rb'), delimiter='\t')
row = IrregularCSV.split()
print row




MyValues = []
for line in open('myfile'):
    row = line.split()
    MyValues.append(row[5] if len(row)>4 else None)
print MyValues