from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

from models.Users import User


class LoginForm(FlaskForm):
    """ The login form """

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):
    """ The user registration form  """

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm',
                                                                             message='Passwords must match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self, field):
        """ The func which is checking the emails """

        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been already registered!')

    def check_username(self, field):
        """ The func which is checking you username """

        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been already registered!')
