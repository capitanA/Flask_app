from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired


class BlogPostForm(FlaskForm):
    title = StringField("what is the title for your post?", validators=[DataRequired()])
    body = TextAreaField("what is your post body:", validators=[DataRequired()])
    submit = SubmitField("post")
