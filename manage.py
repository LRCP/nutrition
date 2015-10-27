#!/usr/bin/env python
#The following lines of code is the original file.
# from migrate.versioning.shell import main

# if __name__ == '__main__':
#     main()

#New code:
#handles both run.py and migrate.py
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import app
from app import BaseNutrition, BaseUSDA, session
import csv



class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata
 
migrate = Migrate(app, DB(BaseNutrition.metadata))
    
manager = Manager(app)
#add migrate to the manager
#default run file is built into the manager
manager.add_command('db', MigrateCommand)
@manager.command
def import_targets():
    from app.models.target import Target
    with open('nutritionTablesReformatted.csv', 'rU') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        #to skip the first row in the csv file containing headings
        reader.next()

        for row in reader:
            #create a new line in the database using sqlalchemy
            #instantiate in instance of the model, add it and commit
            target = Target()
            target.group = row[0]
            target.lower_age = float(row[1])
            target.upper_age = float(row[2])
            target.nutrient_no = row[3]
            if row[4] == "":
                target.value = None
            else:
                target.value = row[4]
            session.add(target)
        session.commit()
    





if __name__ == '__main__':
    manager.run()

