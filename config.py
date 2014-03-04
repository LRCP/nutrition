import os
basedir = os.path.abspath(os.path.dirname(__file__))
print basedir

# if we hae acces to the heroku Url
if "DATABASE_URL" in os.environ:
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
else:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'
    )
    
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]


