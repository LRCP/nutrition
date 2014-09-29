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
from app import BaseNutrition

class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata
 
migrate = Migrate(app, DB(BaseNutrition.metadata))
manager = Manager(app)
#add migrate to the manager
#default run file is built into the manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

