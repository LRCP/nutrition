import csv
#
import sys

#../ goes up a level in the path when the file is in a different folder.
with open('../nutritionTablesReformatted.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        #create a new line in the database using sqlalchemy
        #instantiate in instance of the model, add it and commit

        
        target = Target()
        target.group = row[0]
        target.lower_age = row[1]
        target.upper_age = row[2]
        target.nutrient_no = row[3]
        target.value = row[4]
        session.add(target)
    session.commit(target)


        