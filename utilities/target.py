import csv
#../ goes up a level in the path when the file is in a different folder.
with open('../nutritionTablesReformatted.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print ', '.join(row)