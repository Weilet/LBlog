from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from LBlog import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    about = db.Column(db.Text)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', back_populates='auth')
    @property
    def password(self):
        raise AttributeError('密码是只读的')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)



