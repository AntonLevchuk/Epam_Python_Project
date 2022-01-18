from Flask_project.forms import RegistrationForm

from Flask_project import app, db

from models.Users import User

from flask import render_template, redirect, url_for, flash


@app.route('/register', methods=['GET', 'POST'])
def register():
    """ The register view"""

    form = RegistrationForm()
    if form.validate_on_submit():  # creating a new user
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)
