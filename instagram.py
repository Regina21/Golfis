import csv
from pathlib import Path

# change the name of the *.csv file to the name of the tennis user
with open('big.csv', 'w', encoding='Latin-1') as out_file:
    csv_out = csv.writer(out_file)
    csv_out.writerow(['FileName', 'Content'])
    for fileName in Path('.').glob('*.txt'):
        lines = [ ]
        with open(str(fileName.absolute()),'rb') as one_text:
            for line in one_text.readlines():
                lines.append(line.decode(encoding='Latin-1',errors='ignore').strip())
        csv_out.writerow([str(fileName),' '.join(lines)])
