from app import app
@app.route('/')
@app.route('/index')
#this will be the home page
def index():
    return "Craft and Track Meals and Snacks to Meet Your Nutritional Goals"
