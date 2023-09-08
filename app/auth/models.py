from datetime import datetime
from app import db, bcrypt


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    user_email = db.Column(db.String(20))
    user_password = db.Column(db.String(80))
    registration_date = db.Column(db.DateTime, default=datetime.now)

    @classmethod
    def create_user(cls, name, email, password):
        user = cls(user_name=name, user_email=email, user_password=password)
        db.session.add(user)
        db.session.commit()
        return user