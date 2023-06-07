from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

# User model
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(120), index=True, unique=True)
    phone_number = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(128))

    def __repr__(self) -> str:
        return "<User {}>".format(self.username)


# Game model
class Game(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(256))
    game_type = db.Column(db.String(64))
    min_players = db.Column(db.Integer)
    max_players = db.Column(db.Integer)

    def __repr__(self):
        return "<Game {}>".format(self.name)


# GameNight model
class GameNight(db.Model):
    __tablename__ = "game_nights"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return "<GameNight {}>".format(self.id)


# GameNightGame model
class GameNightGame(db.Model):
    __tablename__ = "game_night_games"

    id = db.Column(db.Integer, primary_key=True)
    game_night_id = db.Column(db.Integer, db.ForeignKey("game_nights.id"))
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))

    def __repr__(self):
        return "<GameNightGame {}>".format(self.id)

# Attendance model
class Attendance(db.Model):
    __tablename__ = "attendance"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    game_night_id = db.Column(db.Integer, db.ForeignKey("game_nights.id"))
    status = db.Column(
        db.String(10)
    )  # Possible statuses could be: Attending, Not Attending, Maybe

    def __repr__(self):
        return "<Attendance {}>".format(self.id)

# Announcement model
class Announcement(db.Model):
    __tablename__ = "announcements"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    content = db.Column(db.String(200))

    def __repr__(self):
        return "<Announcement {}>".format(self.id)
    
def init_app(app: Flask):
    db.init_app(app)
