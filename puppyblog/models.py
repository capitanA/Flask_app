from puppyblog import login_manager, db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    user_name = db.Column(db.String(64), nullable=False, unique=True, index=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    hash_password = db.Column(db.String(128), unique=True, nullable=False)
    profile_image = db.Column(db.String(64), default='default_profile.png')
    blog_post = db.relationship('BlogPost', backref='Author', lazy=True)

    def __init__(self, user_name, email, password):
        self.user_name = user_name
        self.email = email
        self.hash_password = generate_password_hash(password)

    def match_password(self, password):
        return check_password_hash(self.hash_password, password)

    def __repr__(self):
        return f"{self.user_name} this user name create his/her last post {self.BlogPost.title} at {self.logPost.date}"


class BlogPost(db.Model):
    __tabelname__ = "blogposts"
    users = db.relationship(User)
    id = db.Column(db.Integer, unique=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow())
    body = db.Column(db.Text(), nullable=False)

    def __init__(self, title, body, user_id):
        self.title = title
        self.body = body
        self.user_id = user_id

    def __repr__(self):
        return f"post ID:{self.id} was created at{self.date}. The author of the post was {self.user.user_name}"
