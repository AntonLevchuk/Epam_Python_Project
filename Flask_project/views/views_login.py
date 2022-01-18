from Flask_project.forms import LoginForm

from Flask_project import app

from models.Users import User

from flask_login import login_user, login_required, logout_user

from flask import render_template, redirect, request, url_for, flash

# from app import login_manager


@app.route('/logout')
@login_required
def logout():
    """ LOGOUT view """

    logout_user()
    flash('You logged out!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ The login view"""

    form = LoginForm()
    if form.validate_on_submit():  # checking if the form is valid on submission
        user = User.query.filter_by(email=form.email.data).first()  # checking if email is registered
        # if it's not user will be None

        if user.check_password(form.password.data) and user is not None:  # checking if password is correct and user
            # is not None
            login_user(user)
            flash('Logged in Successfully!')

            next_page = request.args.get('next_page')  # if user was trying to access the page that they had to be
            # logged, the page would be saved in 'next_page'

            if next_page is None or not next_page[0] == '/':  # if 'next_page' is None the user would be redirected
                # to the 'home' page
                next_page = url_for('home')

            return redirect(next_page)
            # if user was successfully logged he would be redirected to the 'next_page'

    return render_template('login.html', form=form)
