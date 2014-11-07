from app import app, session, login_manager
from flask import g, request, flash, redirect
from flask import url_for, render_template
from flask.ext.login import current_user, login_user, LoginManager
from app.models.user import User
from werkzeug.security import check_password_hash
from app.forms import LoginForm




def load_user(userid):
    return User.get(userid)
#before any requests come in, then set the g.logged_in variable
#to see if the user is authenticated.
@app.before_request
def load_globals():
    g.logged_in = current_user.is_authenticated()

@app.route('/login', methods=['GET', 'POST'])
def login():
    #login_manager = LoginManager()
    #login_manager.init_app()
    
    form = LoginForm(request.form)
    #form = LoginForm()
    #if form.validate_on_submit():
    
    if request.method == 'POST' and form.validate():
        #want to find the user with the username or email address as enterred
        user = session.query(User).filter(
            (User.email == form.username_or_email.data) |
            (User.username == form.username_or_email.data)
            ).first()
        #want to check to see if the user is registered and password info is correct.
        if user is None or not check_password_hash(user.password,
                                                   form.password.data):
            flash("Your login information is incorrect. Please try again.")
            return redirect(url_for('login'))
        #check to see if the password is correct.
        

        #then log in the user
        login_user(user)
        flash("Logged in successfully.")
        return redirect(url_for('food_log_get'))
    return render_template(
        'login.html',
        title='Sign In',
        form=form
        #providers=app.config['OPENID_PROVIDERS'])
        )
#state changes fall between a GET and a POST

@login_manager.user_loader
def load_user(id):
    return session.query(User).get(int(id))
