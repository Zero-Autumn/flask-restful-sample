from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, EqualTo, DataRequired, Length, ValidationError
# import app
import models



class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(),Length(min=4, max=10)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=32)])
    register = SubmitField('register')

    
    def validate_username(self, username):
        user = models.User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('username already exists')

    def validate_email(self, email):
        user = models.User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email already exists')




class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(),Length(min=4, max=10)])
    password = PasswordField('password', validators=[DataRequired()])
    login = SubmitField('login')

    
        