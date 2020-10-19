from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField, IntegerField, TextField, DateField
from wtforms.validators import EqualTo, DataRequired, Email
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from puppyblog.models import User


class LoginForm(FlaskForm):
    email = StringField(" email", validators=[DataRequired(), Email()])
    password = PasswordField("Please, provide your password!", validators=[DataRequired()])
    submit = SubmitField("Log in")


class RegistrationForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), ])
    email = StringField(" email", validators=[DataRequired(), Email()])
    password = PasswordField("Please, provide your password!",
                             validators=[DataRequired(), EqualTo("confirm_password", message="Password must match!")])
    confirm_password = PasswordField("confirm your password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("This email have been registered already !")

    def check_username(self, field):
        if User.query.filter_by(user_name=field.data).first():
            raise ValidationError("This username have been registered already !")


class UpdateFileForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), ])
    email = StringField(" email", validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Save")

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("This email have been registered already !")

    def check_username(self, field):
        if User.query.filter_by(user_name=field.data).first():
            raise ValidationError("This username have been registered already !")
