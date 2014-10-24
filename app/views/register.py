from app import app, session, flash, render_template, redirect
from app import url_for, render_template
from app.forms import RegistrationForm
from flask import request
from app.models.user import User
from sqlalchemy.exc import IntegrityError

@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm(request.form)
    print form.validate()
    print form.errors
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
            form.password.data)
        session.add(user)
        try:
            session.commit()
        except IntegrityError as error:
            flash("Registration is unsucessful. A user with the same username or email address is already in use.")
            print error
            session.rollback()
            return render_template(
                'register.html',
                title="Register",
                form=form
            )
        flash("Registration is successful.")
        return redirect(url_for('login'))
    return render_template(
        'register.html',
        title="Register",
        form=form
        )

