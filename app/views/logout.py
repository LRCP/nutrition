from flask.ext.login import logout_user
from flask import flash, redirect, url_for
from app import app

@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out successfully")
    return redirect(url_for('login'))
    #consider return redirect(url_for('home'))
    #after a home page is created.