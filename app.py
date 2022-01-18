from Flask_project import app

from models.Artists import Artists
from models.Tracks import Tracks
# from models.Users import User
#
# from Flask_project.forms import LoginForm, RegistrationForm

from flask_login import LoginManager

from flask import render_template, redirect, request, url_for, flash

from models.Users import User

from Flask_project.views import views_login
from Flask_project.views import views_register

artists_items = Artists.query.all()
tracks_items = Tracks.query.all()

login_manager = LoginManager()


@app.route('/')
def home():
    """ HOME page """

    return render_template('home.html')


@app.route('/top_artists')
def top_artists():
    """ TOP_ARTISTS page """
    return render_template('top_artists.html', artists_items=artists_items)


@app.route('/top_tracks')
def top_tracks():
    """ TOP_TRACKS page """

    return render_template('top_tracks.html', tracks_items=tracks_items)


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None


# @app.route('/logout')
# @login_required
# def logout():
#     """ LOGOUT view """
#
#     logout_user()
#     flash('You logged out!')
#     return redirect(url_for('home'))
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     """ The login view"""
#
#     form = LoginForm()
#     if form.validate_on_submit():  # checking if the form is valid on submission
#         user = User.query.filter_by(email=form.email.data).first()  # checking if email is registered
#         # if it's not user will be None
#
#         if user.check_password(form.password.data) and user is not None:  # checking if password is correct and user
#             # is not None
#             login_user(user)
#             flash('Logged in Successfully!')
#
#             next_page = request.args.get('next_page')  # if user was trying to access the page that they had to be
#             # logged, the page would be saved in 'next_page'
#
#             if next_page is None or not next_page[0] == '/':  # if 'next_page' is None the user would be redirected
#                 # to the 'home' page
#                 next_page = url_for('home')
#
#             return redirect(next_page)
#             # if user was successfully logged he would be redirected to the 'next_page'
#
#     return render_template('login.html', form=form)


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     """ The register view"""
#
#     form = RegistrationForm()
#     if form.validate_on_submit():  # creating a new user
#         user = User(email=form.email.data,
#                     username=form.username.data,
#                     password=form.password.data)
#
#         db.session.add(user)
#         db.session.commit()
#         flash('Thanks for registration!')
#         return redirect(url_for('login'))
#
#     return render_template('register.html', form=form)
#
#

# login_manager.init_app(app)
# login_manager.login_view = 'login'

if __name__ == '__main__':
    app.run(debug=True)
